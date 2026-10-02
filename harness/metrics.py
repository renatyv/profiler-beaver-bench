"""Metrics: execution accuracy, CIs, McNemar, subgroups, cost projection."""
from __future__ import annotations

import json
import math
from collections import defaultdict
from pathlib import Path


# ---------------------------------------------------------------------------
# Execution accuracy + CIs
# ---------------------------------------------------------------------------
def wilson_ci(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    """95% Wilson score interval for a proportion."""
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    denom = 1 + z * z / n
    center = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return (max(0.0, center - half), min(1.0, center + half))


def mcnemar(a_correct: list[bool], b_correct: list[bool]) -> dict:
    """Paired McNemar test for two arms on identical questions."""
    assert len(a_correct) == len(b_correct), "paired test needs identical questions"
    b = sum(1 for a, bb in zip(a_correct, b_correct) if a and not bb)  # A right, B wrong
    c = sum(1 for a, bb in zip(a_correct, b_correct) if not a and bb)  # A wrong, B right
    n_disc = b + c
    # exact two-sided binomial p-value (robust for small n)
    if n_disc == 0:
        p_exact = 1.0
    else:
        from math import comb
        k = min(b, c)
        p_exact = 2 * sum(comb(n_disc, i) for i in range(0, k + 1)) * 0.5 ** n_disc
        p_exact = min(1.0, p_exact)
    stat = (abs(b - c) - 1) ** 2 / n_disc if n_disc else 0.0  # continuity-corrected χ²
    return {"b": b, "c": c, "n_discordant": n_disc,
            "mcnemar_chi2_cc": round(stat, 4), "p_value_exact": round(p_exact, 6)}


def paired_diff_ci(a_correct: list[bool], b_correct: list[bool]) -> dict:
    """CI for Δ = p_b - p_a using the paired (discordant-pair) standard error.

    ``a_correct`` is the subtrahend, ``b_correct`` the minuend, so a positive
    ``delta`` means arm b beats arm a. The returned ``acc_a`` / ``acc_b`` keys
    are positional (first / second argument), not tied to any arm name.
    """
    n = len(a_correct)
    acc_a = sum(a_correct) / n if n else 0.0
    acc_b = sum(b_correct) / n if n else 0.0
    delta = acc_b - acc_a
    m = mcnemar(a_correct, b_correct)
    b, c = m["b"], m["c"]
    n_disc = b + c
    if n_disc == 0:
        se = 0.0
    else:
        # Wald on discordant pairs: SE(Δ) = sqrt(b+c)/n
        se = math.sqrt(n_disc) / n
    z = 1.96
    return {
        "n": n, "acc_a": round(acc_a, 4), "acc_b": round(acc_b, 4),
        "delta": round(delta, 4),
        "ci_low": round(delta - z * se, 4), "ci_high": round(delta + z * se, 4),
        "se": round(se, 4), **m,
    }


# ---------------------------------------------------------------------------
# Per-arm aggregation
# ---------------------------------------------------------------------------
def aggregate(records: list[dict]) -> dict:
    n = len(records)
    if n == 0:
        return {"n": 0}
    correct = sum(1 for r in records if r.get("correct"))
    valid = sum(1 for r in records if r.get("valid_sql"))
    lo, hi = wilson_ci(correct, n)
    operational_metrics = all(r.get("metrics_available", True) for r in records)
    # pi's `input` counts only uncached prompt tokens; the cached bulk of the
    # conversation lives in cacheRead/cacheWrite, so all three are reported
    # separately rather than as a single misleading "tokens_in".
    tok_in_uncached = sum(r.get("usage", {}).get("input", 0) for r in records)
    tok_cache_read = sum(r.get("usage", {}).get("cacheRead", 0) for r in records)
    tok_cache_write = sum(r.get("usage", {}).get("cacheWrite", 0) for r in records)
    tok_out = sum(r.get("usage", {}).get("output", 0) for r in records)
    tok_total = sum(r.get("usage", {}).get("totalTokens", 0) for r in records)
    cost = sum((r.get("cost") or {}).get("total", 0) or 0 for r in records)
    turns = [r.get("turns", 0) for r in records]
    dbq = [r.get("db_queries", 0) for r in records]
    lat = [r.get("latency_s", 0) for r in records]
    return {
        "n": n,
        "accuracy": round(correct / n, 4),
        "accuracy_ci95": [round(lo, 4), round(hi, 4)],
        "valid_sql_pct": round(valid / n, 4),
        "mean_turns": round(sum(turns) / n, 2) if operational_metrics else None,
        "mean_db_queries": round(sum(dbq) / n, 2) if operational_metrics else None,
        "mean_latency_s": round(sum(lat) / n, 2),
        "tokens_input_uncached": tok_in_uncached if operational_metrics else None,
        "tokens_cache_read": tok_cache_read if operational_metrics else None,
        "tokens_cache_write": tok_cache_write if operational_metrics else None,
        "tokens_out": tok_out if operational_metrics else None,
        "tokens_total": tok_total if operational_metrics else None,
        "cost_usd": round(cost, 6) if operational_metrics else None,
        "operational_metrics_available": operational_metrics,
    }


def subgroup_accuracy(records: list[dict], key: str) -> dict:
    buckets: dict[str, list[dict]] = defaultdict(list)
    for r in records:
        buckets[str(r.get(key, "?"))].append(r)
    return {k: aggregate(v) for k, v in sorted(buckets.items())}


def value_counts(records: list[dict], key: str) -> dict:
    c: dict[str, int] = defaultdict(int)
    for r in records:
        c[str(r.get(key, "?"))] += 1
    return dict(sorted(c.items(), key=lambda kv: -kv[1]))


# ---------------------------------------------------------------------------
# Cost projection (Phase-1 go/no-go gate, plan §Phasing)
# ---------------------------------------------------------------------------
def project_cost(arm_records: dict[str, list[dict]], total_questions: int) -> dict:
    """Estimate full-run cost by summing per-arm averages (B >> A due to profile)."""
    per_arm: dict[str, dict] = {}
    total_cost = 0.0
    total_tokens = 0
    unavailable = False
    for arm, recs in arm_records.items():
        n = len(recs)
        if n == 0:
            per_arm[arm] = {"avg_cost_per_question": 0.0, "avg_tokens_per_question": 0.0}
            continue
        if not all(r.get("metrics_available", True) for r in recs):
            per_arm[arm] = {"avg_cost_per_question": None, "avg_tokens_per_question": None}
            unavailable = True
            continue
        c = sum(r.get("cost", {}).get("total", 0) or 0 for r in recs) / n
        t = sum(r.get("usage", {}).get("totalTokens", 0) for r in recs) / n
        per_arm[arm] = {"avg_cost_per_question": round(c, 6),
                        "avg_tokens_per_question": round(t, 1)}
        total_cost += c * total_questions
        total_tokens += t * total_questions
    return {
        "per_arm": per_arm,
        "total_questions": total_questions,
        "estimated_cost_usd": None if unavailable else round(total_cost, 4),
        "estimated_tokens_total": None if unavailable else round(total_tokens, 1),
        "basis_questions": {a: len(r) for a, r in arm_records.items()},
    }


# ---------------------------------------------------------------------------
# Persistence helpers
# ---------------------------------------------------------------------------
def write_jsonl(path: Path, records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]
