"""Proof-directed prime-arity averaging, with independent labelled replay.

No search over operation words or position subsets is used. Universal
quantifiers are established in prime_arity_averaging_large_dimension.md.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from functools import cache
from math import gcd, isqrt
from random import Random

if not __debug__:
    raise RuntimeError('Assertions are required.')


@cache
def is_prime(p):
    return p >= 2 and all(p % q for q in range(2, isqrt(p) + 1))


@cache
def protected_primes(n, p):
    remaining = n
    result = []
    factor = 2
    while factor * factor <= remaining:
        if remaining % factor == 0:
            if factor != p:
                result.append(factor)
            while remaining % factor == 0:
                remaining //= factor
        factor += 1
    if remaining > 1 and remaining != p:
        result.append(remaining)
    return tuple(result)


def legal(counts, factors):
    return all(len({x % q for x in counts}) > 1 for q in factors)


def heavy(counts, p):
    return [x for x, f in counts.items() if f >= p]


def conditions(n, p):
    d = len(protected_primes(n, p))
    return n >= p * d + 3 * p * p - 2 and n > p * (p - 1) ** 2


def change(counts, values, p):
    assert len(values) == p and len(set(values)) > 1
    selected = Counter(values)
    assert all(counts[x] >= f for x, f in selected.items())
    total = sum(values)
    mean, remainder = divmod(total, p)
    assert remainder == 0
    after = counts - selected
    after[mean] += p
    assert sum((x - mean) ** 2 for x in values) >= 2
    return after


def pool_move(counts, pool, n, p, factors, avoid=None):
    available = pool.copy()
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
    assert len({x % p for x in available}) == 1
    needed = p if avoid is None else p + 1
    chosen = []
    for x, f in available.items():
        chosen.extend([x] * min(f, needed - len(chosen)))
        if len(chosen) == needed:
            break
    assert len(chosen) == needed
    if avoid is not None:
        total = sum(chosen)
        omit = next(i for i, x in enumerate(chosen) if total - x != p * avoid)
        chosen.pop(omit)
    return tuple(chosen)


def initialize(counts, n, p, factors):
    assert legal(counts, factors) and all(x % p == 0 for x in counts)
    h = heavy(counts, p)
    if len(h) >= 2:
        return []
    if h:
        a = h[0]
        if counts[a] >= 2 * p - 1:
            b = next(x for x in counts if x != a)
            return [(a,) * (p - 1) + (b,)]
        pool = counts.copy()
        del pool[a]
        return [pool_move(counts, pool, n, p, factors, avoid=a)]
    first = pool_move(counts, counts, n, p, factors)
    after = change(counts, first, p)
    a, = heavy(after, p)
    assert p <= after[a] <= 2 * p - 1
    pool = after.copy()
    del pool[a]
    second = pool_move(after, pool, n, p, factors, avoid=a)
    return [first, second]


def controller(a, b, x, p):
    delta_inverse = pow((a - b) % p, -1, p)
    i = ((b - x) * delta_inverse) % p
    return (a,) * i + (b,) * (p - 1 - i) + (x,)


def choose(counts, n, p, factors):
    h = heavy(counts, p)
    assert len(h) >= 2 and legal(counts, factors)
    if len(h) >= p + 2:
        seen = {}
        for a in h:
            if a % p in seen:
                b = seen[a % p]
                return (a,) * (p - 1) + (b,), 'many-heavy', None
            seen[a % p] = a
        raise AssertionError('pigeonhole principle')
    light = Counter({x: f for x, f in counts.items() if f < p})
    if sum(light.values()) >= p * (len(factors) + p):
        residues = Counter()
        for x, f in light.items():
            residues[x % p] += f
        residue = next(r for r, f in residues.items() if f >= len(factors) + p)
        pool = Counter({x: f for x, f in light.items() if x % p == residue})
        return pool_move(counts, pool, n, p, factors), 'large-light-pool', None
    b = max(h, key=counts.get)
    assert counts[b] >= 2 * p - 1
    a = next(x for x in h if x != b)
    if (a - b) % p == 0:
        return (b,) * (p - 1) + (a,), 'same-residue-background', None
    others = [x for x in counts if x not in (a, b)]
    assert others, 'two-value arithmetic exclusion'
    for x in others:
        move = controller(a, b, x, p)
        if sum(move) != p * b:
            return move, 'single-value-controller', None
    delta = a - b
    for x in others:
        assert (b - x) % delta == 0
        j = (b - x) // delta
        assert 1 <= j <= p - 1
    if counts[a] >= 2 * p - 1:
        return controller(a, b, others[0], p), 'large-second-heavy', None
    for x in others:
        if counts[x] >= 2 * p - 1:
            return controller(x, b, a, p), 'large-progression-heavy', None
    assert counts[a] <= 2 * p - 2
    assert all(counts[x] <= 2 * p - 2 for x in others)
    defect = counts[a] - sum(((b - x) // delta) * counts[x] for x in others)
    assert gcd(delta, n) == 1
    assert n * b + delta * defect == 0
    assert abs(defect) <= p * (p - 1) ** 2 < n
    assert defect == b == 0
    return None, 'explicit-progression-terminal', delta


class LabelledReplay:
    def __init__(self, initial, p):
        self.p = p
        self.state = [p * x for x in initial]
        self.locations = defaultdict(set)
        for i, x in enumerate(self.state):
            self.locations[x].add(i)
        self.energy = sum(x * x for x in self.state)
        self.word = []

    def counts(self):
        return Counter({x: len(indices) for x, indices in self.locations.items() if indices})

    def step(self, values):
        p = self.p
        assert len(values) == p
        indices = []
        for x in values:
            assert self.locations[x]
            indices.append(self.locations[x].pop())
        assert len(set(indices)) == p
        mean, remainder = divmod(sum(self.state[i] for i in indices), p)
        assert remainder == 0
        decrease = sum(self.state[i] ** 2 for i in indices) - p * mean * mean
        assert decrease >= 2
        self.energy -= decrease
        assert self.energy >= 0
        for i in indices:
            self.state[i] = mean
            self.locations[mean].add(i)
        for x in set(values):
            if not self.locations[x]:
                del self.locations[x]
        self.word.append(indices)


def solve(initial, p):
    n = len(initial)
    assert is_prime(p) and conditions(n, p) and sum(initial) == 0
    if not any(initial):
        return 0, Counter()
    factors = protected_primes(n, p)
    assert legal(Counter(initial), factors)
    replay = LabelledReplay(initial, p)
    branches = Counter()
    for move in initialize(replay.counts(), n, p, factors):
        replay.step(move)
        assert legal(replay.counts(), factors)
    while any(replay.state):
        counts = replay.counts()
        move, branch, delta = choose(counts, n, p, factors)
        branches[branch] += 1
        if move is None:
            for x, f in counts.items():
                if x in (0, delta):
                    continue
                j = -x // delta
                assert x == -j * delta and 1 <= j <= p - 1
                for _ in range(f):
                    replay.step((x,) + (delta,) * j + (0,) * (p - j - 1))
            break
        expected = change(counts, move, p)
        assert legal(expected, factors) and len(heavy(expected, p)) >= 2
        replay.step(move)
        assert replay.counts() == expected
    assert not any(replay.state) and replay.energy == 0
    assert 2 * len(replay.word) <= p * p * sum(x * x for x in initial)
    original = list(map(Fraction, initial))
    for indices in replay.word:
        mean = sum(original[i] for i in indices) / p
        assert mean.denominator in (1, p)
        for i in indices:
            original[i] = mean
    assert not any(original)
    return len(replay.word), branches


def local_audit(counts, n, p, branches):
    factors = protected_primes(n, p)
    assert sum(counts.values()) == n and sum(x * f for x, f in counts.items()) == 0
    if not legal(counts, factors) or len(heavy(counts, p)) < 2:
        return False
    move, branch, delta = choose(counts, n, p, factors)
    branches[branch] += 1
    if move is None:
        assert counts[0] >= 2 * p - 1 and delta != 0
        assert counts[delta] == sum((-x // delta) * f for x, f in counts.items() if x not in (0, delta))
    else:
        after = change(counts, move, p)
        assert legal(after, factors) and len(heavy(after, p)) >= 2
        assert sum(x * f for x, f in after.items()) == 0
    return True


def main():
    random = Random(2026091201)
    branches = Counter()
    capacity = local = initializations = 0
    for p in (2, 3, 5, 7, 11, 17, 31):
        for offset in range(100):
            n = 2 * p ** 3 + offset
            assert conditions(n, p)
            capacity += 1
        for _ in range(250):
            n = 2 * p ** 3 + random.randrange(200)
            m = random.randrange(3, min(n - 2 * p + 2, 2 * p + 15))
            weights = [p, p] + [1] * (m - 2)
            remaining = n - sum(weights)
            # Assign multiplicities directly; never materialize n positions.
            for j in range(m - 1):
                add = random.randrange(remaining + 1)
                weights[j] += add
                remaining -= add
            weights[-1] += remaining
            values = [random.randrange(-10**10, 10**10) * weights[-1] for _ in range(m - 1)]
            values.append(-sum(x * f for x, f in zip(values, weights)) // weights[-1])
            counts = Counter()
            for x, f in zip(values, weights):
                counts[x] += f
            local += local_audit(counts, n, p, branches)

        for style in ('one-heavy', 'one-heavy-minimal', 'no-heavy', 'already-heavy'):
            n = 2 * p ** 3 + 1
            if style == 'one-heavy':
                values = [0] * (2 * p) + list(range(1, n - 2 * p))
            elif style == 'one-heavy-minimal':
                values = [0] * p + list(range(1, n - p))
            elif style == 'no-heavy':
                values = list(range(1, n))
            else:
                values = [1] * p + [2] * p + list(range(3, n - 2 * p + 2))
            values.append(-sum(values))
            assert len(values) == n
            counts = Counter(p * x for x in values)
            factors = protected_primes(n, p)
            assert legal(counts, factors)
            moves = initialize(counts, n, p, factors)
            assert len(moves) <= 2
            for move in moves:
                counts = change(counts, move, p)
                assert legal(counts, factors)
            assert len(heavy(counts, p)) >= 2
            initializations += 1
    print('prime-arity threshold instances: PASS', capacity, flush=True)
    print('compressed large-integer closure checks: PASS', local, flush=True)
    print('all initialization branches: PASS', initializations, flush=True)

    # Explicit stress patterns for the light pool and progression exits.
    for p in (2, 3, 5, 7, 11):
        n = 2 * p ** 3 + 1
        light = list(range(2, n - 2 * p + 1))
        counts = Counter({0: p, 1: p})
        counts.update(light)
        counts[-sum(x * f for x, f in counts.items())] += 1
        assert local_audit(counts, n, p, branches)
        for j in (1, p - 1):
            # p positives, with p/j an integer when j=1; the other pattern
            # uses p-1 and1 as the two negative coefficients.
            negatives = [-1] * p if j == 1 else [-(p - 1), -1]
            counts = Counter({0: n - p - len(negatives), 1: p})
            counts.update(negatives)
            assert local_audit(counts, n, p, branches)
        # Every third value collapses to the background, but another heavy
        # value supplies the reserve needed by the final multiplicity branch.
        counts = Counter({2: 4 * p, 1: n - 8 * p, 0: 4 * p})
        # Translate to zero mean when its mean is integral.
        assert sum(x * f for x, f in counts.items()) == n
        counts = Counter({x - 1: f for x, f in counts.items() if f})
        assert local_audit(counts, n, p, branches)

    solved = 0
    longest = (0, 0, 0)
    for p in (2, 3, 5, 7):
        n = 2 * p ** 3
        for _ in range(4):
            values = [random.randrange(-2, 3) for _ in range(n - 1)]
            values.append(-sum(values))
            if not legal(Counter(values), protected_primes(n, p)):
                continue
            length, used = solve(values, p)
            branches.update(used)
            longest = max(longest, (length, p, n))
            solved += 1
        values = [1] * p + [-(p - 1), -1] + [0] * (n - p - 2)
        length, used = solve(values, p)
        branches.update(used)
        longest = max(longest, (length, p, n))
        solved += 1
    print('labelled end-to-end prime-arity paths: PASS', solved, 'longest', longest, flush=True)
    print('proof branches:', dict(sorted(branches.items())), flush=True)
    print('prime-arity large-dimension theorem checks: PASS', flush=True)


if __name__ == '__main__':
    main()
