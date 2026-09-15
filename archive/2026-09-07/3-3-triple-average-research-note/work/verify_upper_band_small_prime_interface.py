"""Small-prime instances of one capacity-and-unit-density interface.

Only exact return capacities, matrix identities, unit counts and local lifts.
The infinite-input proof is the same principal-congruence argument as before.
"""
from fractions import Fraction as F
from math import gcd
from random import Random

from verify_four_prime_entry_and_band import factors
from verify_uniform_odd_middle_cores import mm, invq, residue, bezout
from verify_upper_band_unrestricted_completion import ceildiv, scale, det, apply_mod, local_cycle_hit
from verify_upper_band_overlap_completion import physical, direction_matrix
from verify_four_p_tail_completion import safe_a, interval_units, phi
from verify_even_odd_half_core import I, U, mod_power, crt_pairs, principal_unit_log


if not __debug__:
    raise RuntimeError("Assertions are required.")


def parameters(p, r):
    n = 3*p+r
    j, jmax = ceildiv(2*p-r, 6), min((2*p-r)//4, p//3)
    h, hmax = ceildiv(2*p-r+3, 6), (p+3)//4
    assert j+1 <= jmax and h+1 <= hmax
    ds = tuple(p*p-n*(j+k) for k in range(2))
    fs = tuple(p**3-n*(p-1)*(h+k) for k in range(2))
    aa = tuple((0, -d, -1, 0) for d in ds)
    jj = tuple((-p, p*(n*(h+k)-p*(p+1)), -(p-1), p) for k in range(2))
    assert gcd(*ds) == gcd(*fs) == 1
    assert all(gcd(value, n*p) == 1 for value in ds+fs)
    for matrix, f in zip(jj, fs):
        assert mm(matrix, matrix) == scale(I, p*f)
    diagonal, affine = mm(invq(aa[0]), aa[1]), mm(invq(jj[0]), jj[1])
    commutator = mm(mm(mm(diagonal, affine), invq(diagonal)), invq(affine))
    assert commutator == U(F(-p*n*n, ds[1]*fs[1]))
    nilpotent = (p*(p-1), -p*p, (p-1)**2, -p*(p-1))
    assert mm(mm(jj[0], U(p*n*n)), invq(jj[0])) == tuple(
        x+y for x, y in zip(I, scale(nilpotent, F(n*n, fs[0]))))
    basis = (p, -ds[0]*(p-1), p-1, -p)
    assert gcd(det(basis), p) == 1
    assert mm(mm(invq(basis), nilpotent), basis) == (0, -det(basis), 0, 0)
    assert mm(mm(mm(mm(invq(basis), aa[0]), nilpotent), invq(aa[0])), basis) == (
        0, 0, -F(det(basis), ds[0]), 0)
    low, high = r//2+(2 if r % 2 == 0 else 5), 3*(p//2)+r//2
    count = interval_units(low, high, tuple(factors(n)))
    assert high < F(n, 2) and 4*count > phi(n)
    for q in range(low, high+1):
        safe_a(p, r-p, q)
    return (n, j, h, ds, fs, aa, jj), (low, high, count)


def unit_lift(p, r, wanted, interval):
    n, (low, high, _) = 3*p+r, interval
    for b in range(low, high+1):
        if gcd(b, n) != 1:
            continue
        a = wanted*b % n
        sign = 1
        if 2*a > n:
            a, sign = n-a, -1
        if low <= a <= high:
            da = safe_a(p, r-p, a)[0][1]
            db = safe_a(p, r-p, b)[0][1]
            answer = sign*F(da, db)
            assert residue(answer, n) == wanted % n
            return answer
    raise AssertionError("Missing unit intersection.")


def kernel_base(p, r, data):
    n, _, _, ds, _, _, _ = data
    first = F(ds[1], ds[0])
    if n % 4 != 2:
        return first, first, n, None
    q = p+6
    assert gcd(q, n) == 1
    matrix, j, s = safe_a(p, r-p, q)
    d0 = matrix[1]
    j2, s2 = j+2, s-6
    assert s2 >= 0 and 3*j2+s2 == q
    assert 0 <= 2*(p-j2-s2) <= 2*p-r and 2*j2 <= p and 2*s2 <= r
    d2 = r*j2-p*s2
    assert d2 == d0+2*n and gcd(d0*d2, n) == 1
    second = F(d2, d0)
    assert residue(first, 4) == 3 and residue(second, 8) == 5
    return first, second, 2*n, (q, j, j2, d0, d2)


def transport(p, r, data, interval, pair):
    n = data[0]
    modulus = n**4
    v = direction_matrix(p, r, data)
    local = [(local_cycle_hit(v, ell, 4*e, pair), ell**(4*e))
             for ell, e in factors(n).items()]
    power = crt_pairs(local)
    pair = apply_mod(mod_power(v, power, modulus), pair, modulus)
    assert pair[0] == 0 and gcd(pair[1], modulus) == 1
    first = unit_lift(p, r, pair[1] % n, interval)
    correction = pair[1]*pow(residue(first, modulus), -1, modulus) % modulus
    k1, base, start, _ = kernel_base(p, r, data)
    flag = int(n % 4 == 2 and correction % 4 != 1)
    correction = correction*pow(residue(k1, modulus), -flag, modulus) % modulus
    exponent = principal_unit_log(base, correction, modulus, start, False)
    assert residue(first, modulus)*pow(residue(k1, modulus), flag, modulus)*pow(
        residue(base, modulus), exponent, modulus) % modulus == pair[1]

    eps = F(1, data[3][0])
    z, y = modulus*eps, (modulus+1)*eps
    _, alpha, beta = bezout(modulus, modulus+1)
    alpha, beta = alpha/eps, beta/eps
    t = residue(-alpha/y, modulus)
    alpha, beta = alpha+t*y, beta-t*z
    final = (y/eps, -z/eps, eps*alpha, eps*beta)
    assert det(final) == 1 and tuple(residue(x, modulus) for x in final) == I
    assert (final[0]*z+final[1]*y, final[2]*z+final[3]*y) == (0, eps)


def main():
    rng = Random(2026091519)
    literal = transports = units = 0
    table = []
    for p in (19, 23, 29, 31):
        for r in (p-2, p-1):
            data, interval = parameters(p, r)
            n = data[0]
            literal += physical(p, r, data)
            for wanted in range(1, n):
                if gcd(wanted, n) == 1:
                    unit_lift(p, r, wanted, interval)
                    units += 1
            for _ in range(5):
                z, y = rng.randrange(-10**8, 10**8), rng.randrange(1, 10**8)
                if gcd(y, n) != 1:
                    y = 1
                transport(p, r, data, interval, (z, y))
                transports += 1
            table.append((p, n, data[1], data[2], interval[0], interval[1],
                          interval[2], phi(n), kernel_base(p, r, data)[3]))
    for row in table:
        print("interface-row", row)
    print("small-prime upper-boundary capacity interfaces: PASS", len(table))
    print("small-prime upper-boundary literal scalar returns: PASS", literal)
    print("small-prime upper-boundary full unit representatives: PASS", units)
    print("small-prime upper-boundary exact local terminal interfaces: PASS", transports)
    print("uniform upper boundaries for every prime at least19: PASS")


if __name__ == "__main__":
    main()

