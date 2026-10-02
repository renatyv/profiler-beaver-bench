"""Run manifest: freeze question lists + seed so all arms see identical questions.

Manifest layout (JSON), one file per (dataset, phase, num_samples):
  {
    "dataset": "neutron",
    "phase": "pilot",
    "seed": 77,
    "num_samples": 20,
    "mysql_db": "neutron",
    "mysql_dbs": ["neutron"],        # schemas to grant for this run
    "profile": "neutron.md",
    "created_at": "...",
    "questions": [ {id, question, sql, db, category, detailed_category,
                    contains_domain_knowledge}, ... ]
  }
"""
from __future__ import annotations

import json
import random
from datetime import datetime, timezone
from pathlib import Path

from . import config

SAMPLE_SEED = 77  # plan: matches data/build_local.py

# phase0 is a sanity check ("get 1 question producing valid SQL in all arms"),
# so we pin the easiest question present in neutron's dev_sampled.json rather
# than letting the stratified sampler (which starts at the hard
# "complex query|False" bucket for n=1) pick a CTE+ROLLUP monster that all arms
# fail. neutron_546 is the shortest base SQL in the sampled set (flat single
# SELECT, one JOIN, COUNT(*), every filter value stated in the question).
# Scoped to phase0 only; pilot/main keep using _stratified_sample.
# NOTE: must be an id present in data/<db>/dev_sampled.json, else the loader
# falls back to _stratified_sample.
PHASE0_PIN_ID = "neutron_546"


def _load_questions(db_label: str) -> list[dict]:
    """Load the full split; use the old sampled file only as a fallback."""
    sampled = config.DATA_DIR / db_label / "dev_sampled.json"
    full = config.DATA_DIR / db_label / "dev.json"
    if full.exists():
        return json.loads(full.read_text(encoding="utf-8"))
    if sampled.exists():
        return json.loads(sampled.read_text(encoding="utf-8"))
    raise FileNotFoundError(
        f"No dev data for '{db_label}' (looked in {config.DATA_DIR / db_label}). "
        f"Build it first with: python data/build_local.py --datasets {db_label}"
    )


def _stratify(questions: list[dict], strata: list[str]) -> dict[str, list[dict]]:
    """Bucket by the benchmark's strata fields for balanced sampling."""
    buckets: dict[str, list[dict]] = {}
    for q in questions:
        key = "|".join(str(q.get(field, "?")) for field in strata)
        buckets.setdefault(key, []).append(q)
    return buckets


def _stratified_sample(questions: list[dict], n: int, seed: int,
                       strata: list[str] | None = None) -> list[dict]:
    """Sample n questions, proportionally across strata, seed-stable."""
    strata = strata or ["category", "contains_domain_knowledge"]
    rng = random.Random(seed)
    buckets = _stratify(questions, strata)
    total = len(questions)
    n = min(n, total)
    quotas = {k: n * len(v) / total for k, v in buckets.items()}
    counts = {k: int(q) for k, q in quotas.items()}
    for k in sorted(buckets, key=lambda key: (quotas[key] - counts[key], key), reverse=True)[:n - sum(counts.values())]:
        counts[k] += 1
    picked = [q for k, bucket in buckets.items() for q in rng.sample(bucket, counts[k])]
    rng.shuffle(picked)
    return picked


def build_manifest(db_label: str, phase: str, num_samples: int | None) -> Path:
    """Create (or reuse) the frozen manifest and return its path."""
    config.MANIFEST_DIR.mkdir(parents=True, exist_ok=True)
    n_tag = "full" if num_samples is None else f"n{num_samples}"
    path = config.MANIFEST_DIR / f"manifest__{db_label}__{phase}__{n_tag}.json"
    if path.exists():
        existing = load_manifest(path)
        if phase == "phase0" or num_samples is None or existing.get("num_samples", 0) >= num_samples:
            return path
        print(f"[manifest] rebuilding undersized {path} ({existing.get('num_samples')} < {num_samples})")

    spec = config.dataset_spec(db_label)
    all_q = _load_questions(db_label)
    if phase == "phase0":
        # Sanity phase: pin one easy question so all arms can succeed end-to-end.
        # Falls back to the sampler if the pinned id is absent (e.g. wrong dataset).
        pin = next((q for q in all_q if q["id"] == PHASE0_PIN_ID), None)
        chosen = [pin] if pin is not None else _stratified_sample(all_q, 1, SAMPLE_SEED, spec["strata"])
    elif num_samples is None or num_samples >= len(all_q):
        chosen = all_q
    else:
        chosen = _stratified_sample(all_q, num_samples, SAMPLE_SEED, spec["strata"])

    slim = []
    for q in chosen:
        slim.append({
            "id": q["id"],
            "question": q["question"],
            "sql": q.get("sql"),
            "db": q.get("db", config.mysql_db_for(db_label) or db_label),
            "category": q.get("category"),
            "detailed_category": q.get("detailed_category"),
            "contains_domain_knowledge": bool(q.get("contains_domain_knowledge")),
        })

    mysql_db = config.mysql_db_for(db_label) or None
    manifest = {
        "dataset": db_label,
        "mysql_db": mysql_db,
        "mysql_dbs": sorted({r["db"] for r in slim} or ({mysql_db} if mysql_db else set())),
        "profile": spec.get("profile"),
        "phase": phase,
        "seed": SAMPLE_SEED,
        "num_samples": len(slim),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "questions": slim,
    }
    path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[manifest] {path} ({len(slim)} questions)")
    return path


def load_manifest(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))
