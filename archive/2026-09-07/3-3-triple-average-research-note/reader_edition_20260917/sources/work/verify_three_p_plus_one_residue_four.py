"""Analytic n=3p+1 completion for primes p=4 mod9.

Fixed original-position words, exact affine roots and local transports.
Auxiliary-prime removal uses a written perfect-versus-solvable quotient lemma,
not finite group enumeration or word search.
"""
from fractions import Fraction as F
from functools import cache
from math import gcd
from random import Random

from verify_four_prime_entry_and_band import factors, Ledger
from verify_uniform_odd_middle_cores import mm, invq, residue, bezout
from verify_upper_band_unrestricted_completion import (
    scale, det, zy, apply_mod, local_cycle_hit, pure_prime_order)
from verify_even_odd_half_core import I, U, mod_power, crt_pairs, principal_unit_log, valuation
from verify_upper_band_descent_boundary import apply_return


def comm(a, b):
    return mm(mm(mm(a, b), invq(a)), invq(b))


def carrier_inverse(ledger, groups, p):
    a, b, c = (list(group) for group in groups)
    j, cap = (p-1)//3, (2*p+1)//3
    fresh = a[:2*j]+b[:j]+c
    ledger.average(fresh)
    a, b = a[2*j:], b[j:]
    kept, fresh = fresh[:1], fresh[1:]
    left = a[:cap]+fresh[:j]
    right = a[cap:]+fresh[j:2*j]
    other = b+fresh[2*j:]
    assert sorted(left+right+other+kept) == list(range(3*p+1))
    for group in (left, right, other):
        ledger.average(group)
    return [left+right, other, kept]


@cache
def data(p):
    assert p >= 13 and p % 9 == 4 and factors(p) == {p: 1}
    n, j, k = 3*p+1, (p-1)//3, (2*p+1)//9
    cap = 3*k
    f = (1, j, 0, p)
    b = (1, j, 2, -1)
    a = (p-3*k, k, -1, 0)
    a1 = (p-3, 1, -1, 0)
    j0 = mm(f, a)
    assert j0 == (0, k, -p, 0)
    assert mm(j0, j0) == scale(I, -p*k)
    assert mm(b, b) == scale(I, cap)
    assert gcd(p*cap, n) == 1
    h = mm(mm(mm(a, f), b), invq(a))
    assert h == (-p, -j*(cap+p)-2*p*k, 0, cap)
    upper = comm(f, h)
    assert upper == U(F(n*(p-1), 2*p+1))
    assert mm(mm(j0, U(1)), invq(j0)) == (1, 0, F(-p, k), 1)
    initial_level = (n*(p-1))**2
    final_level = 2**(2*valuation(p-1, 2))*n*n
    auxiliaries = [ell for ell in factors(p-1) if ell not in (2, 3) and cap % ell]
    for ell in auxiliaries:
        e = 2*valuation(p-1, ell)
        x = mod_power(a1, 2, ell*ell)
        assert tuple(residue(z, ell) for z in a1) == (ell-2, 1, ell-1, 0)
        v, w = (1, 1), (residue(k, ell), -1 % ell)
        assert (v[0]*w[1]-v[1]*w[0]) % ell
        lifted = mod_power(x, ell, ell*ell)
        assert lifted != I and tuple(z % ell for z in lifted) == I
        # Check the integral reduction and local-quotient interfaces.
        conjugate = mm(mm(j0, a1), invq(j0))
        assert det(conjugate) == 1
        assert all(gcd(F(z).denominator, ell) == 1 for z in conjugate)
    c = (0, 1, 1, p)
    for generator in (a1, mm(mm(j0, a1), invq(j0))):
        image = mm(mm(c, generator), invq(c))
        assert residue(image[2], n) == 0
    assert initial_level % final_level == 0
    return n, j, k, cap, f, b, a, j0, initial_level, final_level, auxiliaries


def unit_lift(p, wanted):
    n = 3*p+1
    q = wanted % n
    multiplier = F(1)
    if 2*q > n:
        q, multiplier = n-q, -multiplier
    while 4*q > n:
        if 3*q < n:
            multiplier = -3*multiplier
            q = n-3*q
        else:
            multiplier *= 3
            q = 3*q-n
    assert 1 <= q <= p and gcd(q, n) == 1
    unit = F(q)/multiplier
    assert residue(unit, n) == wanted % n
    return unit


def direction_transport(p, pair):
    n, j, k, cap, f, b, a, j0, old, level, auxiliaries = data(p)
    t = 1 if p % 4 == 1 else 3
    at = scale(zy((p-3*t, t, -1, 0), p), F(1, p))
    assert residue(at[0]+at[3], 4) == 2
    e2 = valuation(level, 2)
    two = 2**e2
    k2 = local_cycle_hit(at, 2, e2, pair)
    pair = apply_mod(mod_power(at, k2, level), pair, level)
    v = zy(comm(f, b), p)
    assert tuple(residue(z, n) for z in v) == (
        1, residue(F(2*(1-p), p), n), 0, 1)
    assert tuple(residue(z, 2) for z in v) == I
    order2 = pure_prime_order(v, 2, e2)
    exponents = [(0, order2)]
    for ell, e in factors(n).items():
        if ell == 2:
            continue
        assert ell >= 5
        exponents.append((local_cycle_hit(v, ell, 2*e, pair), ell**(2*e)))
    pair = apply_mod(mod_power(v, crt_pairs(exponents), level), pair, level)
    assert pair[0] == 0 and gcd(pair[1], level) == 1
    return pair


def scale_transport(p, target):
    n, j, k, cap, f, b, a, j0, old, level, auxiliaries = data(p)
    first = unit_lift(p, target % n)
    residual = target*pow(residue(first, level), -1, level) % level
    k0, k1 = F(-3*p), F(cap, p*p)
    assert k0 == 1-n and k1 == 1-F(n*j, p*p)
    if n % 4 == 2:
        assert valuation(p-1, 2) == 1
        flag = int(residual % 4 != 1)
        residual = residual*pow(residue(k0, level), -flag, level) % level
        base, start = k1, 2*n
    else:
        flag, base, start = 0, k0, n
    exponent = principal_unit_log(base, residual, level, start, False)
    lifted = residue(first, level)*pow(residue(k0, level), flag, level)
    lifted *= pow(residue(base, level), exponent, level)
    assert lifted % level == target
    z, y = level, level+1
    _, alpha, beta = bezout(z, y)
    shift = -alpha*pow(y, -1, level) % level
    alpha, beta = alpha+shift*y, beta-shift*z
    matrix = (y, -z, alpha, beta)
    assert det(matrix) == 1 and tuple(value % level for value in matrix) == I
    assert (matrix[0]*z+matrix[1]*y, matrix[2]*z+matrix[3]*y) == (0, 1)


def physical(p):
    n, j, k, cap, f, b, a, j0, old, level, auxiliaries = data(p)
    count = 0
    for aa, zz in ((1, 0), (0, 1)):
        raw = [aa]*(2*p)+[-2*aa+zz]*p+[-p*zz]
        ledger = Ledger(raw, p)
        groups = [list(range(2*p)), list(range(2*p, 3*p)), [3*p]]
        groups = carrier_inverse(ledger, groups, p)
        expected_a = F(cap*(p*aa-j*zz), p*p)
        expected_z = F(cap*zz, p*p)
        assert all(ledger.state[index] == value
                   for group, value in zip(groups, (expected_a, -2*expected_a+expected_z, -p*expected_z))
                   for index in group)
        groups = apply_return(ledger, groups, "C", j, 0)
        scalar = F(cap, p*p)
        assert all(ledger.state[index] == value for group, value in zip(
            groups, (scalar*aa, scalar*(-2*aa+zz), -scalar*p*zz)) for index in group)
        ledger.independent_replay(raw)
        count += 1
        ledger = Ledger(raw, p)
        groups = [list(range(2*p)), list(range(2*p, 3*p)), [3*p]]
        for _ in range(2):
            groups = apply_return(ledger, groups, "A", k, 0)
            groups = apply_return(ledger, groups, "C", j, 0)
        scalar = F(-k, p**3)
        assert all(ledger.state[index] == value for group, value in zip(
            groups, (scalar*aa, scalar*(-2*aa+zz), -scalar*p*zz)) for index in group)
        ledger.independent_replay(raw)
        count += 1
        ledger = Ledger(raw, p)
        groups = [list(range(2*p)), list(range(2*p, 3*p)), [3*p]]
        for _ in range(2):
            groups = apply_return(ledger, groups, "B", j, 0)
        scalar = F(cap, p*p)
        assert all(ledger.state[index] == value for group, value in zip(
            groups, (scalar*aa, scalar*(-2*aa+zz), -scalar*p*zz)) for index in group)
        ledger.independent_replay(raw)
        count += 1
    return count


def main():
    rng = Random(2026091509)
    systems = literal = units = lifts = aux = 0
    for p in range(13, 1000, 9):
        if factors(p) != {p: 1}:
            continue
        record = data(p)
        systems += 1
        aux += len(record[-1])
        if p <= 103:
            literal += physical(p)
        for u in range(1, record[0]):
            if gcd(u, record[0]) == 1:
                unit_lift(p, u)
                units += 1
        for _ in range(6):
            y = rng.randrange(1, 10**8)
            if gcd(y, record[0]) != 1:
                y = 1
            pair = direction_transport(p, (rng.randrange(-10**8, 10**8), y))
            scale_transport(p, pair[1])
            lifts += 1
    print("3p+1 residue4mod9 fixed controller systems: PASS", systems)
    print("3p+1 residue4mod9 literal positive inverse cycles: PASS", literal)
    print("3p+1 residue4mod9 perfect-solvable local interfaces: PASS", aux)
    print("3p+1 residue4mod9 complete unit representatives: PASS", units)
    print("3p+1 residue4mod9 direction-scale terminal transports: PASS", lifts)
    print("3p+1 residue4mod9 completion interfaces: PASS")


if __name__ == "__main__":
    main()

