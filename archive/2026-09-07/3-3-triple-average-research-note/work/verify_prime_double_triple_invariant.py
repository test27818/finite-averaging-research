"""Constructive prime theorem checks; no search over averaging words.

The selector implements the cases in the proof. A separate labelled replay
checks physical positions, exact integer precision and energy at every step.
Unbounded quantifiers are proved in the document, not by this finite suite.
"""

from collections import Counter
from itertools import combinations, combinations_with_replacement
from math import isqrt
from random import Random

if not __debug__:
    raise RuntimeError('Verification requires assertions; do not run with -O.')


def heavy(counts):
    return sorted(x for x, count in counts.items() if count >= 3)


def incongruent(counts, p):
    return len({x % p for x, count in counts.items() if count}) > 1


def changed(counts, triple):
    used = Counter(triple)
    assert all(counts[x] >= count for x, count in used.items())
    total = sum(triple)
    assert total % 3 == 0
    assert len(used) > 1
    after = counts - used
    after[total // 3] += 3
    return after


def preserves(counts, triple, p):
    after = changed(counts, triple)
    return incongruent(after, p) and len(heavy(after)) >= 2


def terminal(counts, p):
    if len(counts) != 3 or counts.get(0) != p - 6:
        return False
    others = [x for x in counts if x]
    return (len(others) == 2 and sum(others) == 0
            and all(counts[x] == 3 for x in others))


def pool_move(counts, pool, p, avoid=None):
    residues = Counter()
    for x, count in counts.items():
        residues[x % p] += count
    majority = next((r for r, count in residues.items() if count >= p - 3), None)
    available = pool.copy()
    if majority is not None:
        exceptions = {x: count for x, count in counts.items() if x % p != majority}
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
        if avoid is not None and sum(triple) == 3 * avoid:
            continue
        after = changed(counts, triple)
        assert incongruent(after, p)
        return triple
    raise AssertionError(('pool lemma', counts, pool, avoid))


def initialize(counts, p):
    assert incongruent(counts, p)
    assert all(x % 3 == 0 for x in counts)
    h = heavy(counts)
    if len(h) >= 2:
        return []
    if h:
        a = h[0]
        if counts[a] >= 5:
            b = next(x for x in counts if x != a)
            triple = (a, a, b)
        else:
            pool = counts.copy()
            del pool[a]
            triple = pool_move(counts, pool, p, avoid=a)
        assert preserves(counts, triple, p)
        return [triple]
    first = pool_move(counts, counts, p)
    after = changed(counts, first)
    h = heavy(after)
    assert len(h) == 1 and 3 <= after[h[0]] <= 5
    a = h[0]
    pool = after.copy()
    del pool[a]
    assert sum(pool.values()) >= 6
    second = pool_move(after, pool, p, avoid=a)
    assert preserves(after, second, p)
    return [first, second]


def choose(counts, p):
    h = heavy(counts)
    assert len(h) >= 2 and incongruent(counts, p)
    assert sum(x * count for x, count in counts.items()) == 0
    if terminal(counts, p):
        return None, 'terminal'
    same = next(((a, b) for a, b in combinations(h, 2) if (a - b) % 3 == 0), None)
    if len(h) >= 3:
        if same:
            a, b = same
            for triple in ((a, a, b), (b, b, a)):
                if preserves(counts, triple, p):
                    return triple, 'many-heavy-same-residue'
            raise AssertionError(('many heavy same residue', counts))
        assert len(h) == 3
        light = next((x for x in counts if x not in h), None)
        if light is not None:
            a = next(a for a in h if (a - light) % 3 == 0)
            return (a, a, light), 'three-heavy-light'
        assert preserves(counts, tuple(h), p)
        return tuple(h), 'three-heavy-rainbow'

    a, b = h
    pool = counts.copy()
    del pool[a], pool[b]
    if (a - b) % 3 == 0:
        if counts[a] >= 4:
            return (b, b, a), 'same-heavy-spare-copy'
        if counts[b] >= 4:
            return (a, a, b), 'same-heavy-spare-copy'
        assert counts[a] == counts[b] == 3
        neighbor = next((x for x in pool if (x - a) % 3 == 0), None)
        if neighbor is not None:
            for triple in ((a, a, neighbor), (b, b, neighbor)):
                if preserves(counts, triple, p):
                    return triple, 'same-heavy-neighbor'
            raise AssertionError(('same heavy neighbor', counts))
        groups = {}
        for x in pool:
            groups.setdefault(x % 3, []).append(x)
        if len(groups) == 1:
            return pool_move(counts, pool, p), 'same-heavy-one-pool'
        left, right = groups.values()
        # At most one physical cross-pair is blocked. Two distinct value
        # choices in each residue class suffice; duplicates cannot add danger.
        for c in left[:2]:
            for d in right[:2]:
                for triple in ((a, c, d), (b, c, d)):
                    if preserves(counts, triple, p):
                        return triple, 'same-heavy-two-pools'
        raise AssertionError(('same heavy two pools', counts))

    neighbors = {}
    for first, other in ((a, b), (b, a)):
        for x in pool:
            if (x - first) % 3:
                continue
            triple = (first, first, x)
            if preserves(counts, triple, p):
                return triple, 'different-heavy-neighbor'
            if counts[x] >= 2:
                triple = (first, x, x)
                assert preserves(counts, triple, p)
                return triple, 'different-heavy-double-neighbor'
            assert counts[first] <= 4 and x == 3 * other - 2 * first
            assert first not in neighbors
            neighbors[first] = x
    zpool = Counter({x: count for x, count in pool.items()
                     if x % 3 not in (a % 3, b % 3)})
    if len(neighbors) == 2:
        assert zpool
        return (neighbors[a], neighbors[b], next(iter(zpool))), 'different-heavy-two-singletons'
    if len(neighbors) == 1:
        if b in neighbors:
            a, b = b, a
        x = neighbors[a]
        assert zpool
        if counts[b] >= 4:
            return (x, b, next(iter(zpool))), 'different-heavy-one-singleton-spare'
        assert counts[b] == 3 and sum(zpool.values()) >= 3
        z = next(z for z in zpool if z != 5 * a - 4 * b)
        return (x, b, z), 'different-heavy-one-singleton-choice'
    r = sum(zpool.values())
    if r >= 4:
        return pool_move(counts, zpool, p), 'different-heavy-large-pool'
    assert 1 <= r <= 3
    if counts[a] >= 4 and counts[b] >= 4:
        return (a, b, next(iter(zpool))), 'different-heavy-small-pool-spare'
    if counts[b] == 3:
        a, b = b, a
    assert counts[a] == 3 and counts[b] >= 5
    z = next(z for z in zpool if z != 2 * b - a)
    return (a, b, z), 'different-heavy-small-pool-choice'


def replay_step(state, triple):
    """Use actual labelled positions; do not normalize or rescale the state."""
    unused = set(range(len(state)))
    positions = []
    for value in triple:
        i = next(i for i in unused if state[i] == value)
        unused.remove(i)
        positions.append(i)
    total = sum(state[i] for i in positions)
    assert total % 3 == 0
    mean = total // 3
    before_energy = sum(x * x for x in state)
    result = state.copy()
    for i in positions:
        result[i] = mean
    assert sum(result) == 0
    assert sum(x * x for x in result) < before_energy
    return result, positions


def solve(state):
    p = len(state)
    assert p >= 11 and all(p % k for k in range(2, isqrt(p) + 1))
    assert sum(state) == 0 and incongruent(Counter(state), p)
    current = [3 * x for x in state]
    word = []
    branches = Counter()
    for triple in initialize(Counter(current), p):
        current, positions = replay_step(current, triple)
        word.append(positions)
    while not terminal(Counter(current), p):
        counts = Counter(current)
        triple, branch = choose(counts, p)
        assert triple is not None and preserves(counts, triple, p)
        current, positions = replay_step(current, triple)
        word.append(positions)
        branches[branch] += 1
    a = next(x for x in current if x)
    for _ in range(3):
        current, positions = replay_step(current, (a, -a, 0))
        word.append(positions)
    assert not any(current)
    # Repeat from the unscaled input with rational arithmetic independently.
    from fractions import Fraction
    original = list(map(Fraction, state))
    for positions in word:
        mean = sum(original[i] for i in positions) / 3
        assert mean.denominator in (1, 3)
        for i in positions:
            original[i] = mean
    assert not any(original)
    return len(word), branches


def local_check(state, branches):
    p = len(state)
    counts = Counter(state)
    if not incongruent(counts, p) or len(heavy(counts)) < 2:
        return False
    triple, branch = choose(counts, p)
    branches[branch] += 1
    if triple is None:
        assert terminal(counts, p)
    else:
        assert preserves(counts, triple, p), (state, branch, triple)
        after, _ = replay_step(list(state), triple)
        assert Counter(after) == changed(counts, triple)
    return True


def main():
    branches = Counter()
    exhaustive = 0
    for p, bound in ((11, 5), (13, 4), (17, 3)):
        for prefix in combinations_with_replacement(range(-bound, bound + 1), p - 1):
            last = -sum(prefix)
            if prefix[-1] <= last <= bound:
                exhaustive += local_check(prefix + (last,), branches)
    print('bounded integer closure checks: PASS', exhaustive, flush=True)

    random = Random(180608875)
    large = 0
    initializations = 0
    for p in (11, 13, 17, 23, 71, 431):
        for _ in range(600):
            m = random.randrange(3, min(p - 3, 13))
            weights = [3, 3] + [1] * (m - 2)
            for _ in range(p - sum(weights)):
                weights[random.randrange(m)] += 1
            values = [random.randrange(-10**12, 10**12) * weights[-1] for _ in range(m - 1)]
            values.append(-sum(x * f for x, f in zip(values, weights)) // weights[-1])
            state = tuple(x for x, f in zip(values, weights) for _ in range(f))
            large += local_check(state, branches)
            raw = [random.randrange(-20, 21) for _ in range(p - 1)]
            raw.append(-sum(raw))
            counts = Counter(3 * x for x in raw)
            if not incongruent(counts, p):
                continue
            moves = initialize(counts, p)
            assert len(moves) <= 2
            for triple in moves:
                counts = changed(counts, triple)
                assert incongruent(counts, p)
            assert len(heavy(counts)) >= 2
            initializations += 1
    print('large-coordinate closure checks: PASS', large, flush=True)
    print('two-step initialization checks: PASS', initializations, flush=True)

    solved = 0
    longest = (0, None)
    for p in (11, 13, 17, 23, 71):
        samples = [[1] * (p - 4) + [v] * 3 + [-(p - 4) - 3 * v]
                   for v in (0, 2, -1)]
        for _ in range(8):
            sample = [random.randrange(-3, 4) for _ in range(p - 1)]
            sample.append(-sum(sample))
            samples.append(sample)
        for sample in samples:
            if not incongruent(Counter(sample), p):
                continue
            length, used = solve(sample)
            branches.update(used)
            solved += 1
            if length > longest[0]:
                longest = length, p
    print('labelled end-to-end one-trit replays: PASS', solved, 'longest', longest, flush=True)
    print('proof branches exercised:', dict(sorted(branches.items())), flush=True)
    print('prime double-triple invariant: PASS', flush=True)


if __name__ == '__main__':
    main()
