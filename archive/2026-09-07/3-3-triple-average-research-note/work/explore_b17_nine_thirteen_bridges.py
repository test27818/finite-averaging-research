"""Enumerate weighted 9 -> 13 B17 returns, without enumerating positions.

The 13-point call is guarded by a nonconstant residue class at 13. All
matrices retained are nonsingular at 17, preserving the global witness.
This is local coverage, not a descent or reachability theorem.
"""

from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import gcd, lcm


U, V, W = (F(1), F(0)), (F(0), F(1)), (F(-13), F(-3))


def add(*values):
    return tuple(sum(x[i] for x in values) for i in (0, 1))


def scale(value, scalar):
    return tuple(x * scalar for x in value)


def mod(value, prime):
    value = F(value)
    return value.numerator * pow(value.denominator, -1, prime) % prime


def at(value, pair):
    return value[0] * pair[0] + value[1] * pair[1]


def projective(pair, prime):
    x, y = (mod(t, prime) for t in pair)
    if x:
        return (1, y * pow(x, -1, prime) % prime)
    return (0, 1) if y else None


def points(prime):
    return [(1, t) for t in range(prime)] + [(0, 1)]


def primitive_matrix(matrix):
    denominator = lcm(*(x.denominator for x in matrix))
    integer = tuple(int(x * denominator) for x in matrix)
    content = gcd(*integer)
    integer = tuple(x // content for x in integer)
    return min(integer, tuple(-x for x in integer))


@lru_cache(maxsize=1)
def generate():
    unique = {}
    for beta, gamma in product(range(4), range(2)):
        alpha = 9 - beta - gamma
        if beta == gamma == 0:
            continue
        first_block = ((U, alpha), (V, beta), (W, gamma))
        a = scale(add(*(scale(x, c) for x, c in first_block)), F(1, 9))
        state = Counter({U: 13 - alpha, V: 3 - beta, W: 1 - gamma})
        state += Counter({a: 9})
        values = sorted(state)
        # A 13-block is specified by its four-position complement.
        for counts in product(*(range(min(4, state[x]) + 1) for x in values)):
            if sum(counts) != 4:
                continue
            leftover = tuple((x, c) for x, c in zip(values, counts) if c)
            total = add(*(scale(x, c) for x, c in leftover))
            mean = scale(total, F(-1, 13))
            block = tuple((x, state[x] - c) for x, c in zip(values, counts)
                          if state[x] > c)
            guards = tuple(p for p in points(13) if mod(at(total, p), 13) == 0
                           and len({mod(at(x, p), 13) for x, _ in block}) > 1)
            if not guards:
                continue
            for singleton, _ in leftover:
                repaired = scale(add(total, scale(singleton, -1)), F(1, 3))
                assert add(scale(mean, 13), scale(repaired, 3), singleton) == (0, 0)
                matrix = mean + repaired
                determinant = matrix[0] * matrix[3] - matrix[1] * matrix[2]
                if not determinant or mod(determinant, 17) == 0:
                    continue
                row = dict(first_block=first_block, a=a, block=block,
                           leftover=leftover, singleton=singleton, matrix=matrix,
                           integer=primitive_matrix(matrix), guards=guards)
                key = (row['integer'], guards)
                unique.setdefault(key, row)
    return tuple(unique.values())


def run():
    rows = generate()
    print('weighted 9-to-13 return templates', len(rows))
    coverage = Counter(g for row in rows for g in row['guards'])
    print('guard coverage at 13', dict(sorted(coverage.items())))
    # A 5-adic slope different from infinity and 3 reaches -1 in <=3 A steps.
    for source in ((1, 3), (0, 1)):
        covered = set()
        candidates = []
        for row in rows:
            matrix = row['matrix']
            target = projective((at(matrix[:2], source), at(matrix[2:], source)), 5)
            if target is not None and target[0] and target[1] != 3:
                covered.update(row['guards'])
                candidates.append(row)
        missing = set(points(13)) - covered
        print('source mod5', source, 'direct guard coverage', len(covered),
              'missing', sorted(missing), 'templates', len(candidates))
        remaining = set(missing)
        for source13 in missing:
            current = source13
            for _ in range(6):
                current = projective((3 * current[0], -13 * current[0] - current[1]), 13)
                if current in covered:
                    remaining.discard(source13)
                    break
        print('after A prelude missing', sorted(remaining))
        # A compact reproducible cover, selected over residue signatures.
        uncovered = set(covered)
        selected = []
        for row in sorted(candidates, key=lambda r: (max(abs(x) for x in r['integer']), r['integer'])):
            if uncovered.intersection(row['guards']):
                selected.append(row)
                uncovered.difference_update(row['guards'])
        for row in selected:
            print('certificate', source, row['guards'], row['integer'],
                  'nine', tuple(c for _, c in row['first_block']),
                  'leftover', row['leftover'], 'singleton', row['singleton'])


if __name__ == '__main__':
    run()
