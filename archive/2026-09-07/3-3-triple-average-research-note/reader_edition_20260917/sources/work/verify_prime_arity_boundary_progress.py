"""Exact audits for reserved multiplicities and critical boundary structures."""

from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import gcd, isqrt, prod
from random import Random

try:
    import verify_prime_arity_linear_threshold as linear
except ModuleNotFoundError:
    import verify_linear_threshold as linear

base = linear.base

if not __debug__:
    raise RuntimeError('Assertions are required.')


def conditions(n, p):
    return n >= len(base.protected_primes(n, p)) + 5 * p - 1


def choose(counts, n, p, factors):
    h = base.heavy(counts, p)
    assert len(h) >= 2
    if len(h) >= 4 or max(counts[x] for x in h) >= 2 * p - 1:
        return linear.choose(counts, n, p, factors)
    reserved = Counter({x: p for x in h})
    pool = counts - reserved
    assert sum(pool.values()) >= len(factors) + 2 * p - 1
    assert max(pool.values()) < p
    return linear.protected_egz(counts, pool, n, p, factors), 'reserved-heavy-EGZ', None


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
        after = base.change(counts, move, p)
        assert base.legal(after, factors) and len(base.heavy(after, p)) >= 2
    return True


def solve(initial, p):
    n = len(initial)
    factors = base.protected_primes(n, p)
    assert sum(initial) == 0 and conditions(n, p) and base.legal(Counter(initial), factors)
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
        after = base.change(counts, move, p)
        assert base.legal(after, factors) and len(base.heavy(after, p)) >= 2
        replay.step(move)
        assert replay.counts() == after
    assert not any(replay.state) and replay.energy == 0
    replay_original(initial, replay.word, p)
    return len(replay.word), branches


def replay_original(initial, word, p):
    state = list(map(Fraction, initial))
    for indices in word:
        assert len(indices) == len(set(indices)) == p
        mean = sum(state[i] for i in indices) / p
        assert mean.denominator in (1, p)
        for i in indices:
            state[i] = mean
    assert not any(state)


def zero_tail(initial, p):
    assert len(initial) == 2 * p + 1 and initial[0] == sum(initial) == 0
    replay = base.LabelledReplay(initial, p)
    for block in (initial[1:p + 1], initial[p + 1:]):
        values = tuple(p * x for x in block)
        if len(set(values)) > 1:
            replay.step(values)
    a = sum(initial[1:p + 1])
    assert replay.counts() == Counter([a] * p + [-a] * p + [0])
    if a:
        h = (p - 1) // 2
        replay.step((a,) * h + (-a,) * h + (0,))
        replay.step((a,) * h + (-a,) * h + (0,))
        replay.step((a, -a) + (0,) * (p - 2))
    assert not any(replay.state) and len(replay.word) <= 5
    replay_original(initial, replay.word, p)


def critical_four_steps(p):
    initial = [1] * p + [2] * p + [-3 * p]
    replay = base.LabelledReplay(initial, p)
    h = (p - 1) // 2
    moves = ((1,) * (p - 2) + (2, -3 * p),
             (-2,) * h + (1, 1) + (2,) * (h - 1),
             (-2,) * h + (2,) * h + (0,),
             (-2, 2) + (0,) * (p - 2))
    expected = (Counter({1: 2, 2: p - 1, -2: p}),
                Counter({0: p, -2: h + 1, 2: h + 1}),
                Counter({0: 2 * p - 1, -2: 1, 2: 1}),
                Counter({0: 2 * p + 1}))
    for move, after in zip(moves, expected):
        replay.step(tuple(p * x for x in move))
        assert replay.counts() == Counter({p * x: f for x, f in after.items()})
    replay_original(initial, replay.word, p)
    for exceptional in (0, 1):
        for ones in range(p - exceptional + 1):
            twos = p - exceptional - ones
            assert -3 * p * exceptional + ones + 2 * twos != 0
    assert len(replay.word) == 4


def partition_obstruction():
    qs = (3, 5, 7, 11, 13, 29)
    edges = list(combinations(range(4), 2))
    n = prod(qs)
    p = (n - 1) // 2
    assert (p, n) == (217717, 435435)
    assert base.is_prime(p) and isqrt(p) == 466
    values = []
    for vertex in range(4):
        value = 0
        for q, (a, b) in zip(qs, edges):
            residue = 0 if vertex == a else 2 if vertex == b else 1
            cofactor = n // q
            value += residue * cofactor * pow(cofactor, -1, q)
        values.append(value % n)
    total = n - 4 + sum(values) + n
    assert total % n == 0
    counts = Counter({1: n - 6, 1 + n: 1, 1 - total: 1})
    counts.update(values)
    assert sum(counts.values()) == n and sum(x * f for x, f in counts.items()) == 0
    assert gcd(*(x - 1 for x in counts)) == 1
    layouts = 0
    for assignment in product(range(3), repeat=4):
        if assignment.count(2) > 1:
            continue
        edge_id = next(i for i, (a, b) in enumerate(edges) if assignment[a] == assignment[b])
        q = qs[edge_id]
        assert assignment[edges[edge_id][0]] != 2
        outputs = []
        for block in (0, 1):
            vertices = [i for i, location in enumerate(assignment) if location == block]
            block_sum = p - len(vertices) + sum(values[i] for i in vertices)
            outputs.append(block_sum * pow(p, -1, q) % q)
        singleton = next((values[i] for i, location in enumerate(assignment) if location == 2), 1)
        outputs.append(singleton % q)
        assert outputs == [1, 1, 1]
        layouts += 1
    assert layouts == 48
    print('K4 blocking input:', dict(sorted(counts.items())))
    return layouts


def prime_dimension_entry(random):
    checked = repairs = 0
    for p in (3, 5, 11, 23, 29, 41):
        q = 2 * p + 1
        assert base.is_prime(p) and base.is_prime(q)
        for _ in range(80):
            state = [random.randrange(-10**8, 10**8) for _ in range(q - 1)]
            state.append(-sum(state))
            assert len({x % q for x in state}) > 1
            c = state[0]
            left = state[1:p + 1]
            right = state[p + 1:]
            if (2 * sum(left) + c) % q == 0:
                a = left[0]
                j = next((j for j, y in enumerate(right) if (y - a) % q), None)
                if j is not None:
                    left[0], right[j] = right[j], left[0]
                else:
                    y = right[0]
                    i = next(i for i, x in enumerate(left) if (x - y) % q)
                    left[i], right[0] = right[0], left[i]
                repairs += 1
            scaled = [p * c] + [sum(left)] * p + [sum(right)] * p
            assert sum(scaled) == 0
            divisor = gcd(*scaled)
            difference = gcd(*(x - scaled[0] for x in scaled))
            assert difference // divisor == 1
            checked += 1
    return checked, repairs


def cone_checks():
    count = 0
    for p in (5, 7, 11, 17, 31, 61):
        lower = Fraction(1) - Fraction(2, p)
        upper = Fraction(1) - Fraction(1, 2 * p)
        assert Fraction(1, 2) < lower <= upper < 1
        assert gcd(2 * p - 1, 2 * p + 1) == 1
        for denominator in range(1, 18):
            for numerator in range((denominator + 1) // 2, 2 * denominator + 1):
                t = Fraction(numerator, denominator)
                for result in (1 - t / p, 1 - 1 / (p * t)):
                    assert lower <= result <= upper
                    assert Fraction(1, 2) <= 1 / result <= 2
                    assert result != 1
                    count += 1
    assert 1 - Fraction(2, 3) < Fraction(1, 2)
    initial = [5] * 5 + [-4] * 5 + [-5]
    replay = base.LabelledReplay(initial, 5)
    for move in ((5, 5, 5, 5, -5), (-4, 3, 3, 3, 5),
                 (-4, -4, 3, 3, 2), (-4, 2, 2, 0, 0), (-4, 2, 2, 0, 0)):
        replay.step(tuple(5 * x for x in move))
    replay_original(initial, replay.word, 5)
    return count


def main():
    random = Random(2026091203)
    branches = Counter()
    capacities = local = initializations = 0
    for p in (2, 3, 5, 7, 11, 17, 31, 61):
        ell = (p - 1).bit_length()
        start = 5 * p + ell + 1
        assert start <= 6 * p
        for n in range(start, start + 150):
            assert conditions(n, p)
            capacities += 1
        for _ in range(160):
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
        raw = list(range(1, start))
        raw.append(-sum(raw))
        factors = base.protected_primes(start, p)
        counts = Counter(p * x for x in raw)
        moves = base.initialize(counts, start, p, factors)
        assert len(moves) <= 2
        for move in moves:
            counts = base.change(counts, move, p)
            assert base.legal(counts, factors)
        assert len(base.heavy(counts, p)) >= 2
        initializations += 1
    for p, start, exceptional_end in ((5, 25, 27), (7, 35, 38)):
        for n in range(start, exceptional_end + 1):
            assert conditions(n, p)
        n = exceptional_end + 1
        assert n - (n.bit_length() - 1) >= 5 * p - 1
    targets = ((2, Counter({0: 2, 1: 2, -1: 2, 2: 1, 3: 1, 4: 1, -2: 1, -3: 1, -4: 1})),
               (3, Counter({0: 4, 1: 4, -1: 4, 2: 1, 3: 1, 4: 1, -2: 1, -3: 1, -4: 1})),
               (5, Counter({0: 8, 1: 8, -1: 8, 2: 1, 3: 1, 4: 1, -2: 1, -7: 1})),
               (7, Counter({0: 12, 1: 12, -1: 12, 2: 1, 3: 1, -5: 1})),
               (11, Counter({0: 20, 1: 20, -1: 20})))
    for p, counts in targets:
        n = sum(counts.values())
        assert choose(counts, n, p, base.protected_primes(n, p))[1] == 'reserved-heavy-EGZ'
        assert audit(counts, n, p, branches)
    print('reserved-pool threshold instances: PASS', capacities)
    print('reserved-pool large-integer closure: PASS', local)
    print('reserved-pool initialization: PASS', initializations)

    zeros = critical = 0
    for p in (3, 5, 7, 11, 17, 31, 61):
        for _ in range(8):
            values = [0] + [random.randrange(-10**6, 10**6) for _ in range(2 * p - 1)]
            values.append(-sum(values))
            zero_tail(values, p)
            zeros += 1
        critical_four_steps(p)
        critical += 1
    print('critical zero-coordinate five-step tails: PASS', zeros)
    print('critical Y_p optimal four-step identities: PASS', critical)
    print('K4 obstruction all singleton-compatible layouts: PASS', partition_obstruction())
    print('prime critical-dimension partition entry: PASS', *prime_dimension_entry(random))
    print('natural-return invariant interval and p5 escape: PASS', cone_checks())

    solved = 0
    maximum = (0, 0, 0)
    for p in (2, 3, 5, 7, 11):
        start = 5 * p + (p - 1).bit_length() + 1
        if p in (5, 7):
            start = 5 * p
        for offset in range(4):
            n = start + offset
            raw = [random.randrange(-2, 3) for _ in range(n - 1)]
            raw.append(-sum(raw))
            assert base.legal(Counter(raw), base.protected_primes(n, p))
            length, used = solve(raw, p)
            branches.update(used)
            maximum = max(maximum, (length, p, n))
            solved += 1
    print('reserved-pool complete labelled paths: PASS', solved, 'longest', maximum)
    print('branches exercised:', dict(sorted(branches.items())))
    print('prime-arity boundary progress: PASS')


if __name__ == '__main__':
    main()
