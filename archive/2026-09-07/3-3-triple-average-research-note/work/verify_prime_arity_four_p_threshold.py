"""Proof-directed 4p threshold and exact 3p one-step-closure obstruction."""

from collections import Counter
from itertools import combinations
from math import gcd
from random import Random

try:
    import verify_prime_arity_boundary_progress as previous
except ModuleNotFoundError:
    import verify_boundary_progress as previous

base = previous.base
linear = previous.linear

if not __debug__:
    raise RuntimeError('Assertions are required.')


def conditions(n, p):
    return p >= 3 and n >= len(base.protected_primes(n, p)) + 4 * p - 1


def choose(counts, n, p, factors):
    h = sorted(base.heavy(counts, p))
    if len(h) != 3:
        # For h=2, exactly2p positions are reserved. For h>=4 the existing
        # extreme-anchor move has no large-dimension assumption beyond n>2p.
        return previous.choose(counts, n, p, factors)
    pair = next(((u, v) for u, v in combinations(h, 2) if (u - v) % p == 0), None)
    if pair is not None:
        u, v = pair
        w = next(x for x in h if x not in pair)
        first = (u,) * (p - 1) + (v,)
        second = (v,) * (p - 1) + (u,)
        move = first if sum(first) != p * w else second
        assert sum(move) != p * w
        return move, 'three-heavy-shared-residue', None
    a, b, c = h
    light = next((x for x in counts if x not in h), None)
    if light is not None:
        if light < c:
            move = base.controller(a, b, light, p)
            assert sum(move) < p * c
            return move, 'three-heavy-light-below', None
        move = base.controller(b, c, light, p)
        assert sum(move) > p * a
        return move, 'three-heavy-light-above', None
    if counts[a] >= p + 1:
        move = base.controller(b, c, a, p)
        assert sum(move) > p * a
        return move, 'three-heavy-minimum-spare', None
    if counts[c] >= p + 1:
        move = base.controller(a, b, c, p)
        assert sum(move) < p * c
        return move, 'three-heavy-maximum-spare', None
    assert counts[a] == counts[c] == p
    assert counts[b] == n - 2 * p >= 2 * p - 1
    return linear.choose(counts, n, p, factors)


def audit(counts, n, p, branches):
    assert conditions(n, p)
    assert sum(counts.values()) == n and sum(x * f for x, f in counts.items()) == 0
    factors = base.protected_primes(n, p)
    if not base.legal(counts, factors) or len(base.heavy(counts, p)) < 2:
        return False
    move, branch, delta = choose(counts, n, p, factors)
    branches[branch] += 1
    if move is None:
        assert set(counts) == {0, delta, -delta} and counts[delta] == counts[-delta]
    else:
        result = base.change(counts, move, p)
        assert base.legal(result, factors) and len(base.heavy(result, p)) >= 2
    return True


def solve(initial, p):
    n = len(initial)
    assert conditions(n, p) and sum(initial) == 0
    factors = base.protected_primes(n, p)
    assert base.legal(Counter(initial), factors)
    replay = base.LabelledReplay(initial, p)
    branches = Counter()
    for move in base.initialize(replay.counts(), n, p, factors):
        replay.step(move)
        assert base.legal(replay.counts(), factors)
    while any(replay.state):
        counts = replay.counts()
        move, branch, delta = choose(counts, n, p, factors)
        branches[branch] += 1
        if move is None:
            for _ in range(counts[delta]):
                replay.step((delta, -delta) + (0,) * (p - 2))
            break
        result = base.change(counts, move, p)
        assert base.legal(result, factors) and len(base.heavy(result, p)) >= 2
        replay.step(move)
        assert replay.counts() == result
    assert not any(replay.state)
    previous.replay_original(initial, replay.word, p)
    return len(replay.word), branches


def light_examples(p, n, above):
    r = n - 3 * p
    counts = Counter({-1: p, 0: p, 1: p})
    values = []
    start = 2
    if r % 2:
        values.extend((2, 3, -5))
        r -= 3
        start = 6
    for i in range(r // 2):
        values.extend((start + i, -start - i))
    values.sort(reverse=above)
    counts.update(values)
    return counts


def main():
    random = Random(2026091204)
    branches = Counter()
    capacity = local = initializations = 0
    ps = (3, 5, 7, 11, 17, 31, 61)
    for p in ps:
        start = 4 * p + (p - 1).bit_length() + 1
        assert start <= 5 * p
        for n in range(start, start + 120):
            assert conditions(n, p)
            capacity += 1
        for _ in range(180):
            n = start + random.randrange(40)
            m = random.randrange(3, min(n - 2 * p + 3, 13))
            weights = [p, p] + [1] * (m - 2)
            remaining = n - sum(weights)
            for i in range(m - 1):
                extra = random.randrange(remaining + 1)
                weights[i] += extra
                remaining -= extra
            weights[-1] += remaining
            values = [random.randrange(-10**12, 10**12) * weights[-1] for _ in range(m - 1)]
            values.append(-sum(x * f for x, f in zip(values, weights)) // weights[-1])
            counts = Counter()
            for x, f in zip(values, weights):
                counts[x] += f
            local += audit(counts, n, p, branches)
        for counts in (Counter({0: start - 2 * p, p: p, -p: p}),
                       light_examples(p, start, False), light_examples(p, start, True),
                       Counter({-(2 * p + 1): p + 1, 0: p, p + 1: 2 * p + 1}),
                       Counter({-(3 * p + 1): p, p: 2 * p, p + 1: p})):
            assert audit(counts, sum(counts.values()), p, branches)
        if p >= 5 and p % 5 != 2:
            counts = Counter({-(p + 2): p, 1: 2 * p + 1, p - 1: p + 1})
            assert audit(counts, sum(counts.values()), p, branches)
        values = list(range(1, start))
        values.append(-sum(values))
        factors = base.protected_primes(start, p)
        counts = Counter(p * x for x in values)
        moves = base.initialize(counts, start, p, factors)
        assert len(moves) <= 2
        for move in moves:
            counts = base.change(counts, move, p)
            assert base.legal(counts, factors)
        assert len(base.heavy(counts, p)) >= 2
        initializations += 1
    for p, start, end in ((3, 12, 13), (5, 20, 22), (7, 28, 30)):
        for n in range(start, end + 1):
            assert conditions(n, p)
        n = end + 1
        assert n - (n.bit_length() - 1) >= 4 * p - 1
    print('four-p threshold capacity checks: PASS', capacity)
    print('four-p large-coordinate closure: PASS', local)
    print('four-p initialization: PASS', initializations)

    obstruction = 0
    for p in (5, 7, 11, 13, 17, 19, 31, 61):
        kappa = 1 if p % 3 == 2 else 2
        values = (-kappa * p - 1, 1, kappa * p)
        counts = Counter({x: p for x in values})
        assert gcd(values[1] - values[0], values[2] - values[0]) == 1
        assert base.legal(counts, base.protected_primes(3 * p, p))
        for r in range(p + 1):
            for s in range(p - r + 1):
                t = p - r - s
                total = r * values[0] + s * values[1] + t * values[2]
                assert total != 0
                if total % p or max(r, s, t) == p:
                    continue
                assert min(r, s, t) > 0
                result = base.change(counts, (values[0],) * r + (1,) * s + (values[2],) * t, p)
                assert len(base.heavy(result, p)) == 1
                obstruction += 1
    print('three-p complete value-type closure obstruction: PASS', obstruction)

    cases = 0
    maximum = (0, 0, 0)
    for p in (3, 5, 7, 11):
        start = 4 * p
        for offset in range(4):
            n = start + offset
            assert conditions(n, p)
            values = [random.randrange(-2, 3) for _ in range(n - 1)]
            values.append(-sum(values))
            assert base.legal(Counter(values), base.protected_primes(n, p))
            length, used = solve(values, p)
            branches.update(used)
            maximum = max(maximum, (length, p, n))
            cases += 1
    print('four-p full original-position paths: PASS', cases, 'longest', maximum)
    print('branches exercised:', dict(sorted(branches.items())))
    print('prime-arity four-p threshold: PASS')


if __name__ == '__main__':
    main()
