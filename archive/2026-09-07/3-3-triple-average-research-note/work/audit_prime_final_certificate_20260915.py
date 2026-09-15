"""Independent audit of the fixed final prime-arity certificate.

Uses only the standard library. Reconstructs each reflection from weighted
physical means rather than importing the research matrix/count functions.
Finite checks do not certify the external arithmetic-group theorems.
"""

from fractions import Fraction as F
from math import gcd, isqrt
from pathlib import Path
import json


def multiply(a, b):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))
                 for i in range(2) for j in range(2))


def inverse(a):
    d = a[0]*a[3]-a[1]*a[2]
    return tuple(F(x, d) for x in (a[3], -a[1], -a[2], a[0]))


def mean(values, weights, p):
    assert sum(weights) == p and min(weights) >= 0
    return tuple(sum(w*v[j] for w, v in zip(weights, values))/p
                 for j in range(2))


def reflection(p, s, counts):
    i, j, k, x, y, u, v = counts
    r, n = p+s, 3*p+s
    old = ((F(1), F(0)), (F(-1), F(r)), (F(0), F(-p)))
    assert min(counts) >= 0
    available = (p-2*i, p-2*j, r-2*k, p-s)
    assert min(available) >= 0
    fresh = mean(old, (i, j, k), p)
    values = old+(fresh,)
    first = mean(values, (x, y, u, v), p)
    leftover = tuple(a-b for a, b in zip(available, (x, y, u, v)))
    second = mean(values, leftover, p)
    z = tuple(-a/p for a in fresh)
    assert second == tuple(r*zz-aa for aa, zz in zip(first, z))
    actual = first+z
    integer = tuple(a*p*p for a in actual)
    assert all(a.denominator == 1 for a in integer)
    integer = tuple(int(a) for a in integer)
    alpha, beta = i-j, r*j-p*k
    assert alpha > 0 and p*(x-y)+alpha*v == beta
    assert integer == (beta, p*r*y-p*p*u+v*beta, -alpha, -beta)
    squared = multiply(actual, actual)
    assert squared[1] == squared[2] == 0 and squared[0] == squared[3] != 0
    f = squared[0]*p**3
    assert f.denominator == 1 and gcd(int(f), n) == 1
    return integer, int(f)


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


def outside_support(value, support):
    value = abs(value)
    while gcd(value, support) > 1:
        value //= gcd(value, support)
    return value


def audit_certificate():
    path = Path(__file__).with_name('large_symmetric_carrier_small_certificate.json')
    cases = json.loads(path.read_text(encoding='utf-8'))['cases']
    expected = {(p, s) for p in range(11, 307) if prime(p) for s in range(1, 10)}
    assert len(cases) == len(expected) == 522
    assert {(c['p'], c['s']) for c in cases} == expected
    rows = new_binary_units = levels = 0
    example = None
    for case in cases:
        p, s = case['p'], case['s']
        n, r = 3*p+s, p+s
        support, alpha_gcd, root_gcd = 1, 0, 0
        for pair in case['root_pairs']:
            a, f = reflection(p, s, pair[0])
            b, g = reflection(p, s, pair[1])
            rows += 2
            alpha, beta = -a[2], a[0]
            t = multiply(inverse(a), b)
            assert t == (1, F(-beta*n, f), 0, F(g, f))
            swap = (-1, r, 0, 1)
            commutator = multiply(multiply(multiply(swap, t), swap), inverse(t))
            h = 2*beta+r*alpha
            assert commutator == (1, F(n*h, g), 0, 1)
            ratio = F(g, f)
            support *= abs(ratio.numerator*ratio.denominator)
            alpha_gcd = gcd(alpha_gcd, alpha)
            root_gcd = gcd(root_gcd, h)
        if (p, s) != (11, 3):
            assert alpha_gcd == 1 and root_gcd in (1, 2, 4)
            modulus = n**4*(64 if n % 2 == 0 else 1)
            assert modulus % ((root_gcd*n)**2) == 0
            levels += 1
        for q in range(2, p+1):
            if gcd(q, n) == 1:
                support *= q
        if case['binary_unit']:
            pair = case['binary_unit']
            a, f = reflection(p, s, pair[0])
            b, g = reflection(p, s, pair[1])
            rows += 2
            assert pair[0][:3] == pair[1][:3] and pair[0][6] == pair[1][6]
            t = multiply(inverse(a), b)
            assert t[0] == 1 and t[2] == 0 and t[3] == F(g, f)
            ratio = F(g, f)
            assert gcd(ratio.numerator*ratio.denominator, n) == 1
            assert (ratio-1).numerator % 8 == 4
            remaining = outside_support(ratio.numerator*ratio.denominator, support)
            if remaining != 1:
                new_binary_units += 1
                if example is None:
                    example = (p, s, str(ratio), remaining)
            # Both t and its inverse are genuine reflection words. Their upper
            # root conjugations therefore extend the coefficient ring by the
            # reduced ratio and its inverse, including this additional support.
        direction = [reflection(p, s, c)[0] for c in case['direction']]
        rows += 2
        assert -direction[1][2] == 1-direction[0][2]
        matrix = multiply(direction[0], direction[1])
        trace = matrix[0]+matrix[3]
        determinant = matrix[0]*matrix[3]-matrix[1]*matrix[2]
        if n % 2 == 0:
            assert trace % 4 == 2
        if n % 3 == 0:
            c = (trace*trace-4*determinant)*pow(trace*trace, -1, 9) % 9
            assert c in (0, 3)
    print('independent physical-mean certificate audit: PASS', len(cases), rows)
    print('ordinary principal-level divisibility: PASS', levels)
    print('binary ratios needing additional legitimate localization:', new_binary_units)
    print('first extra unit example:', example)


def audit_auxiliary_13():
    a = (-27, 568, -2, 27)
    b = (-27, 172, -2, 27)
    t = multiply(inverse(a), b)
    d = tuple(x/t[3] for x in multiply(t, t))
    j, f = reflection(11, 3, (4, 1, 6, 2, 7, 1, 1))
    assert f == -1
    e = multiply(multiply(j, d), inverse(j))

    def mod(matrix, modulus):
        return tuple(F(x).numerator*pow(F(x).denominator, -1, modulus) % modulus
                     for x in matrix)

    generators = (mod(d, 13), mod(e, 13))
    identity = (1, 0, 0, 1)
    reached, queue = {identity}, [identity]
    for current in queue:
        for generator in generators:
            nxt = tuple(x % 13 for x in multiply(current, generator))
            if nxt not in reached:
                reached.add(nxt)
                queue.append(nxt)
    assert len(reached) == 13*(13*13-1)
    assert mod(d, 36) == mod(e, 36) == identity
    print('independent auxiliary13 full group: PASS', len(reached))


if __name__ == '__main__':
    if not __debug__:
        raise RuntimeError('Assertions are required.')
    audit_certificate()
    audit_auxiliary_13()
