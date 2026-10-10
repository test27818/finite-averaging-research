"""One overlapping average supplies uniform near-4p congruence control.

Closed capacities, exact four-atom position replays and prime-power lifts.
No averaging-word search or enumeration of a large matrix group.
"""
from fractions import Fraction as F
from math import gcd
from random import Random

from verify_four_prime_entry_and_band import factors, Ledger
from verify_uniform_odd_middle_cores import mm, invq, residue, bezout
from verify_upper_band_three_value_reduction import core_state
from verify_upper_band_unrestricted_completion import (
    ceildiv, scale, det, zy, apply_mod, local_cycle_hit, unit_lift)
from verify_even_odd_half_core import I, U, mod_power, valuation, crt_pairs, principal_unit_log

if not __debug__:
    raise RuntimeError("Assertions are required.")


def parameters(p, r):
    assert p >= 37 and ceildiv(p+21, 2) <= r < p
    n = 3*p+r
    j = ceildiv(2*p-r, 6)
    jmax = min((2*p-r)//4, p//3)
    h = ceildiv(2*p-r+3, 6)
    hmax = (p+3)//4
    assert j+2 <= jmax and h+1 <= hmax
    ds = tuple(p*p-n*(j+k) for k in range(3))
    fs = tuple(p**3-n*(p-1)*(h+k) for k in range(2))
    matrices_a = tuple((0, -d, -1, 0) for d in ds)
    matrices_j = tuple((-p, p*(n*(h+k)-p*(p+1)), -(p-1), p) for k in range(2))
    for k in range(2):
        hh = h+k
        x, y, u = 2*hh-1, hh, p+1-3*hh
        assert x >= 0 and y >= 0 and u >= 0
        assert x+y+u == p and 2*x <= p+1 and 2*y <= p and 2*u <= r-1
        assert mm(matrices_j[k], matrices_j[k]) == scale(I, p*fs[k])
    assert gcd(ds[0], ds[1]) == gcd(fs[0], fs[1]) == 1
    assert all(gcd(v, n*p) == 1 for v in ds+fs)
    diagonal = mm(invq(matrices_a[0]), matrices_a[1])
    affine = mm(invq(matrices_j[0]), matrices_j[1])
    assert affine == (1, F(-p*n, fs[0]), 0, F(fs[1], fs[0]))
    commutator = mm(mm(mm(diagonal, affine), invq(diagonal)), invq(affine))
    assert commutator == U(F(-p*n*n, ds[1]*fs[1]))

    a, overlap = matrices_a[0], matrices_j[0]
    nilpotent = (p*(p-1), -p*p, (p-1)**2, -p*(p-1))
    transvection = mm(mm(overlap, U(p*n*n)), invq(overlap))
    assert transvection == tuple(x+y for x, y in zip(I, scale(nilpotent, F(n*n, fs[0]))))
    basis = (p, -ds[0]*(p-1), p-1, -p)
    assert gcd(det(basis), p) == 1
    first = mm(mm(invq(basis), nilpotent), basis)
    second = mm(mm(mm(mm(invq(basis), a), nilpotent), invq(a)), basis)
    assert first == (0, -det(basis), 0, 0)
    assert second == (0, 0, -F(det(basis), ds[0]), 0)
    for parameter in (0, 1, p, p*p-1):
        g = tuple(x+y for x, y in zip(I, scale(nilpotent, F(n**4*parameter, fs[0]))))
        assert det(g) == 1 and tuple(residue(x, n**4) for x in g) == I
    return n, j, h, ds, fs, matrices_a, matrices_j


def overlap_return(ledger, groups, h):
    a, b, c = (list(g) for g in groups)
    p, r = ledger.p, len(c)
    new = a[:p-1]+c[:1]
    ledger.average(new)
    a, c = a[p-1:], c[1:]
    kept, new = new[:r], new[r:]
    x, y, u = 2*h-1, h, p+1-3*h
    left = a[:x]+b[:y]+c[:u]
    right = a[x:2*x]+b[y:2*y]+c[u:2*u]
    other = a[2*x:]+b[2*y:]+c[2*u:]+new
    assert sorted(left+right+other+kept) == list(range(3*p+r))
    for group in (left, right, other):
        ledger.average(group)
    return [left+right, other, kept]


def physical(p, r, data):
    n, j, h, ds, fs, aa, jj = data
    count = 0
    for k in range(2):
        for a, z in ((1, 0), (0, 1)):
            raw = core_state(p, r, a+p*z, z)
            ledger = Ledger(raw, p)
            groups = [list(range(2*p)), list(range(2*p, 3*p)), list(range(3*p, n))]
            groups = overlap_return(ledger, groups, h+k)
            matrix = jj[k]
            ax, zx = F(matrix[0]*a+matrix[1]*z, p*p), F(matrix[2]*a+matrix[3]*z, p*p)
            expected = (ax, -2*ax+r*zx, -p*zx)
            assert all(ledger.state[index] == value
                       for group, value in zip(groups, expected) for index in group)
            groups = overlap_return(ledger, groups, h+k)
            scalar = F(fs[k], p**3)
            assert [ledger.state[g[0]] for g in groups] == [scalar*a, scalar*(-2*a+r*z), -scalar*p*z]
            ledger.independent_replay(raw)
            count += 1
    return count


def general_weighted_physical():
    checked = 0
    for p in (37, 53, 101):
        for m in (1, 3, 4):
            for r in (p-2, p-1):
                n = (m+1)*p+r
                h = ceildiv(m*p+m+1-r, m*(m+1))
                assert h <= ((m-1)*p+m+1)//(m*m)
                x, y, u = m*h-1, h, p+1-(m+1)*h
                assert min(x, y, u) >= 0 and x+y+u == p
                for a, z in ((1, 0), (0, 1)):
                    raw = [a]*(m*p)+[-m*a+r*z]*p+[-p*z]*r
                    ledger = Ledger(raw, p)
                    ga = list(range(m*p))
                    gb = list(range(m*p, (m+1)*p))
                    gc = list(range((m+1)*p, n))
                    new = ga[:p-1]+gc[:1]
                    ledger.average(new)
                    ga, gc = ga[p-1:], gc[1:]
                    kept, new = new[:r], new[r:]
                    repeated = [ga[t*x:(t+1)*x]+gb[t*y:(t+1)*y]+gc[t*u:(t+1)*u]
                                for t in range(m)]
                    other = ga[m*x:]+gb[m*y:]+gc[m*u:]+new
                    for group in repeated+[other]:
                        ledger.average(group)
                    matrix = (-p, p*(n*h-p*(p+1)), -(p-1), p)
                    aa = F(matrix[0]*a+matrix[1]*z, p*p)
                    zz = F(matrix[2]*a+matrix[3]*z, p*p)
                    groups = [sum(repeated, []), other, kept]
                    values = (aa, -m*aa+r*zz, -p*zz)
                    assert all(ledger.state[index] == value
                               for group, value in zip(groups, values) for index in group)
                    ledger.independent_replay(raw)
                    checked += 1
    return checked


def direction_matrix(p, r, data):
    n, j, h, ds, fs, aa, jj = data
    hk = int(n % 4 == 2 and h % 2)
    jk = 0
    if n % 3 == 0 and n % 9:
        while (n//3)*(j+jk-h-hk)*pow(p, -3, 3) % 3 == 2:
            jk += 1
    assert jk <= 1
    v = scale(zy(mm(jj[hk], aa[jk]), p), F(1, p**3))
    assert tuple(residue(x, n) for x in v) == (1, residue(F(-1, p*p), n), 0, 1)
    trace = v[0]+v[3]
    assert trace == 2-F(n*(p*(h+hk)+(p-1)*(j+jk)), p**3)
    if n % 2 == 0:
        assert residue(trace, 4) == 2
    if n % 3 == 0:
        c = 1-4*det(v)/(trace*trace)
        assert residue(c, 3) == 0 and residue(c, 9) != 6
    return v


def transport(p, r, data, pair):
    n, j, h, ds, fs, aa, jj = data
    modulus = n**4
    v = direction_matrix(p, r, data)
    exponents = [(local_cycle_hit(v, ell, 4*e, pair), ell**(4*e))
                 for ell, e in factors(n).items()]
    power = crt_pairs(exponents)
    pair = apply_mod(mod_power(v, power, modulus), pair, modulus)
    assert pair[0] == 0 and gcd(pair[1], modulus) == 1
    first = unit_lift(p, r, pair[1] % n)
    correction = pair[1]*pow(residue(first, modulus), -1, modulus) % modulus
    k1, k2 = F(ds[1], ds[0]), F(ds[2], ds[0])
    if n % 4 == 2:
        flag = int(correction % 4 != 1)
        correction = correction*pow(residue(k1, modulus), -flag, modulus) % modulus
        base, start = k2, 2*n
    else:
        flag, base, start = 0, k1, n
    exponent = principal_unit_log(base, correction, modulus, start, False)
    lifted = residue(first, modulus)*pow(residue(k1, modulus), flag, modulus)
    assert lifted*pow(residue(base, modulus), exponent, modulus) % modulus == pair[1]

    eps = F(1, ds[0])
    z, y = modulus*eps, (modulus+1)*eps
    _, alpha, beta = bezout(modulus, modulus+1)
    alpha, beta = alpha*ds[0], beta*ds[0]
    t = residue(-alpha/y, modulus)
    alpha, beta = alpha+t*y, beta-t*z
    final = (y/eps, -z/eps, eps*alpha, eps*beta)
    assert det(final) == 1 and tuple(residue(x, modulus) for x in final) == I
    assert (final[0]*z+final[1]*y, final[2]*z+final[3]*y) == (0, eps)


def main():
    systems = endpoints = words = transports = 0
    rng = Random(2026091504)
    for p in range(37, 200):
        if factors(p) != {p: 1}:
            continue
        for r in range(ceildiv(p+21, 2), p):
            data = parameters(p, r)
            systems += 1
            endpoints += int(r >= p-2)
            if p <= 53 and r >= p-2:
                words += physical(p, r, data)
            for _ in range(2):
                z, y = rng.randrange(-10**7, 10**7), rng.randrange(1, 10**7)
                if gcd(y, data[0]) != 1:
                    y = 1
                transport(p, r, data, (z, y))
                transports += 1
    print("overlap upper-band capacities and root identities: PASS", systems)
    print("overlap upper-band local-p congruence removal: PASS", systems)
    print("overlap upper-band literal scalar returns: PASS", words)
    print("overlap upper-band complete direction-scale transports: PASS", transports)
    print("overlap upper-band two final dimensions: PASS", endpoints)
    print("overlap arity-independent weighted return formula: PASS", general_weighted_physical())
    print("overlap upper-band completion: PASS")


if __name__ == "__main__":
    main()
