#!/usr/bin/env python3
"""One-time setup: register the OpenRouter provider + GPT-6 Luna model
with pi so the experiment's locked model resolves, WITHOUT clobbering an
existing models.json or an OAuth-minted openrouter key.

What it does:
  * prints the GPT-6 Luna context/pricing (Phase-0 confirmation);
  * merges harness/openrouter_models.json into ~/.pi/agent/models.json
    (creates it if missing; leaves an existing `openrouter` block untouched);
  * checks OPENROUTER_API_KEY and runs `pi auth check --provider openrouter`.

Usage:
  python harness/setup_openrouter.py            # merge + check
  python harness/setup_openrouter.py --check    # check only, no file changes
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

# allow `python harness/setup_openrouter.py` from the repo root
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from harness import config

MODEL = config.DEFAULT_MODEL_ID  # openai/gpt-6-luna
FRAGMENT = config.HARNESS_DIR / "openrouter_models.json"
AGENT_DIR = Path(os.path.expanduser("~/.pi/agent"))
MODELS_JSON = AGENT_DIR / "models.json"


def confirm_model() -> None:
    print(f"[phase0] confirming model '{MODEL}' on OpenRouter ...")
    try:
        with urllib.request.urlopen("https://openrouter.ai/api/v1/models", timeout=15) as r:
            data = json.loads(r.read().decode("utf-8"))
    except Exception as e:
        print(f"  ! could not reach OpenRouter: {e}")
        return
    for m in data.get("data", []):
        if m.get("id") == MODEL:
            print(f"  context_length = {m.get('context_length'):,}  (token guard = {config.TOKEN_GUARD:,})")
            pr = m.get("pricing", {})
            print(f"  pricing $/Mtok: prompt={pr.get('prompt')} completion={pr.get('completion')} cache_read={pr.get('input_cache_read')}")
            if (m.get("context_length") or 0) >= config.TOKEN_GUARD:
                print("  ✓ context window exceeds the 320K token guard — guard is the binding cap.")
            else:
                print("  ⚠ context window BELOW the token guard — lower TOKEN_GUARD in config.py.")
            return
    print(f"  ⚠ model '{MODEL}' not found in OpenRouter catalog.")


def merge(check_only: bool) -> None:
    if not FRAGMENT.exists():
        print(f"  ! missing {FRAGMENT}")
        return
    frag = json.loads(FRAGMENT.read_text(encoding="utf-8"))
    if not MODELS_JSON.exists():
        if check_only:
            print(f"[setup] would create {MODELS_JSON}")
            return
        AGENT_DIR.mkdir(parents=True, exist_ok=True)
        MODELS_JSON.write_text(json.dumps(frag, indent=2), encoding="utf-8")
        print(f"[setup] created {MODELS_JSON}")
        return
    existing = json.loads(MODELS_JSON.read_text(encoding="utf-8"))
    providers = existing.setdefault("providers", {})
    if "openrouter" in providers:
        print(f"[setup] {MODELS_JSON} already defines 'openrouter' — left untouched.")
        print("        If it lacks the gpt-6-luna model, merge harness/openrouter_models.json manually.")
        return
    if check_only:
        print(f"[setup] would add 'openrouter' provider to {MODELS_JSON}")
        return
    shutil.copy(MODELS_JSON, str(MODELS_JSON) + ".bak")
    providers["openrouter"] = frag["providers"]["openrouter"]
    MODELS_JSON.write_text(json.dumps(existing, indent=2), encoding="utf-8")
    print(f"[setup] added 'openrouter' provider to {MODELS_JSON} (backup: models.json.bak)")


def check_key() -> None:
    if os.environ.get("OPENROUTER_API_KEY"):
        print("[auth] OPENROUTER_API_KEY is set in env.")
    else:
        print("[auth] OPENROUTER_API_KEY is NOT set — set it (or run `/login openrouter` in pi).")
    try:
        out = subprocess.run(["pi", "auth", "check", "--provider", "openrouter"],
                             capture_output=True, text=True, timeout=30)
        print(f"[auth] pi auth check --provider openrouter -> {out.stdout.strip() or out.stderr.strip()}")
    except Exception as e:
        print(f"[auth] could not run `pi auth check`: {e}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="inspect only; do not modify models.json")
    args = ap.parse_args()
    confirm_model()
    merge(check_only=args.check)
    check_key()
    print("\nNext: export OPENROUTER_API_KEY=sk-... && python run_experiment.py --dataset neutron --phase phase0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
