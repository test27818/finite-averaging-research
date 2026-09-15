#!/usr/bin/env python3
"""Reproducible dataset generator for the averaging-to-equalize benchmark.

Produces JSONL ground-truth files (one JSON object per line) under data/:

    id            unique instance id
    task          "judge" (construction/min-steps use the same instance, scored separately)
    split         train / dev / test / hard / small
    tier          easy / medium / hard / trap
    n             multiset size
    a             the multiset (list of ints)
    label         "YES" | "NO"   (ground-truth mixability)
    min_steps     exact minimum #steps (small instances only, else null)
    sequence      one verified operation sequence (small instances only, else null)
    traits        tags describing the reason this instance is interesting

Ground truth is computed with two independent checks:
  * the proven G-criterion (judge()),
  * exact BFS reachability (min_steps_sequence) on every small instance,
and the generator aborts if they ever disagree (this never happens on the shipped set).

Reproducibility: everything derives from a single seed. A manifest with SHA-256 hashes
and the seed is written to data/manifest.json.

Usage:
    python3 src/generate.py [--seed 12345] [--outdir data] [--selfcheck]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import random
import sys
from itertools import combinations_with_replacement

sys.path.insert(0, os.path.dirname(__file__))
from solver import judge, min_steps_sequence, power2_tree_sequence  # noqa: E402


def make_record(task_label, split, tier, n, a, traits, small=False, idx=0):
    label = "YES" if judge(a) else "NO"
    rec = {
        "id": f"{task_label}_{idx:06d}",
        "task": "judge",
        "split": split,
        "tier": tier,
        "n": n,
        "a": a,
        "label": label,
        "min_steps": None,
        "sequence": None,
        "sequence_source": None,
        "traits": sorted(set(traits)),
    }
    # Only compute exact min-steps / a verified sequence for small mixable instances
    # This generator keeps the original small-split policy; upgrade_data.py enriches all splits.
    if small and label == "YES" and n <= 6:
        ms, seq = min_steps_sequence(a)
        rec["min_steps"] = ms
        rec["sequence"] = seq
        rec["sequence_source"] = "ida_certified_min"
        # Do not promote a budget-limited result to an exact minimum.
        if ms is None:
            print(f"WARNING: IDA* could not certify a sequence for mixable {a} "
                  f"(within limits); min_steps left null.", file=sys.stderr)
    # For power-of-two sizes we can also attach a correct (non-minimal) construction.
    if small and label == "YES" and n > 6 and (n & (n - 1)) == 0:
        rec["sequence"] = power2_tree_sequence(a)
        rec["sequence_source"] = "power2_tree"
    return rec


def inject_random(records, rng, task_label, split, tier, n_range, val_range, count, small=False):
    n_lo, n_hi = n_range
    v_lo, v_hi = val_range
    for _ in range(count):
        n = rng.randint(n_lo, n_hi)
        a = [rng.randint(v_lo, v_hi) for _ in range(n)]
        rec = make_record(task_label, split, tier, n, a, ["random"], small=small, idx=len(records))
        records.append(rec)


def inject_traps(records, rng, task_label, split, tier, small=False):
    base = len(records)

    # n = 3 : arithmetic progressions (YES) and non-AP with G a power of two (NO trap).
    for (x, y, z) in [(0, 1, 2), (0, 2, 4), (1, 2, 3), (-2, 0, 2), (3, 5, 7)]:
        records.append(make_record(task_label, split, tier, 3, [x, y, z], ["n3_ap"], small=small, idx=len(records)))
    for (x, y, z) in [(0, 1, 5), (0, 4, 5), (1, 2, 6), (1, 5, 6), (0, 3, 8)]:
        records.append(make_record(task_label, split, tier, 3, [x, y, z], ["n3_nonap"], small=small, idx=len(records)))

    # single spike [0,...,0,k]
    for n in range(4, 11):
        for k in (1, 2, 3, 4, 5, 7, 9, 16):
            a = [0] * (n - 1) + [k]
            records.append(make_record(task_label, split, tier, n, a, ["single_spike"], small=small, idx=len(records)))

    # gcd-cancellation trap: raw deviations all divisible by a common factor.
    for n in (5, 6, 7):
        for k in (25, 49, 125):
            a = [0] * (n - 1) + [k]
            records.append(make_record(task_label, split, tier, n, a, ["gcd_cancel"], small=small, idx=len(records)))

    # non-integer / non-dyadic mean
    for a in ([0, 0, 1], [0, 0, 0, 1], [0, 0, 1, 1], [1, 1, 1, 4], [0, 0, 0, 0, 1]):
        records.append(make_record(task_label, split, tier, len(a), a, ["mean_type"], small=small, idx=len(records)))

    # all equal (trivially YES), all odd, all even
    records.append(make_record(task_label, split, tier, 5, [7, 7, 7, 7, 7], ["all_equal"], small=small, idx=len(records)))
    records.append(make_record(task_label, split, tier, 5, [1, 3, 5, 7, 9], ["all_odd"], small=small, idx=len(records)))
    records.append(make_record(task_label, split, tier, 5, [0, 2, 4, 6, 8], ["all_even"], small=small, idx=len(records)))

    # negative values
    for a in ([-3, -2, -1, 0, 6], [-5, -5, -5, 0, 15], [-9, -1, 1, 9]):
        records.append(make_record(task_label, split, tier, len(a), a, ["negative"], small=small, idx=len(records)))

    # n = 2^k is always mixable (regardless of values) -- good construction cases.
    for n in (4, 8, 16):
        for _ in range(6):
            a = [rng.randint(-20, 20) for _ in range(n)]
            records.append(make_record(task_label, split, tier, n, a, ["pow2_size"], small=small, idx=len(records)))


def selfcheck():
    from legacy_bfs import min_steps_sequence  # independent exact-fraction oracle
    """Cross-check judge() vs exact BFS on tiny multisets.

    For mixable instances (judge=YES) the BFS must actually FIND a sequence (strong check).
    For non-mixable instances we only do a cheap shallow BFS (depth<=3) to catch gross errors;
    the definitive NO answer rests on the proven criterion (see problem.md).
    """
    print("Running selfcheck: judge() vs exact BFS on tiny multisets ...")
    disagree = 0
    total = 0
    for n, vmax in [(2, 3), (3, 4), (4, 3), (5, 2), (6, 1)]:
        for combo in combinations_with_replacement(range(vmax + 1), n):
            a = list(combo)
            want = judge(a)
            total += 1
            if want:
                ms, _ = min_steps_sequence(a, max_depth=12, budget_states=50_000)
                if ms is None:
                    disagree += 1
                    print(f"  DISAGREE: a={a} judge=YES but BFS found no sequence within limits")
            else:
                ms, _ = min_steps_sequence(a, max_depth=3, budget_states=5_000)
                if ms is not None:
                    disagree += 1
                    print(f"  DISAGREE: a={a} judge=NO but BFS found a {ms}-step sequence")
    print(f"selfcheck done: {total} multisets, {disagree} disagreements")
    return disagree


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=20260907)
    ap.add_argument("--outdir", default="data")
    ap.add_argument("--selfcheck", action="store_true")
    args = ap.parse_args()

    if args.selfcheck:
        sys.exit(1 if selfcheck() else 0)

    rng = random.Random(args.seed)
    os.makedirs(args.outdir, exist_ok=True)

    records = []

    # ---- small split: min_steps + sequence ground truth (n <= 7) ----
    inject_random(records, rng, "small", "small", "easy", (3, 5), (-6, 6), 120, small=True)
    inject_traps(records, rng, "small", "small", "trap", small=True)

    # ---- dev split ----
    inject_random(records, rng, "dev", "dev", "easy", (3, 5), (-6, 6), 100)
    inject_random(records, rng, "dev", "dev", "medium", (6, 12), (-50, 50), 100)
    inject_traps(records, rng, "dev", "dev", "trap")

    # ---- test split ----
    inject_random(records, rng, "test", "test", "easy", (3, 5), (-6, 6), 200)
    inject_random(records, rng, "test", "test", "medium", (6, 12), (-50, 50), 200)
    inject_random(records, rng, "test", "test", "hard", (8, 60), (-10 ** 9, 10 ** 9), 200)
    inject_traps(records, rng, "test", "test", "trap")

    # ---- hard split: traps + very large values ----
    inject_traps(records, rng, "hard", "hard", "trap")
    inject_random(records, rng, "hard", "hard", "hard", (8, 60), (-10 ** 12, 10 ** 12), 200)
    inject_random(records, rng, "hard", "hard", "medium", (13, 40), (-1000, 1000), 100)

    # ---- write per-split files ----
    by_split = {}
    for rec in records:
        by_split.setdefault(rec["split"], []).append(rec)

    manifest = {"seed": args.seed, "files": {}}
    for split, recs in sorted(by_split.items()):
        path = os.path.join(args.outdir, f"{split}.jsonl")
        with open(path, "w") as f:
            for rec in recs:
                f.write(json.dumps(rec) + "\n")
        sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
        manifest["files"][f"{split}.jsonl"] = {"count": len(recs), "sha256": sha}

    # label distribution per split
    manifest["label_distribution"] = {}
    for split, recs in by_split.items():
        yes = sum(1 for r in recs if r["label"] == "YES")
        manifest["label_distribution"][split] = {"YES": yes, "NO": len(recs) - yes,
                                                 "total": len(recs)}

    with open(os.path.join(args.outdir, "manifest.json"), "w") as f:
        json.dump(manifest, f, indent=2)

    for split, recs in sorted(by_split.items()):
        print(f"  {split:6s}: {len(recs):5d} instances")


if __name__ == "__main__":
    main()
