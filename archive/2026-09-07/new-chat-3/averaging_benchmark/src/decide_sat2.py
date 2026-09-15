#!/usr/bin/env python3
"""Decision model "does a <= K move solution exist?" in two encodings.

  model A (as in src/decide9_sat.py, src/min_steps_sat.py):
      values scaled by 2^K, transition  2*v[t+1][i] == v[t][i] + v[t][j]   (division!)
      domains +-2^K*max|x|  -> weak bound propagation, huge domains.

  model B (this file, the division-free / "additive" form that follows from the
      projective-integer reformulation of solver_v2):  track y_i(t) = 2^t*(value of
      position i at time t) so that ALL y are integers and a move is pure addition:

          y_i(t+1) = y_j(t+1) = y_i(t) + y_j(t),      y_p(t+1) = 2 y_p(t)  (p != i,j)

      target y(0) = primitive deviations, y(K) = 0.  Only additions + one-hot pair
      selection, which linear-propagates far better.  Also carries the same
      non-zero-count cutting plane  #{nonzero at t} <= 2(K-t).

Usage:  python3 src/decide_sat2.py A|B <K> a1 a2 ... an   [seconds]
"""
from __future__ import annotations
import sys
import time

from ortools.sat.python import cp_model


def build(model_class, E, K, time_limit):
    n = len(E)
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    m = cp_model.CpModel()
    mx = max(abs(e) for e in E)
    if model_class == "A":                      # scaled-by-2^K, division in the step
        S = 1 << K
        LO, HI = min(E) * S - 4, max(E) * S + 4
        v = [[m.NewIntVar(LO, HI, f"v{t}_{p}") for p in range(n)] for t in range(K + 1)]
        for p in range(n):
            m.Add(v[0][p] == E[p] * S)
            m.Add(v[K][p] == 0)
    else:                                       # B: division-free additive form
        # y(t) entries are bounded by mx * 2^t (each move at most doubles the max)
        v = [[m.NewIntVar(-mx * (1 << t) - 1, mx * (1 << t) + 1, f"y{t}_{p}")
              for p in range(n)] for t in range(K + 1)]
        for p in range(n):
            m.Add(v[0][p] == E[p])
            m.Add(v[K][p] == 0)
    b = []
    for t in range(K):
        bt = [m.NewBoolVar(f"b{t}_{q}") for q in range(len(pairs))]
        b.append(bt)
        m.AddExactlyOne(bt)
        for q, (i, j) in enumerate(pairs):
            if model_class == "A":
                half = m.NewIntVar(LO, HI, f"h{t}_{q}")
                m.Add(2 * half == v[t][i] + v[t][j])
                m.Add(v[t + 1][i] == half).OnlyEnforceIf(bt[q])
                m.Add(v[t + 1][j] == half).OnlyEnforceIf(bt[q])
                for p in range(n):
                    if p not in (i, j):
                        m.Add(v[t + 1][p] == v[t][p]).OnlyEnforceIf(bt[q])
            else:
                s = m.NewIntVar(-mx * (1 << (t + 1)) - 1, mx * (1 << (t + 1)) + 1,
                               f"s{t}_{q}")
                m.Add(s == v[t][i] + v[t][j])
                m.Add(v[t + 1][i] == s).OnlyEnforceIf(bt[q])
                m.Add(v[t + 1][j] == s).OnlyEnforceIf(bt[q])
                for p in range(n):
                    if p not in (i, j):
                        m.Add(v[t + 1][p] == 2 * v[t][p]).OnlyEnforceIf(bt[q])
    # cutting planes: non-zero positions <= 2*(K-t); sum of deviations stays 0
    for t in range(K + 1):
        nz = [m.NewBoolVar(f"nz{t}_{p}") for p in range(n)]
        for p in range(n):
            m.Add(v[t][p] == 0).OnlyEnforceIf(nz[p].Not())
            m.Add(v[t][p] != 0).OnlyEnforceIf(nz[p])
        m.Add(sum(nz) <= 2 * (K - t))
    # symmetry break: the first move is on an ordered pair
    m.Add(b[0][0] == 1) if False else None
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit
    solver.parameters.num_search_workers = 8
    solver.parameters.log_search_progress = False
    t0 = time.time()
    st = solver.Solve(m)
    el = time.time() - t0
    name = solver.StatusName(st)
    out = {"status": name, "secs": round(el, 1), "branches": solver.NumBranches(),
           "conflicts": solver.NumConflicts(), "walltime": round(solver.WallTime(), 1)}
    if name in ("OPTIMAL", "FEASIBLE"):
        seq = []
        for t in range(K):
            for q, (i, j) in enumerate(pairs):
                if solver.Value(bt := b[t][q]):
                    seq.append((i + 1, j + 1))
                    break
        out["sequence"] = seq
        # independent replay of the additive dynamics (exact, integer)
        y = list(E)
        for (i, j) in seq:
            s = y[i - 1] + y[j - 1]
            y = [s if p in (i - 1, j - 1) else 2 * x for p, x in enumerate(y)]
        out["replay_ok"] = all(x == 0 for x in y)
    return out


def primitive_deviations(a):
    from math import gcd
    n, S = len(a), sum(a)
    d = [n * x - S for x in a]
    g = 0
    for x in d:
        g = gcd(g, x)
    return [x // g for x in d] if g else d


if __name__ == "__main__":
    cls = sys.argv[1]
    K = int(sys.argv[2])
    a = [int(x) for x in sys.argv[3:]]
    tl = float(sys.argv[-1]) if sys.argv[-1].replace(".", "").isdigit() else 600.0
    if len(sys.argv) > 4:
        try:
            tl = float(sys.argv[-1])
        except Exception:
            tl = 600.0
    E = primitive_deviations(a)
    print(f"model {cls}, K={K}, n={len(a)}, primitive deviations {E}", flush=True)
    print(build(cls, E, K, tl), flush=True)
