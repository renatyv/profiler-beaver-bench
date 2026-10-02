"""Small regression checks for container-run isolation bookkeeping."""
from __future__ import annotations

import json
import re
from io import BytesIO
import subprocess
import sys
import os
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from harness import parse_sql, pi_stream, runner_container, runner_pi


class ContainerIsolationTests(unittest.TestCase):
    def test_success_requires_a_completed_successful_tool_call(self) -> None:
        events = []
        for ident, details, is_error in (
            ("failed", {"code": 1}, False),
            ("timeout", {"code": 0, "timedOut": True}, False),
            ("error", {"code": 0}, True),
            ("ok", {"code": 0}, False),
            ("unfinished", None, False),
        ):
            events.append({"type": "tool_execution_start", "toolCallId": ident,
                           "toolName": "sql_exec", "args": {"sql": f"SELECT '{ident}'"}})
            if details is not None:
                events.append({"type": "tool_execution_end", "toolCallId": ident,
                               "toolName": "sql_exec", "isError": is_error,
                               "result": {"details": details}})
        parsed = pi_stream.parse_stream("\n".join(map(json.dumps, events)))
        self.assertEqual(parsed["db_queries"], 5)
        self.assertEqual(parsed["successful_sqls"], ["SELECT 'ok'"])
        self.assertEqual([c.get("execution_ok") for c in parsed["tool_calls"]],
                         [False, False, False, True, None])

    def test_final_extraction_requires_a_closed_answer(self) -> None:
        self.assertIsNone(parse_sql.extract_final_sql("<ans>SELECT 1"))
        self.assertIsNone(parse_sql.extract_final_sql("```sql\nSELECT 1\n```"))
        self.assertIsNone(parse_sql.extract_final_sql("<ans>SELECT 1</ans><ans>SELECT 2</ans>"))

    def test_bash_success_cannot_mask_failure_or_expand_the_recorded_sql(self) -> None:
        for command, expected in (
            ("mysql -e 'SELECT 1'", True),
            ("mysql -e 'SELECT 1'; true", False),
            ("mysql -e 'SELECT 1' | head", False),
            ('mysql -e "SELECT \'$VALUE\'"', False),
            ("mysql -e 'SELECT * FROM `table`'", True),
        ):
            self.assertEqual(pi_stream._successful_sql(
                {"name": "bash", "arguments": {"command": command}},
                {"isError": False, "result": {}}), expected)

    @patch("harness.runner_container.network.is_ready", return_value=True)
    @patch("harness.runner_container.subprocess.run")
    def test_runner_does_not_recover_an_earlier_draft(self, run, _ready) -> None:
        messages = [
            {"type": "turn_end", "message": {"role": "assistant", "stopReason": "toolUse",
             "model": "test", "content": [{"type": "text", "text": "<ans>SELECT 1</ans>"}]}},
            {"type": "turn_end", "message": {"role": "assistant", "stopReason": "stop",
             "content": [{"type": "text", "text": "I could not finish."}]}},
        ]
        run.return_value = subprocess.CompletedProcess([], 0, "\n".join(map(json.dumps, messages)), "")
        rec = runner_container.run("neutron", "question", "raw", 6, Path("/tmp/x"))
        self.assertIsNone(rec["pred_sql"])

    def test_mysql_wrapper_logs_only_successful_queries(self) -> None:
        with TemporaryDirectory() as temp:
            directory = Path(temp)
            timeout = directory / "timeout"
            timeout.write_text('#!/bin/sh\nshift\nexec "$@"\n')
            mysql = directory / "mysql"
            mysql.write_text('#!/bin/sh\nexit "${FAKE_MYSQL_EXIT:-0}"\n')
            for path in (timeout, mysql):
                path.chmod(0o755)
            wrapper = directory / "wrapper.sh"
            wrapper.write_text((runner_container.config.HARNESS_DIR / "mysql_timeout.sh").read_text()
                               .replace("/usr/bin/timeout", str(timeout)).replace("/usr/bin/mysql", str(mysql)))
            log = directory / "success.jsonl"
            for status in (0, 1, 124):
                proc = subprocess.run(["sh", str(wrapper), "-e", "SELECT 'literal value'"],
                                      env=os.environ | {"BEAVER_SQL_SUCCESS_LOG": str(log),
                                                        "FAKE_MYSQL_EXIT": str(status)},
                                      capture_output=True, text=True)
                self.assertEqual(proc.returncode, status, proc.stderr)
            self.assertEqual([json.loads(line) for line in log.read_text().splitlines()],
                             ["SELECT 'literal value'"])

    @patch("harness.runner_container.network.is_ready", return_value=True)
    def test_non_pi_runner_uses_mysql_completion_log(self, _ready) -> None:
        for success in (True, False):
            def run(argv, **_kwargs):
                if success:
                    mount = next(arg for arg in argv if arg.endswith(":/tmp/beaver-sql-success.jsonl"))
                    Path(mount.split(":")[0]).write_text(json.dumps("SELECT 1") + "\n")
                return subprocess.CompletedProcess(argv, 0, "<ans>SELECT 1</ans>", "")
            with (patch.object(runner_container.config, "CONTAINER_AGENT", "codex"),
                  patch("harness.runner_container.subprocess.run", side_effect=run)):
                rec = runner_container.run("neutron", "question", "raw", 6, Path("/tmp/x"))
            self.assertEqual(rec["pred_sql"], "SELECT 1;")
            self.assertEqual(rec["successful_sqls"], ["SELECT 1"] if success else [])

    def test_all_agent_choices_have_noninteractive_argv(self) -> None:
        for agent in ("pi", "claude", "opencode", "codex"):
            argv = runner_container._agent_argv(agent, "system", "user", 3)
            self.assertTrue(argv)
        self.assertIn("--max-turns", runner_container._agent_argv("claude", "s", "u", 3))
        self.assertEqual(runner_container._agent_argv("codex", "s", "u", 3)[0], "exec")

    def test_pi_uses_the_selected_container_model(self) -> None:
        with (patch.object(runner_container.config, "CONTAINER_AGENT_MODEL", "openai/gpt-6-luna"),
              patch.object(runner_container.config, "PI_THINKING", "low")):
            argv = runner_container._agent_argv("pi", "system", "user", 3)
        self.assertEqual(argv[argv.index("--model") + 1], "openai/gpt-6-luna")
        self.assertEqual(argv[argv.index("--thinking") + 1], "low")
        tools = argv[argv.index("--tools") + 1].split(",")
        self.assertEqual(
            set(tools),
            {"read", "bash", "edit", "write", "grep", "find", "ls", "sql_exec"},
        )
        self.assertNotIn("--no-builtin-tools", argv)
        self.assertFalse(any("subagent" in arg for arg in argv))
        self.assertTrue(any("sql_exec.ts" in arg for arg in argv))

    def test_host_pi_has_builtin_tools(self) -> None:
        argv = runner_pi._argv("system")
        tools = argv[argv.index("--tools") + 1].split(",")
        self.assertEqual(
            set(tools),
            {"read", "bash", "edit", "write", "grep", "find", "ls", "sql_exec"},
        )
        self.assertNotIn("--no-builtin-tools", argv)
        self.assertFalse(any("subagent" in arg for arg in argv))

    @patch("harness.runner_container.network.is_ready", return_value=True)
    @patch("harness.runner_container.subprocess.run")
    def test_profile_and_toc_are_mounted_without_prompt_injection(self, run, _ready) -> None:
        run.return_value = subprocess.CompletedProcess(["docker", "run"], 0, "", "")
        runner_container.run("neutron", "question", "profile", 3, Path("/tmp/x"))
        argv = run.call_args.args[0]
        mounts = [argv[i + 1] for i, arg in enumerate(argv) if arg == "-v"]
        self.assertTrue(any("neutron.md:/workspace/profile.md:ro" in mount for mount in mounts))
        # The TOC mount is the resolved one: the enriched file once generated,
        # otherwise the plain db-snooper TOC.
        self.assertTrue(any(
            re.search(r"(profiles|generated-metadata)/neutron\.toc\.md"
                      r":/workspace/profile\.toc\.md:ro$", mount)
            for mount in mounts), mounts)
        self.assertTrue(any("neutron.md:/workspace/schema-links.md:ro" in mount for mount in mounts))
        self.assertNotIn("BEGIN DB PROFILE", run.call_args.kwargs["input"])

    def test_missing_openrouter_model_gets_resolved_metadata(self) -> None:
        model = "vendor/test-model"
        remote = {"data": {
            "id": model,
            "name": "Test Model",
            "architecture": {"input_modalities": ["text", "image"]},
            "supported_parameters": ["tools", "reasoning"],
            "pricing": {"prompt": "0.000001", "completion": "0.000002"},
            "top_provider": {"context_length": 1_000_000,
                             "max_completion_tokens": 128_000},
        }}
        runner_container.config._MODEL_CONFIGS.pop(model, None)
        runner_container.config._REMOTE_MODELS.pop(model, None)
        with (patch.object(runner_container.config, "CONTAINER_AGENT_MODEL", model),
              patch("harness.config.urlopen",
                    return_value=BytesIO(json.dumps(remote).encode())) as fetch):
            registry = runner_container.config.openrouter_models_path()
            self.assertEqual(registry, runner_container.config.openrouter_models_path())
        resolved = next(m for m in json.loads(registry.read_text())["providers"]["openrouter"]["models"]
                        if m["id"] == model)
        self.assertEqual(resolved["contextWindow"], 1_000_000)
        self.assertEqual(resolved["maxTokens"], 128_000)
        self.assertTrue(resolved["reasoning"])
        self.assertEqual(resolved["cost"]["input"], 1.0)
        fetch.assert_called_once()

    def test_mysql_bash_is_counted_and_recoverable(self) -> None:
        events = ('{"type":"turn_start"}\n'
                  '{"type":"tool_execution_start","toolName":"bash",'
                  '"args":{"command":"mysql -D neutron -e \'SELECT 1\'"}}\n')
        parsed = pi_stream.parse_stream(events)
        self.assertEqual(parsed["db_queries"], 1)
        self.assertEqual(parsed["executed_sqls"], ["SELECT 1"])
        self.assertEqual(parsed["tool_calls"], [{
            "source": "main", "name": "bash", "turn": 1,
            "arguments": {"command": "mysql -D neutron -e 'SELECT 1'"},
        }])

    def test_subagent_usage_and_sql_are_counted(self) -> None:
        events = '{"type":"turn_start"}\n' + json.dumps({
            "type": "tool_execution_start", "toolName": "subagent",
            "args": {"agent": "critic", "task": "check SQL"},
        }) + "\n" + json.dumps({
            "type": "tool_execution_end",
            "toolName": "subagent",
            "result": {"details": {"results": [{
                "usage": {"input": 10, "output": 5, "cacheRead": 3, "cacheWrite": 2,
                          "cost": 0.25, "turns": 1},
                "messages": [{"role": "assistant", "content": [{
                    "type": "toolCall", "name": "bash",
                    "arguments": {"command": "mysql -e 'SELECT 2'"},
                }]}],
            }]}},
        })
        parsed = pi_stream.parse_stream(events)
        self.assertEqual(parsed["subagent_calls"], 1)
        self.assertEqual(parsed["subagent_turns"], 1)
        self.assertEqual(parsed["usage"]["totalTokens"], 20)
        self.assertEqual(parsed["cost"]["total"], 0.25)
        self.assertEqual(parsed["executed_sqls"], ["SELECT 2"])
        self.assertEqual(parsed["tool_calls"], [
            {"source": "main", "name": "subagent", "turn": 1,
             "arguments": {"agent": "critic", "task": "check SQL"}},
            {"source": "subagent", "name": "bash", "turn": 1,
             "arguments": {"command": "mysql -e 'SELECT 2'"}},
        ])

    def test_tool_calls_are_tagged_with_their_turn(self) -> None:
        events = "\n".join([
            '{"type":"agent_start"}',
            '{"type":"turn_start"}',
            '{"type":"tool_execution_start","toolName":"sql_exec","args":{"sql":"SHOW TABLES"}}',
            '{"type":"tool_execution_start","toolName":"sql_exec","args":{"sql":"DESCRIBE t"}}',
            '{"type":"turn_end"}',
            '{"type":"turn_start"}',  # text-only turn: no tool calls
            '{"type":"turn_end"}',
            '{"type":"turn_start"}',
            '{"type":"tool_execution_start","toolName":"subagent","args":{"task":"t"}}',
            json.dumps({
                "type": "tool_execution_end", "toolName": "subagent",
                "result": {"details": {"results": [{"messages": [{"role": "assistant", "content": [{
                    "type": "toolCall", "name": "sql_exec", "arguments": {"sql": "SELECT 2"},
                }]}]}]}},
            }),
            '{"type":"turn_end"}',
            '{"type":"agent_start"}',  # auto-retry restarts turn numbering
            '{"type":"turn_start"}',
            '{"type":"tool_execution_start","toolName":"sql_exec","args":{"sql":"SELECT 9"}}',
            '{"type":"turn_end"}',
        ])
        parsed = pi_stream.parse_stream(events)
        self.assertEqual(parsed["turns"], 4)
        self.assertEqual([(c["source"], c["name"], c["turn"]) for c in parsed["tool_calls"]], [
            ("main", "sql_exec", 1),
            ("main", "sql_exec", 1),
            ("main", "subagent", 3),
            ("subagent", "sql_exec", 3),  # nested call inherits the spawning turn
            ("main", "sql_exec", 1),      # retry attempt: numbering restarted
        ])

    def test_unclosed_sql_fence_is_recoverable(self) -> None:
        self.assertEqual(parse_sql.extract_sql("```sql\nSELECT 1;"), "SELECT 1;")
        self.assertEqual(parse_sql.extract_sql("<ans>SELECT 2</ans>"), "SELECT 2;")
        self.assertEqual(parse_sql.extract_sql("<ans>WITH q AS (SELECT 3) SELECT * FROM q"),
                         "WITH q AS (SELECT 3) SELECT * FROM q;")

    def test_ans_html_entities_are_unescaped(self) -> None:
        self.assertEqual(parse_sql.extract_sql("<ans>SELECT 1 WHERE 2 &gt; 1</ans>"),
                         "SELECT 1 WHERE 2 > 1;")

    def test_non_pi_telemetry_is_not_reported_as_zero(self) -> None:
        parsed = runner_container._parse_agent_output("codex", "```sql\nSELECT 1\n```")
        self.assertFalse(parsed["metrics_available"])
        self.assertEqual(parsed["turns"], 0)

    @patch("harness.runner_container.network.is_ready", return_value=True)
    @patch("harness.runner_container.prompts.agent_prompts", return_value=("system", "user"))
    @patch("harness.runner_container.subprocess.run")
    def test_timeout_force_removes_the_named_container(self, run, _prompts, _ready) -> None:
        run.side_effect = [
            subprocess.TimeoutExpired(["docker", "run"], 1, output=""),
            subprocess.CompletedProcess(["docker", "rm"], 0),
        ]
        with patch("harness.runner_container.uuid.uuid4", return_value=type("U", (), {"hex": "test"})()):
            rec = runner_container.run("neutron", "question", "raw", 1, Path("/tmp/x"))
        self.assertIn("wall-clock timeout", rec["error"])
        self.assertEqual(rec["budget_exhausted"], "wall_clock")
        self.assertNotIn("infrastructure_error", rec)
        self.assertIn("-i", run.call_args_list[0].args[0])
        self.assertEqual(run.call_args_list[1].args[0][:3], ["docker", "rm", "-f"])
        self.assertTrue(any("mysql_timeout.sh:/usr/local/bin/mysql:ro" in str(arg)
                            for arg in run.call_args_list[0].args[0]))
        self.assertTrue(any("sql_exec.ts:/extensions/sql_exec.ts:ro" in str(arg)
                            for arg in run.call_args_list[0].args[0]))

    def test_terminal_api_error_is_visible_despite_zero_exit(self) -> None:
        events = ('{"type":"auto_retry_start"}\n'
                  '{"type":"turn_end","message":{"role":"assistant",'
                  '"stopReason":"error","errorMessage":"429 rate limited","content":[]}}\n')
        parsed = pi_stream.parse_stream(events)
        self.assertEqual(parsed["retry_count"], 1)
        self.assertEqual(parsed["api_error"], "429 rate limited")
        self.assertTrue(pi_stream.retryable_api_error(parsed["api_error"]))
        self.assertTrue(pi_stream.retryable_api_error(
            "Upstream error: generation ended before the streamed tool call was complete"
        ))
        self.assertFalse(pi_stream.retryable_api_error("HTTP 401 invalid API key"))

    @patch("harness.runner_container.network.is_ready", return_value=True)
    @patch("harness.runner_container.prompts.agent_prompts", return_value=("system", "user"))
    @patch("harness.runner_container.subprocess.run")
    def test_turn_guard_abort_is_budget_exhaustion(self, run, _prompts, _ready) -> None:
        tool_turn = ('{"type":"turn_end","message":{"role":"assistant",'
                     '"stopReason":"toolUse","content":[]}}\n')
        error_turn = ('{"type":"turn_end","message":{"role":"assistant",'
                      '"stopReason":"error","errorMessage":"This operation was aborted",'
                      '"content":[]}}\n')
        run.return_value = subprocess.CompletedProcess(
            ["docker", "run"], 0, tool_turn * 6 + error_turn, ""
        )
        rec = runner_container.run("neutron", "question", "raw", 6, Path("/tmp/x"))
        self.assertEqual(rec["budget_exhausted"], "turns")
        self.assertEqual(rec["turns"], 6)
        self.assertEqual(rec["error"], "no final SQL within 6-turn budget")
        self.assertNotIn("infrastructure_error", rec)
        self.assertIsNone(rec["api_error"])

    def test_streamed_runner_reports_turns(self) -> None:
        events = [
            '{"type":"tool_execution_start","toolName":"bash",'
            '"args":{"command":"mysql -e SELECT"}}',
            '{"type":"turn_end","message":{"role":"assistant"}}',
        ]
        script = "import sys; sys.stdin.read(); " + "; ".join(
            f"print({event!r})" for event in events
        )
        statuses = []
        completed = runner_container._run_pi_streamed(
            [sys.executable, "-c", script], "prompt", lambda turn, dbq: statuses.append((turn, dbq))
        )
        self.assertEqual(completed.returncode, 0)
        self.assertEqual(statuses, [(1, 1)])


if __name__ == "__main__":
    unittest.main()
