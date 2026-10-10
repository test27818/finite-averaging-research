"""Direct all-dimension double-triple construction and exact finite checks.

The unbounded closure proof is in the accompanying document. This program
chooses one step from those cases; it never searches averaging words.
"""

from collections import Counter
from functools import cache
from itertools import combinations, combinations_with_replacement, product
from random import Random

from verify_prime_double_triple_invariant import (
    changed, heavy, replay_step, terminal,
)

if not __debug__:
    raise RuntimeError("Verification requires assertions; do not run with -O.")


@cache
def protected_primes(n):
    remaining = n
    result = []
    factor = 2
    while factor * factor <= remaining:
        if remaining % factor == 0:
            if factor != 3:
                result.append(factor)
            while remaining % factor == 0:
                remaining //= factor
        factor += 1
    if remaining > 1 and remaining != 3:
        result.append(remaining)
    return tuple(result)


def incongruent(counts, n):
    return all(len({x % q for x in counts}) > 1 for q in protected_primes(n))


def preserves(counts, triple, n):
    after = changed(counts, triple)
    return incongruent(after, n) and len(heavy(after)) >= 2


def pool_move(counts, pool, n, avoid=None):
    available = pool.copy()
    removed = 0
    for q in protected_primes(n):
        residues = Counter()
        for x, count in counts.items():
            residues[x % q] += count
        majority = next((r for r, f in residues.items() if f >= n - 3), None)
        if majority is None:
            continue
        exceptions = {x: f for x, f in counts.items() if x % q != majority}
        assert 2 <= sum(exceptions.values()) <= 3
        if all(available[x] == f for x, f in exceptions.items()):
            available[next(iter(exceptions))] -= 1
            available += Counter()
            removed += 1
    assert removed <= len(protected_primes(n))
    assert max(available.values()) <= 2
    assert len({x % 3 for x in available}) == 1
    needed = 4 if avoid is not None else 3
    selected = list(available.elements())[:needed]
    assert len(selected) == needed
    for triple in combinations(selected, 3):
        if avoid is not None and sum(triple) == 3 * avoid:
            continue
        assert incongruent(changed(counts, triple), n)
        return triple
    raise AssertionError(("protected pool", counts, pool, avoid))


def initialize(counts, n):
    assert n >= 11 and sum(counts.values()) == n
    assert all(x % 3 == 0 for x in counts)
    assert incongruent(counts, n)
    h = heavy(counts)
    if len(h) >= 2:
        return []
    if h:
        a = h[0]
        if counts[a] >= 5:
            b = next(x for x in counts if x != a)
            move = (a, a, b)
        else:
            pool = counts.copy()
            del pool[a]
            move = pool_move(counts, pool, n, avoid=a)
        assert preserves(counts, move, n)
        return [move]
    first = pool_move(counts, counts, n)
    after = changed(counts, first)
    h = heavy(after)
    assert len(h) == 1 and 3 <= after[h[0]] <= 5
    pool = after.copy()
    del pool[h[0]]
    second = pool_move(after, pool, n, avoid=h[0])
    assert preserves(after, second, n)
    return [first, second]


def choose(counts, n):
    assert n >= 11 and sum(counts.values()) == n
    assert sum(x * f for x, f in counts.items()) == 0
    assert incongruent(counts, n)
    h = heavy(counts)
    assert len(h) >= 2
    if terminal(counts, n):
        return None, "terminal"
    same = next(((a, b) for a, b in combinations(h, 2) if (a - b) % 3 == 0), None)
    if len(h) >= 3:
        if same:
            a, b = same
            for move in ((a, a, b), (b, b, a)):
                if preserves(counts, move, n):
                    return move, "many-heavy-same-residue"
            raise AssertionError(("many heavy", counts))
        assert len(h) == 3
        light = next((x for x in counts if x not in h), None)
        if light is not None:
            a = next(a for a in h if (a - light) % 3 == 0)
            return (a, a, light), "three-heavy-light"
        return tuple(h), "three-heavy-rainbow"

    a, b = h
    pool = counts.copy()
    del pool[a], pool[b]
    if (a - b) % 3 == 0:
        if counts[a] >= 4:
            return (b, b, a), "same-heavy-spare"
        if counts[b] >= 4:
            return (a, a, b), "same-heavy-spare"
        assert counts[a] == counts[b] == 3
        x = next((x for x in pool if (x - a) % 3 == 0), None)
        if x is not None:
            for move in ((a, a, x), (b, b, x)):
                if preserves(counts, move, n):
                    return move, "same-heavy-neighbor"
            raise AssertionError(("same heavy neighbor", counts))
        groups = {}
        for x in pool:
            groups.setdefault(x % 3, []).append(x)
        if len(groups) == 1:
            return pool_move(counts, pool, n), "same-heavy-protected-pool"
        left, right = groups.values()
        for c, d in product(left, right):
            for move in ((a, c, d), (b, c, d)):
                if preserves(counts, move, n):
                    return move, "same-heavy-cross-pools"
        raise AssertionError(("same heavy cross pools", counts))

    neighbors = {}
    for first, other in ((a, b), (b, a)):
        for x in pool:
            if (x - first) % 3:
                continue
            move = (first, first, x)
            if preserves(counts, move, n):
                return move, "different-heavy-neighbor"
            assert counts[first] <= 4 and x == 3 * other - 2 * first
            if counts[x] >= 2:
                # The untouched other heavy value protects characteristic 2.
                move = (first, x, x)
                assert preserves(counts, move, n)
                return move, "different-heavy-affine-double"
            assert first not in neighbors
            neighbors[first] = x
    zpool = Counter({x: f for x, f in pool.items()
                     if x % 3 not in (a % 3, b % 3)})
    if len(neighbors) == 2:
        assert zpool
        return (neighbors[a], neighbors[b], next(iter(zpool))), "two-affine-singletons"
    if len(neighbors) == 1:
        if b in neighbors:
            a, b = b, a
        assert zpool
        x = neighbors[a]
        if counts[b] >= 4:
            return (x, b, next(iter(zpool))), "one-affine-singleton-spare"
        assert counts[b] == 3 and sum(zpool.values()) >= 3
        z = next(z for z in zpool if z != 5 * a - 4 * b)
        return (x, b, z), "one-affine-singleton-choice"

    assert zpool
    if counts[a] == counts[b] == 3:
        assert sum(zpool.values()) >= len(protected_primes(n)) + 4
        return pool_move(counts, zpool, n), "two-minimal-heavy-protected-pool"
    if counts[a] >= 4 and counts[b] >= 4:
        return (a, b, next(iter(zpool))), "different-heavy-spare"
    if counts[b] == 3:
        a, b = b, a
    assert counts[a] == 3 and counts[b] >= 4
    z = next(z for z in zpool if z != 2 * b - a)
    return (a, b, z), "different-heavy-third-residue-choice"


def local_check(state, branches):
    n = len(state)
    counts = Counter(state)
    if not incongruent(counts, n) or len(heavy(counts)) < 2:
        return False
    move, branch = choose(counts, n)
    branches[branch] += 1
    if move is None:
        assert terminal(counts, n)
    else:
        assert preserves(counts, move, n), (state, branch, move)
        after, _ = replay_step(list(state), move)
        assert Counter(after) == changed(counts, move)
    return True


def solve(state):
    from fractions import Fraction

    n = len(state)
    assert n >= 11 and sum(state) == 0
    if not any(state):
        return 0, Counter()
    assert incongruent(Counter(state), n)
    current = [3 * x for x in state]
    word = []
    branches = Counter()
    for move in initialize(Counter(current), n):
        current, positions = replay_step(current, move)
        word.append(positions)
    while not terminal(Counter(current), n):
        move, branch = choose(Counter(current), n)
        assert preserves(Counter(current), move, n)
        current, positions = replay_step(current, move)
        word.append(positions)
        branches[branch] += 1
    a = next(x for x in current if x)
    for _ in range(3):
        current, positions = replay_step(current, (a, -a, 0))
        word.append(positions)
    assert not any(current)
    assert len(word) <= 9 * sum(x * x for x in state) + 3

    # Independently replay on unscaled labelled rational coordinates.
    original = list(map(Fraction, state))
    for positions in word:
        assert len(positions) == len(set(positions)) == 3
        assert all(0 <= i < n for i in positions)
        mean = sum(original[i] for i in positions) / 3
        assert mean.denominator in (1, 3)
        for i in positions:
            original[i] = mean
    assert not any(original)
    return len(word), branches


def main():
    branches = Counter()
    capacity_cases = 0
    for n in range(11, 10001):
        assert n >= len(protected_primes(n)) + 10
        capacity_cases += 1
    print("uniform protected-pool capacity checks: PASS", capacity_cases, flush=True)

    exhaustive = 0
    for n, bound in ((11, 4), (12, 4), (13, 3), (14, 3), (15, 3),
                     (16, 3), (18, 3), (20, 3)):
        for prefix in combinations_with_replacement(range(-bound, bound + 1), n - 1):
            last = -sum(prefix)
            if prefix[-1] <= last <= bound:
                exhaustive += local_check(prefix + (last,), branches)
    print("composite-inclusive bounded closure checks: PASS", exhaustive, flush=True)

    rng = Random(3112026)
    large = initializations = 0
    dimensions = (11, 12, 14, 15, 16, 18, 20, 21, 25, 27, 30, 35, 42, 70, 105, 210)
    for n in dimensions:
        for _ in range(300):
            weights = [3, 3] + [1] * rng.randrange(1, min(n - 6, 10) + 1)
            for _ in range(n - sum(weights)):
                weights[rng.randrange(len(weights) - 1)] += 1
            values = [rng.randrange(-10**9, 10**9) for _ in weights[:-1]]
            values.append(-sum(x * f for x, f in zip(values, weights)))
            state = tuple(x for x, f in zip(values, weights) for _ in range(f))
            assert len(state) == n and sum(state) == 0
            large += local_check(state, branches)
            raw = [rng.randrange(-8, 9) for _ in range(n - 1)]
            raw.append(-sum(raw))
            counts = Counter(3 * x for x in raw)
            if not incongruent(counts, n):
                continue
            moves = initialize(counts, n)
            assert len(moves) <= 2
            for move in moves:
                counts = changed(counts, move)
                assert incongruent(counts, n)
            assert len(heavy(counts)) >= 2
            initializations += 1
    print("multi-prime large-coordinate closure checks: PASS", large, flush=True)
    print("multi-prime two-step initialization checks: PASS", initializations, flush=True)

    # The unrestricted (a,x,x) rule really fails at 2; the affine case used
    # above is stronger and retains two witnesses.
    unsafe = Counter([3] * 3 + [0] * 2 + [1] * 6 + [-15])
    assert incongruent(unsafe, 12)
    assert not incongruent(changed(unsafe, (3, 0, 0)), 12)
    parity_checks = 0
    for a in range(-5, 6):
        for b in range(-5, 6):
            if a == b or (a - b) % 3 == 0:
                continue
            x = 3 * b - 2 * a
            state = [a] * 3 + [b] * 3 + [x] * 2
            state += [0, 0, 0, -sum(state)]
            counts = Counter(state)
            if incongruent(counts, 12):
                assert incongruent(changed(counts, (a, x, x)), 12)
                parity_checks += 1
    print("characteristic-two obstruction and affine repair: PASS", parity_checks, flush=True)

    solved = 0
    longest = (0, None)
    for n in dimensions:
        for _ in range(5):
            state = [rng.randrange(-3, 4) for _ in range(n - 1)]
            state.append(-sum(state))
            if not any(state) or not incongruent(Counter(state), n):
                continue
            length, used = solve(state)
            branches.update(used)
            solved += 1
            if length > longest[0]:
                longest = length, n
    print("all-dimension labelled one-trit replays: PASS", solved, "longest", longest, flush=True)
    print("proof branches exercised:", dict(sorted(branches.items())), flush=True)
    print("all-dimension double-triple invariant: PASS", flush=True)


if __name__ == "__main__":
    main()
