#!/usr/bin/env python3
"""
Build BEAVER data files *locally* — no Hugging Face auth required.

Sources already present on this machine (no Hugging Face auth needed):
  * beaver-query/<split>-00000-of-00001.parquet  -> per-question annotations
  * beaver-db/tables/<split>-00000-of-00001.parquet -> OFFICIAL beaver-table
    schema metadata (column names/types, example rows, frequent values).
    This is the canonical dev_tables.json source and is used by default.
  * (optional) the `dw`/`neutron`/`nova` MySQL DBs -> richer, live example_rows,
    usable via --tables-from mysql if you want to deviate from the benchmark data.

Outputs (same layout/format that `data/download_hf.py` would produce):
  data/<split>/dev.json           full question set
  data/<split>/dev_sampled.json   random sample (seed 77, to match HF script)
  data/<split>/dev_tables.json    {table_name: {db, table_name, column_names,
                                                column_types, example_rows,
                                                example_columns}}

Usage:
  python data/build_local.py --datasets neutron nova dw --sample 100

Notes:
  * dev_sampled.json is a pure subset of dev.json, so SAMPLING THE QUESTIONS is
    100% local. The table *schema* lives in the separate `beaverbench/beaver-table`
    HF dataset, whose parquet dumps ship in beaver-db/tables/ — so we build
    dev_tables.json from those by default (no HF, no MySQL).
  * Default (--tables-from parquet): the official beaver-table data, exactly as
    the benchmark intends (ENUM/Oracle types, curated example_rows). dw contains
    nulls encoded as NaN, which we coerce to None for valid JSON.
  * Optional (--tables-from mysql): derive schemas live from MySQL instead, which
    fills example_rows for every non-empty table (richer prompts, but NOT the
    canonical benchmark data). Uses COLUMN_TYPE, first 3 rows, top-10 values.
"""
import argparse
import json
import os
import random
from datetime import date, datetime
from decimal import Decimal
from pathlib import Path

import pymysql
import pyarrow.parquet as pq


def json_default(o):
    """Serialize MySQL scalar types that json can't handle natively."""
    if isinstance(o, (datetime, date)):
        return o.isoformat()
    if isinstance(o, Decimal):
        return float(o)
    if isinstance(o, (bytes, bytearray)):
        try:
            return o.decode("utf-8")
        except Exception:
            return o.decode("latin-1", errors="replace")
    return str(o)


def clean_jsonable(o):
    """Recursively normalize values for valid JSON (NaN/inf -> None, etc.)."""
    import math
    if isinstance(o, float):
        return None if math.isnan(o) or math.isinf(o) else o
    if isinstance(o, (datetime, date)):
        return o.isoformat()
    if isinstance(o, Decimal):
        return float(o)
    if isinstance(o, (bytes, bytearray)):
        try:
            return o.decode("utf-8")
        except Exception:
            return o.decode("latin-1", errors="replace")
    if isinstance(o, dict):
        return {k: clean_jsonable(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [clean_jsonable(v) for v in o]
    return o


SCAN_LIMIT = 5000          # rows scanned per table for frequent-value sampling
EXAMPLE_ROWS = 3           # rows shown in prompts
TOP_N_VALUES = 10          # values per column (matches BEAVER "top-10 values")
SAMPLE_SEED = 77           # matches data/download_hf.py
BASE_DATA_DIR = Path(__file__).resolve().parent  # .../data
PARQUET_DIR = BASE_DATA_DIR.parent / "beaver-query"
TABLES_PARQUET_DIR = BASE_DATA_DIR.parent / "beaver-db" / "tables"


def parse_if_string(val, default_type=list):
    if isinstance(val, str):
        try:
            return json.loads(val)
        except Exception:
            return default_type()
    return val if val is not None else default_type()


def mysql_connect(database):
    return pymysql.connect(
        host=os.environ.get("MYSQL_HOST", "localhost"),
        user=os.environ.get("MYSQL_USER", "beaver"),
        password=os.environ.get("MYSQL_PASSWORD", ""),
        database=database,
        port=int(os.environ.get("MYSQL_PORT", "3307")),
        connect_timeout=10,
        read_timeout=60,
        charset="utf8mb4",
    )


def list_tables(conn):
    cur = conn.cursor()
    cur.execute("SELECT table_name FROM information_schema.tables "
                "WHERE table_schema = DATABASE() ORDER BY table_name")
    tables = [r[0] for r in cur.fetchall()]
    cur.close()
    return tables


def table_schema(conn, table):
    """Return (column_names, column_types) ordered by ordinal position."""
    cur = conn.cursor()
    cur.execute(
        "SELECT column_name, column_type FROM information_schema.columns "
        "WHERE table_schema = DATABASE() AND table_name = %s "
        "ORDER BY ordinal_position",
        (table,),
    )
    rows = cur.fetchall()
    cur.close()
    col_names = [r[0] for r in rows]
    col_types = [str(r[1]).upper() for r in rows]  # e.g. VARCHAR(36), BIGINT(20)
    return col_names, col_types


def safe_ident(name):
    """Backtick an identifier (handles reserved words / mixed case)."""
    return "`" + str(name).replace("`", "``") + "`"


def example_rows(conn, table, col_names, n=EXAMPLE_ROWS):
    cur = conn.cursor()
    try:
        cur.execute(f"SELECT {', '.join(safe_ident(c) for c in col_names)} "
                    f"FROM {safe_ident(table)} LIMIT %s", (n,))
        rows = [list(r) for r in cur.fetchall()]
    except Exception as e:
        print(f"    ! example_rows failed for {table}: {e}")
        rows = []
    finally:
        cur.close()
    return rows


def example_columns(conn, table, col_names, scan_limit=SCAN_LIMIT, top_n=TOP_N_VALUES):
    """Up to `top_n` most-frequent values per column over a bounded scan."""
    result = []
    for col in col_names:
        values = []
        cur = conn.cursor()
        try:
            sql = (f"SELECT {safe_ident(col)} FROM ("
                   f"SELECT {safe_ident(col)} FROM {safe_ident(table)} LIMIT %s) sub "
                   f"GROUP BY {safe_ident(col)} ORDER BY COUNT(*) DESC LIMIT %s")
            cur.execute(sql, (scan_limit, top_n))
            values = [r[0] for r in cur.fetchall()]
        except Exception as e:
            # Non-fatal: some columns (e.g. very wide text) may fail to group.
            print(f"    ! example_columns failed for {table}.{col}: {e}")
        finally:
            cur.close()
        result.append(values)
    return result


def build_tables_json_from_parquet(split):
    """Build dev_tables.json from the OFFICIAL beaver-table parquet dump.

    These ship in beaver-db/tables/<split>.parquet and are the canonical source.
    List fields are JSON-string-encoded; nulls appear as NaN (coerced to None).
    """
    src = TABLES_PARQUET_DIR / f"{split}-00000-of-00001.parquet"
    if not src.exists():
        raise FileNotFoundError(f"Missing {src}. No beaver-table parquet for '{split}'.")
    rows = pq.read_table(src).to_pylist()
    tables = {}
    for r in rows:
        entry = {
            "db": r.get("db"),
            "table_name": r.get("table_name"),
            "column_names": clean_jsonable(parse_if_string(r.get("column_names"))),
            "column_types": clean_jsonable(parse_if_string(r.get("column_types"))),
            "example_rows": clean_jsonable(parse_if_string(r.get("example_rows"))),
            "example_columns": clean_jsonable(parse_if_string(r.get("example_columns"))),
        }
        tables[entry["table_name"]] = entry
    print(f"    done: {len(tables)} tables (from {src.name})")
    return tables


def build_tables_json_from_mysql(database, db_label):
    print(f"Building dev_tables.json from MySQL database '{database}' ...")
    conn = mysql_connect(database)
    try:
        tables = {}
        all_tables = list_tables(conn)
        for i, t in enumerate(all_tables, 1):
            col_names, col_types = table_schema(conn, t)
            ex_rows = example_rows(conn, t, col_names)
            ex_cols = example_columns(conn, t, col_names)
            tables[t] = {
                "db": db_label,
                "table_name": t,
                "column_names": col_names,
                "column_types": col_types,
                "example_rows": ex_rows,
                "example_columns": ex_cols,
            }
            if i % 25 == 0:
                print(f"    ...{i}/{len(all_tables)} tables")
        print(f"    done: {len(tables)} tables")
        return tables
    finally:
        conn.close()


def build_questions_json(split):
    parquet = PARQUET_DIR / f"{split}-00000-of-00001.parquet"
    if not parquet.exists():
        raise FileNotFoundError(f"Missing {parquet}. The beaver-query parquet for "
                                f"'{split}' was not found.")
    table = pq.read_table(parquet)
    cols = table.column_names
    data = table.to_pylist()
    out = []
    for entry in data:
        out.append({
            "id": entry.get("id"),
            "question": entry.get("question"),
            "db": entry.get("db"),
            "sql": entry.get("sql"),
            "tables": parse_if_string(entry.get("tables")),
            "column_mapping": parse_if_string(entry.get("column_mapping"), dict),
            "join_keys": parse_if_string(entry.get("join_keys")),
            "domain_knowledge": parse_if_string(entry.get("domain_knowledge")),
            "sub_questions": parse_if_string(entry.get("sub_questions")),
            "sub_sqls": parse_if_string(entry.get("sub_sqls")),
            "category": entry.get("category"),
            "detailed_category": entry.get("detailed_category"),
            "contains_domain_knowledge": entry.get("contains_domain_knowledge"),
        })
    return out, cols


def build_domain_knowledge_combined(question_lists):
    """Flatten per-split question lists into one {id: domain_knowledge} map.

    Only questions whose `domain_knowledge` is a non-empty list are included;
    the result is sorted by id for stable diffs. Question ids are globally
    unique (prefixed by split), so no split nesting is needed.
    """
    combined = {}
    for split, questions in question_lists.items():
        for q in questions:
            dk = q.get("domain_knowledge") or []
            if dk:
                combined[q["id"]] = dk
    return {k: combined[k] for k in sorted(combined)}


def write_json(obj, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=4, ensure_ascii=False, default=json_default)


def report_table_coverage(questions, tables, split):
    """Warn if any question references a table missing from dev_tables.json."""
    table_keys_ci = {k.lower(): k for k in tables}
    missing = set()
    for q in questions:
        for t in q.get("tables", []):
            if str(t).lower() not in table_keys_ci:
                missing.add(t)
    if missing:
        print(f"  ⚠ {split}: {len(missing)} referenced table(s) not in dev_tables.json: "
              f"{sorted(missing)[:10]}{' ...' if len(missing) > 10 else ''}")
    else:
        print(f"  ✓ {split}: all referenced tables present in dev_tables.json")


def build_split(split, sample_size, do_tables, tables_from="parquet"):
    split_dir = BASE_DATA_DIR / split
    split_dir.mkdir(parents=True, exist_ok=True)

    questions, cols = build_questions_json(split)
    write_json(questions, split_dir / "dev.json")
    print(f"  dev.json: {len(questions)} questions (parquet cols: {len(cols)})")

    if sample_size and sample_size < len(questions):
        random.seed(SAMPLE_SEED)
        sampled = random.sample(questions, sample_size)
    else:
        sampled = questions
    write_json(sampled, split_dir / "dev_sampled.json")
    print(f"  dev_sampled.json: {len(sampled)} questions (seed={SAMPLE_SEED})")

    if do_tables:
        if tables_from == "parquet":
            print(f"Building dev_tables.json from beaver-table parquet ...")
            tables = build_tables_json_from_parquet(split)
        else:
            tables = build_tables_json_from_mysql(split, split)
        write_json(tables, split_dir / "dev_tables.json")
        print(f"  dev_tables.json: {len(tables)} tables")
        report_table_coverage(questions, tables, split)

    return questions


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--datasets", nargs="+", default=["neutron"],
                        help="splits to build (e.g. neutron nova dw)")
    parser.add_argument("--sample", type=int, default=100,
                        help="dev_sampled.json size (matches run.sh default)")
    parser.add_argument("--no-tables", action="store_true",
                        help="skip building dev_tables.json (questions only)")
    parser.add_argument("--tables-from", choices=["parquet", "mysql"], default="parquet",
                        help="source for dev_tables.json: 'parquet' = official "
                             "beaver-table dump (default, canonical); 'mysql' = derive "
                             "live schemas from the loaded BEAVER database")
    args = parser.parse_args()

    for split in args.datasets:
        print(f"\n=== Building '{split}' ===")
        build_split(split, args.sample, do_tables=not args.no_tables,
                    tables_from=args.tables_from)

    print("\nDone. Next: uv run python run_experiment.py --dataset neutron --phase phase0")


if __name__ == "__main__":
    main()
