# custom-bench

Does a pre-generated [db-snooper](https://github.com/renatyv/db-snooper) database profile improve a coding agent's execution accuracy on [BEAVER](https://huggingface.co/datasets/BeaverBench/beaver), compared with raw read-only database access?

The latest recorded run shows no improvement from the profile, but its 30-question sample is too small to establish an effect. The current harness uses protocol v12; the recorded results below were produced with v11, before previews switched to a session row cap.

## Latest recorded results

September 30, 2026: 10 questions per database, 30 distinct questions and 60 agent attempts across `raw` and `profile`. Both arms used [pi](https://pi.dev/), `openai/gpt-6-luna` via OpenRouter, low reasoning effort, and a 15-turn budget. Run directories are `results/<db>__main__n10_v11-openai-gpt-6-luna-low-t15/`.

Execution accuracy requires the same number of columns and matching row values as the gold query. Columns are compared positionally; duplicate rows count, and a top-level gold `ORDER BY` makes row order significant.

| Database (10 questions each) | Raw | + Profile |
|---|---:|---:|
| neutron | 3 | 2 |
| nova | 1 | 1 |
| dw | 0 | 0 |
| **Total (of 30 per arm)** | **4 (13.3%)** | **3 (10.0%)** |

| Pooled metric | Raw | + Profile |
|---|---:|---:|
| Input tokens, including cache reads/writes | 1,219,412 | 2,934,992 |
| Mean turns per question | 6.0 | 6.8 |
| Mean DB queries per question | 10.87 | 4.13 |
| Reported cost (USD) | $0.056408 | $0.099402 |

The profile reduced DB queries by about 62%, while using 2.4× input tokens and 1.76× reported cost. All 30 gold queries succeeded; no questions were excluded for gold failures. Of 60 predictions, 59 executed successfully and seven matched gold.

These results include known issues: outer preview `LIMIT 100` clauses remained in both answers to `dw_4522`, and in the profile answer to `dw_808` (which also had a syntax error). Some gold queries also differ from the question wording, including projection order and the definition of an overall average. Scores measure agreement with gold, not independent correctness against the question. Protocol v12 removes the need to add sampling limits to preview SQL; it has not yet produced a recorded benchmark run.

Open `results-viz.html` in a browser and select the `results/` folder. The per-question drill-down shows multiple observed errors together, including wrong cardinality and wrong column count, with answer/gold row and column counts. These diagnostics also work on existing records containing those counts.

## Experiment arms

- `raw` — agent + read-only MySQL access, nothing else.
- `profile` — raw access + `profile.md` and `schema-links.md` in the agent's workspace, with the profile's table-of-contents index (table → line ranges, ~1 KB) inlined into the prompt so no turns are spent discovering it. The full profile is never injected; the agent reads only the relevant profile ranges.

`profile_no_links` is the schema-linker ablation: the same profile and TOC as `profile`, without the schema-links file or its prompt instruction. To reuse the latest 100-question manifests without rerunning the existing arms:

```bash
BEAVER_AGENT=pi uv run python run_experiment.py --phase main \
  --samples neutron=100 nova=100 dw=100 --arms profile_no_links \
  --model openai/gpt-6-luna --effort low --max-turns 15 --workers 4
```

A third arm — `metadata`, a compact 20–50-line summary inlined into the prompt — was used in an earlier experiment and was retired. The latest run contains only `raw` and `profile`.

All arms share the agent, prompt instructions, error-avoidance checklist, tools, model, and caps. The default evaluation budget is 15 turns and 600 seconds per question; exhausting either counts as an incorrect answer. Only transient provider/API failures are retried.

From protocol v12, previews use session `SQL_SELECT_LIMIT=100` instead of adding sampling limits to candidate SQL. Explicit question-required limits are preserved; final scoring uses a separate uncapped connection.

From protocol v11, final answers must contain one complete `<ans>` block. The prompt requires successful validation of the unchanged final candidate. Preview connections bound otherwise unbounded SELECT results through the session setting; explicit SQL limits override that setting. The harness tracks successful executions but scores the final SQL on its result, without enforcing a match to a preview. The scorer executes final SQL outside the model context. Gold queries execute once per question per dataset invocation and their results are shared across arms; a gold failure excludes that question from every arm and the paired comparison, is listed in the summary, and makes the command exit unsuccessfully. Rerunning retries gold failures without reusing their failed executions.

## Isolation model

Each agent question gets `docker run --rm` on the internal `beaver-sandbox` network. It has an empty `/workspace`, runs as the non-root `node` user, has no Docker socket or repo mount, and is deleted after the run. A wall-clock timeout explicitly force-removes the container as well.

The only permitted connections are:

- MySQL at `beaver-mysql:3306`, via a separate account that is reset at experiment startup to `SELECT` on `neutron`, `nova`, and `dw` only.
- `https://openrouter.ai`, via `beaver-egress-proxy`. The proxy is the only container with internet access and accepts `CONNECT` only for the exact allow-listed hostname.

The host's loader/scorer credentials and coding-agent configuration are never mounted into an agent. The runner mounts only its own read-only agent configuration and pins the selected model. This prevents filesystem state from one question reaching the next and prevents arbitrary internet access. It cannot prevent the required OpenRouter model call itself from seeing the prompt and tool outputs.

## Setup

Prerequisites: Docker (or OrbStack), `uv`, and the `mysql` client on PATH.

1. Load BEAVER into MySQL (one-time; the dumps are ~2 GB total):

```bash
docker run -d --name beaver-mysql -p 3307:3306 \
  -e MYSQL_ROOT_PASSWORD=root mysql:9.3

# Download neutron.sql, nova.sql, dw.sql from
# https://huggingface.co/datasets/BeaverBench/beaver-db
# Each dump creates its own schema and data:
for db in neutron nova dw; do
  mysql -h 127.0.0.1 -P 3307 -u root -p < $db.sql
done

# Privileged harness account (.env defaults to beaver/beaver):
mysql -h 127.0.0.1 -P 3307 -u root -p -e "
  CREATE USER 'beaver'@'%' IDENTIFIED BY 'beaver';
  GRANT ALL PRIVILEGES ON *.* TO 'beaver'@'%' WITH GRANT OPTION;"
```

2. Configure and install:

```bash
cp .env.example .env    # then fill in your OPENROUTER_API_KEY
uv sync
```

`data/` (questions, gold SQL, table metadata) is committed, so the harness is runnable as-is; `uv run --group data python data/download_hf.py` rebuilds it from Hugging Face if needed.

3. Build the sandbox images:

```bash
make agent-image
make proxy-image
```

4. The frozen artifacts under `profiles/` and `schema-links/` are committed — the exact bytes used by the profile arm. Regenerate them with `make generate-profiles` and `make generate-schema-links` (db-snooper and schema-linker are installed as dependencies). The profile arm inlines the *enriched* TOC (`generated-metadata/<db>.toc.md`): the db-snooper index plus a one-line description per table, built once by `make generate-enriched-toc` — an agent distills the profile, and the harness merges the descriptions back in code so line ranges and row counts stay byte-exact. Until that file exists, the plain TOC is used (the protocol fingerprint hashes whichever file runs, so the two never mix in one cache). `make generate-metadata` still rebuilds the retired arm's summaries if you ever need them.

## Run

```bash
uv run python run_experiment.py --dataset neutron --phase phase0   # sanity: 1 question, all arms
make benchmark-pilot                                               # 20 questions per DB
make benchmark-post                                                # 100 questions per DB, both arms
```

`make benchmark-post` runs 100 questions per database across both arms (300 distinct questions, 600 agent attempts) with `--model openai/gpt-6-luna --effort low` and four workers. `make benchmark-pilot` uses 20 questions per database with the same model and worker settings. These targets run the current protocol; they do not reproduce the v11 results above.

Useful variants:

```bash
uv run python run_experiment.py --phase main --samples neutron=100 nova=80 dw=50 --arms raw profile
uv run python run_experiment.py --dataset neutron --phase pilot --estimate-cost
uv run python run_experiment.py --dataset neutron --phase pilot --score-only
```

At startup the runner creates the two networks, attaches MySQL to the internal one, starts the proxy, and provisions the SELECT-only `beaver_agent` account. The privileged host MySQL credentials come from `.env` (`BEAVER_MYSQL_*` or `MYSQL_*`). Do not set `BEAVER_AGENT_MYSQL_PWD` unless a stable debugging password is necessary; otherwise a new random password is used for each experiment process.

## Records, caching, and protocol fingerprints

Completed records are reused only when their protocol fingerprint matches the current prompts, artifacts, model, runner, reasoning effort, and budgets — so a prompt or budget change cannot silently mix incompatible results. Run ids carry the protocol identity (version, model, effort, turn budget), and records from a different protocol found in a results file are archived as `arm<N>.jsonl.stale-<ts>` rather than overwritten. While pi runs, the progress bar shows the latest completed agent turn and database-query count.

## Switch coding agents

The default is pi. Set `BEAVER_AGENT` before a run; all choices keep the same fresh container, SELECT-only MySQL account, and OpenRouter-only proxy:

```bash
BEAVER_AGENT=claude  uv run python run_experiment.py --dataset neutron --phase phase0
BEAVER_AGENT=opencode uv run python run_experiment.py --dataset neutron --phase phase0
BEAVER_AGENT=codex   uv run python run_experiment.py --dataset neutron --phase phase0
```

Choose any OpenRouter model with `--model`; its slug is passed through unchanged (an optional `openrouter/` prefix is accepted). Reasoning effort defaults to `low` and can be changed with `--effort`. Claude Code is configured with OpenRouter's Anthropic-compatible endpoint; Codex and OpenCode use its OpenAI-compatible endpoint. Pi and Claude have a CLI turn cap; Codex and OpenCode retain the prompt budget and the same 600-second container wall-clock cap. Non-pi runs record execution accuracy, but their CLI telemetry is deliberately reported as unavailable rather than a false zero; use pi when you need turns, database-query counts, tokens, or cost projections.

`--no-container` is a legacy debugging path. It runs pi on the host with `sql_exec.ts`; it does not provide the container isolation described above.

## Review run results with OpenRouter

From `custom-bench/`, loop over all directories in `results/` and write to a new
output directory (existing outputs are never overwritten):

```bash
uv run python -m harness.analyze_results \
  --output analysis/all-results
```

To select specific runs, pass one or more `results/<run>` directories as positional
arguments. All runs contribute to the same aggregate review.
Progress shows completed questions, the current run/question, elapsed time and an
ETA; the aggregate review shows an indeterminate bar while its request runs.

The script joins arm records to their frozen run manifests. Every recorded question
gets an independent OpenRouter chat-completion request with only its question, gold SQL, final candidates
from available arms, and scoring diagnostics. It asks whether each candidate is
actually wrong, including possible gold/wording conflicts and uncertainty.
Reviews are static: each request has no tools, database credentials, profiles,
or previous reviews. The script uses Python's stdlib HTTP client directly.

`sentences.txt` targets 80 characters per verdict and accepts nonempty verdicts
under 200 characters with a warning above 80 (excluding the run/question prefix).
Line wrapping is normalized and invalid replies are
retried up to three attempts. `reviews.jsonl` keeps the same
verdicts with run/question IDs. A separate request reads all saved verdicts and
writes `summary.md`. `inputs.json` records the supplied evidence. Completed verdicts
remain on disk if a later call fails. Add `--resume` with the same output directory
to skip completed reviews and regenerate the aggregate report. Saved inputs must
match, and saved verdicts must be under 200 characters; keep the same model
and effort when resuming. Longer verdicts require a new output directory.
Transient HTTP errors and timeouts are also retried with a short backoff;
exhausted retries report the final API error with API keys redacted. Permanent
HTTP errors such as invalid credentials fail immediately.

Use `--model <OpenRouter slug>` for the reviewers and optionally `--summary-model
<slug>` for synthesis (otherwise the same model runs in a separate request).
The default model/effort follows `PI_MODEL`/`PI_THINKING`; override effort with
`--effort`. `--timeout` defaults to 60 seconds per API request. Only
`OPENROUTER_API_KEY` and the local result/manifest files are required. Add
`--dry-run` to save inputs without LLM calls.

## Verify the boundary

After a run, the sandbox should be internal and contain only the proxy and MySQL. The egress network should contain only the proxy.

```bash
docker network inspect beaver-sandbox
docker network inspect beaver-net
docker run --rm --network beaver-sandbox --entrypoint sh beaver-agent -lc \
  'curl --noproxy "*" --connect-timeout 5 -I https://example.com || true; \
   curl -x http://beaver-egress-proxy:8888 -I https://example.com || true'
```

The direct request must fail because the network has no internet route; the proxied request must fail with `CONNECT tunnel failed, response 403`. A request to `https://openrouter.ai` through that proxy is the one allowed external route.

## Layout

```text
run_experiment.py           phase orchestrator (phase0 | pilot | main)
harness/
  runner_container.py       default ephemeral-container runner
  network.py                network + SELECT-only MySQL account setup
  egress/egress-proxy.js    exact-host HTTPS CONNECT allow-list
  turn_guard.ts             hard agent turn cap
  pi_extension/sql_exec.ts  purpose-built SQL tool
  prompts.py                arm-specific prompts
  scorer.py                 execution-accuracy scorer
  generate_profiles.py      db-snooper driver
  generate_schema_links.py  schema-linker driver
  generate_metadata.py      compact-metadata generation sandbox
  generate_enriched_toc.py  per-table TOC descriptions sandbox + merge
  setup_openrouter.py       one-time pi/OpenRouter registration helper
Dockerfile.agent            coding-agent CLIs + analytics tools image
Dockerfile.proxy            egress proxy image
data/                       BEAVER splits (questions + gold SQL + tables)
profiles/                   db-snooper profiles + table-of-contents indexes
schema-links/               schema-linker join hints
generated-metadata/         enriched TOCs (default for the profile arm) + compact metadata summaries (retired arm; kept for regeneration)
results-viz.html            offline viewer for results/ directories
```

## License

[MIT](LICENSE)
