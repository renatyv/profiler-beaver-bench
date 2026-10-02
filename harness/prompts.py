"""Prompt construction for the raw-vs-profile experiment arms.

The system prompt is shared by every arm; the arm only changes which database
context the user turn supplies (none / profile files / compact metadata).
Cached records are keyed by a prompt hash, so any change here invalidates
prior runs automatically.
"""
from __future__ import annotations

from . import config

# Common text-to-SQL failure modes (grouping, schema linking, predicates, ...).
# Loaded once; spliced into the system prompt ONLY for arms with checklist=True.
_ERROR_CHECKLIST = (config.HARNESS_DIR / "error_avoidance_checklist.txt").read_text(
    encoding="utf-8").strip()

# The agentic system prompt with the checklist slot left as a placeholder. The
# slot is filled with the checklist text (checklist=True) or an empty string
# (checklist=False) by _agent_system() below.
_AGENT_SYSTEM_TEMPLATE = r"""\
You are an expert text-to-SQL agent targeting a MySQL database.

Use the `sql_exec` tool when it is available. Independent lookups may be issued
together in one turn.
Other supported agents expose `bash`; for those, run MySQL with:

  mysql --skip-ssl --init-command="SET SESSION SQL_SELECT_LIMIT=100" -D "$BEAVER_DB" -e "<SQL>"
The MySQL server is at $MYSQL_HOST:$MYSQL_PORT (user $MYSQL_USER, password in
$MYSQL_PWD). Each query should finish within {timeout}s.

Workflow:
1. Use any supplied database context first to choose tables and columns. It may be
   incomplete or stale, so query the database for anything it does not fully
   answer (missing columns, uncertain values/joins). If context is absent or
   insufficient, inspect only relevant tables. Batch independent DESCRIBE/SHOW
   calls in one turn. Use `SHOW TABLES` only when you cannot identify tables
   otherwise.
2. Reason about joins, filters, and aggregations needed to answer the question.
3. VALIDATION IS MANDATORY and supplied context never replaces it. By turn {validation_turn}, run the complete candidate query as a bounded preview against
   the database — even when the supplied context already describes the schema.
   Preview connections use SESSION SQL_SELECT_LIMIT=100 to bound returned rows
   without changing the candidate SQL. Execute the candidate exactly as intended
   for the final answer. NEVER add a sampling LIMIT 10 / LIMIT 100 to the query.
   Preserve any LIMIT required by the question, including bounds inside subqueries.
   Before answering, check the returned rows against the question:
    - Projection: the SELECT list returns exactly the columns the question
      asks for — remove any extra id, name, or aggregate columns.
    - Cardinality: DISTINCT only when the question says distinct/unique;
      LIMIT/top-N where a bounded number of rows is requested.
    - Values: literal values (strings, dates, IDs) match the question or database exactly.
   Then verify the query against the error checklist.
   If any check changes the query, use turn {repair_turn} to repair
   and execute the complete corrected query as a bounded preview again. An empty result may be valid.
   Investigate unexpected emptiness without inventing filters or values.
4. Output the validated candidate unchanged inside exactly one answer block.
   Include LIMIT only where required by the question, never for preview sampling.
   Make no changes after successful preview execution.

<ans>
<your final query>
</ans>

Rules:
- Run ONLY read-only statements (SELECT / WITH / SHOW / DESCRIBE / EXPLAIN) —
  never INSERT/UPDATE/DELETE/DROP. The database is shared; do not mutate it.
- Return exactly ONE final SELECT/WITH statement that answers the question.
- Do NOT wrap the final query in a transaction or procedure; it must run standalone.
- Do NOT include Markdown fences or commentary inside or after the final </ans>.
- Prefer explicit table-qualified columns. Respect MySQL syntax (backticks for
  reserved/odd-case identifiers).
- Budget: you have at most {max_turns} agent turns. Turn {max_turns} is reserved
  for your FINAL SQL response, so finish all tool use by turn {penultimate_turn}.
  Leave at least 1 (better 2) steps for final corrections before returning final answer.
{checklist_block}\
"""

# Trailer appended to the agentic system prompt when checklist=True. Indented to
# sit cleanly under the Rules block above.
_AGENT_CHECKLIST_BLOCK = """
Before finalizing your query, re-check it against this list of common
text-to-SQL errors and avoid them:

"""


def _agent_system(timeout: int, max_turns: int, checklist: bool) -> str:
    """Format the agentic system-prompt APPEND text, optionally with checklist."""
    return _AGENT_SYSTEM_TEMPLATE.format(
        timeout=timeout,
        max_turns=max_turns,
        penultimate_turn=max(0, max_turns - 1),
        validation_turn=max(1, max_turns - 2),
        repair_turn=max(1, max_turns - 1),
        checklist_block=(_AGENT_CHECKLIST_BLOCK + _ERROR_CHECKLIST + "\n") if checklist else "",
    )


def _toc_index_for(profile_key: str) -> str:
    """TOC body (table → line ranges, + descriptions when enriched) without
    the generator frontmatter."""
    text = config.resolved_toc_path_for(profile_key).read_text(encoding="utf-8")
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:].strip()
    return text.strip()


def agent_prompts(db_label: str, question: str, arm: str,
                  max_turns: int) -> tuple[str, str]:
    """Return (system_prompt, user_prompt) for an agentic arm.

    All arms share tooling, checklist, and base instructions. The arm only
    controls which frozen artifacts are supplied: the profile arm gets the
    profile's table-of-contents index inlined into the user turn (so no turns
    are spent discovering it) plus the full `profile.md` and `schema-links.md`
    as workspace files.
    """
    spec = config.arm_spec(arm)
    assert spec["tools"], f"agent_prompts called for non-agentic arm '{arm}'"
    system = _agent_system(
        timeout=config.MYSQL_QUERY_TIMEOUT,
        max_turns=max_turns,
        checklist=spec["checklist"],
    )
    db = config.mysql_db_for(db_label)
    context = []
    if spec["profile"]:
        index_kind = ("table → line ranges + one-line table descriptions"
                      if config.resolved_toc_path_for(db) == config.enriched_toc_path_for(db)
                      else "table → line ranges")
        context.append(
            f"DB profile ({db}) — index into `profile.md` ({index_kind}, "
            "already in your context, no need to look for it):\n\n"
            f"{_toc_index_for(db)}\n\n"
            "The full profile is the workspace file `profile.md`; read only the "
            "line ranges relevant to the question, using the index above."
            + (" `schema-links.md` contains candidate relationships inferred from "
               "the schema and data." if spec["schema_links"] else "")
        )
    grounding = "\n\n".join(context) if context else "(none supplied)"
    user = (
        f"Target MySQL database: `{db}`.\n\n"
        f"===== BEGIN SUPPLIED DATABASE CONTEXT =====\n{grounding}\n"
        f"===== END SUPPLIED DATABASE CONTEXT =====\n\n"
        f"Natural-language question:\n\"\"\"\n{question}\n\"\"\"\n\n"
        f"Return your FINAL SQL inside <ans>...</ans>."
    )
    return system, user
