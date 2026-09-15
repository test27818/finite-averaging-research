#!/usr/bin/env python3
"""Trivial baselines for the averaging-to-equalize benchmark.

Each baseline reads a ground-truth JSONL file and emits a predictions JSONL file.

Baselines:
  judge      : always_no, always_yes, majority, oracle
  min_steps  : guess_n_minus_1, oracle
  construct  : power2_tree, oracle

`oracle` uses the ground-truth answer (reference upper bound / sanity check: must be 100%).
`majority` predicts the majority label of the SAME file (leaky; only for diagnostics).

Usage:
    python3 baselines/trivial.py <baseline> <ground.jsonl> <preds.jsonl>
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from solver import power2_tree_sequence  # noqa: E402


def main():
    baseline, ground_path, preds_path = sys.argv[1], sys.argv[2], sys.argv[3]
    rows = [json.loads(l) for l in open(ground_path)]

    if baseline.startswith("judge:"):
        kind = baseline.split(":", 1)[1]
        out = []
        majority = None
        if kind == "majority":
            yes = sum(1 for r in rows if r["label"] == "YES")
            majority = "YES" if yes >= len(rows) - yes else "NO"
        for r in rows:
            if kind == "always_no":
                ans = "NO"
            elif kind == "always_yes":
                ans = "YES"
            elif kind == "majority":
                ans = majority
            elif kind == "oracle":
                ans = r["label"]
            else:
                raise SystemExit(f"unknown judge baseline {kind}")
            out.append({"id": r["id"], "answer": ans})

    elif baseline.startswith("min_steps:"):
        kind = baseline.split(":", 1)[1]
        out = []
        for r in rows:
            if r.get("min_steps") is None:
                continue
            if kind == "guess_n_minus_1":
                ans = r["n"] - 1
            elif kind == "oracle":
                ans = r["min_steps"]
            else:
                raise SystemExit(f"unknown min_steps baseline {kind}")
            out.append({"id": r["id"], "answer": ans})

    elif baseline.startswith("construct:"):
        kind = baseline.split(":", 1)[1]
        out = []
        for r in rows:
            if r.get("sequence") is None:
                continue
            if kind == "oracle":
                steps = r["sequence"]
            elif kind == "power2_tree":
                steps = power2_tree_sequence(r["a"])
                if steps is None:
                    continue
            else:
                raise SystemExit(f"unknown construct baseline {kind}")
            out.append({"id": r["id"], "steps": steps})

    else:
        raise SystemExit(f"unknown baseline {baseline}")

    with open(preds_path, "w") as f:
        for o in out:
            f.write(json.dumps(o) + "\n")
    print(f"wrote {len(out)} predictions -> {preds_path}")


if __name__ == "__main__":
    main()
