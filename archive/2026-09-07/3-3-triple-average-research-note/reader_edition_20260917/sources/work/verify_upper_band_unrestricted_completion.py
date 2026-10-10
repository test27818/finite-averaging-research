"""Audit the unrestricted upper interior using exact arithmetic and local lifts.

No averaging-word search. Bounded checks test the written formulas, not the
Morris/Serre subgroup theorems or the unbounded quantifiers of the proof.
"""
from fractions import Fraction as F
from math import gcd
from random import Random

from verify_four_prime_entry_and_band import factors, Ledger
from verify_uniform_odd_middle_cores import mm, invq, residue, bezout
from verify_upper_band_four_return_congruence import system
from verify_upper_band_descent_boundary import apply_return
from verify_upper_band_three_value_reduction import core_state
from verify_even_odd_half_core import I, U, mod_power, valuation, crt_pairs, principal_unit_log
from verify_even_interior_completion import companion_inverse_sandwich

if not __debug__:
    raise RuntimeError("Assertions are required.")


def scale(matrix, scalar):
    return tuple(scalar*x for x in matrix)


def det(matrix):
    a, b, c, d = matrix
    return a*d-b*c


def ceildiv(a, b):
    return -((-a)//b)


def capacity(p, r, q):
    low = max(0, ceildiv(q-r//2, 3))
    high = min(p//2, q//3, (q-ceildiv(r, 2))//2)
    return low, high


def interval(p, r):
    return r//2+(2 if r % 2 == 0 else 5), 3*(p//2)+r//2


def a_return(p, r, q, j=None):
    low, high = capacity(p, r, q)
    assert low <= high, (p, r, q, low, high)
    if j is None:
        j = low
    assert low <= j <= high
    s = q-3*j
    i = p-j-s
    assert 0 <= 2*s <= r and 0 <= 2*j <= p and 0 <= 2*i <= 2*p-r
    return (p-q, r*j-p*s, -1, 0), j, s


def zy(matrix, p):
    change = (0, 1, 1, p)
    return mm(mm(change, matrix), invq(change))


def large_divisor_q(p, r):
    n = 3*p+r
    assert r > p//2 and factors(r) == {r: 1} and p % 3 != r % 3
    if 5*r >= 3*p:
        q = (n-1)//4
        if q % 2 == 0:
            q -= 1
    else:
        q = n//5
        choices = (q-2, q-1, q, q+1, q+2)
        q = min((v for v in choices if v % 2 and gcd(v, n) == 1),
                key=lambda v: (abs(5*v-n), v))
    assert r < q < p and 2*q <= 3*r and q % 2 and gcd(q, n) == 1, (p, r, q)
    return q


def unit_representative(p, r, wanted):
    n = 3*p+r
    lower, upper = interval(p, r)
    assert gcd(wanted, n) == 1
    if n % 3:
        b = wanted % n
        b = min(b, n-b)
        while 4*b > n:
            nxt = abs(n-3*b)
            assert 0 < nxt < b and gcd(nxt, n) == 1
            b = nxt
        while b < lower:
            b *= 3
        assert lower <= b <= upper and gcd(b, n) == 1
        a_return(p, r, b)
        return b
    k = n//3
    b = wanted % k
    b = min(b, k-b)
    candidates = (k-b, k+b, b)
    viable = [q for q in candidates if lower <= q <= upper and gcd(q, n) == 1]
    assert viable, (p, r, wanted, b, candidates, lower, upper)
    q = viable[0]
    assert (q-wanted) % k == 0 or (q+wanted) % k == 0
    a_return(p, r, q)
    for q0 in (k-1, k+1):
        if gcd(q0, n) == 1:
            a_return(p, r, q0)
    return q


def triadic_return(p, r):
    n = 3*p+r
    k = n//3
    delta = {0: 3, 1: 1, 2: -1}[(-p-k) % 3]
    q = k+delta
    assert gcd(q, n) == 1
    low, high = capacity(p, r, q)
    assert high >= low+1, (p, r, q, low, high)
    j = low
    if n % 9 and k*j % 3 == 1:
        j += 1
    matrix, j, s = a_return(p, r, q, j)
    c = F((p+q)**2-4*n*j, (p-q)**2)
    assert residue(c, 3) == 0 and residue(c, 9) != 6, (p, r, q, j, c)
    return matrix, q, j, s


def digit_unit(p, r, q):
    matrix, _, _ = a_return(p, r, q)
    unit = F(-matrix[1], p)
    assert residue(unit, 3*p+r) == q % (3*p+r)
    return unit


def unit_lift(p, r, wanted):
    n = 3*p+r
    q = unit_representative(p, r, wanted)
    if n % 3:
        b = wanted % n
        multiplier = F(1)
        if 2*b > n:
            b = n-b
            multiplier = -multiplier
        three = F(-r, p)
        while 4*b > n:
            multiplier *= three if 3*b > n else -three
            b = abs(n-3*b)
        while b < interval(p, r)[0]:
            b *= 3
            multiplier *= three
        assert b == q and residue(multiplier*wanted-q, n) == 0
        answer = digit_unit(p, r, q)/multiplier
    else:
        k = n//3
        generator = digit_unit(p, r, k+1) if k % 3 != 2 else -digit_unit(p, r, k-1)
        quotient = wanted*pow(q, -1, n) % n
        correction = next(sign*generator**power for sign in (1, -1) for power in range(3)
                          if residue(sign*generator**power, n) == quotient)
        answer = digit_unit(p, r, q)*correction
    assert residue(answer-wanted, n) == 0
    return answer


def unit_scale_transport(p, r, modulus, target):
    n = 3*p+r
    first = unit_lift(p, r, target % n)
    correction = target*pow(residue(first, modulus), -1, modulus) % modulus
    entries = system(p, r)
    kap_a = F(entries[1][3], entries[0][3])
    kap_b = F(entries[3][3], entries[2][3])
    if n % 4 == 2:
        flag = int(correction % 4 != 1)
        correction = correction*pow(residue(kap_a, modulus), -flag, modulus) % modulus
        base, start = kap_b, 2*n
    else:
        flag, base, start = 0, kap_a, n
    power = principal_unit_log(base, correction, modulus, start, False)
    lifted = residue(first, modulus)*pow(residue(kap_a, modulus), flag, modulus)
    lifted = lifted*pow(residue(base, modulus), power, modulus) % modulus
    assert lifted == target


def exact_fiber(p, r):
    n = 3*p+r
    modulus = 3**(2*valuation(r, 3))*n**4
    denominator = system(p, r)[0][3]
    eps = F(1, denominator)
    z, y = modulus*eps, (modulus+1)*eps
    common, alpha, beta = bezout(modulus, modulus+1)
    assert common == 1
    alpha *= denominator
    beta *= denominator
    t = residue(-alpha/y, modulus)
    alpha, beta = alpha+t*y, beta-t*z
    matrix = (y/eps, -z/eps, eps*alpha, eps*beta)
    assert det(matrix) == 1
    assert tuple(residue(x, modulus) for x in matrix) == I
    assert (matrix[0]*z+matrix[1]*y, matrix[2]*z+matrix[3]*y) == (0, eps)


def apply_mod(matrix, pair, modulus):
    a, b, c, d = (residue(x, modulus) for x in matrix)
    u, v = pair
    return ((a*u+b*v) % modulus, (c*u+d*v) % modulus)


def local_cycle_hit(matrix, ell, exponent, pair):
    modulus = ell**exponent
    a, b, c, d = (residue(x, ell) for x in matrix)
    assert c == 0 and a == d and a and b
    step = b*pow(a, -1, ell) % ell
    x = pair[0]*pow(pair[1], -1, ell) % ell
    power = -x*pow(step, -1, ell) % ell
    for level in range(1, exponent):
        mod = ell**(level+1)
        u, v = apply_mod(mod_power(matrix, power, mod), pair, mod)
        x = u*pow(v, -1, mod) % mod
        jump = mod_power(matrix, ell**level, mod)
        u1, v1 = apply_mod(jump, (u, v), mod)
        x1 = u1*pow(v1, -1, mod) % mod
        difference = (x1-x) % mod
        assert x % ell**level == 0
        assert difference % ell**level == 0 and difference//ell**level % ell
        digit = -(x//ell**level)*pow(difference//ell**level, -1, ell) % ell
        power += digit*ell**level
    u, v = apply_mod(mod_power(matrix, power, modulus), pair, modulus)
    assert u == 0 and gcd(v, modulus) == 1
    return power


def pure_prime_order(matrix, ell, exponent):
    modulus = ell**exponent
    current = tuple(residue(x, modulus) for x in matrix)
    power = 1
    for _ in range(exponent+3):
        if current == I:
            return power
        current = mod_power(current, ell, modulus)
        power *= ell
    raise AssertionError("Expected a pure prime-power order.")


def direction_transport(p, r, pair):
    n = 3*p+r
    a = valuation(r, 3)
    modulus = 3**(2*a)*n**4
    entries = system(p, r)
    aj, bk = entries[0][2], entries[2][2]
    if n % 4 == 2 and sum(mm(bk, aj)[::3]) % 4 != 2:
        bk = entries[3][2]
    v = scale(zy(mm(bk, aj), p), F(1, p*p))
    assert tuple(residue(x, n) for x in v) == (1, residue(F(-3, p), n), 0, 1)
    if n % 2 == 0:
        assert residue(v[0]+v[3], 4) == 2
    local = []
    if n % 3 == 0:
        matrix, _, _, _ = triadic_return(p, r)
        t = scale(zy(matrix, p), F(1, p))
        e3 = 4*valuation(n, 3)+2*a
        k3 = local_cycle_hit(t, 3, e3, pair)
        pair = apply_mod(mod_power(t, k3, modulus), pair, modulus)
        order3 = pure_prime_order(v, 3, e3)
        local.append((0, order3))
    for ell, exponent in factors(n).items():
        if ell == 3:
            continue
        exponent *= 4
        power = local_cycle_hit(v, ell, exponent, pair)
        local.append((power, ell**exponent))
    power = crt_pairs(local)
    final = apply_mod(mod_power(v, power, modulus), pair, modulus)
    assert final[0] == 0 and gcd(final[1], modulus) == 1
    return modulus, final


def check_parameters(p, r, physical=False):
    n = 3*p+r
    entries = system(p, r)
    aj, d = entries[0][2:]
    e, mu, nu = entries[1][3], entries[2][3], entries[3][3]
    lower, upper = interval(p, r)
    for q in range(lower, upper+1):
        matrix, j, s = a_return(p, r, q)
        assert zy(matrix, p) == (p, -1, n*j, -q)
        if gcd(q, n) == 1:
            assert gcd(det(matrix), n) == 1
    eps = 1 if p % 3 == 1 else -1
    j = (p-eps)//3
    assert 0 <= j <= p//2
    fe = (F(eps, p), F(r*j, p), 0, 1)
    assert mm(invq(fe), fe) == I
    for ell in factors(r):
        if ell == 3 or ell > p//2:
            continue
        q = ell if ell % 3 == 1 else -ell
        digit = eps*q
        j = (p-digit)//3
        assert 0 <= j <= p//2 and p-3*j == digit, (p, r, ell, digit)
        fq = (F(digit, p), F(r*j, p), 0, 1)
        cq = mm(fq, invq(fe))
        assert cq == (q, F(r*(1-q), 3), 0, 1)
        h = scale(mm(mm(cq, aj), cq), F(1, q))
        assert all(F(x).denominator == 1 for x in h) and det(h) == det(aj)
        assert det(mm(h, invq(aj))) == 1
        assert mm(mm(aj, cq), invq(h)) == scale(invq(cq), q)
    if factors(r) == {r: 1} and r > p//2 and p % 3 != r % 3:
        q = large_divisor_q(p, r)
        s = q-r
        ns = (p-s, -p*s, 2, -r)
        assert s > 0 and 2*s <= r and gcd(det(ns), r*n) == 1
        h = mm(ns, invq(entries[2][2]))
        assert h[2:] == (0, 1) and residue(h[1], r)
        diagonal = (1, 0, 0, F(e, d))
        comm = mm(mm(mm(diagonal, h), invq(diagonal)), invq(h))
        assert comm == U(h[1]*F(n, e))
        assert gcd(comm[1].numerator, r) == 1
    for wanted in range(1, n):
        if gcd(wanted, n) == 1:
            unit_representative(p, r, wanted)
    if n % 3 == 0:
        triadic_return(p, r)
    kap_a, kap_b = F(e, d), F(nu, mu)
    for ell, exponent in factors(n).items():
        if ell != 2 or exponent > 1:
            assert valuation(abs((kap_a-1).numerator), ell) == exponent
        else:
            assert residue(kap_a, 4) == 3
            assert valuation(abs((kap_b-1).numerator), 2) == 2
    if not physical:
        return 0
    qs = {lower, upper, unit_representative(p, r, 1)}
    if n % 3 == 0:
        qs.add(triadic_return(p, r)[1])
    count = 0
    for q in sorted(qs):
        if gcd(q, n) != 1:
            continue
        matrix, j, s = a_return(p, r, q)
        companion_inverse_sandwich(matrix[0], matrix[1], 3**(2*valuation(r, 3))*n**4)
        for a, z in ((1, 0), (0, 1)):
            raw = core_state(p, r, a+p*z, z)
            ledger = Ledger(raw, p)
            groups = [list(range(2*p)), list(range(2*p, 3*p)), list(range(3*p, n))]
            groups = apply_return(ledger, groups, 'A', j, s)
            aa, zz = F(matrix[0]*a+matrix[1]*z, p), F(-a, p)
            expected = (aa, -2*aa+r*zz, -p*zz)
            assert all(ledger.state[index] == value
                       for group, value in zip(groups, expected) for index in group)
            ledger.independent_replay(raw)
            count += 1
    return count


def main():
    systems = physical = directions = scales = 0
    rng = Random(20260915)
    for p in range(13, 200):
        if factors(p) != {p: 1}:
            continue
        for r in range(10, p-2):
            physical += check_parameters(p, r, p <= 29)
            systems += 1
            for _ in range(2):
                z, y = rng.randrange(-10**8, 10**8), rng.randrange(1, 10**8)
                if gcd(y, 3*p+r) != 1:
                    y = 1
                modulus, final = direction_transport(p, r, (z, y))
                directions += 1
                if r in {10, 11, 12, p-3}:
                    unit_scale_transport(p, r, modulus, final[1])
                    exact_fiber(p, r)
                    scales += 1
    print("upper interior capacity, inverse and unit formulas: PASS", systems)
    print("upper interior literal original-position returns: PASS", physical)
    print("upper interior all-prime direction transports: PASS", directions)
    print("upper interior unit-scale lifts and exact fibers: PASS", scales)
    print("upper interior unrestricted completion interfaces: PASS")


if __name__ == "__main__":
    main()
