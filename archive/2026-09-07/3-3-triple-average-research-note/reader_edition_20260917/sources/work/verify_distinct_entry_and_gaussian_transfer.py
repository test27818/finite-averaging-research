"""Distinct-value integer entry and transfer limits of old ternary proofs.

Bounded exact constructions only. Gaussian cycles are checked on complete
coefficient bases using original-position p-averages; no macro search.
"""

from collections import Counter
from fractions import Fraction as F
from math import gcd, isqrt
from pathlib import Path
import json

if not __debug__:
    raise RuntimeError('Assertions are required.')

ROOT = Path(__file__).resolve().parent


def prime(n):
    return n >= 2 and all(n % q for q in range(2, isqrt(n)+1))


def factors(n):
    result, q = [], 2
    while q*q <= n:
        if n % q == 0:
            result.append(q)
            while n % q == 0:
                n //= q
        q += 1
    return result+([n] if n > 1 else [])


def multiply(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def identity(r):
    return [[int(i == j) for j in range(r)] for i in range(r)]


def determinant(matrix):
    # Fraction-free Bareiss elimination keeps the integer matrices small.
    a, sign, previous = [row[:] for row in matrix], 1, 1
    n = len(a)
    for k in range(n-1):
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        v = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                numerator = a[i][j]*v-a[i][k]*a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator//previous
            a[i][k] = 0
        previous = v
    return sign*a[-1][-1]


def distinct_step(raw, k):
    n = len(raw)
    qs = [q for q in factors(n) if k % q]
    assert n > 2*k and sum(raw) == 0
    assert all(len({x % q for x in raw}) > 1 for q in qs)
    representatives = {}
    for i, x in enumerate(raw):
        representatives.setdefault(x, i)
    assert len(representatives) >= len(qs)+2*k-1
    protected_values = set()
    for q in qs:
        counts = Counter(x % q for x in raw)
        major = next((a for a, f in counts.items() if f >= n-k), None)
        if major is not None:
            protected_values.add(next(x for x in raw if x % q != major))
    pool = [i for x, i in representatives.items() if x not in protected_values][:2*k-1]
    dp = [{} for _ in range(k+1)]
    dp[0][0] = ()
    for i in pool:
        for size in range(k, 0, -1):
            for residue, group in dp[size-1].items():
                dp[size].setdefault((residue+raw[i]) % k, group+(i,))
    group = dp[k][0]
    assert len(group) == len(set(group)) == len({raw[i] for i in group}) == k
    result = list(map(F, raw))
    mean = sum(result[i] for i in group)/k
    assert mean.denominator == 1
    for i in group:
        result[i] = mean
    assert sum(result) == 0
    assert sum(x*x for x in result) < sum(x*x for x in raw)
    assert all(len({x % q for x in result}) > 1 for q in qs)
    return {'k': k, 'n': n, 'input': raw, 'protected_values': sorted(protected_values),
            'group_1based': [i+1 for i in group], 'mean': str(mean)}


def orbits(p, ell):
    assert prime(p) and prime(ell) and p % 2 and (ell-1) % p == 0
    omega = next(pow(a, (ell-1)//p, ell) for a in range(2, ell)
                 if pow(a, (ell-1)//p, ell) != 1)
    H = {pow(omega, j, ell) for j in range(p)}
    assert len(H) == p
    remaining, groups = set(range(1, ell)), []
    while remaining:
        a = min(remaining)
        group = sorted(a*h % ell for h in H)
        groups.append(group)
        remaining.difference_update(group)
    lookup = {x: i for i, group in enumerate(groups) for x in group}
    return sorted(H), groups, lookup


def layer_matrix(p, ell, c, groups, lookup):
    r = len(groups)
    result = [[0]*r for _ in range(r)]
    for i, group in enumerate(groups):
        for x in group:
            source = (x+c) % ell
            if source:
                result[i][lookup[source]] += 1
            else:
                result[i] = [value-p for value in result[i]]
    return result


def cycle(p, ell):
    H, groups, lookup = orbits(p, ell)
    r = len(groups)
    K = layer_matrix(p, ell, 1, groups, lookup)
    Km = layer_matrix(p, ell, ell-1, groups, lookup)
    B = multiply(Km, K)
    for i in range(r):
        B[i][i] -= 1
    norm = determinant(K)
    unit_test = determinant(B)
    product = identity(r)
    locations = list(range(ell))
    physical = [tuple(F(-p) for _ in range(r))]
    physical += [tuple(F(i == lookup[x]) for i in range(r)) for x in range(1, ell)]
    word = []
    for orbit in groups:
        c = orbit[0]
        matrix = layer_matrix(p, ell, c, groups, lookup)
        product = multiply(matrix, product)
        for block in groups:
            indices = [locations[(x+c) % ell] for x in block]
            assert len(indices) == len(set(indices)) == p
            value = tuple(sum(physical[i][j] for i in indices)/p for j in range(r))
            for i in indices:
                physical[i] = value
            word.append([i+1 for i in indices])
        locations = [locations[(x+c) % ell] for x in range(ell)]
    assert product == [[norm*int(i == j) for j in range(r)] for i in range(r)]
    assert 0 < norm < p**r and norm % ell == pow(p, r, ell)
    scale = F(norm, p**r)
    for x in range(ell):
        expected = tuple(scale*(-p if x == 0 else int(j == lookup[x])) for j in range(r))
        assert physical[locations[x]] == expected
    assert len(word) == r*r
    if p == 3:
        assert unit_test == 1
    return {'p': p, 'ell': ell, 'leaf_count': r, 'subgroup': H,
            'period_norm': norm, 'physical_scale': str(scale),
            'det_Kminus_K_minus_I': unit_test, 'operations': word}


def main():
    entries = []
    for k in (2, 3, 4, 5, 7, 11):
        n = 2*k+12
        raw = list(range(0, 2*(n-2), 2))+[1]
        raw.append(-sum(raw))
        entries.append(distinct_step(raw, k))
    print('distinct-value safe integer entry general arity: PASS', len(entries))
    cycles = [cycle(p, ell) for p, ell in ((3, 7), (3, 19), (5, 11), (5, 31), (7, 29), (7, 43))]
    for record in cycles:
        print('Gaussian transfer:', record['p'], record['ell'], record['leaf_count'],
              record['period_norm'], record['det_Kminus_K_minus_I'])
    example = next(x for x in cycles if (x['p'], x['ell']) == (5, 11))
    assert example['det_Kminus_K_minus_I'] == 4
    print('general Gaussian global positive cycles and ternary unit boundary: PASS', len(cycles))
    capacities = 0
    for p in range(3, 100):
        if not prime(p):
            continue
        assert not any(prime(n) and (n-1) % p == 0 for n in range(3*p+1, 4*p))
        for n in range(2*p+1, 4*p):
            for a in range(2, isqrt(n)+1):
                if n % a == 0:
                    assert a < 2*p and n//a < 2*p
                    capacities += 1
    print('critical band split-prime and factor capacity boundaries: PASS', capacities)
    (ROOT/'distinct_entry_gaussian_transfer_records.json').write_text(json.dumps({
        'scope': 'Safe entry and Gaussian scalar cycles only; no p-averaging prime/composite closure or root generation claim.',
        'distinct_value_entries': entries, 'gaussian_cycles': cycles}, indent=2)+'\n', encoding='utf-8')
    print('distinct-value entry and historical-route transfer: PASS')


if __name__ == '__main__':
    main()
