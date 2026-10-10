"""Small residue-type audit of all-collision equations; not a theorem proof.

Enumerate multiplicities, not position subsets or averaging words. Solve the
overdetermined rational equations incrementally, stopping at inconsistency.
Only constant actual values within a residue type are modeled here.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import combinations_with_replacement, product
from math import gcd, lcm


def solve_rows(rows, width):
    pivots = {}
    for coefficients, rhs in rows:
        row = list(map(F, coefficients)) + [F(rhs)]
        for j, pivot in sorted(pivots.items()):
            if row[j]:
                factor = row[j]
                row = [x-factor*y for x, y in zip(row, pivot)]
        first = next((j for j in range(width) if row[j]), None)
        if first is None:
            if row[-1]:
                return None
        else:
            factor = row[first]
            pivots[first] = [x/factor for x in row]
    free = [i for i in range(width) if i not in pivots]
    basis = []
    for k in [None]+free:
        vector = [F(0)]*width
        if k is not None:
            vector[k] = 1
        for j, row in sorted(pivots.items(), reverse=True):
            vector[j] = (row[-1] if k is None else 0)-sum(row[i]*vector[i] for i in range(j+1, width))
        basis.append(vector)
    return basis


def rows_for(residues, frequencies, alpha, beta, p):
    for counts in product(*(range(f+1) for f in frequencies)):
        size = sum(counts)
        if not 1 <= size <= p:
            continue
        remainder = sum(x*c for x, c in zip(residues, counts)) % p
        i = -remainder % p
        if i <= min(alpha, p-size):
            yield counts, p-i
        j = (remainder-size) % p
        if j <= min(beta, p-size):
            yield counts, size+j-p


def main():
    summary, samples = Counter(), []
    for p in (5, 7):
        for extra in (0, 1, 2):
            n = 3*p+extra
            for alpha in range(p-2):
                for beta in range(min(alpha, p-3-alpha)+1):
                    length = p+extra-alpha-beta
                    for sequence in combinations_with_replacement(range(2, p), length):
                        counts = Counter(sequence)
                        if max(counts.values()) >= p:
                            continue
                        residues, frequencies = list(counts), list(counts.values())
                        solution = solve_rows(rows_for(residues, frequencies, alpha, beta, p), len(residues))
                        summary['systems'] += 1
                        if solution is None:
                            summary['inconsistent'] += 1
                            continue
                        summary['consistent'] += 1
                        summary['consistent-extra-'+str(extra)] += 1
                        if len(solution) > 1:
                            summary['positive-dimensional'] += 1
                            if len(samples) < 12:
                                samples.append((p, extra, alpha, beta, dict(counts), 'free', str(solution)))
                            continue
                        values = solution[0]
                        if any(x.denominator % p == 0 or x.numerator*pow(x.denominator, -1, p) % p != r
                               for x, r in zip(values, residues)):
                            summary['wrong-residue'] += 1
                            continue
                        mean = (p+alpha+sum(x*f for x, f in zip(values, frequencies)))/n
                        centered = [1-mean, -mean]+[x-mean for x in values]
                        denominator = lcm(*(x.denominator for x in centered))
                        ints = [int(x*denominator) for x in centered]
                        common = gcd(*ints)
                        ints = [x//common for x in ints]
                        difference = gcd(*(x-ints[0] for x in ints))
                        summary['G1' if difference == 1 else 'nontrivial-G'] += 1
                        if len(samples) < 12 or (extra and len(samples) < 25):
                            samples.append((p, extra, alpha, beta, dict(counts), list(map(str, values)), difference))
    print('bounded constant-residue collision systems:', dict(summary))
    print('consistent sample systems:', samples)


if __name__ == '__main__':
    main()
