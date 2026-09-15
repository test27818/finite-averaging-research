#!/usr/bin/env python3
"""Compare the legacy Fraction-BFS solver with solver_v2 (projective integer A*).

Measures: agreement on min_steps, states/nodes explored, wall time, and how far each
gets on larger n (the legacy BFS dies at n>=7).

    python3 src/bench_v2.py            # ground-truth cross check on data/small.jsonl
    python3 src/bench_v2.py --scale    # push n up, compare reach
"""
from __future__ import annotations
import json
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from solver import judge, min_steps_sequence, verify_sequence  # noqa: E402
from legacy_bfs import min_steps_sequence  # independent baseline
import solver_v2 as v2  # noqa: E402


def cross_check(path=os.path.join(HERE, "..", "tests", "fixtures", "original_small.jsonl"), limit=None):
    rows = [json.loads(l) for l in open(path)]
    rows = [r for r in rows if r.get("min_steps") is not None]
    if limit:
        rows = rows[:limit]
    agree = disagree = 0
    t_old = t_new = 0.0
    slow = []
    for r in rows:
        a = r["a"]
        t0 = time.time(); old, oseq = min_steps_sequence(a); dt_old = time.time() - t0; t_old += dt_old
        t0 = time.time(); res = v2.solve(a, deadline_s=20.0); dt_new = time.time() - t0; t_new += dt_new
        new = res.get("min_steps")
        ok = (new == old)
        if ok:
            agree += 1
        else:
            disagree += 1
            print(f"  MISMATCH {a}: legacy={old} v2={new} ({res.get('method')})")
        if res.get("sequence"):
            assert verify_sequence(a, res["sequence"])[0], f"bad seq {a}"
        if dt_old > 0.05 and dt_new < 0.01:
            slow.append((a, old, dt_old, dt_new))
    print(f"cross-check: agree={agree} disagree={disagree} n={len(rows)}")
    print(f"total time  legacy BFS {t_old:.2f}s   v2 IDA* {t_new:.2f}s  "
          f"({(t_old/t_new if t_new else 0):.1f}x)")
    if slow:
        print("instances where v2 is >10x faster:")
        for a, m, to, tn in sorted(slow, key=lambda x: -x[2])[:8]:
            print(f"   {a} min={m}  legacy {to:.2f}s  v2 {tn:.3f}s")


def scale_probe(seed=7, ns=(5, 6, 7, 8, 9, 10)):
    rng = random.Random(seed)
    print(f"{'n':>3} {'instance':>28} {'v2 min':>7} {'v2 states':>10} {'v2 t':>7} "
          f"{'cert':>5} | {'legacy t':>9} {'legacy res':>10}")
    for n in ns:
        for trial in range(3):
            while True:
                a = [rng.randint(-9, 9) for _ in range(n)]
                if judge(a) and len({x for x in a}) >= 3:
                    break
            t0 = time.time(); r = v2.solve(a, deadline_s=60.0, node_budget=6_000_000)
            t_new = time.time() - t0
            t0 = time.time()
            try:
                old = min_steps_sequence(a, budget_states=2_000_000, max_den_exp=20)[0]
            except Exception:
                old = "ERR"
            t_old = time.time() - t0
            shown = str(a) if len(str(a)) <= 26 else str(a)[:23] + "..."
            print(f"{n:>3} {shown:>28} {str(r.get('min_steps')):>7} "
                  f"{r.get('states', 0):>10} {t_new:>6.2f}s "
                  f"{str(bool(r.get('certified') is True)):>5} | {t_old:>8.2f}s "
                  f"{str(old):>10}")


if __name__ == "__main__":
    if "--scale" in sys.argv:
        scale_probe()
    else:
        cross_check()
