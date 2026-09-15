"""Independent checks of uniform collision lemmas, without averaging-word search.

High-frequency systems have at most three exceptional positions. Each anchor
count and exceptional subset determines the dominant count by a modular inverse;
there is no loop over all p-element subsets or over dominant multiplicities.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement
from math import gcd
from random import Random


def prime(p):
    return p >= 2 and all(p % d for d in range(2, int(p**0.5) + 1))


def subset_masks(length):
    return [tuple(i for i in range(length) if mask >> i & 1)
            for mask in range(1 << length)]


def patterns(p, alpha, beta, residue, frequency, exceptional):
    for side, cap in ((0, alpha), (1, beta)):
        inverse = pow((residue-side) % p, -1, p)
        for chosen in subset_masks(len(exceptional)):
            total = sum(exceptional[i]-side for i in chosen)
            for anchors in range(cap+1):
                count = ((anchors if side else -anchors)-total)*inverse % p
                size = count+len(chosen)
                if not size or count > frequency or size+anchors > p:
                    continue
                yield side, anchors, count, chosen


def collision_rows(p, alpha, beta, residue, frequency, exceptional):
    for side, anchors, count, chosen in patterns(
            p, alpha, beta, residue, frequency, exceptional):
        row = (count,)+tuple(int(i in chosen) for i in range(len(exceptional)))
        light_size = count+len(chosen)
        if p-anchors-light_size <= (alpha if side else beta):
            yield (0,)*len(row), 1
            return
        yield row, light_size+anchors-p if side else p-anchors


def solve_rows(rows, width):
    pivots = {}
    originals = []
    for coefficients, rhs in rows:
        originals.append((coefficients, rhs))
        row = tuple(coefficients)+(rhs,)
        for column, pivot in sorted(pivots.items()):
            if row[column]:
                u, v = pivot[column], row[column]
                row = tuple(u*x-v*y for x, y in zip(row, pivot))
                common = gcd(*row)
                if common:
                    row = tuple(x//common for x in row)
        column = next((i for i in range(width) if row[i]), None)
        if column is None:
            if row[-1]:
                return None
        else:
            pivots[column] = row
    assert len(pivots) == width, ('unexpected free parameter', originals)
    values = [F(0)]*width
    for column, row in sorted(pivots.items(), reverse=True):
        values[column] = (F(row[-1])-sum(row[j]*values[j]
                          for j in range(column+1, width)))/row[column]
    assert all(sum(c*x for c, x in zip(row, values)) == rhs
               for row, rhs in originals)
    return tuple(values)


def predicted(p, alpha, beta, residue, frequency, exceptional):
    if beta:
        return None
    if alpha in (2, 3) and not exceptional and residue == 2:
        assert frequency == p+1-alpha
        return (F(2),)
    if alpha == 1 and frequency == p-1 and exceptional == ((residue-1) % p,):
        h = -pow(residue, -1, p) % p
        y = F(p-1, h)
        x = p-(p-1-h)*y
        k = -(exceptional[0]-1)*pow(residue-1, -1, p) % p
        if x+k*y == k+1-p:
            d = p-1-h
            assert (p-1)*(2*p-1) % d == 0
            assert k == 3*p-2-(p-1)*(2*p-1)//d
            return y, x
    return None


def verify_classification():
    tested = compatible = 0
    for p in (5, 7, 11, 13, 17, 19):
        for frequency in (p-2, p-1):
            for alpha in range(min(3, p-3)+1):
                for beta in range(min(alpha, p-3-alpha)+1):
                    extra = p+1-alpha-beta-frequency
                    if not 0 <= extra <= 3:
                        continue
                    for residue in range(2, p):
                        others = [r for r in range(p) if r != residue]
                        for exceptional in combinations_with_replacement(others, extra):
                            if exceptional.count(0) > 1 or exceptional.count(1) > 1:
                                continue
                            values = solve_rows(collision_rows(
                                p, alpha, beta, residue, frequency, exceptional), extra+1)
                            expected = predicted(p, alpha, beta, residue, frequency, exceptional)
                            assert values == expected, (p, alpha, beta, residue,
                                                        frequency, exceptional, values, expected)
                            tested += 1
                            if values is not None:
                                compatible += 1
                                mass = p+alpha+frequency*values[0]+sum(values[1:])
                                assert mass in (3*p-1, 3*p)
                                assert frequency+extra <= p
                                assert any(0 < count < frequency for _, _, count, _ in
                                           patterns(p, alpha, beta, residue, frequency, exceptional))
                                for value, label in zip(values, (residue,)+exceptional):
                                    assert value.denominator % p
                                    assert value.numerator*pow(value.denominator, -1, p) % p == label
    print('uniform high-frequency symbolic classification: PASS', tested, compatible)


def high_frequency_move(values, p, a, b, protected=()):
    protected = set(protected)
    ai = [i for i, x in enumerate(values) if x == a]
    bi = [i for i, x in enumerate(values) if x == b]
    alpha, beta = len(ai)-p, len(bi)-p
    inverse = pow(a-b, -1, p)
    classes = {}
    for i, x in enumerate(values):
        if i not in protected and x not in (a, b):
            classes.setdefault((x-b)*inverse % p, []).append(i)
    residue, dominant = max(classes.items(), key=lambda item: len(item[1]))
    assert len(values)-len(protected) == 3*p+1
    assert len(dominant) in (p-2, p-1) and residue not in (0, 1)
    assert alpha >= beta >= 0 and alpha+beta <= p-3
    dominant = sorted(dominant, key=lambda i: values[i])
    exceptional = [i for r, positions in classes.items() if r != residue for i in positions]
    labels = tuple((values[i]-b)*inverse % p for i in exceptional)
    for side, anchors, count, chosen in patterns(
            p, alpha, beta, residue, len(dominant), labels):
        target, reserve, padding = (b, bi, ai) if side else (a, ai, bi)
        for selected in (dominant[:count], dominant[len(dominant)-count:] if count else []):
            group = selected+[exceptional[i] for i in chosen]+reserve[:anchors]
            group += padding[:p-len(group)]
            assert len(group) == p and len(set(group)) == p and not protected.intersection(group)
            total = sum(values[i] for i in group)
            assert total % p == 0
            mean = total//p
            used_padding = sum(i in padding for i in group)
            if mean != target or len(padding)-used_padding >= p:
                return tuple(group)
    raise AssertionError(('legal high-frequency closure failed', p, values, protected))


def legal(values, p):
    n = len(values)
    return sum(values) == 0 and all(
        len({x % q for x in values}) > 1
        for q in range(2, n+1) if n % q == 0 and q != p and prime(q))


def replay(values, p, group, protected=()):
    assert legal(values, p)
    assert len(group) == len(set(group)) == p
    assert not set(group).intersection(protected)
    mean = sum((F(values[i]) for i in group), F(0))/p
    assert mean.denominator == 1
    result = list(values)
    for i in group:
        result[i] = int(mean)
    assert legal(result, p)
    assert len([x for x, count in Counter(result).items() if count >= p]) >= 2
    assert sum(x*x for x in result) < sum(x*x for x in values)


def centered_lifts(p, alpha, beta, labels, rng):
    n = 2*p+alpha+beta+len(labels)
    assert n % p
    light = [r+p*rng.randrange(10, 10000) for r in labels]
    total = p+alpha+sum(light)
    light[-1] += p*(-total*pow(p, -1, n) % n)
    shift = (p+alpha+sum(light))//n
    values = [1-shift]*(p+alpha)+[-shift]*(p+beta)+[x-shift for x in light]
    return values, 1-shift, -shift


def verify_literal_high_frequency():
    rng, tested, protected_tests = Random(120926), 0, 0
    for p in (5, 7, 11, 13, 17, 23, 47, 101):
        for _ in range(64):
            alpha = rng.randrange(min(3, p-3)+1)
            beta = rng.randrange(min(alpha, p-3-alpha)+1)
            frequency = rng.choice((p-2, p-1))
            extra = p+1-alpha-beta-frequency
            if not 0 <= extra <= 3:
                continue
            residue = rng.randrange(2, p)
            others = [r for r in range(p) if r != residue]
            exceptional = [rng.choice(others) for _ in range(extra)]
            labels = [residue]*frequency+exceptional
            values, a, b = centered_lifts(p, alpha, beta, labels, rng)
            replay(values, p, high_frequency_move(values, p, a, b))
            tested += 1
        q = 3*p+2
        if prime(q):
            for alpha in (2, 3):
                if alpha > p-3:
                    continue
                a, b, frequency = 1+q, 1, p+1-alpha
                for c in range(2, 4*p):
                    if (c-b) % q == 0 or (c-b)*pow(a-b, -1, p) % p in (0, 1):
                        continue
                    core = [a]*(p+alpha)+[b]*p+[c]*frequency
                    values = core+[-sum(core)]
                    protected = (len(core),)
                    assert len({x % q for x in values}) > 1
                    replay(values, p, high_frequency_move(values, p, a, b, protected), protected)
                    protected_tests += 1
    print('uniform high-frequency literal legal steps: PASS', tested, protected_tests)


def zero_piece(labels, p):
    prefix, seen = 0, {0: 0}
    for end, value in enumerate(labels[:p], 1):
        prefix = (prefix+value) % p
        if prefix in seen:
            return tuple(range(seen[prefix], end))
        seen[prefix] = end
    raise AssertionError('zero-sum input or p-item prefix required')


def verify_atoms_and_windows():
    partitions, windows = 0, 0
    for p in (3, 5, 7):
        for length in range(1, (3*p+1)//2+1):
            for labels in combinations_with_replacement(range(p), length):
                if sum(labels) % p:
                    continue
                remaining, sizes = list(labels), []
                while remaining:
                    selected = set(zero_piece(remaining, p))
                    sizes.append(len(selected))
                    remaining = [x for i, x in enumerate(remaining) if i not in selected]
                if all(a+b > p for a, b in combinations(sizes, 2)):
                    assert len(sizes) <= 2
                    if len(sizes) == 2:
                        assert sum(sizes) > p
                partitions += 1
    for p in (5, 7, 11, 13, 17, 23, 31):
        for alpha in range(p-2):
            for beta in range(min(alpha, p-3-alpha)+1):
                for extra in range(1, (p+1)//2+1):
                    for side, cap, other in ((0, alpha, beta), (1, beta, alpha)):
                        for j in range(cap+1):
                            length = p+extra-other-j
                            assert 0 < length < 3*(p+1)/2
                            factors = 1 if length <= p else 2
                            mass = ((factors+1)*p+j if not side else
                                    (2-factors)*p+extra-j)
                            assert 0 < mass < 3*p+extra
                            windows += 1
    for p in (q for q in range(5, 500) if prime(q) and q % 3 == 2):
        h = (p-2)//3
        y, x = F(p-1, h), F(2*p-1)-F((p-1)**2, h)
        assert 1+h*y == p
        assert x+(p-1-h)*y == p
        assert x+y == 2-p
        assert p+1+x+(p-1)*y == 3*p
    print('zero-sum factor and mass-window checks: PASS', partitions, windows)


def support_parameters(p):
    k = min(range(1, (p-1)//2+1), key=lambda k: 2*k+(p-2+k)//k)
    size = k+(p-2+k)//k
    assert k*(size-k) >= p-1 and 2*k <= p
    return k, size


def fixed_cardinality_zero(labels, p, k):
    mask, reached = (1 << p)-1, [1]+[0]*k
    parents = {}
    for position, label in enumerate(labels):
        label %= p
        for count in range(min(k, position+1), 0, -1):
            old = reached[count-1]
            rotated = ((old << label) | (old >> (p-label))) & mask
            new = rotated & ~reached[count]
            reached[count] |= rotated
            while new:
                bit = new & -new
                residue = bit.bit_length()-1
                parents[count, residue] = position, (residue-label) % p
                new -= bit
    assert reached[k] & 1
    result, residue = [], 0
    for count in range(k, 0, -1):
        position, residue = parents[count, residue]
        result.append(position)
    assert len(set(result)) == k and sum(labels[i] for i in result) % p == 0
    return tuple(result)


def verify_support_moves():
    rng, tested = Random(120927), 0
    for p in (7, 11, 17, 23, 47, 101):
        k, size = support_parameters(p)
        assert size+k <= p
        for _ in range(24):
            labels = list(range(p))+[rng.randrange(p)]
            values, a, b = centered_lifts(p, 0, 0, labels, rng)
            representatives = list(range(2*p, 3*p))
            rng.shuffle(representatives)
            first_pool = representatives[:size]
            first = tuple(first_pool[i] for i in fixed_cardinality_zero(
                [values[j]-b for j in first_pool], p, k))
            second_pool = [i for i in representatives if i not in first][:size]
            second = tuple(second_pool[i] for i in fixed_cardinality_zero(
                [values[j]-b for j in second_pool], p, k))
            assert not set(first).intersection(second)
            for selected in (first, second, first+second):
                group = selected+tuple(range(p, 2*p-len(selected)))
                if sum(values[i] for i in group) != p*a:
                    replay(values, p, group)
                    break
            else:
                raise AssertionError('two same-side collisions did not repair')
            tested += 1
    # Force both separate means to collide; verify the union exactly.
    p, a, b = 11, 3, -2
    first, second = (13, 38), (4, 47)
    assert sum(first)+(p-2)*b == p*a
    assert sum(second)+(p-2)*b == p*a
    assert sum(first+second)+(p-4)*b == p*(2*a-b)
    print('restricted-sum original-position selection: PASS', tested)


def main():
    verify_classification()
    verify_literal_high_frequency()
    verify_atoms_and_windows()
    verify_support_moves()
    print('uniform collision structure: PASS')


if __name__ == '__main__':
    main()
