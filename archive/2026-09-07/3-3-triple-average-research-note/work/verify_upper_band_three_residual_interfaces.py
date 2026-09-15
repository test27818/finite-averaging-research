"""The same affine-minor and congruence-lifting interface for three residual pairs."""
from fractions import Fraction as F
from math import gcd
from random import Random

from verify_four_prime_entry_and_band import factors, Ledger
from verify_uniform_odd_middle_cores import mm, invq, residue
from verify_upper_band_unrestricted_completion import (
    scale, det, zy, apply_mod, local_cycle_hit, pure_prime_order)
from verify_upper_band_small_prime_interface import unit_lift
from verify_upper_band_descent_boundary import apply_return
from verify_four_p_tail_completion import safe_a, interval_units, phi
from verify_even_odd_half_core import I, U, L, mod_power, crt_pairs, principal_unit_log, valuation

CASES = ((13, 11, 3, 3, 4, 17, 4),
         (13, 12, 3, 3, 4, 14, 3),
         (17, 15, 4, 4, 5, 25, 6))

if not __debug__:
    raise RuntimeError("Assertions are required.")


def add_identity(matrix):
    return tuple(x+y for x, y in zip(I, matrix))


def overlap(ledger, groups, sigma, h):
    p = ledger.p
    a, b, c = (list(g) for g in groups)
    r = len(c)
    new = a[:p-sigma]+c[:sigma]
    ledger.average(new)
    a, c = a[p-sigma:], c[sigma:]
    kept, new = new[:r], new[r:]
    x, y, u = 2*h-sigma, h, p+sigma-3*h
    assert min(x, y, u) >= 0
    assert 2*x <= len(a) and 2*y <= len(b) and 2*u <= len(c)
    left, right = a[:x]+b[:y]+c[:u], a[x:2*x]+b[y:2*y]+c[u:2*u]
    other = a[2*x:]+b[2*y:]+c[2*u:]+new
    assert sorted(left+right+other+kept) == list(range(3*p+r))
    for group in (left, right, other):
        ledger.average(group)
    return [left+right, other, kept]


def system(case):
    p, r, ja, h1, h3, q, jq = case
    n = 3*p+r
    d = p*p-n*ja
    a = (0, -d, -1, 0)
    assert (2*p-r+5)//6 <= ja <= min((2*p-r)//4, p//3)
    families = []
    for sigma, h in ((1, h1), (3, h3)):
        fs, matrices = [], []
        for hh in (h, h+1):
            x, u = 2*hh-sigma, p+sigma-3*hh
            assert x >= 0 and u >= 0 and 2*x <= p+sigma and 2*hh <= p and 2*u <= r-sigma
            f = p**3-n*(p-sigma)*hh
            j = (-p*sigma, p*(n*hh-p*(p+sigma)), -(p-sigma), p*sigma)
            assert mm(j, j) == scale(I, p*f) and gcd(f, n*p*2) == 1
            fs.append(f)
            matrices.append(j)
        assert gcd(*fs) == 1
        t = mm(invq(matrices[0]), matrices[1])
        assert t == (1, F(-p*sigma*n, fs[0]), 0, F(fs[1], fs[0]))
        families.append((sigma, h, fs, matrices, t))
    t1, t3 = families[0][4], families[1][4]
    comm = mm(mm(mm(t1, t3), invq(t1)), invq(t3))
    assert comm == U(F(-2*p*p*n*n, families[0][2][1]*families[1][2][1]))
    assert mm(mm(a, U(d*2*p*p*n*n)), invq(a)) == L(2*p*p*n*n)

    # Two-level local-p saturation, checked without enumerating SL2(Z/p^4).
    m = 4*n**4
    j1, f = families[0][3][0], families[0][2][0]
    nilpotent = (p*(p-1), -p*p, (p-1)**2, -p*(p-1))
    e = mm(mm(j1, U(p*p*m*d)), invq(j1))
    assert e == add_identity(scale(nilpotent, F(p*m*d, f)))
    e2 = mm(mm(a, e), invq(a))
    assert all(gcd(F(x).denominator, p*m) == 1 for x in e+e2)
    basis = (p, -d*(p-1), p-1, -p)
    delta = det(basis)
    assert gcd(delta, p) == 1
    assert mm(mm(invq(basis), e), basis) == U(F(-p*m*d*delta, f))
    assert mm(mm(invq(basis), e2), basis) == L(F(-p*m*delta, f))
    coefficient = f*pow(d*d, -1, p) % p
    corrected = add_identity(scale(tuple(x-y for x, y in zip(e2, I)), coefficient))
    assert tuple(residue(x, p*p) for x in corrected) == tuple(residue(x, p*p) for x in U(p*m))
    assert tuple(residue(x, m) for x in corrected) == I
    final_e = mm(mm(j1, U(p*m*d)), invq(j1))
    final_e2 = mm(mm(a, final_e), invq(a))
    assert mm(mm(invq(basis), final_e), basis) == U(F(-m*d*delta, f))
    assert mm(mm(invq(basis), final_e2), basis) == L(F(-m*delta, f))
    assert tuple(residue(x, m) for x in final_e+final_e2) == I+I

    modulus = m
    if n % 2:
        assert d == 16
        assert mm(mm(a, U(d*n**4)), invq(a)) == L(n**4)
        rotation = t1
        basis2 = (0, rotation[1], 1, rotation[3])
        assert residue(det(basis2), 2) == 1
        for v in (L(n**4), mm(mm(rotation, L(n**4)), invq(rotation))):
            assert tuple(residue(x, n**4) for x in v) == I
        first = mm(mm(invq(basis2), L(n**4)), basis2)
        second = mm(mm(mm(mm(invq(basis2), rotation), L(n**4)), invq(rotation)), basis2)
        assert first[0] == first[3] == second[0] == second[3] == 1
        assert first[2] == second[1] == 0
        assert residue(first[1], 2) == residue(second[2], 2) == 1
        modulus = n**4

    low, high = r//2+(2 if r % 2 == 0 else 5), 3*(p//2)+r//2
    count = interval_units(low, high, tuple(factors(n)))
    assert 4*count > phi(n)
    d0 = n*jq-p*q
    d1 = d0+n
    assert gcd(d0, d) == 1 and gcd(d0*d1, n) == 1
    for j in (jq, jq+1):
        s = q-3*j
        assert s >= 0 and 2*s <= r and 2*j <= p and 0 <= 2*(p-j-s) <= 2*p-r
    delta_a, kappa = F(d1, d0), F(families[1][2][1], families[1][2][0])
    if n % 2 == 0:
        assert residue(delta_a, 4) == 3 and residue(kappa, 8) == 5
    return n, a, families, modulus, (low, high, count), delta_a, kappa


def physical(case, data):
    p, r, _, _, _, q, jq = case
    n, _, families, _, _, _, _ = data
    count = 0
    for aa, zz in ((1, 0), (0, 1)):
        raw = [aa]*(2*p)+[-2*aa+r*zz]*p+[-p*zz]*r
        for sigma, h, fs, matrices, _ in families:
            for index in range(2):
                ledger = Ledger(raw, p)
                groups = [list(range(2*p)), list(range(2*p, 3*p)), list(range(3*p, n))]
                groups = overlap(ledger, groups, sigma, h+index)
                mat = matrices[index]
                a1, z1 = F(mat[0]*aa+mat[1]*zz, p*p), F(mat[2]*aa+mat[3]*zz, p*p)
                assert [ledger.state[g[0]] for g in groups] == [a1, -2*a1+r*z1, -p*z1]
                groups = overlap(ledger, groups, sigma, h+index)
                scalar = F(fs[index], p**3)
                assert [ledger.state[g[0]] for g in groups] == [scalar*aa, scalar*(-2*aa+r*zz), -scalar*p*zz]
                ledger.independent_replay(raw)
                count += 1
        for j in (jq, jq+1):
            s = q-3*j
            ledger = Ledger(raw, p)
            groups = [list(range(2*p)), list(range(2*p, 3*p)), list(range(3*p, n))]
            groups = apply_return(ledger, groups, "A", j, s)
            av, zv = F((p-q)*aa+(n*j-p*q)*zz, p), F(-aa, p)
            assert [ledger.state[g[0]] for g in groups] == [av, -2*av+r*zv, -p*zv]
            ledger.independent_replay(raw)
            count += 1
    return count


def transport(case, data, pair):
    p, r, _, _, _, _, _ = case
    n, a, families, modulus, interval, delta, kappa = data
    hcycle = 4 if n % 2 == 0 else 3
    index = hcycle-families[0][1]
    v = scale(zy(mm(families[0][3][index], a), p), F(1, p**3))
    assert tuple(residue(x, n) for x in v) == (1, residue(F(-1, p*p), n), 0, 1)
    if n % 2 == 0:
        assert residue(v[0]+v[3], 4) == 2
    if n % 3 == 0:
        c = 1-4*det(v)/(v[0]+v[3])**2
        assert residue(c, 9) != 6
    powers = [(local_cycle_hit(v, ell, e, pair), ell**e) for ell, e in factors(modulus).items()]
    pair = apply_mod(mod_power(v, crt_pairs(powers), modulus), pair, modulus)
    assert pair[0] == 0 and gcd(pair[1], modulus) == 1
    first = unit_lift(p, r, pair[1] % n, interval)
    target = pair[1]*pow(residue(first, modulus), -1, modulus) % modulus
    if n % 2:
        k = principal_unit_log(delta, target, modulus, n, False)
        lifted = pow(residue(delta, modulus), k, modulus)
    else:
        two = 2**valuation(modulus, 2)
        odd = modulus//two
        flag = int(target % 4 == 3)
        target = target*pow(residue(delta, modulus), -flag, modulus) % modulus
        k2 = principal_unit_log(kappa, target, two, 4, False)
        residual = target*pow(residue(kappa, modulus), -k2, modulus) % modulus
        assert residual % two == 1
        order2 = pure_prime_order((delta, 0, 0, delta), 2, valuation(two, 2))
        base = delta**order2
        ko = principal_unit_log(base, residual, odd, n//2, False)
        lifted = pow(residue(delta, modulus), flag+order2*ko, modulus)*pow(residue(kappa, modulus), k2, modulus)
    assert residue(first, modulus)*lifted % modulus == pair[1]


def main():
    rng = Random(2026091513)
    literal = unit_count = transports = 0
    for case in CASES:
        data = system(case)
        p, r = case[:2]
        n = data[0]
        literal += physical(case, data)
        for wanted in range(1, n):
            if gcd(wanted, n) == 1:
                unit_lift(p, r, wanted, data[4])
                unit_count += 1
        for _ in range(5):
            z, y = rng.randrange(-10**8, 10**8), rng.randrange(1, 10**8)
            if gcd(y, n) != 1:
                y = 1
            transport(case, data, (z, y))
            transports += 1
        print("residual-interface-row", p, n, data[4], str(data[5]), str(data[6]))
    print("three residual affine-minor and saturation interfaces: PASS", len(CASES))
    print("three residual original-position returns: PASS", literal)
    print("three residual full unit representatives: PASS", unit_count)
    print("three residual complete direction-scale transports: PASS", transports)
    print("all-prime three-p-plus10 threshold interfaces: PASS")


if __name__ == "__main__":
    main()

