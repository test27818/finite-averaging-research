"""Compile universal subproblem calls using localized row-lattice inclusion.

Only coefficient vectors and block multiplicities are enumerated. The
subproblem sizes 13, 14, 15 use already established complete criteria.
"""

from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, product
from math import gcd, lcm

from explore_b17_nine_thirteen_bridges import U, V, W, add, scale, primitive_matrix


def away_three(integer):
    integer = abs(integer)
    while integer and integer % 3 == 0:
        integer //= 3
    return integer


def row_lattice_contains(rows, target):
    """Test target in span_{Z[1/3]}(rows), for rational two-column rows."""
    if target == (0, 0):
        return True
    if any(away_three(x.denominator) != 1 for row in rows + [target] for x in row):
        return False
    denominator = lcm(*(x.denominator for row in rows + [target] for x in row))
    rows = [tuple(int(x * denominator) for x in row) for row in rows]
    target = tuple(int(x * denominator) for x in target)
    minors = lambda matrix: [a[0]*b[1]-a[1]*b[0] for a, b in combinations(matrix, 2)]
    determinant_content = gcd(*minors(rows)) if len(rows) > 1 else 0
    augmented = rows + [target]
    if determinant_content:
        return away_three(determinant_content) == away_three(gcd(*minors(augmented)))
    if any(minors(augmented)):
        return False
    content = gcd(*(x for row in rows for x in row)) if rows else 0
    if not content:
        return target == (0, 0)
    return away_three(content) == away_three(gcd(content, *target))


def universal_call(block, mean):
    anchor = block[0][0]
    return row_lattice_contains([add(x, scale(anchor, -1)) for x, _ in block],
                                add(mean, scale(anchor, -1)))


@lru_cache(maxsize=None)
def generate(initial_sizes=(3, 9)):
    unique = {}
    for size0 in initial_sizes:
        for beta, gamma in product(range(4), range(2)):
            alpha = size0 - beta - gamma
            if not 0 <= alpha <= 13 or beta == gamma == 0:
                continue
            first_block = tuple((x, c) for x, c in ((U, alpha), (V, beta), (W, gamma)) if c)
            a = scale(add(*(scale(x, c) for x, c in first_block)), F(1, size0))
            if not universal_call(first_block, a):
                continue
            state = Counter({U: 13-alpha, V: 3-beta, W: 1-gamma})
            state += Counter({a: size0})
            values = sorted(state)
            for size in (13, 14, 15):
                complement_size = 17-size
                for counts in product(*(range(min(complement_size, state[x])+1) for x in values)):
                    if sum(counts) != complement_size:
                        continue
                    leftover = tuple((x, c) for x, c in zip(values, counts) if c)
                    total = add(*(scale(x, c) for x, c in leftover))
                    mean = scale(total, F(-1, size))
                    block = tuple((x, state[x]-c) for x, c in zip(values, counts) if state[x] > c)
                    if not universal_call(block, mean):
                        continue
                    for singleton, _ in leftover:
                        triple = Counter(dict(leftover))
                        triple[singleton] -= 1
                        triple[mean] += size-13
                        triple = +triple
                        assert sum(triple.values()) == 3
                        repaired = scale(add(*(scale(x, c) for x, c in triple.items())), F(1, 3))
                        assert add(scale(mean, 13), scale(repaired, 3), singleton) == (0, 0)
                        matrix = mean+repaired
                        if matrix[0]*matrix[3] == matrix[1]*matrix[2]:
                            continue
                        integer = primitive_matrix(matrix)
                        row = dict(first_block=first_block, size0=size0, a=a,
                                   size=size, block=block, mean=mean, triple=tuple(triple.items()),
                                   singleton=singleton, matrix=matrix, integer=integer)
                        unique.setdefault(integer, row)
    return tuple(unique.values())


def run():
    rows = generate()
    print('universal B17 subproblem macros', len(rows))
    for row in rows:
        a,b,c,d = row['integer']
        print(row['integer'], 'det', a*d-b*c, 'trace', a+d,
              'calls', row['size0'], row['size'],
              'first', row['first_block'], 'block', row['block'],
              'singleton', row['singleton'])


if __name__ == '__main__':
    run()
