"""Runner for agentic arms — pi inside a fresh, isolated Docker container.

Replaces runner_pi.py as the default agentic runner. Per-question flow (plan
§Anti-cheat #1–3):

  * a BRAND-NEW `docker run --rm` container per question — no shared state;
    only runner-owned tools/configuration are bind-mounted read-only, so
    question N cannot read question N-1's filesystem;
  * the container lives on the `beaver-sandbox` internal network (no internet
    route); its only egress is the allow-list proxy (openrouter.ai) and MySQL
    (beaver-mysql:3306), so the correct answer cannot leak via the internet;
  * pi gets its built-in tools and the purpose-built sql_exec tool
    under the SELECT-only DB account;
    other agents use their built-in tools and the installed MySQL/Python utilities;
  * turn_guard.ts reserves the last turn for final SQL.

The runner signature matches runner_pi.run() so run_experiment.py dispatches
through the same code path. ``BEAVER_AGENT`` selects pi, Claude Code, OpenCode,
or Codex without changing the isolation boundary. Network/proxy bring-up
happens once at experiment start (harness.network.setup()); this module assumes
it's already up.
"""
from __future__ import annotations

import json
import os
import subprocess
import tempfile
import threading
import time
import uuid
from pathlib import Path
from typing import Callable

from . import config, network, parse_sql, pi_stream, prompts


def _container_env(db_label: str, max_turns: int) -> list[str]:
    """Build the -e flags for the agent container.

    Creds + caps go in via env (the agent never sees the repo or the host).
    HTTPS_PROXY forces pi's OpenRouter calls through the allow-list proxy.
    MySQL is pointed at the container-internal name/port.
    """
    proxy_url = f"http://{config.EGRESS_PROXY_CONTAINER}:{config.EGRESS_PROXY_PORT}"
    env = {
        # LLM routing — pi reads these.
        "HTTPS_PROXY": proxy_url,
        "HTTP_PROXY": proxy_url,
        "NO_PROXY": "beaver-mysql,localhost,127.0.0.1",
        "OPENROUTER_API_KEY": os.environ.get("OPENROUTER_API_KEY", ""),
        # Claude Code uses OpenRouter's Anthropic-compatible endpoint. The
        # empty ANTHROPIC_API_KEY prevents any fallback to api.anthropic.com.
        "ANTHROPIC_BASE_URL": "https://openrouter.ai/api",
        "ANTHROPIC_AUTH_TOKEN": os.environ.get("OPENROUTER_API_KEY", ""),
        "ANTHROPIC_API_KEY": "",
        # OpenCode is given only its repo-owned config and no persisted state,
        # plugins, auto-update, or dynamic LSP downloads.
        "OPENCODE_CONFIG": "/config/opencode.json",
        "OPENCODE_CONFIG_DIR": "/tmp/opencode-config",
        "OPENCODE_DISABLE_AUTOUPDATE": "true",
        "OPENCODE_DISABLE_DEFAULT_PLUGINS": "true",
        "OPENCODE_DISABLE_LSP_DOWNLOAD": "true",
        # Experiment caps (turn_guard.ts + the prompt read these).
        "BEAVER_MAX_TURNS": str(max_turns),
        "BEAVER_QUERY_TIMEOUT": str(config.MYSQL_QUERY_TIMEOUT),
        # MySQL as seen inside the container (by name, internal port 3306).
        "MYSQL_HOST": config.MYSQL_HOST_CONTAINER,
        "MYSQL_PORT": str(config.MYSQL_PORT_CONTAINER),
        "MYSQL_USER": config.AGENT_MYSQL_USER,
        "MYSQL_PASSWORD": config.AGENT_MYSQL_PWD,
        "MYSQL_PWD": config.AGENT_MYSQL_PWD,  # the mysql CLI reads MYSQL_PWD
        "BEAVER_DB": config.mysql_db_for(db_label),
    }
    # Flatten to ["-e", "KEY=VAL", ...]
    flags: list[str] = []
    for k, v in env.items():
        flags += ["-e", f"{k}={v}"]
    return flags


def _agent_argv(agent: str, system_prompt: str, user_prompt: str, max_turns: int) -> list[str]:
    """Return the selected CLI's non-interactive argv inside the container."""
    model = config.CONTAINER_AGENT_MODEL
    if agent == "claude":
        return [
            "-p", "--output-format", "json", "--max-turns", str(max_turns),
            "--no-session-persistence", "--bare", "--no-chrome",
            "--disable-slash-commands", "--dangerously-skip-permissions",
            "--append-system-prompt", system_prompt, "--model", model, user_prompt,
        ]
    if agent == "opencode":
        return ["run", "--pure", "--format", "default", "--model", f"openrouter/{model}",
                "--auto", f"{system_prompt}\n\n{user_prompt}"]
    if agent == "codex":
        return [
            "exec", "--ephemeral", "--skip-git-repo-check", "--ignore-rules",
            "--dangerously-bypass-approvals-and-sandbox", "--model", model,
            f"{system_prompt}\n\n{user_prompt}",
        ]
    # pi is the default and the only runner with custom lifecycle extensions.
    # The SELECT-only database account and ephemeral container enforce safety.
    tools = "read,bash,edit,write,grep,find,ls,sql_exec"
    return [
        "-p",
        "--mode", "json",
        "--no-session",
        "--offline",
        "--no-extensions",
        "--no-skills",
        "--no-prompt-templates",
        "--no-context-files",
        "--no-themes",
        "-e", "/extensions/sql_exec.ts",
        "-e", "/extensions/turn_guard.ts",
        "--tools", tools,
        "--thinking", config.PI_THINKING,
        "--append-system-prompt", system_prompt,
        "--provider", config.DEFAULT_PROVIDER,
        "--model", config.CONTAINER_AGENT_MODEL,
    ]


def _parse_agent_output(agent: str, stdout: str) -> dict:
    """Normalize final text from the lightweight non-pi CLI adapters."""
    if agent == "pi":
        return pi_stream.parse_stream(stdout)
    text = stdout
    if agent == "claude":
        try:
            text = json.loads(stdout).get("result", stdout)
        except json.JSONDecodeError:
            pass
    return {
        # These CLIs do not expose pi-compatible tool and token telemetry in
        # their default headless output. Keep record shapes numeric but flag
        # that aggregate operational metrics are unavailable.
        "turns": 0, "db_queries": 0, "metrics_available": False,
        "raw_text": text, "all_text": [text],
        "executed_sqls": [],
        "usage": {"input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0,
                  "reasoning": 0, "totalTokens": 0},
        "cost": {"input": 0.0, "output": 0.0, "cacheRead": 0.0,
                 "cacheWrite": 0.0, "total": 0.0},
        "model": config.CONTAINER_AGENT_MODEL, "provider": "openrouter",
    }


def _run_pi_streamed(argv: list[str], prompt: str, status: Callable[[int, int], None]):
    """Run pi while draining JSON stdout and reporting completed turns."""
    proc = subprocess.Popen(
        argv, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    stdout: list[str] = []
    stderr: list[str] = []
    counters = {"turns": 0, "db_queries": 0}

    def read_stdout() -> None:
        assert proc.stdout is not None
        for line in proc.stdout:
            stdout.append(line)
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            if event.get("type") == "tool_execution_start":
                args = event.get("args") or {}
                if args.get("sql") or pi_stream._sql_from_bash(str(args.get("command", ""))):
                    counters["db_queries"] += 1
            elif event.get("type") == "turn_end":
                counters["turns"] += 1
                status(counters["turns"], counters["db_queries"])

    def read_stderr() -> None:
        assert proc.stderr is not None
        stderr.extend(proc.stderr)

    readers = [threading.Thread(target=read_stdout), threading.Thread(target=read_stderr)]
    for reader in readers:
        reader.start()
    assert proc.stdin is not None
    try:
        proc.stdin.write(prompt)
        proc.stdin.close()
        returncode = proc.wait(timeout=config.PI_WALL_CLOCK)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait()
        for reader in readers:
            reader.join()
        proc.stdout.close()
        proc.stderr.close()
        raise subprocess.TimeoutExpired(
            argv, config.PI_WALL_CLOCK, output="".join(stdout), stderr="".join(stderr)
        )
    for reader in readers:
        reader.join()
    proc.stdout.close()
    proc.stderr.close()
    return subprocess.CompletedProcess(argv, returncode, "".join(stdout), "".join(stderr))


def run(db_label: str, question: str, arm: str, max_turns: int,
        sandbox: Path, status_callback: Callable[[int, int], None] | None = None) -> dict:
    """Run one question in a fresh isolated container, return a result record.

    ``sandbox`` is accepted for signature parity with runner_pi.run but is NOT
    used as a bind-mount (the container is fully ephemeral); it's recorded in
    the output for traceability.
    """
    system_prompt, user_prompt = prompts.agent_prompts(db_label, question, arm, max_turns)
    agent = config.CONTAINER_AGENT
    started = time.time()
    rec: dict = {
        "arm": arm, "runner": f"container:{agent}", "db_label": db_label,
        "max_turns": max_turns, "sandbox": str(sandbox), "container": True,
    }
    if not network.is_ready():
        rec["error"] = ("agent network not ready — call harness.network.setup() "
                        "before running (or check `docker ps` for the egress proxy).")
        rec["infrastructure_error"] = True
        return rec

    # Assemble the full `docker run` command. --network attaches to the internal
    # sandbox net; -v mounts only runner-owned configuration read-only; resource
    # caps contain runaway work; --rm guarantees teardown.
    volumes = [
        "-v", f"{config.PI_EXTENSION}:/extensions/sql_exec.ts:ro",
        "-v", f"{config.HARNESS_DIR / 'turn_guard.ts'}:/extensions/turn_guard.ts:ro",
        "-v", f"{(config.openrouter_models_path() if agent == 'pi' else config.HARNESS_DIR / 'openrouter_models.json')}:/home/node/.pi/agent/models.json:ro",
        "-v", f"{config.HARNESS_DIR / 'codex_config.toml'}:/home/node/.codex/config.toml:ro",
        "-v", f"{config.HARNESS_DIR / 'opencode.json'}:/config/opencode.json:ro",
        "-v", f"{config.HARNESS_DIR / 'mysql_timeout.sh'}:/usr/local/bin/mysql:ro",
    ]
    # Non-pi CLIs lack tool-result telemetry. Persist only successful mysql -e
    # calls in a fresh, per-question trace; never mount the host sandbox/repo.
    trace = None
    if agent != "pi":
        trace = tempfile.TemporaryDirectory(prefix="beaver-sql-")
        trace_path = Path(trace.name) / "success.jsonl"
        trace_path.touch(mode=0o666)
        trace_path.chmod(0o666)
        volumes += ["-v", f"{trace_path}:/tmp/beaver-sql-success.jsonl",
                    "-e", "BEAVER_SQL_SUCCESS_LOG=/tmp/beaver-sql-success.jsonl"]
    if config.arm_spec(arm)["profile"]:
        key = config.mysql_db_for(db_label)
        volumes += [
            "-v", f"{config.profile_path_for(key)}:/workspace/profile.md:ro",
            "-v", f"{config.resolved_toc_path_for(key)}:/workspace/profile.toc.md:ro",
        ]
        if config.arm_spec(arm)["schema_links"]:
            volumes += ["-v", f"{config.schema_links_path_for(key)}:/workspace/schema-links.md:ro"]
    container_name = f"beaver-agent-{uuid.uuid4().hex}"
    docker_argv = [
        "docker", "run", "--rm", "-i",
        "--name", container_name,
        "--network", config.AGENT_NET_SANDBOX,
        "--memory", config.CONTAINER_MEMORY,
        "--cpus", config.CONTAINER_CPUS,
        "--pids-limit", config.CONTAINER_PIDS_LIMIT,
        "--cap-drop", "ALL",
        "--security-opt", "no-new-privileges",
        "--workdir", "/workspace",
        *volumes,
        *_container_env(db_label, max_turns),
        *( [] if agent == "pi" else ["--entrypoint", agent] ),
        config.CONTAINER_IMAGE,
        *_agent_argv(agent, system_prompt, user_prompt, max_turns),
    ]

    try:
        if agent == "pi" and status_callback:
            proc = _run_pi_streamed(docker_argv, user_prompt, status_callback)
        else:
            proc = subprocess.run(
                docker_argv,
                input=user_prompt if agent == "pi" else None,
                capture_output=True,
                text=True,
                timeout=config.PI_WALL_CLOCK,
            )
        rec["returncode"] = proc.returncode
        rec["stderr_tail"] = (proc.stderr or "")[-1000:]
        parsed = _parse_agent_output(agent, proc.stdout or "")
    except subprocess.TimeoutExpired as e:
        rec["error"] = f"container wall-clock timeout ({config.PI_WALL_CLOCK}s)"
        rec["budget_exhausted"] = "wall_clock"
        output = e.stdout or ""
        rec["stdout"] = output.decode("utf-8", "replace") if isinstance(output, bytes) else output
        parsed = _parse_agent_output(agent, rec.get("stdout", ""))
        # Killing the docker CLI does not reliably stop its container. Explicit
        # teardown is required to keep an over-time question from surviving
        # into a later one.
        cleanup = subprocess.run(["docker", "rm", "-f", container_name],
                                 capture_output=True, text=True, timeout=30)
        if cleanup.returncode != 0:
            rec["cleanup_error"] = (cleanup.stderr or "").strip()
    except FileNotFoundError:
        rec["error"] = "`docker` not found on PATH — install Docker/OrbStack."
        rec["infrastructure_error"] = True
        if trace:
            trace.cleanup()
        return rec

    if trace:
        try:
            parsed["successful_sqls"] = [json.loads(line) for line in trace_path.read_text().splitlines()]
        finally:
            trace.cleanup()

    if pi_stream.is_turn_limit_abort(parsed.get("api_error"), parsed.get("turns", 0), max_turns):
        parsed["api_error"] = None
        parsed["turns"] = max_turns
    rec.update(parsed)
    candidate = None
    if not rec.get("budget_exhausted") and not parsed.get("api_error"):
        candidate = parse_sql.extract_final_sql(
            parsed.get("final_response", parsed.get("raw_text", "")))
    if parsed.get("api_error"):
        rec["error"] = f"model API error: {parsed['api_error']}"
        rec["infrastructure_error"] = True
        rec["retryable_error"] = pi_stream.retryable_api_error(parsed["api_error"])
    if (agent == "pi" and not rec.get("budget_exhausted")
            and not parsed.get("model") and not parsed.get("turns")):
        rec["error"] = rec.get("error") or "pi emitted no assistant events"
        rec["infrastructure_error"] = True
    if parsed.get("turns", 0) >= max_turns and not candidate and not rec.get("api_error"):
        rec["error"] = rec.get("error") or f"no final SQL within {max_turns}-turn budget"
        rec["budget_exhausted"] = "turns"
    if (rec.get("returncode") and not rec.get("budget_exhausted")
            and not (parsed.get("turns", 0) >= max_turns and candidate)):
        rec["error"] = rec.get("error") or f"agent container exited {rec['returncode']}"
        rec["infrastructure_error"] = True
    rec["latency_s"] = round(time.time() - started, 2)
    rec["pred_sql"] = candidate
    # Token runaway guard (plan §Locked decisions #4).
    if parsed["usage"]["totalTokens"] > config.TOKEN_GUARD:
        rec["token_guard_hit"] = True
    return rec
