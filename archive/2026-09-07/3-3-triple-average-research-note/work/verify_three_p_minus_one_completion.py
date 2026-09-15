"""All-prime n=3p-1 completion, including five-average fourteen.

Fixed overlapping reflections, exact affine commutators, modular digit lifts,
and original-position returns. No word discovery or finite orbit search.
"""
from fractions import Fraction as F
from functools import cache
from math import gcd
from pathlib import Path
from random import Random
import json

from verify_four_prime_entry_and_band import Ledger, factors
from verify_uniform_odd_middle_cores import mm, invq, residue, bezout, normalize_pair
from verify_upper_band_unrestricted_completion import (
    scale, det, zy, apply_mod, local_cycle_hit, pure_prime_order)
from verify_even_odd_half_core import I, U, L, mod_power, valuation, crt_pairs, principal_unit_log

if not __debug__:
    raise RuntimeError("Assertions are required.")


def comm(a, b):
    return mm(mm(mm(a, b), invq(a)), invq(b))


def reflection(p, sigma, h):
    n, r = 3*p-1, p-1
    x, y, c = h-sigma, h, p+sigma-2*h
    assert min(x, y, c) >= 0 and x <= sigma and y <= p and c <= r-sigma
    f = p**3-n*(p-sigma)*h
    matrix = (-p*sigma, p*(n*h-p*(p+sigma)), -(p-sigma), p*sigma)
    assert mm(matrix, matrix) == scale(I, p*f)
    assert gcd(f, n*p) == 1
    return matrix, f


def overlapping_return(ledger, groups, sigma, h):
    a, b, c = (list(g) for g in groups)
    p, r = ledger.p, len(c)
    fresh = a[:p-sigma]+c[:sigma]
    ledger.average(fresh)
    a, c = a[p-sigma:], c[sigma:]
    kept, fresh = fresh[:r], fresh[r:]
    x, y, u = h-sigma, h, p+sigma-2*h
    selected = a[:x]+b[:y]+c[:u]
    other = a[x:]+b[y:]+c[u:]+fresh
    assert sorted(selected+other+kept) == list(range(2*p+r))
    for g in (selected, other):
        ledger.average(g)
    return [selected, other, kept]


def carrier_return(ledger, groups, t):
    a, b, c = (list(g) for g in groups)
    p = ledger.p
    j = (p-t)//2
    assert p-t == 2*j and 0 <= j <= p
    left, right = a[:p-j]+b[:j], a[p-j:]+b[j:]
    ledger.average(left)
    ledger.average(right)
    return [left, right, c]


@cache
def general(p):
    assert p >= 7 and factors(p) == {p: 1}
    n, r = 3*p-1, p-1
    d = p*p-3*p+1
    a, s = (0, -d, -1, 0), (-1, r, 0, 1)
    fs, roots, ratios = {}, [], {}
    for sigma, h in ((2, 3), (3, 4)):
        j, f = reflection(p, sigma, h)
        j1, f1 = reflection(p, sigma, h+1)
        assert gcd(f, f1) == 1
        affine = mm(invq(j), j1)
        assert affine == (1, F(-p*sigma*n, f), 0, F(f1, f))
        c = n*sigma-r*p
        root = comm(s, affine)
        assert root == U(F(n*c, f1))
        roots.append(c)
        fs[sigma] = (f, f1)
        ratios[sigma] = F(f1, f)
    assert gcd(*roots) == 2
    assert mm(mm(a, U(d*2*n)), invq(a)) == L(2*n)
    v = scale(zy(mm(reflection(p, 3, 4)[0], a), p), F(1, p**3))
    assert tuple(residue(x, n) for x in v) == (1, residue(F(-3, p*p), n), 0, 1)
    assert v[0]+v[3] == 2-F(n*(5*p-3), p**3)
    assert residue(v[0]+v[3], 4) == 2
    assert n % 3
    return n, r, d, a, s, fs, ratios, v


def odd_unit_lift(p, wanted):
    n = 3*p-1
    b = wanted % n
    sign = 1
    if 2*b > n:
        b, sign = n-b, -1
    exponent = 0
    while 4*b > n:
        if 3*b < n:
            sign = -sign
        b = abs(n-3*b)
        exponent += 1
    assert 1 <= b <= p and b % 2 and gcd(b, n) == 1
    unit = sign*F(b, 3**exponent)
    assert residue(unit, n) == wanted % n
    return unit


def principal_scale(p, target, modulus):
    n, _, _, _, _, _, ratios, _ = general(p)
    k2, k3 = ratios[2], ratios[3]
    assert target % n == 1
    e = valuation(modulus, 2)
    two = 2**e
    odd = modulus//two
    flag = 0
    if n % 4 == 2:
        flag = int(target % 4 != 1)
        target = target*pow(residue(k2, modulus), -flag, modulus) % modulus
        base2, start2 = k3, 4
    else:
        base2, start2 = k2, 2**valuation(n, 2)
    exponent2 = principal_unit_log(base2, target, two, start2, False)
    residual = target*pow(residue(base2, modulus), -exponent2, modulus) % modulus
    assert residual % two == 1
    order2 = pure_prime_order((k3, 0, 0, k3), 2, e)
    # Do not expand the exact rational k3**order2.
    base_odd = pow(residue(k3, odd), order2, odd)
    exponent_odd = principal_unit_log(base_odd, residual, odd, n//2**valuation(n, 2), False)
    result = pow(residue(k2, modulus), flag, modulus)
    result *= pow(residue(base2, modulus), exponent2, modulus)
    result *= pow(residue(k3, modulus), order2*exponent_odd, modulus)
    return result % modulus


def exact_fiber(p, level):
    # Primitive reduction is explicit; determinants need only be local units.
    denominator = p*p-3*p+1
    rational_pair = (F(level, denominator), F(level+1, denominator))
    z, y = normalize_pair(*rational_pair)
    assert gcd(z, y) == 1 and z % level == 0 and y % level == 1
    _, alpha, beta = bezout(z, y)
    shift = -alpha*pow(y, -1, level) % level
    alpha, beta = alpha+shift*y, beta-shift*z
    matrix = (y, -z, alpha, beta)
    assert det(matrix) == 1 and tuple(x % level for x in matrix) == I
    assert (matrix[0]*z+matrix[1]*y, matrix[2]*z+matrix[3]*y) == (0, 1)


def general_transport(p, pair):
    n, _, _, _, _, _, _, v = general(p)
    modulus = 4*n*n
    local = [(local_cycle_hit(v, ell, e, pair), ell**e)
             for ell, e in factors(modulus).items()]
    pair = apply_mod(mod_power(v, crt_pairs(local), modulus), pair, modulus)
    assert pair[0] == 0 and gcd(pair[1], modulus) == 1
    unit = odd_unit_lift(p, pair[1] % n)
    target = pair[1]*pow(residue(unit, modulus), -1, modulus) % modulus
    correction = principal_scale(p, target, modulus)
    assert residue(unit, modulus)*correction % modulus == pair[1]
    exact_fiber(p, modulus)


def physical(p):
    n, r = 3*p-1, p-1
    parameters = ((1, 2),) if p == 5 else ((2, 3), (2, 4), (3, 4), (3, 5))
    count = 0
    for sigma, h in parameters:
        matrix, f = reflection(p, sigma, h)
        for a, z in ((1, 0), (0, 1)):
            raw = [a]*p+[r*z-a]*p+[-p*z]*r
            ledger = Ledger(raw, p)
            groups = [list(range(p)), list(range(p, 2*p)), list(range(2*p, n))]
            groups = overlapping_return(ledger, groups, sigma, h)
            aa, zz = F(matrix[0]*a+matrix[1]*z, p*p), F(matrix[2]*a+matrix[3]*z, p*p)
            assert all(ledger.state[index] == value for group, value in zip(
                groups, (aa, -aa+r*zz, -p*zz)) for index in group)
            groups = overlapping_return(ledger, groups, sigma, h)
            scalar = F(f, p**3)
            assert all(ledger.state[index] == value for group, value in zip(
                groups, (scalar*a, scalar*(-a+r*z), -scalar*p*z)) for index in group)
            ledger.independent_replay(raw)
            count += 1
    for t in (1, 3):
        for a, z in ((1, 0), (0, 1)):
            raw = [a]*p+[r*z-a]*p+[-p*z]*r
            ledger = Ledger(raw, p)
            groups = [list(range(p)), list(range(p, 2*p)), list(range(2*p, n))]
            groups = carrier_return(ledger, groups, t)
            aa = F(t*a+r*(p-t)*z//2, p)
            assert all(ledger.state[index] == value for group, value in zip(
                groups, (aa, -aa+r*z, -p*z)) for index in group)
            ledger.independent_replay(raw)
            count += 1
    return count


def five_system():
    p, n = 5, 14
    a, s = (0, -11, -1, 0), (-1, 4, 0, 1)
    j, f = reflection(p, 1, 2)
    w = mm(mm(mm(mm(a, s), a), s), j)
    assert w == (-121, 330, 0, 65) and f == 13
    assert gcd(121, 65) == 1 and comm(s, w) == U(F(84, 65))
    c3 = (3, -4, 0, 1)
    h = scale(mm(mm(c3, j), c3), F(1, 3))
    assert all(F(x).denominator == 1 for x in h) and det(h) == det(j)
    assert det(mm(h, invq(j))) == 1
    assert mm(mm(j, c3), invq(h)) == scale(invq(c3), 3)
    level = 28**2
    v = scale(zy(mm(j, a), p), F(1, 125))
    assert tuple(residue(x, n) for x in v) == (1, residue(F(-1, 25), n), 0, 1)
    assert residue(v[0]+v[3], 4) == 2
    units = (15, 10725, 2145)
    assert [(u % 16, u % 7) for u in units] == [(15, 1), (5, 1), (1, 3)]
    lam = F(-121, 65)
    kernel = lam*lam
    assert residue(kernel, 16) == 1 and valuation(abs((kernel-1).numerator), 7) == 1
    return level, v, units, kernel


def five_unit(target):
    level, _, (sign, generator2, generator7), kernel = five_system()
    target %= level
    a, b = next((a, b) for a in range(2) for b in range(4)
                if pow(sign, a, 16)*pow(generator2, b, 16) % 16 == target % 16)
    c = next(c for c in range(6) if pow(generator7, c, 7) == target % 7)
    base = sign**a*generator2**b*generator7**c
    remainder = target*pow(base, -1, level) % level
    assert remainder % 112 == 1
    coefficient = ((residue(kernel, 49)-1)//7) % 7
    power = ((remainder % 49-1)//7)*pow(coefficient, -1, 7) % 7
    assert base*pow(residue(kernel, level), power, level) % level == target
    return [a, b, c, power]


def main():
    rng = Random(2026091514)
    systems = directions = units = literal = 0
    for p in range(7, 250):
        if factors(p) != {p: 1}:
            continue
        n = general(p)[0]
        systems += 1
        for wanted in range(1, n):
            if gcd(wanted, n) == 1:
                odd_unit_lift(p, wanted)
                units += 1
        for _ in range(4):
            pair = (rng.randrange(-10**8, 10**8), 1+n*rng.randrange(10000))
            general_transport(p, pair)
            directions += 1
        if p <= 23:
            literal += physical(p)
    literal += physical(5)
    level, matrix, _, _ = five_system()
    unit_certificates = {str(u): five_unit(u) for u in range(level) if gcd(u, level) == 1}
    for _ in range(12):
        pair = (rng.randrange(-10**8, 10**8), 1+14*rng.randrange(10000))
        local = [(local_cycle_hit(matrix, ell, e, pair), ell**e)
                 for ell, e in factors(level).items()]
        final = apply_mod(mod_power(matrix, crt_pairs(local), level), pair, level)
        assert final[0] == 0
        five_unit(final[1])
        exact_fiber(5, level)
    print("three-p-minus-one uniform reflections and roots: PASS", systems)
    print("three-p-minus-one complete odd unit representatives: PASS", units)
    print("three-p-minus-one direction-scale and exact-fiber checks: PASS", directions)
    print("three-p-minus-one literal original-position returns: PASS", literal)
    print("five-average fourteen inverse sandwich and unit generators: PASS", len(unit_certificates))
    print("five-average fourteen exact terminal interfaces: PASS 12")
    print("all-prime three-p-minus-one completion: PASS")
    Path(__file__).with_name("three_p_minus_one_completion_records.json").write_text(
        json.dumps({"five_level": level, "five_unit_exponents": unit_certificates,
                    "general_systems": systems, "scope": "Exact formulas and local lifts; not full arithmetic-group word extraction."},
                   indent=2)+"\n", encoding="utf-8")


if __name__ == "__main__":
    main()

