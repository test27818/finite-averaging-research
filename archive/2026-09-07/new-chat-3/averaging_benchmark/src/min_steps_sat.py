#!/usr/bin/env python3
"""CP-SAT 精确求解"最少步数"（任意 n，n<=6 秒出，n=10 要强机器）。

    用法: pip install ortools && python3 src/min_steps_sat.py  a1 a2 ... an  [max_steps]

    从下界(连通性/简单界)起逐个 k 判定"是否存在 k 步解"，直到 SAT 为止。
    返回精确最少步数 + 一条操作序列(1-based 下标)。
"""
import sys
import time
from math import gcd
from ortools.sat.python import cp_model


def judge(a):
    n = len(a)
    if n <= 2:
        return True
    S = sum(a)
    if n == 3:
        b = sorted(a)
        return 2 * b[1] == b[0] + b[2]
    dev = [n * x - S for x in a]
    g = 0
    for d in dev:
        g = gcd(g, d)
    if g == 0:
        return True
    e = [d // g for d in dev]
    G = 0
    for i in range(1, n):
        G = gcd(G, e[i] - e[0])
    return G > 0 and (G & (G - 1)) == 0


def min_steps_sat(a, max_steps=20, maxtime=60, lo=None):
    """返回 (min_steps, sequence) 或 (None, None)。"""
    n = len(a)
    S = sum(a)
    # 偏差化（目标 0）
    E = [n * x - S for x in a]          # 同余缩放不影响，只要和 0
    if sum(E) != 0:
        E = [n * x - S for x in a]
    # 归一化偏差，和必为 0
    g = 0
    for d in E:
        g = gcd(g, d)
    if g:
        E = [d // g for d in E]

    SCALE = 1 << max_steps
    LO = min(E) * SCALE - 4
    HI = max(E) * SCALE + 4
    init = [e * SCALE for e in E]
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]

    kmin = lo if lo is not None else (n - 1)  # 连通下界（单连通）
    t0 = time.time()
    for k in range(kmin, max_steps + 1):
        model = cp_model.CpModel()
        v = [[model.NewIntVar(LO, HI, f'v{t}_{p}') for p in range(n)] for t in range(k + 1)]
        for p in range(n):
            model.Add(v[0][p] == init[p])
            model.Add(v[k][p] == 0)
        bs = []
        for t in range(k):
            b = [model.NewBoolVar(f'b{t}_{q}') for q in range(len(pairs))]
            bs.append(b)
            model.AddExactlyOne(b)
            for q, (i, j) in enumerate(pairs):
                half = model.NewIntVar(LO, HI, f'h{t}_{q}')
                model.Add(2 * half == v[t][i] + v[t][j])
                model.Add(v[t + 1][i] == half).OnlyEnforceIf(b[q])
                model.Add(v[t + 1][j] == half).OnlyEnforceIf(b[q])
                for p in range(n):
                    if p in (i, j):
                        continue
                    model.Add(v[t + 1][p] == v[t][p]).OnlyEnforceIf(b[q])
        # 非零个数上界：第 t 步非零 <= 2(k-t)（剩下每步最多清零 2 个）
        for t in range(k + 1):
            nz = [model.NewBoolVar(f'nz{t}_{p}') for p in range(n)]
            model.Add(sum(nz) <= 2 * (k - t))
            for p in range(n):
                model.Add(v[t][p] == 0).OnlyEnforceIf(nz[p].Not())
                model.Add(v[t][p] != 0).OnlyEnforceIf(nz[p])
        solver = cp_model.CpSolver()
        solver.parameters.max_time_in_seconds = maxtime
        solver.parameters.num_search_workers = 8
        st = solver.Solve(model)
        name = solver.StatusName(st)
        print(f"  k={k}: {name} ({time.time()-t0:.0f}s)", file=sys.stderr, flush=True)
        if name in ("OPTIMAL", "FEASIBLE"):
            seq = []
            for t in range(k):
                for q, (i, j) in enumerate(pairs):
                    if solver.Value(bs[t][q]):
                        seq.append((i + 1, j + 1))
                        break
            return k, seq
        if name != "INFEASIBLE":
            break
    return None, None


if __name__ == "__main__":
    a = [int(x) for x in sys.argv[1:]]
    if not judge(a):
        print("不可平均")
        sys.exit(0)
    r, seq = min_steps_sat(a)
    print("最少步数:", r)
    if seq:
        print("序列:", seq)
