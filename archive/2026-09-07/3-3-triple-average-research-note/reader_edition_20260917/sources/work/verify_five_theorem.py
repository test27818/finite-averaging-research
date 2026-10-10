from __future__ import annotations

from collections import deque
from itertools import combinations, combinations_with_replacement
from math import gcd


def primitive(values):
    d = 0
    for x in values:
        d = gcd(d, abs(x))
    if not d:
        return values
    values = tuple(x // d for x in values)
    # State is a multiset; global sign is harmless for reachability.
    values = tuple(sorted(values))
    neg = tuple(sorted(-x for x in values))
    return min(values, neg)


def step_family(u: int, v: int):
    if u + v == 0:
        return True, 0
    if u % 3 == 0 and u != 0 and v % 3:
        q = u // 3
        ok, d = step_family(v - q, -q)
        return ok, None if d is None else 1 + d
    if v % 3 == 0 and v != 0 and u % 3:
        q = v // 3
        ok, d = step_family(u - q, -q)
        return ok, None if d is None else 1 + d
    return False, None


def criterion_family(state):
    a, b, c, _, _ = state
    return step_family(a - c, b - c)[0]


def bfs(state, depth=8):
    state = primitive(state)
    zero = (0,) * 5
    q = deque([(state, 0)])
    seen = {state}
    while q:
        state, d = q.popleft()
        if state == zero:
            return True
        if d == depth:
            continue
        for S in combinations(range(5), 3):
            S = set(S)
            total = sum(state[i] for i in S)
            nxt = primitive(tuple(total if i in S else 3 * state[i] for i in range(5)))
            if nxt not in seen:
                seen.add(nxt)
                q.append((nxt, d + 1))
    return False


criterion_failures = []
bounded_witnesses = []
for a, b, c in combinations_with_replacement(range(-5, 6), 3):
    if a + b + 3 * c:
        continue
    state = primitive((a, b, c, c, c))
    if state == (0,) * 5:
        continue
    pred = criterion_family(state)
    actual = bfs(state, 10)
    if pred and not actual:
        criterion_failures.append((state, pred, actual))
    elif actual and not pred:
        bounded_witnesses.append((state, pred, actual))
print("checked family states; criterion failures within BFS bound:",
      criterion_failures[:20], "count", len(criterion_failures))
print("bounded BFS witnesses against criterion:",
      bounded_witnesses[:20], "count", len(bounded_witnesses))


def first_step_criterion(state):
    # Centered integer state. Enumerate the ten possible first triples.
    for S0 in combinations(range(5), 3):
        S = set(S0)
        total = sum(state[i] for i in S)
        nxt = primitive(tuple(total if i in S else 3 * state[i] for i in range(5)))
        # Sort the multiset then identify the repeated value. If there are >=3
        # copies, use that value and the two remaining entries.
        for c in set(nxt):
            if nxt.count(c) >= 3:
                rest = list(nxt)
                for _ in range(3):
                    rest.remove(c)
                if len(rest) != 2:
                    continue
                fam = (rest[0], rest[1], c, c, c)
                if criterion_family(fam):
                    return True
    return False


criterion_failures2 = []
bounded_witnesses2 = []
for prefix in combinations_with_replacement(range(-3, 4), 4):
    last = -sum(prefix)
    if not -3 <= last <= 3 or last < prefix[-1]:
        continue
    state = primitive(prefix + (last,))
    if state == (0,) * 5:
        continue
    pred = first_step_criterion(state)
    actual = bfs(state, 7)
    if pred and not actual:
        criterion_failures2.append((state, pred, actual))
    elif actual and not pred:
        bounded_witnesses2.append((state, pred, actual))
print("checked all small centered states; criterion failures within BFS bound:",
      criterion_failures2[:20], "count", len(criterion_failures2))
print("bounded BFS witnesses against criterion:",
      bounded_witnesses2[:20], "count", len(bounded_witnesses2))
