#!/usr/bin/env python3
"""CP-SAT 判定：实例 [38,-23,-14,16,-11,4,63,80,14,38] 是否存在 9 步解。

   用法: pip install ortools && python3 src/decide9_sat.py [max_time_seconds]
   输出: SAT  -> 存在 9 步解，并打印序列（自动精确验证）
         UNSAT -> 不存在（配合已证的下界 9 与已验证的 10 步解，即 min = 10）
         UNKNOWN -> 超时，加大 max_time_seconds 重跑
"""
import sys
from ortools.sat.python import cp_model
import time

# 偏差（目标 0），缩放 2^9 使全程为整数
E = [35, -87, -69, -9, -63, -33, 85, 119, -13, 35]
n = 10
SCALE = 1 << 9
LO = min(E) * SCALE - 4
HI = max(E) * SCALE + 4
init = [e * SCALE for e in E]
MAXTIME = float(sys.argv[1]) if len(sys.argv) > 1 else 3600.0

model = cp_model.CpModel()
v = [[model.NewIntVar(LO, HI, f'v_{t}_{p}') for p in range(n)] for t in range(n)]
nz = [[model.NewBoolVar(f'nz_{t}_{p}') for p in range(n)] for t in range(n)]
for p in range(n):
    model.Add(v[0][p] == init[p])
    model.Add(v[9][p] == 0)
for t in range(n):
    model.Add(sum(v[t][p] for p in range(n)) == 0)          # 总和恒 0（冗余，助线性松弛）
    model.Add(sum(nz[t][p] for p in range(n)) <= 2 * (9 - t))  # 关键：非零个数上界
    for p in range(n):
        model.Add(v[t][p] == 0).OnlyEnforceIf(nz[t][p].Not())
        model.Add(v[t][p] != 0).OnlyEnforceIf(nz[t][p])

pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
bs = []
for t in range(9):
    b = [model.NewBoolVar(f'b_{t}_{k}') for k in range(len(pairs))]
    bs.append(b)
    model.AddExactlyOne(b)
    for k, (i, j) in enumerate(pairs):
        model.Add(2 * v[t + 1][i] == v[t][i] + v[t][j]).OnlyEnforceIf(b[k])
        model.Add(2 * v[t + 1][j] == v[t][i] + v[t][j]).OnlyEnforceIf(b[k])
        for p in range(n):
            if p == i or p == j:
                continue
            model.Add(v[t + 1][p] == v[t][p]).OnlyEnforceIf(b[k])
for k in range(len(pairs)):
    model.Add(sum(bs[t][k] for t in range(9)) <= 1)          # 9 步单连通 => 9 个不同对
for p in range(n):
    model.Add(sum(bs[t][k] for t in range(9) for k, (i, j) in enumerate(pairs) if p in (i, j)) >= 1)

solver = cp_model.CpSolver()
solver.parameters.max_time_in_seconds = MAXTIME
solver.parameters.num_search_workers = 8
t0 = time.time()
st = solver.Solve(model)
print(f"状态: {solver.StatusName(st)}  耗时 {time.time()-t0:.1f}s", flush=True)
if st in (cp_model.OPTIMAL, cp_model.FEASIBLE):
    seq = []
    for t in range(9):
        for k, (i, j) in enumerate(pairs):
            if solver.Value(bs[t][k]):
                seq.append((i + 1, j + 1))
                break
    print("SAT: 存在 9 步解，序列:", seq, flush=True)
    from fractions import Fraction
    vals = [Fraction(x) for x in E]
    for (i, j) in seq:
        m = (vals[i - 1] + vals[j - 1]) / 2
        vals[i - 1] = m
        vals[j - 1] = m
    print("精确验证全 0:", all(x == 0 for x in vals), flush=True)
elif st == cp_model.UNSATISFIABLE:
    print("UNSAT: 不存在 9 步解 -> min = 10", flush=True)
else:
    print("UNKNOWN: 超时，加大时限重跑", flush=True)
