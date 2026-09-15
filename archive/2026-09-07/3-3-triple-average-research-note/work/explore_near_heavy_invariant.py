"""Bounded four-value audit of the (p,p-1) repetition invariant.

This diagnostic ignores output congruence safety and cannot establish safe
closure. The exact three-value counterexample in
verify_sharp_multiplicity_and_precision.py supersedes that attempted use.
Count vectors and modular labels are enumerated; integer row elimination
replaces searches over unbounded numeric values or averaging words.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import gcd, lcm

from verify_provenance_dynamic_stages import count_choices
from verify_uniform_collision_structure import solve_rows


def weights_for(n, p):
    for a in range(p, n-p):
        for b in range(p-1, min(a, n-a-2)+1):
            for c in range(1, min(b, n-a-b-1)+1):
                d = n-a-b-c
                if 1 <= d <= c:
                    yield a, b, c, d


def normalize(values, weights):
    mean = sum(x*w for x, w in zip(values, weights))/sum(weights)
    centered = tuple(x-mean for x in values)
    scale = lcm(*(x.denominator for x in centered))
    ints = tuple(int(x*scale) for x in centered)
    common = gcd(*ints)
    if not common:
        return None
    result = tuple(x//common for x in ints)
    if gcd(*(x-result[0] for x in result)) != 1:
        return None
    return result


def check_counterexample(p, weights, values):
    if len(set(values)) != len(values):
        return False
    if any(x == 0 and w >= p for x, w in zip(values, weights)):
        return False
    for counts in count_choices(weights, p):
        total = sum(x*k for x, k in zip(values, counts))
        if total % p or sum(k > 0 for k in counts) <= 1:
            continue
        mean = total//p
        if mean == 0:
            return False
        after = Counter({x: w-k for x, w, k in zip(values, weights, counts) if w > k})
        after[mean] += p
        if sum(v >= p-1 for v in after.values()) >= 2:
            return False
    return True


def main():
    checks, mass_rejections, inconsistent, free, illegal = 0, 0, 0, 0, 0
    for p in (5, 7, 11):
        for n in range(3*p+1, 4*p):
            for weights in weights_for(n, p):
                menu = []
                for counts in count_choices(weights, p):
                    if sum(k > 0 for k in counts) <= 1:
                        continue
                    retained = [i for i, (w, k) in enumerate(zip(weights, counts)) if w-k >= p-1]
                    if not retained:
                        continue
                    if len(retained) >= 2:
                        row = None
                    else:
                        row = list(counts)
                        row[retained[0]] -= p
                    menu.append((counts, row))
                for z2, z3 in product(range(p), repeat=2):
                    checks += 1
                    labels, rows, rejected = (0, 1, z2, z3), [], False
                    for counts, row in menu:
                        if sum(k*z for k, z in zip(counts, labels)) % p:
                            continue
                        if row is None:
                            mass_rejections += 1
                            rejected = True
                            break
                        rows.append(((row[2], row[3]), -row[1]))
                    if rejected:
                        continue
                    try:
                        solution = solve_rows(rows, 2)
                    except AssertionError:
                        free += 1
                        continue
                    if solution is None:
                        inconsistent += 1
                        continue
                    lifts = (F(0), F(1))+solution
                    if any(x.denominator % p == 0 or x.numerator*pow(x.denominator, -1, p) % p != z
                           for x, z in zip(lifts, labels)):
                        continue
                    values = normalize(lifts, weights)
                    if values is None:
                        illegal += 1
                        continue
                    if check_counterexample(p, weights, values):
                        print('WEAK INVARIANT COUNTEREXAMPLE', p, n, weights, values)
                        print('diagnostic counts', checks, mass_rejections, inconsistent, free, illegal)
                        return
    print('bounded four-value diagnostic', checks, mass_rejections, inconsistent, free, illegal)
    print('No counterexample found; free systems and congruent anchor labels remain outside this diagnostic.')


if __name__ == '__main__':
    main()
