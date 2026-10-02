from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from harness import analyze_results as analysis


class AnalysisTests(unittest.TestCase):
    def test_api_retries_format_failures_without_history(self):
        from io import BytesIO
        calls = []
        answers = [None, "x" * 200, "raw: wrong join;\nprofile: plausible."]
        def api(request, timeout):
            body = json.loads(request.data)
            calls.append(body)
            self.assertEqual(timeout, 60)
            self.assertEqual(request.full_url, analysis.config.OPENROUTER_BASE_URL.rstrip("/") + "/chat/completions")
            self.assertEqual(len(body["messages"]), 2)
            self.assertEqual(body["model"], "test")
            self.assertEqual(body["reasoning"]["effort"], "low")
            return BytesIO(json.dumps({"choices": [{"message": {"content": answers.pop(0)}}]}).encode())
        with patch.object(analysis, "urlopen", side_effect=api), \
                patch.object(analysis.time, "sleep"), \
                patch.dict("os.environ", {"OPENROUTER_API_KEY": "test-key"}):
            self.assertEqual(analysis.review({"id": "q1"}, analysis.REVIEW_PROMPT, "test", "low", True),
                             "raw: wrong join; profile: plausible.")
            self.assertEqual(len(calls), 3)
            self.assertTrue(all(json.loads(c["messages"][1]["content"]) == {"id": "q1"} for c in calls))
            answers[:] = ["я" * 80]
            self.assertEqual(len(analysis.review({}, analysis.REVIEW_PROMPT, "test", "low", True)), 80)
            for length in (128, 199):
                answers[:] = ["x" * length]
                with self.assertWarnsRegex(RuntimeWarning, f"Accepting {length}-character"):
                    self.assertEqual(len(analysis.review({}, analysis.REVIEW_PROMPT, "test", "low", True)), length)
            answers[:] = ["x" * 200] * 3
            with self.assertRaisesRegex(RuntimeError, "200 characters"):
                analysis.review({}, analysis.REVIEW_PROMPT, "test", "low", True)

    def test_api_errors_retry_transient_failures_and_redact_credentials(self):
        from io import BytesIO
        from urllib.error import HTTPError
        with patch.object(analysis.time, "sleep"), \
                patch.dict("os.environ", {"OPENROUTER_API_KEY": "sk-or-secret"}):
            failures = [HTTPError("url", 429, "rate limit", {}, BytesIO(b"sk-or-secret")) for _ in range(3)]
            with patch.object(analysis, "urlopen", side_effect=failures) as api:
                with self.assertRaisesRegex(RuntimeError, "HTTP 429: \\[REDACTED\\]") as error:
                    analysis.review({}, analysis.REVIEW_PROMPT, "test", "low", True)
                self.assertEqual(api.call_count, 3)
                self.assertNotIn("sk-or-secret", str(error.exception))
            with patch.object(analysis, "urlopen", side_effect=HTTPError("url", 401, "unauthorized", {}, BytesIO(b"bad key"))) as api:
                with self.assertRaisesRegex(RuntimeError, "HTTP 401"):
                    analysis.review({}, analysis.REVIEW_PROMPT, "test", "low", True)
                self.assertEqual(api.call_count, 1)

    def test_resume_skips_saved_reviews_and_rebuilds_sentences(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp)
            questions = [{"run": "run", "id": "q1"}, {"run": "run", "id": "q2"}]
            saved = {"run": "run", "id": "q1", "sentence": "x" * 128}
            (output / "inputs.json").write_text(json.dumps(questions))
            (output / "reviews.jsonl").write_text(json.dumps(saved) + "\n")
            (output / "sentences.txt").write_text("interrupted write")
            with patch.object(analysis, "load_questions", return_value=questions), \
                    patch.object(analysis, "review", side_effect=["raw: wrong join.", "Summary"]) as review, \
                    patch.dict("os.environ", {"OPENROUTER_API_KEY": "test"}):
                with self.assertWarnsRegex(RuntimeWarning, "Resuming saved verdicts"):
                    analysis.main(["run", "--output", str(output), "--resume"])
                self.assertEqual(review.call_args_list[0].args[0], questions[1])
                self.assertEqual(len(review.call_args_list[1].args[0]), 2)
                self.assertEqual((output / "sentences.txt").read_text(),
                                 "run/q1: " + "x" * 128 + "\nrun/q2: raw: wrong join.\n")
                (output / "inputs.json").write_text("[]")
                with self.assertRaises(SystemExit):
                    analysis.main(["run", "--output", str(output), "--resume"])
                self.assertEqual(review.call_count, 2)

    def test_default_discovers_all_directories_in_sorted_order(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            results = root / "results"
            results.mkdir()
            for name in ("z-run", "a-run"):
                (results / name).mkdir()
            (results / "notes.txt").write_text("not a run")
            with patch.object(analysis.config, "RESULTS_DIR", results), \
                    patch.object(analysis, "load_questions", side_effect=lambda path: [{"run": path.name}]) as load:
                analysis.main(["--output", str(root / "output"), "--dry-run"])
                self.assertEqual([call.args[0].name for call in load.call_args_list], ["a-run", "z-run"])
                self.assertEqual(json.loads((root / "output" / "inputs.json").read_text()),
                                 [{"run": "a-run"}, {"run": "z-run"}])

    def test_pipeline_keeps_question_requests_and_summary_isolated(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            run = root / "neutron__main__n2_v12-test"
            run.mkdir()
            questions = [{"id": f"q{i}", "db": "neutron", "question": f"Question {i}",
                          "sql": f"SELECT {i}"} for i in (1, 2)]
            (root / "manifest__neutron__main__n2.json").write_text(
                json.dumps({"questions": questions}))
            for arm in ("raw", "profile"):
                (run / f"arm{arm}.jsonl").write_text("\n".join(
                    json.dumps({"id": q["id"], "gold_sql": q["sql"],
                                "pred_sql": q["sql"] if arm == "raw" else None,
                                "correct": arm == "raw", "all_text": ["PRIVATE TRACE"]})
                    for q in questions))
            # Archived files must not be read.
            (run / "armraw.jsonl.stale-old").write_text("not JSON")
            calls = []

            def api(request, timeout):
                from io import BytesIO
                body = json.loads(request.data)
                self.assertEqual(len(body["messages"]), 2)
                payload = json.loads(body["messages"][1]["content"])
                calls.append(body)
                if isinstance(payload, dict):
                    self.assertNotIn("PRIVATE TRACE", json.dumps(payload))
                    self.assertEqual(set(payload["candidates"]), {"raw", "profile"})
                    self.assertIn("question", payload)
                    self.assertIn("gold_sql", payload)
                    answer = "raw: matches the question; profile: missing candidate."
                else:
                    self.assertEqual(len(payload), 2)
                    self.assertTrue(all(set(q) == {"run", "id", "sentence"} for q in payload))
                    answer = "# Review\nTwo profile candidates were missing."
                return BytesIO(json.dumps({"choices": [{"message": {"content": answer}}]}).encode())

            with patch.object(analysis.config, "MANIFEST_DIR", root), \
                    patch.object(analysis.config, "DEFAULT_MODEL_ID", "review-model"), \
                    patch.object(analysis, "urlopen", side_effect=api), \
                    patch.dict("os.environ", {"OPENROUTER_API_KEY": "test"}):
                output = root / "analysis"
                self.assertEqual(analysis.main([str(run), "--output", str(output)]), 0)
                self.assertEqual(len((output / "sentences.txt").read_text().splitlines()), 2)
                self.assertEqual(len((output / "reviews.jsonl").read_text().splitlines()), 2)
                self.assertIn("Two profile", (output / "summary.md").read_text())
                self.assertEqual(len(calls), 3)
                with self.assertRaises(FileExistsError):
                    analysis.main([str(run), "--output", str(output)])
                self.assertEqual(len(calls), 3)
                with patch.object(analysis, "urlopen") as no_agent:
                    analysis.main([str(run), "--output", str(root / "dry"), "--dry-run"])
                    no_agent.assert_not_called()
                with (run / "armraw.jsonl").open("a") as f:
                    f.write("\n" + json.dumps({"id": "q1"}))
                with self.assertRaisesRegex(ValueError, "duplicate"):
                    analysis.load_questions(run)


if __name__ == "__main__":
    unittest.main()
