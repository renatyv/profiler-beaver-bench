#!/usr/bin/env python3
"""Run db-snooper to (re)generate the BEAVER database profiles.

Each dataset is a single MySQL schema; db-snooper writes
`profiles/<schema>.md` plus its table-of-contents `profiles/<schema>.toc.md`.
"""
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

from . import config


def run_mysql(db_label: str) -> Path:
    subprocess.run(
        ["db-snooper", "profile", "--db-type", "mysql",
         "--database", config.mysql_db_for(db_label),
         "--host", config.MYSQL_HOST, "--port", str(config.MYSQL_PORT),
         "--user", config.MYSQL_USER, "--password", config.MYSQL_PWD,
         "--output", str(config.PROFILES_DIR)],
        check=True,
    )
    return config.profile_path(db_label)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", choices=list(config.DATASETS), default="neutron")
    args = parser.parse_args(argv)
    print(f"[profiles] {config.mysql_db_for(args.database)} -> {run_mysql(args.database)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
