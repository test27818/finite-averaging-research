"""Proof-directed ternary averaging for every n >= 11.

Only the Python standard library is needed. The unbounded theorem is proved
in the accompanying paper; finite checks below audit its implementation.
"""

from collections import Counter
from fractions import Fraction
from functools import cache
from itertools import combinations, combinations_with_replacement
from math import gcd
from random import Random

if not __debug__:
    raise RuntimeError('Assertions are required; do not use -O.')


@cache
def primes(n):
    result = []
    q = 2
    while q * q <= n:
        if n % q == 0:
            if q != 3:
                result.append(q)
            while n % q == 0:
                n //= q
        q += 1
    if n > 1 and n != 3:
        result.append(n)
    return tuple(result)


def admissible(counts, factors):
    return all(len({x % q for x in counts}) > 1 for q in factors)


def heavy(counts):
    return sorted(x for x, count in counts.items() if count >= 3)


def changed(counts, triple):
    used = Counter(triple)
    assert len(used) > 1 and sum(triple) % 3 == 0
    assert all(counts[x] >= count for x, count in used.items())
    result = counts - used
    result[sum(triple) // 3] += 3
    return result


def preserves(counts, triple, factors):
    result = changed(counts, triple)
    return admissible(result, factors) and len(heavy(result)) >= 2


def terminal(counts, n):
    if len(counts) <= 2:
        return True
    values = [x for x in counts if x]
    return (len(counts) == 3 and counts.get(0) == n - 6
            and len(values) == 2 and sum(values) == 0
            and all(counts[x] == 3 for x in values))


def pool_move(counts, pool, n, factors, avoid=None):
    available = pool.copy()
    for q in factors:
        residues = Counter()
        for x, count in counts.items():
            residues[x % q] += count
        majority = next((r for r, count in residues.items() if count >= n - 3), None)
        if majority is None:
            continue
        exceptions = {x: count for x, count in counts.items() if x % q != majority}
        assert 2 <= sum(exceptions.values()) <= 3
        if all(available[x] == count for x, count in exceptions.items()):
            available[next(iter(exceptions))] -= 1
            available += Counter()
    assert max(available.values()) <= 2
    assert len({x % 3 for x in available}) == 1
    needed = 4 if avoid is not None else 3
    selected = list(available.elements())[:needed]
    assert len(selected) == needed
    for triple in combinations(selected, 3):
        if avoid is None or sum(triple) != 3 * avoid:
            assert admissible(changed(counts, triple), factors)
            return triple
    raise AssertionError(('pool', counts, pool, avoid))


def initialize(counts, n, factors):
    assert all(x % 3 == 0 for x in counts)
    assert admissible(counts, factors)
    if terminal(counts, n) or len(heavy(counts)) >= 2:
        return []
    h = heavy(counts)
    if h:
        a = h[0]
        if counts[a] >= 5:
            b = next(x for x in counts if x != a)
            move = (a, a, b)
        else:
            pool = counts.copy()
            del pool[a]
            move = pool_move(counts, pool, n, factors, avoid=a)
        assert preserves(counts, move, factors)
        return [move]
    first = pool_move(counts, counts, n, factors)
    after = changed(counts, first)
    a, = heavy(after)
    pool = after.copy()
    del pool[a]
    second = pool_move(after, pool, n, factors, avoid=a)
    assert preserves(after, second, factors)
    return [first, second]


def choose(counts, n, factors):
    assert admissible(counts, factors) and len(heavy(counts)) >= 2
    assert not terminal(counts, n)
    h = heavy(counts)
    same = next(((a, b) for a, b in combinations(h, 2) if (a - b) % 3 == 0), None)
    if len(h) >= 3:
        if same:
            a, b = same
            for move in ((a, a, b), (b, b, a)):
                if preserves(counts, move, factors):
                    return [move], 'many-heavy-same-residue'
            raise AssertionError(('many-heavy', counts))
        assert len(h) == 3
        light = next((x for x in counts if x not in h), None)
        if light is not None:
            a = next(a for a in h if (a - light) % 3 == 0)
            return [(a, a, light)], 'three-heavy-light'
        return [tuple(h)], 'three-heavy-rainbow'

    a, b = h
    pool = counts.copy()
    del pool[a], pool[b]
    if (a - b) % 3 == 0:
        if counts[a] >= 4:
            return [(b, b, a)], 'same-heavy-spare'
        if counts[b] >= 4:
            return [(a, a, b)], 'same-heavy-spare'
        neighbor = next((x for x in pool if (x - a) % 3 == 0), None)
        if neighbor is not None:
            for move in ((a, a, neighbor), (b, b, neighbor)):
                if preserves(counts, move, factors):
                    return [move], 'same-heavy-neighbor'
            raise AssertionError(('same-heavy-neighbor', counts))
        groups = {}
        for x in pool:
            groups.setdefault(x % 3, []).append(x)
        if len(groups) == 1:
            return [pool_move(counts, pool, n, factors)], 'same-heavy-one-pool'
        left, right = groups.values()
        for c in left:
            for d in right:
                for move in ((a, c, d), (b, c, d)):
                    if preserves(counts, move, factors):
                        return [move], 'same-heavy-two-pools'
        raise AssertionError(('same-heavy-two-pools', counts))

    neighbors = {}
    for first, other in ((a, b), (b, a)):
        for x in pool:
            if (x - first) % 3:
                continue
            move = (first, first, x)
            if preserves(counts, move, factors):
                return [move], 'different-heavy-neighbor'
            assert counts[first] <= 4 and x == 3 * other - 2 * first
            if counts[x] >= 2:
                move = (first, x, x)
                # Safety also at q=2 follows from the affine relation above.
                assert preserves(counts, move, factors)
                return [move], 'different-heavy-double-neighbor'
            assert first not in neighbors
            neighbors[first] = x
    zpool = Counter({x: count for x, count in pool.items()
                     if x % 3 not in (a % 3, b % 3)})
    if len(neighbors) == 2:
        assert zpool
        return [(neighbors[a], neighbors[b], next(iter(zpool)))], 'two-singletons'
    if len(neighbors) == 1:
        if b in neighbors:
            a, b = b, a
        x = neighbors[a]
        if not zpool:
            return [(a, a, x)], 'one-singleton-two-value-exit'
        if counts[b] >= 4:
            return [(x, b, next(iter(zpool)))], 'one-singleton-spare'
        z = next(z for z in zpool if z != 5 * a - 4 * b)
        return [(x, b, z)], 'one-singleton-choice'
    r = sum(zpool.values())
    assert r > 0
    if r >= len(factors) + 3:
        return [pool_move(counts, zpool, n, factors)], 'large-pool'
    if counts[a] >= 4 and counts[b] >= 4:
        return [(a, b, next(iter(zpool)))], 'small-pool-spare'
    if counts[b] == 3:
        a, b = b, a
    assert counts[a] == 3 and counts[b] >= 4
    z = next((z for z in zpool if z != 2 * b - a), None)
    if z is not None:
        return [(a, b, z)], 'small-pool-choice'
    assert r <= 2 and len(zpool) == 1
    return [(a, b, next(iter(zpool)))] * r, 'small-pool-two-value-exit'


def replay_step(state, triple, allowed=None):
    unused = set(range(len(state)) if allowed is None else allowed)
    selected = []
    for x in triple:
        i = next(i for i in unused if state[i] == x)
        unused.remove(i)
        selected.append(i)
    mean, remainder = divmod(sum(state[i] for i in selected), 3)
    assert remainder == 0
    energy = sum(x * x for x in state)
    for i in selected:
        state[i] = mean
    assert sum(state) == 0 and sum(x * x for x in state) < energy
    return selected


def power_block(state, indices, word):
    size = len(indices)
    while size % 3 == 0:
        size //= 3
    assert size == 1 and sum(state[i] for i in indices) == 0
    while any(state[i] for i in indices):
        counts = Counter(state[i] for i in indices)
        move = next((t for t in combinations_with_replacement(sorted(counts), 3)
                     if t[0] != t[-1] and sum(t) % 3 == 0
                     and all(counts[x] >= k for x, k in Counter(t).items())), None)
        assert move is not None, ('power block lemma', counts)
        word.append(replay_step(state, move, indices))


def finish(state, word):
    counts = Counter(state)
    n = len(state)
    if not any(state):
        return
    assert terminal(counts, n)
    if len(counts) == 3:
        a = next(x for x in counts if x)
        for _ in range(3):
            word.append(replay_step(state, (a, -a, 0)))
        return
    a, b = sorted(counts)
    s = n
    while s % 3 == 0:
        s //= 3
    assert counts[a] % s == counts[b] % s == 0
    left = [i for i, x in enumerate(state) if x == a]
    right = [i for i, x in enumerate(state) if x == b]
    ka, kb = len(left) // s, len(right) // s
    for j in range(s):
        power_block(state, left[j * ka:(j + 1) * ka] + right[j * kb:(j + 1) * kb], word)


def solve(initial):
    n = len(initial)
    factors = primes(n)
    assert n >= 11 and n - len(factors) >= 9 and sum(initial) == 0
    assert admissible(Counter(initial), factors)
    state = [3 * x for x in initial]
    word = []
    branches = Counter()
    for triple in initialize(Counter(state), n, factors):
        word.append(replay_step(state, triple))
        assert admissible(Counter(state), factors)
    while not terminal(Counter(state), n):
        moves, branch = choose(Counter(state), n, factors)
        branches[branch] += 1
        for triple in moves:
            word.append(replay_step(state, triple))
            assert admissible(Counter(state), factors)
        assert terminal(Counter(state), n) or len(heavy(Counter(state))) >= 2
    finish(state, word)
    assert not any(state)
    original = list(map(Fraction, initial))
    for selected in word:
        assert len(set(selected)) == 3
        mean = sum(original[i] for i in selected) / 3
        assert mean.denominator in (1, 3)
        for i in selected:
            original[i] = mean
    assert not any(original)
    return len(word), branches


def local_check(state, branches):
    n = len(state)
    factors = primes(n)
    counts = Counter(state)
    if not admissible(counts, factors) or len(heavy(counts)) < 2:
        return False
    if terminal(counts, n):
        branches['terminal'] += 1
        return True
    moves, branch = choose(counts, n, factors)
    branches[branch] += 1
    for triple in moves:
        energy = sum(x * x * k for x, k in counts.items())
        counts = changed(counts, triple)
        assert sum(x * k for x, k in counts.items()) == 0
        assert sum(x * x * k for x, k in counts.items()) < energy
        assert admissible(counts, factors)
    assert len(heavy(counts)) >= 2 or terminal(counts, n), (state, branch)
    return True


def main():
    branches = Counter()
    bounded = 0
    for n in range(11, 21):
        bound = 3
        for prefix in combinations_with_replacement(range(-bound, bound + 1), n - 1):
            last = -sum(prefix)
            if prefix[-1] <= last <= bound:
                bounded += local_check(prefix + (last,), branches)
    print('general bounded closure: PASS', bounded, flush=True)
    random = Random(20260911)
    large = initializations = 0
    for n in (11, 12, 14, 15, 16, 18, 20, 25, 30, 35, 70, 71, 105, 210, 350):
        factors = primes(n)
        assert n - len(factors) >= 9
        for _ in range(200):
            m = random.randrange(3, min(n - 3, 14))
            weights = [3, 3] + [1] * (m - 2)
            for _ in range(n - sum(weights)):
                weights[random.randrange(m)] += 1
            values = [random.randrange(-10**12, 10**12) * weights[-1] for _ in range(m - 1)]
            values.append(-sum(x * f for x, f in zip(values, weights)) // weights[-1])
            state = tuple(x for x, f in zip(values, weights) for _ in range(f))
            large += local_check(state, branches)
            raw = [random.randrange(-20, 21) for _ in range(n - 1)]
            raw.append(-sum(raw))
            divisor = gcd(*raw)
            if divisor:
                raw = [x // divisor for x in raw]
            counts = Counter(3 * x for x in raw)
            if not admissible(counts, factors):
                continue
            moves = initialize(counts, n, factors)
            assert len(moves) <= 2
            for triple in moves:
                counts = changed(counts, triple)
                assert admissible(counts, factors)
            assert terminal(counts, n) or len(heavy(counts)) >= 2
            initializations += 1
    print('general large-coordinate closure: PASS', large, flush=True)
    print('general initialization: PASS', initializations, flush=True)
    solved = 0
    maximum = (0, None)
    for n in (11, 12, 14, 15, 16, 18, 20, 25, 30, 35, 70, 71, 105, 210):
        for v in (0, 2, -2):
            initial = [1] * (n - 4) + [v] * 3 + [-(n - 4) - 3 * v]
            if not admissible(Counter(initial), primes(n)):
                continue
            length, used = solve(initial)
            branches.update(used)
            solved += 1
            maximum = max(maximum, (length, n))
    for initial in ([1] * 10 + [8, -34, 5, 11], [-2] * 4 + [1] * 8,
                    [-2] * 12 + [1] * 24, [-2] * 16 + [1] * 32):
        length, used = solve(initial)
        branches.update(used)
        solved += 1
        maximum = max(maximum, (length, len(initial)))
    print('general labelled one-trit paths: PASS', solved, 'maximum', maximum, flush=True)
    print('branches:', dict(sorted(branches.items())), flush=True)
    print('direct all-n invariant: PASS', flush=True)


if __name__ == '__main__':
    main()
