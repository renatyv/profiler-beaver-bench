"""Shared parser for pi's `--mode json` stdout event stream.

Both the legacy host runner (runner_pi.py) and the container runner
(runner_container.py) spawn `pi -p --mode json` and parse the same JSON-lines
event stream, so the parsing logic lives here. The parser extracts:

  * turns          — count of turn_end events
  * db_queries     — count of tool_execution_start events (legacy sql_exec; for
                      the container runner this counts bash tool calls that run
                      SQL — see extract_sql_from_bash below)
  * executed_sqls  — attempted SQL from sql_exec or `mysql -e` bash calls
  * successful_sqls — SQL whose tool call completed successfully
  * tool_calls     — every main-agent and nested subagent tool invocation, each
                      tagged with the 1-based main-agent turn it ran in ("turn";
                      nested subagent calls inherit the turn that spawned them)
  * all_text       — assistant text segments in order (final = the answer)
  * raw_text       — the last assistant text segment (the final answer)
  * usage / cost   — parent usage plus nested subagent usage, with a recovery
                      pass over turn_end if the run was aborted
  * model / provider — from the first assistant message that carries them

The abort-recovery path matters: when the wall-clock timeout kills pi before it
emits agent_end, we reconstruct usage/cost from the per-turn turn_end messages
(better an estimate than zeros).
"""
from __future__ import annotations

import json
import re
import shlex

_USAGE_KEYS = ("input", "output", "cacheRead", "cacheWrite", "reasoning", "totalTokens")
_COST_KEYS = ("input", "output", "cacheRead", "cacheWrite", "total")


def _empty_usage() -> dict:
    return {k: 0 for k in _USAGE_KEYS}


def _empty_cost() -> dict:
    return {k: 0.0 for k in _COST_KEYS}


def _iter_events(stdout: str):
    """Yield parsed JSON objects from pi's stdout, skipping non-JSON lines."""
    for line in stdout.splitlines():
        line = line.strip()
        if not line or not line.startswith("{"):
            continue
        try:
            yield json.loads(line)
        except json.JSONDecodeError:
            continue


def retryable_api_error(message: str | None) -> bool:
    """True only for transient provider/rate/network failures."""
    if not message:
        return False
    lower = message.lower()
    return bool(
        re.search(r"\b(?:429|5\d\d)\b", lower)
        or any(term in lower for term in (
            "rate limit", "connection reset", "connection refused", "timed out",
            "timeout", "econnreset", "fetch failed", "network error", "upstream error",
        ))
    )


def is_turn_limit_abort(message: str | None, turns: int, max_turns: int) -> bool:
    """True when pi reports the turn guard's deliberate abort as an API error."""
    return message == "This operation was aborted" and turns >= max_turns


def _sql_from_bash(command: str, *, preserve_quotes: bool = False) -> str | None:
    """Extract `mysql -e SQL` when a container agent runs it via bash."""
    try:
        args = shlex.split(command, posix=not preserve_quotes)
    except ValueError:
        return None
    for i, arg in enumerate(args):
        if arg.rsplit("/", 1)[-1] not in {"mysql", "mariadb"}:
            continue
        for option in args[i + 1:]:
            if option == "-e":
                pos = args.index(option, i + 1)
                return args[pos + 1] if pos + 1 < len(args) else None
            if option.startswith("--execute="):
                return option.partition("=")[2]
    return None


def _successful_sql(call: dict, event: dict) -> bool:
    if event.get("isError") or (event.get("result") or {}).get("isError"):
        return False
    details = (event.get("result") or {}).get("details") or {}
    if call["name"] == "sql_exec":
        return details.get("code") == 0 and not details.get("timedOut")
    # Bash throws on nonzero exit. Only a plain mysql invocation proves that
    # mysql succeeded: a pipeline or `mysql ...; true` can mask its exit code.
    command = str(call["arguments"].get("command", ""))
    sql = _sql_from_bash(command) or ""
    raw_sql = _sql_from_bash(command, preserve_quotes=True)
    # ponytail: only literal SQL can be verified from bash events; use sql_exec
    # for shell-expanded SQL, or capture resolved argv in an execution log.
    if any(marker in sql for marker in ("$", "`")) and raw_sql != "'" + sql + "'":
        return False
    lexer = shlex.shlex(command, posix=True, punctuation_chars=";&|<>")
    lexer.whitespace_split = True
    try:
        args = list(lexer)
    except ValueError:
        return False
    return (call["name"] == "bash" and event.get("isError") is False
            and bool(args) and args[0].rsplit("/", 1)[-1] in {"mysql", "mariadb"}
            and not any(re.fullmatch(r"[;&|<>]+", arg) for arg in args))


def parse_stream(stdout: str) -> dict:
    """Parse a pi `--mode json` stdout stream into a result dict.

    See module docstring for the fields returned.
    """
    turns = 0
    db_queries = 0
    tool_calls: list[dict] = []
    texts: list[str] = []          # assistant text segments, in order
    executed_sqls: list[str] = []
    successful_sqls: list[str] = []
    pending_sql: dict[str, tuple[dict, str]] = {}
    current_turn = 0               # 1-based; turn_start/turn_end bound each turn's calls
    usage_total = _empty_usage()
    cost_total = _empty_cost()
    model = provider = None
    agent_ended = False
    last_stop_reason = last_error = None
    retry_count = 0
    subagent_calls = subagent_turns = 0

    events = list(_iter_events(stdout))
    for e in events:
        t = e.get("type")
        if t == "agent_start":
            current_turn = 0  # an auto-retry re-runs the agent; turn numbering restarts
        if t == "turn_start":
            current_turn += 1
        if t == "auto_retry_start":
            retry_count += 1
        if t == "turn_end":
            turns += 1
        if t == "tool_execution_start":
            tool_name = e.get("toolName")
            args = e.get("args") or {}
            tool_calls.append({"source": "main", "name": tool_name, "arguments": args,
                               "turn": current_turn})
            sql = args.get("sql")
            if sql:
                db_queries += 1
                executed_sqls.append(sql)
            elif tool_name == "bash":
                sql = _sql_from_bash(str(args.get("command", "")))
                if sql:
                    db_queries += 1
                    executed_sqls.append(sql)
            if sql and e.get("toolCallId"):
                pending_sql[e["toolCallId"]] = (tool_calls[-1], sql)
        if t == "tool_execution_end":
            pending = pending_sql.pop(e.get("toolCallId"), None)
            if pending:
                call, sql = pending
                call["execution_ok"] = _successful_sql(call, e)
                if call["execution_ok"]:
                    successful_sqls.append(sql)
        if t == "tool_execution_end" and e.get("toolName") == "subagent":
            subagent_calls += 1
            for result in (((e.get("result") or {}).get("details") or {}).get("results") or []):
                nested = result.get("usage") or {}
                subagent_turns += nested.get("turns", 0) or 0
                for k in ("input", "output", "cacheRead", "cacheWrite"):
                    usage_total[k] += nested.get(k, 0) or 0
                usage_total["totalTokens"] += sum(
                    nested.get(k, 0) or 0 for k in ("input", "output", "cacheRead", "cacheWrite")
                )
                cost_total["total"] += nested.get("cost", 0.0) or 0.0
                for message in result.get("messages") or []:
                    if message.get("role") != "assistant":
                        continue
                    for part in message.get("content") or []:
                        if part.get("type") != "toolCall":
                            continue
                        args = part.get("arguments") or {}
                        tool_calls.append({
                            "source": "subagent", "name": part.get("name"),
                            "arguments": args, "turn": current_turn,
                        })
                        sql = args.get("sql") if part.get("name") == "sql_exec" else None
                        if part.get("name") == "bash":
                            sql = _sql_from_bash(str(args.get("command", "")))
                        if sql:
                            db_queries += 1
                            executed_sqls.append(sql)
        # Collect per-turn assistant TEXT from turn_end (so the final answer is
        # captured even when agent_end never fires, e.g. on a wall-clock abort).
        if t == "turn_end":
            m = e.get("message") or {}
            if m.get("role") == "assistant":
                last_stop_reason = m.get("stopReason")
                last_error = m.get("errorMessage")
                provider = provider or m.get("provider")
                model = model or m.get("model")
                txt = "".join(c.get("text", "") for c in m.get("content", [])
                              if c.get("type") == "text")
                if txt.strip():
                    texts.append(txt)
        # Accumulate usage/cost ONCE, from the terminal agent_end event (which
        # carries the full assistant message list). Counting turn_end here too
        # would double-count every token, since agent_end repeats all messages.
        elif t == "agent_end":
            agent_ended = True
            for m in e.get("messages") or []:
                if m.get("role") != "assistant":
                    continue
                last_stop_reason = m.get("stopReason")
                last_error = m.get("errorMessage")
                provider = provider or m.get("provider")
                model = model or m.get("model")
                # Fall back to per-turn text already collected from turn_end;
                # only append here if turn_end text was missing (e.g. a turn
                # whose turn_end event was dropped from the stream).
                txt = "".join(c.get("text", "") for c in m.get("content", [])
                              if c.get("type") == "text")
                if txt.strip() and txt not in texts:
                    texts.append(txt)
                u = m.get("usage") or {}
                for k in usage_total:
                    usage_total[k] += u.get(k, 0) or 0
                c = (u.get("cost") or {})
                for k in cost_total:
                    cost_total[k] += c.get(k, 0.0)

    # If the run was aborted before agent_end, recover usage/cost from the
    # turn_end messages we already saw (better an estimate than zeros).
    if not agent_ended:
        for e in events:
            if e.get("type") != "turn_end":
                continue
            m = e.get("message") or {}
            if m.get("role") != "assistant":
                continue
            u = m.get("usage") or {}
            for k in usage_total:
                usage_total[k] += u.get(k, 0) or 0
            c = (u.get("cost") or {})
            for k in cost_total:
                cost_total[k] += c.get(k, 0.0)

    final_text = texts[-1] if texts else ""
    return {
        "turns": turns, "db_queries": db_queries, "raw_text": final_text,
        "all_text": texts, "executed_sqls": executed_sqls, "tool_calls": tool_calls,
        "successful_sqls": successful_sqls,
        "final_response": final_text if last_stop_reason == "stop" else "",
        "usage": usage_total, "cost": cost_total, "model": model, "provider": provider,
        "subagent_calls": subagent_calls, "subagent_turns": subagent_turns,
        "retry_count": retry_count,
        "api_error": last_error if last_stop_reason == "error" else None,
    }
