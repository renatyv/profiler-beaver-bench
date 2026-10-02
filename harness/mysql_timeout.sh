#!/bin/sh
/usr/bin/timeout "${BEAVER_QUERY_TIMEOUT:-20}s" /usr/bin/mysql --init-command="SET SESSION SQL_SELECT_LIMIT=100" "$@"
query_status=$?
if [ "$query_status" -eq 0 ] && [ -n "$BEAVER_SQL_SUCCESS_LOG" ]; then
  python3 - "$@" <<'PY'
import json, os, sys
args = sys.argv[1:]
for i, arg in enumerate(args):
    if arg in ("-e", "--execute") and i + 1 < len(args):
        sql = args[i + 1]
        break
    if arg.startswith("--execute="):
        sql = arg.partition("=")[2]
        break
else:
    sql = None
if sql:
    with open(os.environ["BEAVER_SQL_SUCCESS_LOG"], "a") as log:
        log.write(json.dumps(sql) + "\n")
PY
fi
exit "$query_status"
