"""MySQL helpers for the scorer (gold vs. predicted execution)."""
from __future__ import annotations

import threading
from typing import Any

import pymysql

from . import config


class QueryResult:
    __slots__ = ("rows", "error", "timed_out", "columns")

    def __init__(self, rows: list[tuple] | None, error: str | None, timed_out: bool,
                 columns: int | None = None):
        self.rows = rows
        self.error = error
        self.timed_out = timed_out
        self.columns = columns

    @property
    def ok(self) -> bool:
        return self.error is None and not self.timed_out


def connect(database: str):
    """Fresh read-only-ish connection to a BEAVER database."""
    return pymysql.connect(
        host=config.MYSQL_HOST,
        user=config.MYSQL_USER,
        password=config.MYSQL_PWD,
        database=database,
        port=config.MYSQL_PORT,
        connect_timeout=10,
        read_timeout=config.MYSQL_QUERY_TIMEOUT,
        write_timeout=config.MYSQL_QUERY_TIMEOUT,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.Cursor,  # tuples
    )


def execute(sql: str, database: str, timeout: float | None = None) -> QueryResult:
    """Execute SQL and return tuple rows. Bound by read_timeout + a wall-clock thread.

    Used by the scorer for BOTH gold and predicted SQL, so a fresh connection is
    opened each call to avoid cross-statement state.
    """
    timeout = timeout or config.MYSQL_QUERY_TIMEOUT
    result: QueryResult = QueryResult(None, None, False)

    def _run():
        try:
            conn = connect(database)
            try:
                with conn.cursor() as cur:
                    cur.execute(sql)
                    result.columns = len(cur.description or ())
                    result.rows = [tuple(r) for r in cur.fetchall()]
            finally:
                conn.close()
        except pymysql.err.OperationalError as e:
            msg = str(e)
            if "timeout" in msg.lower() or "lost connection" in msg.lower():
                result.timed_out = True
            else:
                result.error = msg
        except Exception as e:  # programming errors, syntax, etc.
            result.error = f"{type(e).__name__}: {e}"

    t = threading.Thread(target=_run, daemon=True)
    t.start()
    t.join(timeout + 5)  # small grace beyond the server read_timeout
    if t.is_alive():
        result.timed_out = True
        result.rows = None
    return result
