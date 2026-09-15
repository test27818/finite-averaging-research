from fractions import Fraction as F
from itertools import combinations_with_replacement
from collections import Counter, deque

def bstate(n):
    m = n - 4
    return tuple(sorted([(F(1), F(0))] * m + [(F(0), F(1))] * 3 + [(F(-m), F(-3))]))

def add(s):
    return (sum(x for x, y in s), sum(y for x, y in s))

def step(st, sig):
    q = tuple(x / 3 for x in add(sig))
    a = list(st)
    for x in sig:
        a.remove(x)
    a += [q] * 3
    return tuple(sorted(a))

def choices(st):
    vals = sorted(set(st))
    for inds in combinations_with_replacement(range(len(vals)), 3):
        sig = tuple(vals[i] for i in inds)
        c = Counter(sig)
        if len(c) > 1 and all(st.count(x) >= k for x, k in c.items()):
            yield sig

def bparams(n, st):
    m = n - 4
    c = Counter(st)
    if sorted(c.values()) != sorted([1, 3, m]):
        return None
    u = [x for x, k in c.items() if k == m]
    v = [x for x, k in c.items() if k == 3]
    return u[0], v[0]

for n in [17, 19, 23]:
    for depth in [5, 6]:
        start = bstate(n)
        q = deque([(start, ())])
        seen = {start}
        found = None
        while q:
            st, path = q.popleft()
            bp = bparams(n, st)
            if path and bp and bp != ((F(1), F(0)), (F(0), F(1))):
                found = (len(path), bp, path)
                break
            if len(path) >= depth:
                continue
            for sig in choices(st):
                ns = step(st, sig)
                if ns not in seen:
                    seen.add(ns)
                    q.append((ns, path + (sig,)))
        print(n, depth, "seen", len(seen), "found", bool(found), found)
