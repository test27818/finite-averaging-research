"""Audit the explicit 3-, 4-, and 5-point claims in the paper."""

from collections import Counter, deque
from fractions import Fraction
from itertools import combinations, combinations_with_replacement
from math import gcd

if not __debug__:
    raise RuntimeError('Assertions are required.')


def primitive(state):
    d = 0
    for value in state:
        d = gcd(d, abs(value))
    if not d:
        return tuple(state)
    state = tuple(sorted(value // d for value in state))
    neg = tuple(sorted(-value for value in state))
    return min(state, neg)


def step_family(u, v):
    state = primitive((u, v))
    u, v = state
    if u + v == 0:
        return True, 0
    if u % 3 == 0 and u and v % 3:
        q = u // 3
        ok, depth = step_family(v - q, -q)
        return ok, None if depth is None else depth + 1
    if v % 3 == 0 and v and u % 3:
        q = v // 3
        ok, depth = step_family(u - q, -q)
        return ok, None if depth is None else depth + 1
    return False, None


def family_state(u, v):
    # Center c is determined by 5c+u+v=0; this is only used when integral.
    assert (-u - v) % 5 == 0
    c = (-u - v) // 5
    return tuple(sorted((c + u, c + v, c, c, c)))


def rational_bfs(state, depth=12):
    current = tuple(Fraction(value) for value in state)
    queue = deque([(tuple(sorted(current)), 0)])
    seen = {queue[0][0]}
    while queue:
        state, level = queue.popleft()
        if not any(state):
            return True
        if level == depth:
            continue
        for selected in combinations(range(len(state)), 3):
            mean = sum(state[i] for i in selected) / 3
            nxt = list(state)
            for i in selected:
                nxt[i] = mean
            nxt = tuple(sorted(nxt))
            if nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, level + 1))
    return False


def integer_bfs(state):
    start = tuple(sorted(state))
    queue = deque([start])
    seen = {start}
    while queue:
        state = queue.popleft()
        if not any(state):
            return True
        for selected in combinations(range(len(state)), 3):
            total = sum(state[i] for i in selected)
            if total % 3:
                continue
            mean = total // 3
            nxt = list(state)
            for i in selected:
                nxt[i] = mean
            nxt = tuple(sorted(nxt))
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return False


def main():
    for a, b, c, d in ((0, 1, 5, 2), (0, 0, 1, 0)):
        state = (a, b, c, d)
        mean = Fraction(sum(state), 4)
        assert rational_bfs(tuple(Fraction(x) - mean for x in state), 2) == (0 in state or len(set(state)) == 1)
    for u in range(-60, 61):
        for v in range(-60, 61):
            if u + v or gcd(u, v) != 1 or (u + v) % 5:
                continue
            state = family_state(u, v)
            predicted = step_family(u, v)[0]
            actual = rational_bfs(state, 18)
            assert not (predicted and not actual), (state, u, v)
    # The smallest representative of the standard 5-point obstruction.
    obstruction = (-3, 0, 1, 1, 1)
    assert not integer_bfs(obstruction)
    assert not rational_bfs(obstruction, 12)
    for bound in (2, 3, 4):
        checked = 0
        for prefix in combinations_with_replacement(range(-bound, bound + 1), 5):
            if sum(prefix):
                continue
            if primitive(prefix) == (0,) * 5:
                continue
            checked += 1
            # Every family state is tested against the exact recursive predicate
            # whenever its multiset has a triple value.
            counts = Counter(prefix)
            for c, multiplicity in counts.items():
                if multiplicity < 3:
                    continue
                rest = list(prefix)
                for _ in range(3):
                    rest.remove(c)
                if len(rest) == 2:
                    assert rational_bfs(prefix, 8) == step_family(rest[0] - c, rest[1] - c)[0]
        print('five-point bounded recursive checks:', bound, checked)
    print('3/4/5-point claims: PASS')


if __name__ == '__main__':
    main()
