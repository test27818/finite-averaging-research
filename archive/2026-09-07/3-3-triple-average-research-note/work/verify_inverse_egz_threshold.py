"""Inverse EGZ repairs a one-position deficit in the uniform threshold.

Residue bins and largest-bin matching build p-2 unequal pairs. A single residue
bitset per pair recovers a p-subset; no averaging-word or subset-tree search.
"""

from collections import Counter, defaultdict
from heapq import heappop, heappush
from itertools import combinations_with_replacement
from math import gcd
from random import Random

import verify_prime_arity_four_p_threshold as old
import verify_prime_arity_middle_band as middle
import verify_three_heavy_two_spares as triple

base, linear = old.base, old.linear

if not __debug__:
    raise RuntimeError('Assertions are required.')


def inverse_egz(values, p):
    assert p >= 5 and len(values) == 2*p-2
    bins = defaultdict(list)
    for value in values:
        bins[value % p].append(value)
    a = max(bins, key=lambda r: len(bins[r]))
    if len(bins[a]) >= p:
        return tuple(bins[a][:p])
    if len(bins) == 2:
        assert sorted(map(len, bins.values())) == [p-1, p-1]
        return None
    assert len(bins) >= 3 and len(bins[a]) >= 2
    others = [r for r in bins if r != a]
    b = others[0]
    c = next((r for r in others[1:] if (r-a) % p != (a-b) % p), None)
    pairs = []

    def pair(u, v):
        assert u != v and bins[u] and bins[v]
        pairs.append((bins[u].pop(), bins[v].pop()))

    if c is not None:
        pair(a, b)
        pair(a, c)
    else:
        assert len(others) == 2
        b, c = others
        if len(bins[b]) < 2:
            b, c = c, b
        assert len(bins[b]) >= 2
        pair(a, b)
        pair(b, c)
    diffs = [(x-y) % p for x, y in pairs]
    assert diffs[0] not in (diffs[1], -diffs[1] % p)
    heap = [(-len(group), r) for r, group in bins.items() if group]
    from heapq import heapify
    heapify(heap)
    for _ in range(p-4):
        ca, a = heappop(heap)
        cb, b = heappop(heap)
        pair(a, b)
        if ca < -1:
            heappush(heap, (ca+1, a))
        if cb < -1:
            heappush(heap, (cb+1, b))
    leftovers = [x for group in bins.values() for x in group]
    assert len(leftovers) == 2 and len(pairs) == p-2
    rows = [1]
    for x, y in pairs:
        rows.append(linear.rotate_bits(rows[-1], x, p) |
                    linear.rotate_bits(rows[-1], y, p))
    assert rows[-1] == (1 << p)-1
    residue = -sum(leftovers) % p
    chosen = leftovers[:]
    for i in range(len(pairs)-1, -1, -1):
        x, y = pairs[i]
        if rows[i] & (1 << ((residue-x) % p)):
            chosen.append(x)
            residue = (residue-x) % p
        else:
            assert rows[i] & (1 << ((residue-y) % p))
            chosen.append(y)
            residue = (residue-y) % p
    assert residue == 0 and len(chosen) == p and sum(chosen) % p == 0
    return tuple(chosen)


def combined_reserve(counts, a, b, p):
    alpha, beta = counts[a]-p, counts[b]-p
    assert alpha+beta >= p-2
    negative, positive = Counter(), Counter()
    delta = a-b
    for x in counts:
        if x in (a, b):
            continue
        move = base.controller(a, b, x, p)
        after = base.change(counts, move, p)
        if len(base.heavy(after, p)) >= 2:
            return move, 'combined-single'
        mean = sum(move)//p
        if mean == b:
            assert (b-x) % delta == 0
            coefficient = (b-x)//delta
            assert alpha+1 <= coefficient <= p-1
            negative[x] = counts[x]
        else:
            assert mean == a and (x-a) % delta == 0
            coefficient = (x-a)//delta
            assert beta+1 <= coefficient <= p-1
            positive[x] = counts[x]
    n = sum(counts.values())
    assert gcd(delta, n) == 1
    low = sum((b-x)//delta*f for x, f in negative.items())
    high = sum((x-a)//delta*f for x, f in positive.items())
    if low >= p:
        selected = negative+Counter({a:counts[a], b:counts[b]})
        return linear.crossing_move(selected, b, delta, p), 'combined-negative-crossing'
    assert high >= p
    selected = positive+Counter({a:counts[a], b:counts[b]})
    return linear.crossing_move(selected, a, -delta, p), 'combined-positive-crossing'


def protected_pool(counts, a, b, p, factors):
    n = sum(counts.values())
    available = counts-Counter({a:p, b:p})
    for q in factors:
        classes = Counter()
        for x, f in counts.items():
            classes[x % q] += f
        majority = next((r for r, f in classes.items() if f >= n-p), None)
        if majority is None:
            continue
        exceptions = {x:f for x, f in counts.items() if x % q != majority}
        if all(available[x] == f for x, f in exceptions.items()):
            x = next(iter(exceptions))
            assert x not in (a, b)
            available[x] -= 1
    available += Counter()
    values = [a]*available[a]+[b]*available[b]
    for x, f in available.items():
        if x not in (a, b):
            values += [x]*min(f, 2*p-2-len(values))
    assert len(values) == 2*p-2
    assert values.count(a) == counts[a]-p and values.count(b) == counts[b]-p
    return values


def borrow_anchor(a, b, left, right, p):
    u, v = left[0], right[0]
    for anchor, other in ((a, b), (b, a)):
        i = (v-anchor)*pow(u-v, -1, p) % p
        assert 1 <= i <= p-2
        move = (anchor,)+tuple(left[:i])+tuple(right[:p-1-i])
        if sum(move) != p*other:
            return move, 'borrow-one'
        for group, selected, offset in ((left, i, 1), (right, p-1-i, 1+i)):
            selected_index = next((k for k in range(selected) if group[k] != group[selected]), None)
            if selected_index is not None:
                after = list(move)
                after[offset+selected_index] = group[selected]
                return tuple(after), 'borrow-vary-selected'
            spare_index = next((k for k in range(selected, len(group)) if group[k] != group[0]), None)
            if spare_index is not None:
                after = list(move)
                after[offset] = group[spare_index]
                return tuple(after), 'borrow-vary-spare'
        assert len(set(left)) == len(set(right)) == 1
        if i != (p-1)//2:
            j = 2*i % p
            move = (anchor, anchor)+(u,)*j+(v,)*(p-2-j)
            assert sum(move) % p == 0 and sum(move) != p*other
            return move, 'borrow-two'
    raise AssertionError('Two distinct anchor residues cannot both have the exceptional index.')


def conditions(n, p):
    return p >= 5 and base.is_prime(p) and n >= 4*p-2+len(base.protected_primes(n, p))


def choose(counts, n, p, factors):
    heavy = sorted(base.heavy(counts, p))
    if len(heavy) >= 4:
        return linear.choose(counts, n, p, factors)
    if len(heavy) == 3:
        a, b, c = heavy
        if len(counts) == 3 and counts[a] == counts[c] == p and len({x % p for x in heavy}) == 3:
            move, branch = triple.choose_three(counts, p)
            return move, 'three-'+branch, c if move is None else None
        return old.choose(counts, n, p, factors)
    assert len(heavy) == 2
    a, b = heavy
    if max(counts[a], counts[b]) >= 2*p-1:
        return linear.choose(counts, n, p, factors)
    if (a-b) % p == 0:
        return tuple(middle.same_residue_move(counts, p, factors)), 'same-residue', None
    for anchor, other in ((a, b), (b, a)):
        for x in counts:
            if x in (a, b) or (x-anchor) % p:
                continue
            move = (anchor,)*(p-1)+(x,)
            if sum(move) != p*other:
                return move, 'anchor-residue-single', None
            if counts[x] >= 2:
                return (anchor,)*(p-2)+(x, x), 'anchor-residue-double', None
    if counts[a]+counts[b] >= 3*p-2:
        move, branch = combined_reserve(counts, a, b, p)
        return move, branch, None
    values = protected_pool(counts, a, b, p, factors)
    move = inverse_egz(values, p)
    if move is not None:
        return move, 'inverse-EGZ-subset', None
    # Each anchor residue has at most one light singleton after the early
    # repairs. An anchor surplus in a p-1 residue class would force p-2
    # surplus copies, already covered by the combined-reserve branch.
    assert counts[a] == counts[b] == p
    bins = defaultdict(list)
    for x in values:
        bins[x % p].append(x)
    left, right = bins.values()
    assert a % p not in bins and b % p not in bins
    move, branch = borrow_anchor(a, b, left, right, p)
    return move, branch, None


def audit(counts, p, branches):
    n = sum(counts.values())
    assert conditions(n, p) and sum(x*f for x, f in counts.items()) == 0
    factors = base.protected_primes(n, p)
    if not base.legal(counts, factors) or len(base.heavy(counts, p)) < 2:
        return False
    move, branch, delta = choose(counts, n, p, factors)
    branches[branch] += 1
    if move is None:
        assert set(counts) == {-delta, 0, delta}
        assert counts[delta] == counts[-delta] and counts[0] >= p-2
    else:
        after = base.change(counts, move, p)
        assert len(base.heavy(after, p)) >= 2 and base.legal(after, factors)
    return True


def solve(initial, p):
    n, branches = len(initial), Counter()
    factors = base.protected_primes(n, p)
    assert conditions(n, p) and base.legal(Counter(initial), factors)
    replay = base.LabelledReplay(initial, p)
    for move in base.initialize(replay.counts(), n, p, factors):
        replay.step(move)
    while any(replay.state):
        move, branch, delta = choose(replay.counts(), n, p, factors)
        branches[branch] += 1
        if move is None:
            for _ in range(replay.counts()[delta]):
                replay.step((delta, -delta)+(0,)*(p-2))
            break
        after = base.change(replay.counts(), move, p)
        assert base.legal(after, factors) and len(base.heavy(after, p)) >= 2
        replay.step(move)
    old.previous.replay_original(initial, replay.word, p)
    return len(replay.word), branches


def main():
    exact = 0
    for p in (5, 7):
        for residues in combinations_with_replacement(range(p), 2*p-2):
            result = inverse_egz(residues, p)
            rigid = sorted(Counter(residues).values()) == [p-1, p-1]
            assert (result is None) == rigid
            exact += 1
    print('inverse EGZ complete unordered boundary residues: PASS', exact)

    random, branches, cases = Random(2026091213), Counter(), 0
    for p in (5, 7, 11, 17, 31, 61):
        lower = 4*p+(p-1).bit_length()
        for _ in range(350):
            n = lower+random.randrange(7)
            length = random.randrange(3, 10)
            weights = [p, p]+[1]*(length-2)
            for _ in range(n-sum(weights)):
                weights[random.randrange(length)] += 1
            values = [random.randrange(-10**9, 10**9)*weights[-1] for _ in range(length-1)]
            values.append(-sum(w*x for w, x in zip(weights, values))//weights[-1])
            counts = Counter()
            for x, weight in zip(values, weights):
                counts[x] += weight
            cases += audit(counts, p, branches)
        for n in range(lower, lower+500):
            assert conditions(n, p)
    print('inverse EGZ threshold large-coordinate closure: PASS', cases)

    borrowed = Counter()
    for p in (5, 7, 11, 17):
        for i in range(1, p-1):
            u, v = 1, 0
            b = next(x for x in range(2, p) if x % p != -i % p)
            a = p*b-i
            move, branch = borrow_anchor(a, b, [u]*(p-1), [v]*(p-1), p)
            assert sum(move) % p == 0
            borrowed[branch] += 1
            left = [u]*(p-2)+[u+p]
            move, branch = borrow_anchor(a, b, left, [v]*(p-1), p)
            assert sum(move) % p == 0
            borrowed[branch] += 1
    print('inverse EGZ borrowed-anchor collision certificates: PASS', dict(borrowed))

    crossings = Counter()
    for p in (5, 7, 11, 17, 31, 61):
        counts = Counter({1:p+1, 0:2*p-3, -(p+1)//2:2})
        for a, b in ((1, 0), (0, 1)):
            move, branch = combined_reserve(counts, a, b, p)
            after = base.change(counts, move, p)
            assert len(base.heavy(after, p)) >= 2
            assert base.legal(after, base.protected_primes(3*p, p))
            crossings[branch] += 1
    print('combined heavy-reserve two-sided crossings: PASS', dict(crossings))

    paths, longest = 0, 0
    for p, n in ((5, 19), (5, 20), (7, 27), (7, 28), (11, 43), (17, 67)):
        assert conditions(n, p)
        for _ in range(6):
            while True:
                values = [random.randrange(-15, 16) for _ in range(n-1)]
                values.append(-sum(values))
                if base.legal(Counter(values), base.protected_primes(n, p)):
                    break
            length, local = solve(values, p)
            branches.update(local)
            paths += 1
            longest = max(longest, length)
    print('inverse EGZ threshold literal one-digit full paths: PASS', paths, longest)
    print('inverse EGZ threshold observed branches:', dict(sorted(branches.items())))
    print('inverse EGZ improved threshold: PASS')


if __name__ == '__main__':
    main()
