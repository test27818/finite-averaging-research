"""Exact individual-position equations for the five-average collision fiber."""

from collections import Counter
from fractions import Fraction as F
from itertools import combinations_with_replacement
from math import gcd, lcm

from explore_collision_equations import solve_rows


def rows(sequence, alpha, beta):
    size = len(sequence)
    for i, residue in enumerate(sequence):
        if residue in (0, 1):
            yield tuple(int(i == j) for j in range(size)), 5 if residue == 0 else -4
    for mask in range(1, 1 << size):
        count = mask.bit_count()
        if count > 5:
            continue
        coefficients = tuple((mask >> j) & 1 for j in range(size))
        residue = sum(x*c for x, c in zip(sequence, coefficients)) % 5
        i = -residue % 5
        if i <= min(alpha, 5-count):
            if 5-count-i <= beta:
                yield (0,)*size, 1
                return
            yield coefficients, 5-i
        j = (residue-count) % 5
        if j <= min(beta, 5-count):
            yield coefficients, count+j-5


def main():
    stats, exceptional = Counter(), []
    for alpha, beta in ((0, 0), (1, 0), (1, 1), (2, 0)):
        for capacity in (5, 6, 7, 8):
            length = capacity-alpha-beta
            for sequence in combinations_with_replacement(range(5), length):
                counts = Counter(sequence)
                if max(counts.values()) >= 5 or counts[0] > 1 or counts[1] > 1:
                    continue
                solution = solve_rows(rows(sequence, alpha, beta), length)
                stats['systems'] += 1
                if solution is None:
                    continue
                stats['consistent'] += 1
                if len(solution) > 1:
                    exceptional.append((alpha, beta, capacity, sequence, 'free', str(solution)))
                    continue
                values = solution[0]
                if any(x.denominator % 5 == 0 or x.numerator*pow(x.denominator, -1, 5) % 5 != r
                       for x, r in zip(values, sequence)):
                    stats['wrong-residue'] += 1
                    continue
                denominators = lcm(*(x.denominator for x in values))
                stats['denominator-'+str(denominators)] += 1
                stats['capacity-'+str(capacity)] += 1
                exceptional.append((alpha, beta, capacity, sequence, tuple(map(str, values)), denominators))
    print('individual-position collision statistics:', dict(stats))
    print('complete exceptional list:', exceptional)


if __name__ == '__main__':
    main()
