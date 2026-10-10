"""Exact audits for the linear prime-arity threshold and the 2p boundary."""

from collections import Counter, defaultdict
from itertools import combinations_with_replacement
from math import gcd
from random import Random

try:
    import verify_prime_arity_large_dimension as base
except ModuleNotFoundError:
    import verify_prime_arity as base

if not __debug__:
    raise RuntimeError('Assertions are required.')


def rotate_bits(bits, shift, p):
    limit = (1 << p) - 1
    shift %= p
    if not shift:
        return bits
    return ((bits << shift) | (bits >> (p - shift))) & limit


def egz_subset(values, p):
    """Cardinality/residue bitset DP, followed by exact prefix backtracking."""
    assert len(values) == 2 * p - 1
    rows = [1] + [0] * p
    history = [rows.copy()]
    for length, value in enumerate(values, 1):
        for k in range(min(length, p), 0, -1):
            rows[k] |= rotate_bits(rows[k - 1], value, p)
        history.append(rows.copy())
    assert rows[p] & 1, ('EGZ failure', p, values)
    selected = []
    cardinality = p
    residue = 0
    for i in range(len(values), 0, -1):
        if history[i - 1][cardinality] & (1 << residue):
            continue
        selected.append(i - 1)
        residue = (residue - values[i - 1]) % p
        cardinality -= 1
    assert cardinality == residue == 0
    assert len(set(selected)) == p and sum(values[i] for i in selected) % p == 0
    return tuple(values[i] for i in selected)


def protected_egz(counts, light, n, p, factors):
    available = light.copy()
    for q in factors:
        residues = Counter()
        for x, f in counts.items():
            residues[x % q] += f
        majority = next((r for r, f in residues.items() if f >= n - p), None)
        if majority is None:
            continue
        exceptions = {x: f for x, f in counts.items() if x % q != majority}
        assert 2 <= sum(exceptions.values()) <= p
        if all(available[x] == f for x, f in exceptions.items()):
            available[next(iter(exceptions))] -= 1
            available += Counter()
    assert max(available.values()) < p
    values = []
    for x, f in available.items():
        values.extend([x] * min(f, 2 * p - 1 - len(values)))
        if len(values) == 2 * p - 1:
            break
    move = egz_subset(values, p)
    assert len(set(move)) > 1
    return move


def crossing_move(counts, b, delta, p):
    coefficients = []
    for x, f in counts.items():
        if x in (b, b + delta):
            continue
        assert (b - x) % delta == 0
        j = (b - x) // delta
        assert 1 <= j < p
        coefficients.extend([j] * min(f, p))
    coefficients.sort(reverse=True)
    assert coefficients[0] >= 2 and sum(coefficients) >= p
    total = 0
    selected = []
    for j in coefficients:
        selected.append(j)
        total += j
        if total >= p:
            break
    s = len(selected)
    assert 2 <= s < p
    assert total + s <= 2 * p
    t = total - p
    zeros = p - s - t
    move = tuple(b - j * delta for j in selected) + (b + delta,) * t + (b,) * zeros
    assert len(move) == p and len(set(move)) > 1
    assert sum(move) == p * (b - delta)
    return move


def choose(counts, n, p, factors):
    h = sorted(base.heavy(counts, p))
    assert len(h) >= 2 and base.legal(counts, factors)
    if len(h) >= 4:
        first = h[:3]
        pair = next(((a, c) for a in first for c in first if (a - c) % p), None)
        if pair is None:
            return (first[0],) * (p - 1) + (first[1],), 'four-heavy-common-residue', None
        a, c = pair
        x = next(x for x in first if x not in pair)
        return base.controller(a, c, x, p), 'four-heavy-extreme-anchor', None
    light = Counter({x: f for x, f in counts.items() if f < p})
    if sum(light.values()) >= len(factors) + 2 * p - 1:
        return protected_egz(counts, light, n, p, factors), 'protected-EGZ', None
    b = max(h, key=counts.get)
    assert counts[b] >= 2 * p - 1
    a = next(x for x in h if x != b)
    if (a - b) % p == 0:
        return (b,) * (p - 1) + (a,), 'same-residue-background', None
    others = [x for x in counts if x not in (a, b)]
    assert others
    for x in others:
        move = base.controller(a, b, x, p)
        if sum(move) != p * b:
            return move, 'single-value-controller', None
    delta = a - b
    assert gcd(delta, n) == 1
    coefficients = {}
    for x in others:
        assert (b - x) % delta == 0
        coefficients[x] = (b - x) // delta
        assert 1 <= coefficients[x] < p
    if counts[a] >= 2 * p - 1:
        return base.controller(a, b, others[0], p), 'large-second-heavy', None
    for x in others:
        if counts[x] >= 2 * p - 1:
            return base.controller(x, b, a, p), 'large-progression-heavy', None
    total_negative = sum(coefficients[x] * counts[x] for x in others)
    if total_negative >= p and max(coefficients.values()) >= 2:
        return crossing_move(counts, b, delta, p), 'coefficient-crossing', None
    assert total_negative >= p, 'small negative total violates zero-sum legality'
    assert max(coefficients.values()) == 1
    assert counts[a] == counts[b - delta] and b == 0
    return None, 'opposite-pairs-terminal', delta


def conditions(n, p):
    return n >= len(base.protected_primes(n, p)) + 8 * p - 7


def audit(counts, n, p, branches):
    assert conditions(n, p)
    assert sum(counts.values()) == n and sum(x * f for x, f in counts.items()) == 0
    factors = base.protected_primes(n, p)
    if len(base.heavy(counts, p)) < 2 or not base.legal(counts, factors):
        return False
    move, branch, delta = choose(counts, n, p, factors)
    branches[branch] += 1
    if move is None:
        assert set(counts) == {0, delta, -delta}
        assert counts[delta] == counts[-delta] and counts[0] >= 2 * p - 1
    else:
        after = base.change(counts, move, p)
        assert base.legal(after, factors) and len(base.heavy(after, p)) >= 2
    return True


def solve(initial, p):
    n = len(initial)
    factors = base.protected_primes(n, p)
    assert base.is_prime(p) and conditions(n, p) and sum(initial) == 0
    assert base.legal(Counter(initial), factors)
    if not any(initial):
        return 0, Counter()
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
        expected = base.change(counts, move, p)
        assert base.legal(expected, factors) and len(base.heavy(expected, p)) >= 2
        replay.step(move)
        assert replay.counts() == expected
    assert not any(replay.state) and replay.energy == 0
    from fractions import Fraction
    original = list(map(Fraction, initial))
    for positions in replay.word:
        mean = sum(original[i] for i in positions) / p
        assert mean.denominator in (1, p)
        for i in positions:
            original[i] = mean
    assert not any(original)
    return len(replay.word), branches


def main():
    random = Random(2026091202)
    capacity = egz = crossing = local = starts = 0
    branches = Counter()
    for p in (2, 3, 5, 7, 11, 17, 31, 61):
        for n in range(9 * p - 5, 9 * p + 150):
            assert conditions(n, p)
            capacity += 1
        for _ in range(150):
            values = [random.randrange(-10**12, 10**12) for _ in range(2 * p - 1)]
            egz_subset(values, p)
            egz += 1
        if p >= 3:
            for _ in range(200):
                js = [random.randrange(1, p) for _ in range(random.randrange(2, 2 * p))]
                if max(js) < 2 or sum(js) < p:
                    continue
                counts = Counter({0: 3 * p, 1: p})
                counts.update(-j for j in js)
                move = crossing_move(counts, 0, 1, p)
                after = base.change(counts, move, p)
                assert after[-1] >= p and after[0] >= p
                crossing += 1
        for _ in range(180):
            n = 9 * p - 5 + random.randrange(100)
            m = random.randrange(3, min(n - 2 * p + 3, 17))
            weights = [p, p] + [1] * (m - 2)
            remaining = n - sum(weights)
            for i in range(m - 1):
                extra = random.randrange(remaining + 1)
                weights[i] += extra
                remaining -= extra
            weights[-1] += remaining
            values = [random.randrange(-10**10, 10**10) * weights[-1] for _ in range(m - 1)]
            values.append(-sum(x * f for x, f in zip(values, weights)) // weights[-1])
            counts = Counter()
            for x, f in zip(values, weights):
                counts[x] += f
            local += audit(counts, n, p, branches)
        for multiplicity in (0, p, 2 * p):
            n = 9 * p - 5
            raw = [0] * multiplicity + list(range(1, n - multiplicity))
            raw.append(-sum(raw))
            counts = Counter(p * x for x in raw)
            factors = base.protected_primes(n, p)
            assert base.legal(counts, factors)
            moves = base.initialize(counts, n, p, factors)
            assert len(moves) <= 2
            for move in moves:
                counts = base.change(counts, move, p)
                assert base.legal(counts, factors)
            assert len(base.heavy(counts, p)) >= 2
            starts += 1
    # Exhaustive coefficient types at small p; this is independent of n.
    for p in (3, 5, 7):
        for s in range(2, p + 1):
            for js in combinations_with_replacement(range(1, p), s):
                if js[-1] < 2 or sum(js) < p:
                    continue
                counts = Counter({0: 3 * p, 1: p})
                counts.update(-j for j in js)
                base.change(counts, crossing_move(counts, 0, 1, p), p)
                crossing += 1
    # Force new branches in arithmetically legal zero-sum configurations.
    for p in (3, 5, 7, 11):
        n = 9 * p - 5
        examples = [Counter({0: n - 4 * p, 1: p, -1: p, 2: p, -2: p}),
                    Counter({0: n - 4 * p, p: p, -p: p, 2 * p: p, -2 * p: p}),
                    Counter({0: n - p - 2, 1: p, -(p - 1): 1, -1: 1})]
        light = list(range(2, n - 2 * p + 1))
        pool_example = Counter({0: p, 1: p})
        pool_example.update(light)
        pool_example[-sum(x * f for x, f in pool_example.items())] += 1
        examples.append(pool_example)
        for counts in examples:
            assert audit(counts, n, p, branches)
    assert audit(Counter({-2: 7, -1: 38, 4: 13}), 58, 7, branches)
    print('linear threshold capacity checks: PASS', capacity)
    print('EGZ fixed-cardinality residue witnesses: PASS', egz)
    print('coefficient-crossing exact checks: PASS', crossing)
    print('linear-threshold large-integer closure: PASS', local)
    print('linear-threshold initialization: PASS', starts)

    boundary = 0
    for p in (3, 5, 7, 11, 17, 31, 61):
        state = Counter({-p: 1, 0: p - 1, 1: p})
        integral = []
        for negative in (0, 1):
            for ones in range(p + 1):
                zeros = p - negative - ones
                if not 0 <= zeros <= p - 1:
                    continue
                values = (-p,) * negative + (1,) * ones + (0,) * zeros
                if sum(values) % p == 0 and len(set(values)) > 1:
                    integral.append(values)
        assert integral == [(-p,) + (0,) * (p - 1)]
        after = base.change(state, integral[0], p)
        assert after == Counter({-1: p, 1: p})
        assert {x % 2 for x in after} == {1}
        critical = Counter({1: p, 2: p, -3 * p: 1})
        critical_moves = []
        for exceptional in (0, 1):
            for ones in range(p + 1):
                twos = p - exceptional - ones
                if not 0 <= twos <= p:
                    continue
                move = (-3 * p,) * exceptional + (1,) * ones + (2,) * twos
                if sum(move) % p == 0 and len(set(move)) > 1:
                    critical_moves.append(move)
        assert len(critical_moves) == 1
        critical_after = base.change(critical, critical_moves[0], p)
        assert critical_after == Counter({1: 2, 2: p - 1, -2: p})
        assert len(base.heavy(critical_after, p)) == 1
        # At 2p+1 use the fixed four-step word, with exact labelled positions.
        initial = [-p] + [0] * p + [1] * p
        replay = base.LabelledReplay(initial, p)
        h = (p - 1) // 2
        for values in ((-p * p,) + (0,) * (p - 1),
                       (-p,) * h + (p,) * h + (0,),
                       (-p,) * h + (p,) * h + (0,),
                       (-p, p) + (0,) * (p - 2)):
            replay.step(values)
        assert not any(replay.state)
        boundary += 1
    print('2p obstruction and 2p+1 four-step family: PASS', boundary)
    print('2p+1 double-heavy one-step closure obstruction: PASS', boundary)

    complete = 0
    longest = (0, 0, 0)
    for p in (2, 3, 5, 7, 11):
        for offset in (0, 1, 3, 7):
            n = 9 * p - 5 + offset
            values = [random.randrange(-2, 3) for _ in range(n - 1)]
            values.append(-sum(values))
            assert base.legal(Counter(values), base.protected_primes(n, p))
            length, used = solve(values, p)
            branches.update(used)
            longest = max(longest, (length, p, n))
            complete += 1
    print('linear-threshold labelled complete paths: PASS', complete, 'longest', longest)
    print('linear proof branches:', dict(sorted(branches.items())))
    print('prime-arity linear threshold and boundary: PASS')


if __name__ == '__main__':
    main()
