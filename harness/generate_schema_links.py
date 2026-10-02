#!/usr/bin/env python3
"""Generate schema-link reports with schema-linker.

Each dataset is a single MySQL schema; schema-linker compares column value
sets to infer which columns belong together and writes
`schema-links/<schema>.md`.
"""
from __future__ import annotations

import argparse

from schema_linker import SchemaLinkOptions, link_schema
from schema_linker.progress import ProgressBar
from sqlalchemy import URL, create_engine
from sqlalchemy.engine import Engine

from . import config


def generate(database: str) -> str:
    progress_bar = ProgressBar("Linking", 0)

    def show_progress(current: int, total: int, item: str) -> None:
        nonlocal progress_bar
        if progress_bar.total != total:
            progress_bar.finish()
            progress_bar = ProgressBar("Linking", total)
            progress_bar.start(item)
            return
        progress_bar.update(current, item)

    engine: Engine = create_engine(URL.create(
        "mysql+pymysql", username=config.MYSQL_USER, password=config.MYSQL_PWD,
        host=config.MYSQL_HOST, port=config.MYSQL_PORT, database=database,
    ))
    try:
        report = link_schema(
            engine, SchemaLinkOptions(show_declared_links=True), progress=show_progress
        )
        progress_bar.finish("Schema linking complete")
        return report
    except Exception:
        progress_bar.finish()
        raise
    finally:
        engine.dispose()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", choices=list(config.DATASETS), default="neutron")
    args = parser.parse_args(argv)
    config.SCHEMA_LINKS_DIR.mkdir(exist_ok=True)
    config.schema_links_path(args.database).write_text(
        generate(config.mysql_db_for(args.database)), encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
