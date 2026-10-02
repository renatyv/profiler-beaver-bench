#!/usr/bin/env python3
"""Create the compact metadata file in a one-off Docker agent sandbox.

An agent distills `profiles/<schema>.md` + `schema-links/<schema>.md` into the
20–50-line `generated-metadata/<schema>.md` used by the metadata arm. The
benchmark questions, answers, and dataset JSON files are deliberately absent
from the sandbox, so nothing about the gold queries can leak into the summary.
"""
from __future__ import annotations

import argparse
import os
import subprocess
import tempfile
import uuid
from pathlib import Path

from . import config, network

_PI_TOOLS = "bash,read,write,edit,grep,find,ls"


def _prompt(database: str, max_turns: int) -> str:
    probe = ("You may use the read-only mysql CLI against `$BEAVER_DB` to clarify only "
             "ambiguous table or column meanings.")
    return f"""You are documenting the MySQL database `{database}`, not answering benchmark questions.

Your only supplied reference files are `/inputs/profile.md` and `/inputs/schema-links.md`.
Read both. The benchmark questions, answers, and all dataset JSON files are deliberately absent;
do not try to find them. {probe}
Never use SELECT * and every SELECT must have LIMIT 10 (LIMIT
100 is the absolute maximum). Do not copy raw rows, IDs, or value dumps into the result.

Write exactly one concise Markdown file at `/output/{database}.md` with:
1. `# Additional Metadata`
2. `## Clarified Semantics`: only table/column meanings that are not already clear in the profile.
   When sibling tables have overlapping names or columns, contrast their purpose, row grain,
   coverage, and appropriate use in one bullet. Probe only ambiguous siblings; do not enumerate
   every table or maintain a catalog of table-specific rules.
3. `## Potential Join Strategies`: non-obvious, useful joins derived from schema-links, including
   join predicates and any cardinality/filter caveat.

Use factual short bullets. Do not include SQL answers, benchmark content, or a restatement of the
profile/schema-links. Report observed coverage/cardinality instead of blanket default join types or
business filters. Use no more than {max_turns} agent turns. Finish only after the output file exists."""


def _base_argv(max_turns: int, output_dir: Path, extra_docker: list[str]) -> list[str]:
    """Docker prefix + pi argv. Per-engine mounts/env must stay in the docker
    part: after the image they would reach pi, whose `-v` means --version."""
    proxy = f"http://{config.EGRESS_PROXY_CONTAINER}:{config.EGRESS_PROXY_PORT}"
    return [
        "docker", "run", "--rm", "--name", f"beaver-metadata-{uuid.uuid4().hex}",
        "--network", config.AGENT_NET_SANDBOX, "--memory", config.CONTAINER_MEMORY,
        "--cpus", config.CONTAINER_CPUS, "--pids-limit", config.CONTAINER_PIDS_LIMIT,
        "--cap-drop", "ALL", "--security-opt", "no-new-privileges", "--workdir", "/workspace",
        "-v", f"{output_dir}:/output",
        "-v", f"{config.HARNESS_DIR / 'turn_guard.ts'}:/extensions/turn_guard.ts:ro",
        "-v", f"{config.HARNESS_DIR / 'openrouter_models.json'}:/home/node/.pi/agent/models.json:ro",
        "-e", f"HTTPS_PROXY={proxy}", "-e", f"HTTP_PROXY={proxy}",
        "-e", "OPENROUTER_API_KEY=" + os.environ.get("OPENROUTER_API_KEY", ""),
        "-e", f"BEAVER_MAX_TURNS={max_turns}",
        *extra_docker,
        "--entrypoint", "pi", config.CONTAINER_IMAGE,
        "-p", "--no-session", "--offline", "--no-extensions", "--no-skills",
        "--no-prompt-templates", "--no-context-files", "--no-themes", "-e", "/extensions/turn_guard.ts",
        "--tools", _PI_TOOLS, "--thinking", config.PI_THINKING,
        "--provider", config.DEFAULT_PROVIDER, "--model", config.DEFAULT_MODEL_ID,
    ]


def _docker_argv(db_label: str, max_turns: int, output_dir: Path) -> list[str]:
    database = config.mysql_db_for(db_label)
    extra = [
        "-v", f"{config.profile_path(db_label)}:/inputs/profile.md:ro",
        "-v", f"{config.schema_links_path(db_label)}:/inputs/schema-links.md:ro",
        "-e", f"NO_PROXY={config.MYSQL_HOST_CONTAINER},localhost,127.0.0.1",
        "-e", f"MYSQL_HOST={config.MYSQL_HOST_CONTAINER}",
        "-e", f"MYSQL_PORT={config.MYSQL_PORT_CONTAINER}",
        "-e", f"MYSQL_USER={config.AGENT_MYSQL_USER}",
        "-e", f"MYSQL_PASSWORD={config.AGENT_MYSQL_PWD}",
        "-e", f"MYSQL_PWD={config.AGENT_MYSQL_PWD}", "-e", f"BEAVER_DB={database}",
    ]
    return _base_argv(max_turns, output_dir, extra) + [_prompt(database, max_turns)]


def _run_agent(argv: list[str]) -> subprocess.CompletedProcess:
    """Run one metadata container. Killing the docker CLI on a timeout leaves
    the container running, so tear it down explicitly; retry once because a
    hung model turn is usually transient."""
    for _ in range(2):
        try:
            return subprocess.run(argv, capture_output=True, text=True,
                                  timeout=config.PI_WALL_CLOCK)
        except subprocess.TimeoutExpired:
            subprocess.run(["docker", "rm", "-f", argv[argv.index("--name") + 1]],
                           capture_output=True, timeout=30)
    raise subprocess.TimeoutExpired(argv, config.PI_WALL_CLOCK)


def run(db_label: str, max_turns: int = 12) -> Path:
    if not config.profile_path(db_label).is_file() or not config.schema_links_path(db_label).is_file():
        raise FileNotFoundError("generate the profile and schema links before metadata")
    config.GENERATED_METADATA_DIR.mkdir(exist_ok=True)
    network.setup({config.mysql_db_for(db_label)})
    output = config.metadata_path(db_label)
    with tempfile.TemporaryDirectory(dir=config.GENERATED_METADATA_DIR) as temp:
        temporary_output = Path(temp) / f"{db_label}.md"
        result = _run_agent(_docker_argv(db_label, max_turns, Path(temp)))
        if result.returncode:
            detail = (result.stderr or result.stdout)[-2000:].strip()
            raise RuntimeError(f"metadata agent failed with exit code {result.returncode}: {detail}")
        if not temporary_output.is_file() or not temporary_output.read_text(encoding="utf-8").strip():
            raise RuntimeError("metadata agent finished without writing output")
        temporary_output.replace(output)
    return output


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", choices=list(config.DATASETS), default="neutron")
    parser.add_argument("--max-turns", type=int, default=12)
    args = parser.parse_args(argv)
    print(run(args.database, args.max_turns))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
