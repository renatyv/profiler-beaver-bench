#!/usr/bin/env python3
"""Build the enriched profile TOC in a one-off Docker agent sandbox.

An agent reads `profiles/<schema>.md` (plus the plain TOC and schema-links)
and writes one line per table: `` `table`: short description``. The
harness — never the agent — merges those descriptions into the db-snooper
TOC, so row counts and line ranges stay byte-exact and every table is
guaranteed to appear exactly once. The merged file,
`generated-metadata/<schema>.toc.md`, is what the profile arm inlines into
its prompt (config.resolved_toc_path_for prefers it over the plain TOC).

The benchmark questions, answers, and dataset JSON files are deliberately
absent from the sandbox, so nothing about the gold queries can leak into the
descriptions.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import re
import tempfile
from pathlib import Path

from . import config, network
from .generate_metadata import _base_argv, _run_agent

# `` `table` (rows=N): lines A-B `` — one per table in the db-snooper TOC.
_TOC_TABLE_LINE = re.compile(r"^`([^`]+)` \(rows=\d+\): lines \d+-\d+$")
# `` `table`: description `` — the only lines the agent may emit.
_DESCRIPTION_LINE = re.compile(r"^`([^`]+)`:\s*(\S.*)$")

# Hard ceiling so a runaway description cannot bloat the inlined index
# (~20 words in the prompt; 240 chars leaves room for terse models).
_MAX_DESCRIPTION_CHARS = 240
# "Each row …"-style openers are filler next to the table name and row count
# already printed on the TOC line; the prompt bans them and parse rejects them.
_ROW_OPENER = re.compile(r"^(each|one|this)\s+(single\s+)?row\b", re.IGNORECASE)


def _prompt(database: str, max_turns: int) -> str:
    probe = ("You may use the read-only mysql CLI against `$BEAVER_DB` to clarify only "
             "ambiguous table meanings.")
    return f"""You are documenting the MySQL database `{database}`, not answering benchmark questions.

Your only supplied reference files are `/inputs/profile.md`, `/inputs/toc.md`, and
`/inputs/schema-links.md`. `/inputs/toc.md` lists every table in order. The benchmark
questions, answers, and all dataset JSON files are deliberately absent; do not try to
find them. {probe}
Never use SELECT * and every SELECT must have LIMIT 10 (LIMIT
100 is the absolute maximum). Do not copy raw rows, IDs, or value dumps into the result.

Write exactly one description line per table, in the `/inputs/toc.md` order, to
`/output/{database}.descriptions.md`, in this format and nothing else:

`table_name`: one short description of the table (a compact fragment is fine).

Rules for each description:
- At most 20 words, English, a single line.
- Table's purpose
- Never open with "Each row", "One row", or "This row" — the TOC line already names the
  table and its row count
- How the table is different from sibling (near-duplicate names or columns, e.g. current vs
  history vs load copies)
- When many tables share a name prefix (`lbaas_`, `shadow_`, `fclt_`) - do not re-explain that family in every
  line; spend the words on what distinguishes this table.
- Name versions and product families concretely, reusing the terms the supplied
  files use ("LB-v2 pool", not "newer LBaaS pool"; "LB-v1", not "legacy pool").
- Do not enumerate columns and do not repeat counts or line ranges.

The file must contain only those lines — no header, no markdown fences, no other
text. Use no more than {max_turns} agent turns. Finish only after the output file exists."""


def parse_descriptions(text: str, expected: list[str]) -> dict[str, str]:
    """Validate the agent's description list against the TOC table names.

    Raises ValueError naming the exact violation, so a retry or failure is
    diagnosable from the log alone.
    """
    descriptions: dict[str, str] = {}
    for lineno, raw in enumerate(text.splitlines(), start=1):
        line = raw.strip()
        if not line:
            continue
        match = _DESCRIPTION_LINE.match(line)
        if not match:
            raise ValueError(f"line {lineno} is not a `table`: description entry: {line!r}")
        table, description = match.group(1), match.group(2).strip()
        if len(description) > _MAX_DESCRIPTION_CHARS:
            raise ValueError(f"description for `{table}` is {len(description)} chars "
                             f"(max {_MAX_DESCRIPTION_CHARS})")
        if _ROW_OPENER.match(description):
            raise ValueError(f"description for `{table}` opens with a row-opener; "
                             f"lead with the content, not 'Each row …': {description!r}")
        if table in descriptions:
            raise ValueError(f"table `{table}` described more than once")
        descriptions[table] = description
    missing = [t for t in expected if t not in descriptions]
    extra = [t for t in descriptions if t not in set(expected)]
    if missing:
        raise ValueError(f"no description for {len(missing)} table(s): {', '.join(missing[:10])}"
                         + (" ..." if len(missing) > 10 else ""))
    if extra:
        raise ValueError(f"descriptions for unknown table(s): {', '.join(extra[:10])}"
                         + (" ..." if len(extra) > 10 else ""))
    return descriptions


def merge_toc(toc_text: str, descriptions: dict[str, str]) -> str:
    """Append ` — description` to each table line, leaving everything else
    (frontmatter, Relationships/Summary lines) byte-identical, and record the
    enrichment provenance in the frontmatter."""
    lines = toc_text.splitlines()
    for i, line in enumerate(lines):
        match = _TOC_TABLE_LINE.match(line)
        if match and match.group(1) in descriptions:
            lines[i] = f"{line} — {descriptions[match.group(1)]}"
    merged = "\n".join(lines) + "\n"
    marker = "\n---\n"
    if merged.startswith("---") and marker in merged:
        provenance = (f"enriched_model: {config.DEFAULT_PROVIDER}/{config.DEFAULT_MODEL_ID}\n"
                      f"enriched_at_utc: {_dt.datetime.now(_dt.timezone.utc).isoformat()}\n"
                      f"toc_sha256: {hashlib.sha256(toc_text.encode()).hexdigest()}\n")
        merged = merged.replace(marker, "\n" + provenance + marker, 1)
    return merged


def _docker_argv(db_label: str, max_turns: int, output_dir: Path) -> list[str]:
    database = config.mysql_db_for(db_label)
    extra = [
        "-v", f"{config.profile_path(db_label)}:/inputs/profile.md:ro",
        "-v", f"{config.profile_toc_path_for(database)}:/inputs/toc.md:ro",
        "-v", f"{config.schema_links_path(db_label)}:/inputs/schema-links.md:ro",
        "-e", f"NO_PROXY={config.MYSQL_HOST_CONTAINER},localhost,127.0.0.1",
        "-e", f"MYSQL_HOST={config.MYSQL_HOST_CONTAINER}",
        "-e", f"MYSQL_PORT={config.MYSQL_PORT_CONTAINER}",
        "-e", f"MYSQL_USER={config.AGENT_MYSQL_USER}",
        "-e", f"MYSQL_PASSWORD={config.AGENT_MYSQL_PWD}",
        "-e", f"MYSQL_PWD={config.AGENT_MYSQL_PWD}", "-e", f"BEAVER_DB={database}",
    ]
    return _base_argv(max_turns, output_dir, extra) + [_prompt(database, max_turns)]


def _toc_tables(toc_text: str) -> list[str]:
    return [m.group(1) for m in map(_TOC_TABLE_LINE.match, toc_text.splitlines()) if m]


def run(db_label: str, max_turns: int = 16) -> Path:
    for path in (config.profile_path(db_label), config.profile_toc_path(db_label),
                 config.schema_links_path(db_label)):
        if not path.is_file():
            raise FileNotFoundError(f"generate the profile, TOC, and schema links first: {path}")
    toc_text = config.profile_toc_path(db_label).read_text(encoding="utf-8")
    expected = _toc_tables(toc_text)
    config.GENERATED_METADATA_DIR.mkdir(exist_ok=True)
    network.setup({config.mysql_db_for(db_label)})
    output = config.enriched_toc_path(db_label)
    with tempfile.TemporaryDirectory(dir=config.GENERATED_METADATA_DIR) as temp:
        database = config.mysql_db_for(db_label)
        agent_output = Path(temp) / f"{database}.descriptions.md"
        # One retry: a strict-format miss (dropped table, overlong line) is
        # usually transient, same as the hung-turn retry in _run_agent.
        last_error: ValueError | None = None
        for _ in range(2):
            result = _run_agent(_docker_argv(db_label, max_turns, Path(temp)))
            if result.returncode:
                detail = (result.stderr or result.stdout)[-2000:].strip()
                raise RuntimeError(f"enriched-TOC agent failed with exit code "
                                   f"{result.returncode}: {detail}")
            if not agent_output.is_file() or not agent_output.read_text(encoding="utf-8").strip():
                raise RuntimeError("enriched-TOC agent finished without writing output")
            try:
                descriptions = parse_descriptions(
                    agent_output.read_text(encoding="utf-8"), expected)
                break
            except ValueError as e:
                last_error = e
        else:
            raise RuntimeError(f"enriched-TOC agent output invalid after retry: {last_error}")
        merged = merge_toc(toc_text, descriptions)
        (Path(temp) / "merged.md").write_text(merged, encoding="utf-8")
        (Path(temp) / "merged.md").replace(output)
    return output


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", choices=list(config.DATASETS), default="neutron")
    parser.add_argument("--max-turns", type=int, default=16)
    args = parser.parse_args(argv)
    print(run(args.database, args.max_turns))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
