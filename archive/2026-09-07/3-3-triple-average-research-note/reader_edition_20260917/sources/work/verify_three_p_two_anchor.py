"""Savchev--Chen two-anchor interface and exact modular-fiber diagnostics.

Extrema of nonempty subset sums are stored per residue, retaining persistent
parent nodes. This determines whether all actual zero-residue sums collide;
it never enumerates averaging words or all subsets.
"""

from collections import Counter
from itertools import combinations_with_replacement
from math import gcd
from random import Random

import verify_inverse_egz_threshold as previous

base = previous.base


def fiber_extrema(values, p, max_size=None):
    if max_size is not None and len(values) > max_size:
        return bounded_fiber_extrema(values, p, max_size)
    nodes, low, high = [], [None]*p, [None]*p

    def add(value, parent, position):
        idx = len(nodes)
        nodes.append((value, parent, position))
        residue = value % p
        if low[residue] is None or value < nodes[low[residue]][0]:
            low[residue] = idx
        if high[residue] is None or value > nodes[high[residue]][0]:
            high[residue] = idx

    for position, value in enumerate(values):
        parents = set(x for x in low+high if x is not None)
        add(value, None, position)
        for node in parents:
            add(nodes[node][0]+value, node, position)

    def decode(node):
        if node is None:
            return None
        total, parent, position = nodes[node]
        chosen = []
        while node is not None:
            _, node, position = nodes[node]
            chosen.append(position)
        assert chosen and len(chosen) == len(set(chosen))
        assert sum(values[i] for i in chosen) == total and total % p == 0
        return total, tuple(chosen)

    return decode(low[0]), decode(high[0])


def bounded_fiber_extrema(values, p, cap):
    nodes = [(0, None, None)]
    low = [[None]*p for _ in range(cap+1)]
    high = [[None]*p for _ in range(cap+1)]
    low[0][0] = high[0][0] = 0
    for position, value in enumerate(values):
        for count in range(min(position+1, cap), 0, -1):
            parents = set(x for x in low[count-1]+high[count-1] if x is not None)
            for parent in parents:
                total = nodes[parent][0]+value
                residue = total % p
                improve_low = low[count][residue] is None or total < nodes[low[count][residue]][0]
                improve_high = high[count][residue] is None or total > nodes[high[count][residue]][0]
                if improve_low or improve_high:
                    idx = len(nodes)
                    nodes.append((total, parent, position))
                    if improve_low:
                        low[count][residue] = idx
                    if improve_high:
                        high[count][residue] = idx
    def decode(node):
        total, chosen = nodes[node][0], []
        while node:
            _, node, position = nodes[node]
            chosen.append(position)
        assert 1 <= len(chosen) <= cap and len(chosen) == len(set(chosen))
        assert sum(values[i] for i in chosen) == total and total % p == 0
        return total, tuple(chosen)
    minima = [low[k][0] for k in range(1, cap+1) if low[k][0] is not None]
    maxima = [high[k][0] for k in range(1, cap+1) if high[k][0] is not None]
    if not minima:
        return None, None
    return decode(min(minima, key=lambda i: nodes[i][0])), decode(max(maxima, key=lambda i: nodes[i][0]))


def two_anchor(values, alpha, beta, p):
    assert alpha >= beta >= 0 and alpha+beta <= p-3
    assert len(values) == p-alpha-beta
    first, reached, mask = [1]*alpha+values, 1, (1 << p)-1
    for value in first:
        shift = value % p
        rotated = ((reached << shift) | (reached >> (p-shift))) & mask
        if rotated & 1:
            return 'first', None
        reached |= rotated
    # Savchev--Chen forces the unit multiplier to be1. With beta=0 the
    # first sequence has length p and cannot have been zero-free.
    assert beta > 0
    lifts = [x % p for x in values]
    assert all(lifts) and alpha+sum(lifts) <= p-1
    assert sum(x-1 for x in lifts) <= beta-1
    count = lifts[0]-1
    second = [-1]*beta+[x-1 for x in values]
    selected = tuple(range(count))+(beta,)
    assert sum(second[i] for i in selected) % p == 0
    return 'second', (sum(second[i] for i in selected), selected)


def zero_free_repair(a, b, light, alpha, beta, p):
    delta = a-b
    residues = [(x-b)*pow(delta, -1, p) % p for x in light]
    assert alpha >= beta and alpha+sum(residues) <= p-1
    assert all(residues)
    for x, z in zip(light[:2], residues[:2]):
        move = (a,)*(p-z)+(b,)*(z-1)+(x,)
        if sum(move) != p*b:
            return move
    z = residues[0]+residues[1]
    move = (a,)*(p-z)+(b,)*(z-2)+tuple(light[:2])
    assert sum(move) == p*(b-delta) and z-2 <= beta
    return move


def protect_light(counts, a, b, p, factors, truncate=True):
    n = sum(counts.values())
    light = Counter({x:f for x, f in counts.items() if x not in (a, b)})
    for q in factors:
        classes = Counter()
        for x, f in counts.items():
            classes[x % q] += f
        majority = next((r for r, f in classes.items() if f >= n-p), None)
        if majority is None:
            continue
        exceptions = {x:f for x, f in counts.items() if x % q != majority}
        if all(light[x] == f for x, f in exceptions.items()):
            light[next(iter(exceptions))] -= 1
    light += Counter()
    length = p-(counts[a]-p)-(counts[b]-p) if truncate else sum(light.values())
    values = []
    for x, f in light.items():
        values += [x]*min(f, length-len(values))
    assert len(values) == length
    return values


def choose_local(counts, p):
    a, b = sorted(base.heavy(counts, p), key=lambda x: counts[x], reverse=True)
    alpha, beta = counts[a]-p, counts[b]-p
    n = sum(counts.values())
    factors = base.protected_primes(n, p)
    assert n >= 3*p+len(factors) and alpha+beta <= p-3 and (a-b) % p
    light = protect_light(counts, a, b, p, factors)
    first = [a]*alpha+light
    ext = fiber_extrema([x-b for x in first], p)
    if ext[0] is None:
        move = zero_free_repair(a, b, light, alpha, beta, p)
        return move, 'zero-free-repaired', None
    for target, padding, capacity, pool in ((a, b, alpha, first),
                                          (b, a, beta, [b]*beta+light)):
        low, high = fiber_extrema([x-padding for x in pool], p)
        for result in (low, high):
            if result is None:
                continue
            total, positions = result
            if total != p*(target-padding):
                move = tuple(pool[i] for i in positions)+(padding,)*(p-len(positions))
                return move, 'noncolliding-fiber', None
    full_light = protect_light(counts, a, b, p, factors, truncate=False)
    for target, padding, pool in ((a, b, [a]*alpha+full_light),
                                 (b, a, [b]*beta+full_light)):
        for result in fiber_extrema([x-padding for x in pool], p, max_size=p):
            if result is None:
                continue
            total, positions = result
            if total != p*(target-padding):
                move = tuple(pool[i] for i in positions)+(padding,)*(p-len(positions))
                return move, 'expanded-pool-repair', None
    total, positions = ext[0]
    move = tuple(first[i] for i in positions)+(b,)*(p-len(positions))
    assert sum(move) == p*a
    used_a = sum(i < alpha for i in positions)
    after = base.change(counts, move, p)
    assert after[a] == 2*p+alpha-used_a
    if len(base.heavy(after, p)) >= 2:
        return move, 'collision-retains-both', None
    assert len(base.heavy(after, p)) == 1 and 2*p <= after[a] <= 3*p-3
    return move, 'collision-only', {'p':p, 'n':n, 'counts':dict(counts),
                                   'light':light, 'alpha':alpha, 'beta':beta}


def main():
    # A residue-zero fiber need not itself satisfy the matroid basis axiom.
    from itertools import combinations
    labels = [1, 4, 2, 3]
    bases = [frozenset(pair) for pair in combinations(range(4), 2)
             if sum(labels[i] for i in pair) % 5 == 0]
    assert bases == [frozenset((0, 1)), frozenset((2, 3))]
    assert not any((bases[0]-{0}) | {j} in bases for j in bases[1])
    assert fiber_extrema([1, 3, 3], 5)[0] is None
    assert fiber_extrema([-1, 2, 2], 5)[0] is None
    print('modular-fiber exchange and below-three-p boundaries: PASS 2')
    checks, second = 0, 0
    for p in (5, 7, 11):
        for alpha in range(p-2):
            for beta in range(min(alpha, p-3-alpha)+1):
                length = p-alpha-beta
                for values in combinations_with_replacement(range(2, p), length):
                    kind, result = two_anchor(list(values), alpha, beta, p)
                    checks += 1
                    second += kind == 'second'
    print('three-p two-anchor complete small residue instances: PASS', checks, second)

    random, oracle = Random(2026091215), 0
    for p in (5, 7, 11):
        for _ in range(35):
            values = [random.randrange(-30, 31) for _ in range(7)]
            answers = [sum(values[i] for i in range(len(values)) if mask >> i & 1)
                       for mask in range(1, 1 << len(values))]
            zeros = [value for value in answers if value % p == 0]
            low, high = fiber_extrema(values, p)
            assert (low is None) == (not zeros)
            if zeros:
                assert low[0] == min(zeros) and high[0] == max(zeros)
            restricted = [sum(values[i] for i in range(len(values)) if mask >> i & 1)
                          for mask in range(1, 1 << len(values)) if mask.bit_count() <= 4]
            restricted = [x for x in restricted if x % p == 0]
            low, high = fiber_extrema(values, p, max_size=4)
            assert (low is None) == (not restricted)
            if restricted:
                assert low[0] == min(restricted) and high[0] == max(restricted)
            oracle += 1
    print('modular fiber extrema independent small subset oracle: PASS', oracle)

    repairs = 0
    for p in (11, 17, 31, 61):
        alpha, beta = (p-3)//2, (p-3)//2
        length = 3
        z = [1, 1, 1]
        for shift in (0, 1):
            z[-1] += shift
            assert alpha+sum(z) <= p-1
            a, b = 1, 0
            light = [x-p for x in z]
            counts = Counter({a:p+alpha, b:p+beta})
            counts.update(light)
            move = zero_free_repair(a, b, light, alpha, beta, p)
            after = base.change(counts, move, p)
            assert len(base.heavy(after, p)) >= 2
            repairs += 1
    print('zero-free branch exact one/two-light repair: PASS', repairs)

    branches, examples = Counter(), []
    for p in (5, 7, 11, 17, 31):
        for _ in range(1000):
            n = 3*p+max(2, len(base.protected_primes(3*p+2, p)))
            while n < 3*p+len(base.protected_primes(n, p)):
                n += 1
            alpha = random.randrange(p-2)
            beta = random.randrange(p-2-alpha)
            length = n-2*p-alpha-beta
            groups = random.randrange(2, min(8, length)+1)
            weights = [1]*groups
            for _ in range(length-groups):
                weights[random.randrange(groups)] += 1
            if max(weights) >= p:
                continue
            scale = weights[-1]
            a, b = [random.randrange(-30, 31)*scale for _ in range(2)]
            light = [random.randrange(-30, 31)*scale for _ in range(groups-1)]
            light.append(-((p+alpha)*a+(p+beta)*b+sum(w*x for w, x in zip(weights, light)))//scale)
            counts = Counter()
            counts[a] += p+alpha
            counts[b] += p+beta
            for x, f in zip(light, weights):
                counts[x] += f
            if a == b or (a-b) % p == 0 or len(base.heavy(counts, p)) != 2:
                continue
            heavy = base.heavy(counts, p)
            if sum(counts[x] for x in heavy) > 3*p-3:
                continue
            factors = base.protected_primes(n, p)
            if not base.legal(counts, factors):
                continue
            move, branch, example = choose_local(counts, p)
            after = base.change(counts, move, p)
            assert base.legal(after, factors)
            if branch != 'collision-only':
                assert len(base.heavy(after, p)) >= 2
            elif len(examples) < 4:
                examples.append(example)
            branches[branch] += 1
    print('three-p safe actual-value candidate diagnostics:', dict(branches))
    print('remaining all-collision diagnostic examples:', examples)
    print('three-p two-anchor interface: PASS')


if __name__ == '__main__':
    main()
