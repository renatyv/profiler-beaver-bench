from __future__ import annotations

import unittest
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
from unittest.mock import patch

import run_experiment
from harness import manifest, metrics, mysql_io, prompts, scorer


class BenchmarkTests(unittest.TestCase):
    def test_profile_without_links_keeps_profile_but_omits_linker(self) -> None:
        from harness import runner_container
        import subprocess
        linked = prompts.agent_prompts("neutron", "question", "profile", 15)
        unlinked = prompts.agent_prompts("neutron", "question", "profile_no_links", 15)
        self.assertEqual(linked[0], unlinked[0])
        self.assertIn("profile.md", unlinked[1])
        self.assertNotIn("schema-links.md", unlinked[1])
        with (patch("harness.runner_container.network.is_ready", return_value=True),
              patch("harness.runner_container.subprocess.run",
                    return_value=subprocess.CompletedProcess([], 0, "", "")) as run):
            runner_container.run("neutron", "question", "profile_no_links", 15, Path("/tmp/x"))
        argv = run.call_args.args[0]
        self.assertTrue(any(":/workspace/profile.md:ro" in arg for arg in argv))
        self.assertFalse(any("schema-links.md" in arg for arg in argv))
        with patch.object(prompts.config, "schema_links_path_for", side_effect=AssertionError):
            run_experiment._protocol_fingerprint({"question": "question"}, "profile_no_links", "neutron", 15)


    def test_final_repair_is_scored_without_matching_a_preview(self) -> None:
        rec = {"pred_sql": "SELECT 1;", "successful_sqls": ["SELECT 2 LIMIT 100"],
               "final_sql_validated": False}  # historical flags must not penalize scoring
        gold = mysql_io.QueryResult([(1,)], None, False, 1)
        with patch("harness.scorer._execute", return_value=gold):
            run_experiment._score(rec, {"id": "q", "sql": "SELECT 1"}, "neutron", gold)
        self.assertTrue(rec["correct"])
        self.assertEqual(rec["error_class"], "correct")

    def test_previews_do_not_require_sampling_limits_in_candidate_sql(self) -> None:
        system, _ = prompts.agent_prompts("neutron", "question", "raw", 15)
        self.assertIn("SESSION SQL_SELECT_LIMIT=100", system)
        self.assertIn("validated candidate unchanged", system)
        self.assertNotIn("append an outer LIMIT", system)
        for path in ("mysql_timeout.sh", "pi_extension/sql_exec.ts"):
            self.assertIn("--init-command=", (prompts.config.HARNESS_DIR / path).read_text())

    def test_empty_results_must_have_the_same_width(self) -> None:
        gold = mysql_io.QueryResult([], None, False, 1)
        for width, expected in ((1, True), (2, False)):
            with patch("harness.scorer._execute", return_value=mysql_io.QueryResult([], None, False, width)):
                rec = scorer.score_prediction("SELECT 1 WHERE FALSE", "gold", "neutron", gold)
            self.assertEqual(rec["correct"], expected)

    def test_gold_is_shared_and_failures_are_excluded_from_every_arm(self) -> None:
        questions = [{"id": qid, "question": "?", "sql": "SELECT 1"}
                     for qid in ("good", "bad")]
        args = SimpleNamespace(dataset="neutron", phase="main", num_samples=2,
                               limit=None, arms=["raw", "profile"], max_turns=6,
                               no_container=True, tag=None, score_only=False,
                               estimate_cost=False, workers=1, force=False)
        answer = {"pred_sql": "SELECT 1;", "raw_text": "<ans>SELECT 1</ans>",
                  "turns": 1, "model": "test", "usage": {}}
        with (TemporaryDirectory() as temp,
              patch.object(run_experiment.config, "RESULTS_DIR", Path(temp)),
              patch("harness.manifest.build_manifest", return_value=Path("unused")),
              patch("harness.manifest.load_manifest", return_value={"questions": questions}),
              patch("run_experiment._protocol_fingerprint", return_value="test"),
              patch("harness.scorer.execute_gold", side_effect=lambda *_a: (
                  mysql_io.QueryResult([(1,)], None, False, 1) if gold.call_count % 2
                  else mysql_io.QueryResult(None, None, True))) as gold,
              patch("harness.scorer._execute", return_value=mysql_io.QueryResult([(1,)], None, False, 1)),
              patch("run_experiment._run_one", side_effect=lambda *_a: dict(answer)) as agent):
            for score_only in (False, False, True):  # initial, resume, rescore
                args.score_only = score_only
                self.assertEqual(run_experiment._run_dataset(args), 1)
                summary = json.loads(next(Path(temp).glob("*/summary.json")).read_text())
                for arm in args.arms:
                    self.assertEqual(summary[arm]["n"], 1)
                    self.assertEqual(summary[arm]["accuracy"], 1)
                    self.assertEqual(summary[arm]["excluded_gold_questions"], ["bad"])
                self.assertEqual(summary["pairwise"]["profile-raw"]["n"], 1)
            self.assertEqual(gold.call_count, 6)  # each question once per invocation
            self.assertEqual(agent.call_count, 2)  # bad gold never spends model calls

    def test_per_database_samples_are_validated(self) -> None:
        self.assertEqual(run_experiment._parse_samples(["neutron=12", "dw=7"]),
                         [("neutron", 12), ("dw", 7)])
        with self.assertRaises(Exception):
            run_experiment._parse_samples(["neutron=0"])

    def test_empty_agent_record_is_resumable(self) -> None:
        self.assertTrue(run_experiment._is_infrastructure_failure({
            "turns": 0, "usage": {"totalTokens": 0}, "model": None, "pred_sql": None,
        }))
        self.assertFalse(run_experiment._is_infrastructure_failure({
            "turns": 1, "usage": {"totalTokens": 10}, "model": "m", "pred_sql": None,
        }))
        self.assertFalse(run_experiment._is_infrastructure_failure({
            "turns": 0, "budget_exhausted": "wall_clock", "pred_sql": None,
        }))

    @patch("run_experiment._protocol_fingerprint", return_value="new")
    @patch("run_experiment._score", side_effect=lambda rec, *_a: rec | {"correct": False})
    @patch("run_experiment._run_one", return_value={"budget_exhausted": "wall_clock"})
    def test_budget_timeout_is_scored_not_retried(self, run_one, _score, _fingerprint) -> None:
        rec, _ = run_experiment._run_one_and_score(
            {"id": "q", "question": "?", "sql": "SELECT 1"},
            "raw", "neutron", 6, 1,
        )
        self.assertEqual(run_one.call_count, 1)
        self.assertEqual(rec["harness_attempts"], 1)
        self.assertFalse(rec["correct"])

    @patch("run_experiment.time.sleep")
    @patch("run_experiment._protocol_fingerprint", return_value="new")
    @patch("run_experiment._score", side_effect=lambda rec, *_a: rec)
    @patch("run_experiment._run_one", side_effect=[
        {"retryable_error": True, "infrastructure_error": True,
         "tool_calls": [{"source": "main", "name": "read", "arguments": {}}]},
        {"tool_calls": [{"source": "main", "name": "bash", "arguments": {}}]},
    ])
    def test_tool_calls_survive_harness_retry(self, _run_one, _score, _fingerprint, _sleep) -> None:
        rec, _ = run_experiment._run_one_and_score(
            {"id": "q", "question": "?", "sql": "SELECT 1"},
            "raw", "neutron", 6, 1,
        )
        self.assertEqual([call["attempt"] for call in rec["tool_calls"]], [1, 2])

    def test_cache_requires_matching_protocol(self) -> None:
        with TemporaryDirectory() as temp:
            path = Path(temp) / "records.jsonl"
            metrics.write_jsonl(path, [
                {"id": "old", "protocol_fingerprint": "old"},
                {"id": "new", "protocol_fingerprint": "new"},
            ])
            self.assertEqual(set(run_experiment._load_existing(
                path, {"old": "new", "new": "new"}
            )), {"new"})

    def test_sampling_is_proportional_and_stable(self) -> None:
        questions = ([{"id": f"a{i}", "category": "a"} for i in range(80)]
                     + [{"id": f"b{i}", "category": "b"} for i in range(20)])
        first = manifest._stratified_sample(questions, 10, 77)
        second = manifest._stratified_sample(questions, 10, 77)
        self.assertEqual([q["id"] for q in first], [q["id"] for q in second])
        self.assertEqual(sum(q["category"] == "a" for q in first), 8)

    def test_only_outer_order_by_makes_result_order_significant(self) -> None:
        self.assertFalse(scorer._has_top_level_order_by(
            "WITH q AS (SELECT 1 ORDER BY 1) SELECT * FROM q"
        ))
        self.assertFalse(scorer._has_top_level_order_by(
            "SELECT ROW_NUMBER() OVER (ORDER BY id) FROM t"
        ))
        self.assertTrue(scorer._has_top_level_order_by(
            "WITH q AS (SELECT 1 ORDER BY 1) SELECT * FROM q ORDER BY 1"
        ))

    def test_validation_turns_follow_the_budget(self) -> None:
        system, _ = prompts.agent_prompts("neutron", "question", "raw", 16)
        self.assertIn("By turn 14, run the complete candidate query", system)
        self.assertIn("use turn 15 to repair", system)
        self.assertIn("Turn 16 is reserved", system)

    def test_arms_only_change_context(self) -> None:
        for arm, has_profile in {"raw": False, "profile": True}.items():
            system, user = prompts.agent_prompts("neutron", "question", arm, 10)
            self.assertEqual("`profile.md`" in user, has_profile)
            self.assertEqual("schema-links.md" in user, has_profile)
            # The profile arm inlines the TOC index itself, but never the full
            # profile — and not the generator frontmatter either.
            self.assertEqual("`subnets` (rows=49)" in user, has_profile)
            self.assertNotIn("BEGIN DB PROFILE", user)
            self.assertNotIn("generated_at_utc", user)
            self.assertIn("Use any supplied database context first", system)
            self.assertIn("Turn 10 is reserved", system)
            self.assertIn("finish all tool use by turn 9", system)
            self.assertIn("By turn 8, run the complete candidate query", system)
            self.assertIn("use turn 9 to repair", system)
            self.assertIn("<ans>", system)
            self.assertIn("<ans>...</ans>", user)
            self.assertIn("BEGIN SUPPLIED DATABASE CONTEXT", user)


if __name__ == "__main__":
    unittest.main()
