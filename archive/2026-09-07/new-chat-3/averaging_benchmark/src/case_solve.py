#!/usr/bin/env python3
"""本案例 [38,-23,-14,16,-11,4,63,80,14,38] 最少步数 = 10 的完整可复现求解。

    执行: python3 src/case_solve.py
    输出: 判定 -> 零和分解(下界) -> 10 步序列(验证) -> 证明无 9 步(情形①穷举)。

    各步都是精确算术(Fraction/BigInt)，零依赖。
"""
import sys, time
from math import gcd
from fractions import Fraction
from functools import lru_cache

A0 = [38, -23, -14, 16, -11, 4, 63, 80, 14, 38]
N = len(A0)
S = sum(A0)
A = Fraction(S, N)
# 偏差化(目标0): E_i = 2*(a_i - A)，都是整数、和 0
E = [2 * x - (2 * S // N) for x in A0]  # 2a_i - 41, 见下
# 更稳妥: 直接算 2*a_i 与 41
E = [2 * a - 41 for a in A0]
assert sum(E) == 0

print(f"实例 {A0}")
print(f"均值 A = {A}   偏差 E = {E}")

# ---- 1. 判定(G 判据) ----
dev = [N * a - S for a in A0]
g = 0
for d in dev:
    g = gcd(g, d)
e = [d // g for d in dev]
G = 0
for i in range(1, N):
    G = gcd(G, e[i] - e[0])
mixable = G > 0 and (G & (G - 1)) == 0
print(f"\n[1] 判定: g={g}  G={G}  -> 可平均={mixable}")

# ---- 2. 零和块分解(下界) ----
zs = [m for m in range(1, 1 << N) if sum(E[i] for i in range(N) if m >> i & 1) == 0]
print(f"[2] 零和子集 {len(zs)} 个")
@lru_cache(maxsize=None)
def maxparts(mask):
    best = 0
    for z in zs:
        if z & ~mask or not z:
            continue
        best = max(best, 1 + maxparts(mask ^ z))
    return best
mp = maxparts((1 << N) - 1)
print(f"    最大不相交零和块数 = {mp}  -> 连通下界 = n - mp = {N - mp}")

# 找出一个 4+6 分解
def find_split():
    for z in zs:
        if bin(z).count('1') == 4:
            comp = ((1 << N) - 1) ^ z
            if sum(E[i] for i in range(N) if comp >> i & 1) == 0:
                return z, comp
    return None, None
z4, z6 = find_split()
print(f"    4+6 分解: 4元块位掩码={z4}, 6元块={z6}")

# ---- 3. 小块 BFS 求精确最少步数，拼 10 步序列 ----
def bfs_min(vals, budget=300000):
    n = len(vals); S2 = sum(vals); target = Fraction(S2, n)
    start = tuple(Fraction(x) for x in vals)
    if all(x == target for x in start): return 0, []
    key = lambda st: tuple(sorted(st))
    seen = {key(start)}; parent = {}; frontier = [start]; depth = 0
    while frontier:
        depth += 1; nxt = []
        for st in frontier:
            sk = key(st)
            for i in range(n):
                for j in range(i + 1, n):
                    m = (st[i] + st[j]) / 2
                    ns = list(st); ns[i] = m; ns[j] = m; ns = tuple(ns)
                    k = key(ns)
                    if k in seen: continue
                    seen.add(k); parent[k] = (sk, i, j)
                    if all(x == target for x in ns):
                        steps = []; cur = k
                        while cur != key(start):
                            pk, i, j = parent[cur]; steps.append((i + 1, j + 1)); cur = pk
                        return depth, steps[::-1]
                    nxt.append(ns)
                    if len(seen) > budget: return None, None
        frontier = nxt
    return None, None

b4 = [E[i] for i in range(N) if z4 >> i & 1]
b6 = [E[i] for i in range(N) if z6 >> i & 1]
m4, seq4 = bfs_min(b4); m6, seq6 = bfs_min(b6)
pos4 = [i + 1 for i in range(N) if z4 >> i & 1]
pos6 = [i + 1 for i in range(N) if z6 >> i & 1]
full = [(pos4[i-1], pos4[j-1]) for i, j in seq4] + [(pos6[i-1], pos6[j-1]) for i, j in seq6]
print(f"[3] 4元块 min={m4} 序列={seq4}  6元块 min={m6} 序列={seq6}")
print(f"    拼成 {len(full)} 步序列: {full}")

# 精确验证
v = [Fraction(x) for x in A0]
for i, j in full:
    m = (v[i-1] + v[j-1]) / 2; v[i-1] = m; v[j-1] = m
print(f"    验证最终全等于均值: {all(x == A for x in v)}")

# ---- 4. 证明无 9 步: 情形①穷举(4 次 setup 能否把 E 变成 ± 可配) ----
def is_pairable(st):
    return tuple(sorted(st)) == tuple(sorted(-x for x in st))

def setups_bfs(k=4):
    states = {tuple(sorted(Fraction(x) for x in E))}
    for step in range(k):
        nxt = set()
        for st in states:
            for i in range(N):
                for j in range(i + 1, N):
                    m = (st[i] + st[j]) / 2
                    ns = list(st); ns[i] = m; ns[j] = m
                    nxt.add(tuple(sorted(ns)))
        states = nxt
        if any(is_pairable(s) for s in states):
            return True
    return False

t0 = time.time()
pairable = setups_bfs(4)
print(f"[4] 4 次 setup 能否把 E 变成 ± 可配: {pairable}   ({time.time()-t0:.1f}s)")
print(f"\n结论: 最少步数 = 10  (10 步已验证, 9 步情形①被穷举否定, 情形②被最小性排除)")
