"""Exact algebra for all odd remainders in the lower middle band.

General group containments rely on the stated arithmetic group theorems.
No averaging-word discovery search is used. Finite matrix lifts are built
by CRT and Gaussian elimination, not by traversing SL2 of a large modulus.
"""

from fractions import Fraction as F
from math import gcd, lcm, prod
from pathlib import Path
from random import Random
import json

from verify_endpoint_congruence_completion import mm, inverse, prime_divisors
from verify_four_prime_entry_and_band import Ledger, triple_return, band_reduce, carrier_period

I = (1, 0, 0, 1)


def invq(m):
    determinant = m[0]*m[3]-m[1]*m[2]
    return tuple(F(x, determinant) for x in (m[3], -m[1], -m[2], m[0]))


def power(m, k):
    answer = I
    while k:
        if k & 1:
            answer = mm(answer, m)
        k //= 2
        if k:
            m = mm(m, m)
    return answer


def residue(x, n):
    x = F(x)
    return x.numerator*pow(x.denominator, -1, n) % n


def bezout(a, b):
    old_r, r, old_s, s, old_t, t = a, b, 1, 0, 0, 1
    while r:
        q = old_r//r
        old_r, r = r, old_r-q*r
        old_s, s = s, old_s-q*s
        old_t, t = t, old_t-q*t
    sign = 1 if old_r > 0 else -1
    return sign*old_r, sign*old_s, sign*old_t


def normalize_pair(x, z):
    den = lcm(F(x).denominator, F(z).denominator)
    a, b = int(x*den), int(z*den)
    common = gcd(a, b)
    assert common
    return a//common, b//common


def crt_unit_shift(a, c, modulus):
    primes = prime_divisors(modulus)
    radical = prod(primes)
    return sum((radical//q)*pow(radical//q, -1, q)
               for q in primes if a % q == 0) % radical


def lift_sl2(matrix, modulus, known_primes):
    a, b, c, d = matrix
    assert (a*d-b*c) % modulus == 1
    radical = prod(known_primes)
    k = sum((radical//q)*pow(radical//q, -1, q)
            for q in known_primes if a % q == 0) % radical
    u, v = (a+k*c) % modulus, (b+k*d) % modulus
    ui = pow(u, -1, modulus)
    word = [('U', -k), ('L', c*ui), ('U', 1), ('L', u-1),
            ('U', -ui), ('L', -u*(u-1)), ('U', v*ui)]
    result = I
    for kind, value in word:
        value %= modulus
        value = value if value <= modulus//2 else value-modulus
        result = mm(result, (1, value, 0, 1) if kind == 'U' else (1, 0, value, 1))
    assert result[0]*result[3]-result[1]*result[2] == 1
    assert tuple(x % modulus for x in result) == tuple(x % modulus for x in matrix)
    return result


def inverse_activation(p, r):
    n = 2*p+r
    order = n
    for q in prime_divisors(n):
        order = order//q*(q-1)
    for q in prime_divisors(order):
        while order % q == 0 and pow(p, order//q, n) == 1:
            order //= q
    determinant = p**order
    b = r*(determinant-1)//2
    matrix = (1, b, 0, determinant)
    g0 = (b, 1, -1, 0)
    assert tuple(x % n for x in matrix) == I
    modulus = determinant*n
    selected = tuple((v+determinant*((target-v)*pow(determinant, -1, n) % n)) % modulus
                     for v, target in zip(g0, I))
    g = lift_sl2(selected, modulus, sorted(set(prime_divisors(n)+[p])))
    assert tuple(x % n for x in g) == I
    h = tuple(F(x, determinant) for x in mm(mm(matrix, g), matrix))
    assert all(x.denominator == 1 for x in h)
    h = tuple(int(x) for x in h)
    assert tuple(x % n for x in h) == I and h[0]*h[3]-h[1]*h[2] == 1
    assert mm(mm(mm(matrix, g), matrix), inverse(h)) == (determinant, 0, 0, determinant)
    return order, max(abs(x).bit_length() for x in g+h)


def core_algebra(p, r):
    n, d = 2*p+r, -r*(p+r)//2
    e = d+n
    assert gcd(d, e) == gcd(d, n) == gcd(r, n) == 1
    assert d*e and (d*e) % 2 == 0 and abs(F(e, d)) != 1
    j, q, s = (0, d, -1, 0), (0, e, -1, 0), (-1, r, 0, 1)
    scale = mm(invq(j), q)
    assert scale == (1, 0, 0, F(e, d))
    root = mm(mm(mm(s, scale), s), invq(scale))
    assert root == (1, F(r*n, e), 0, 1)
    v = mm(mm(mm(j, s), invq(j)), s)
    assert v[0]*v[3]-v[1]*v[2] == 1
    nilpotent = mm(mm(v, (0, 1, 0, 0)), invq(v))
    assert tuple(x*d*d for x in nilpotent) == (r*d, d*d, -r*r, -r*d)
    assert gcd(r*d, n) == 1
    chart, chart_inverse = (0, 1, 1, p), (-p, 1, 1, 0)
    assert tuple(residue(x, n) for x in mm(mm(chart, v), chart_inverse)) == (1, 2*pow(p, -1, n) % n, 0, 1)
    for t in (-p, -1, 1, p):
        ft = (F(t, p), F(r*(p-t), 2*p), 0, 1)
        f1 = (F(1, p), F(r*(p-1), 2*p), 0, 1)
        assert mm(ft, invq(f1)) == (t, F(r*(1-t), 2), 0, 1)
    return v


def transport(x, z, p, r, v):
    n = 2*p+r
    assert gcd(x, z) == gcd(x+p*z, n) == 1
    k = -z*pow(residue(F(2, p), n)*(x+p*z), -1, n) % n
    vk = power(v, k)
    a, b = normalize_pair(vk[0]*x+vk[1]*z, vk[2]*x+vk[3]*z)
    assert b % n == 0 and gcd(a, n) == 1
    u = pow(a, -1, n)
    u = u if u <= n//2 else u-n
    folding = 0
    if abs(u) > p:
        u = 2*u-(n if u > 0 else -n)
        folding = 1
    assert 0 < abs(u) <= p and gcd(u, n) == 1
    twos = 0
    while u % 2 == 0:
        u //= 2
        twos += 1
    odd = u
    target = F(2)**(folding-twos)
    assert residue(odd*a, n) == residue(target, n)
    shift = crt_unit_shift(b, n*a, abs(odd)) if abs(odd) > 1 else 0
    b += n*shift*a
    assert gcd(b, odd) == 1
    a = odd*a+r*(1-odd)//2*b
    assert gcd(a, b) == 1 and b % n == 0 and residue(a, n) == residue(target, n)
    common, alpha, beta = bezout(a, b)
    assert common == 1
    alpha, beta = alpha*target, beta*target
    adjust = residue(beta, n)*pow(a, -1, n) % n
    alpha, beta = alpha+adjust*b, beta-adjust*a
    matrix = (alpha, beta, -F(b)/target, F(a)/target)
    assert matrix[0]*matrix[3]-matrix[1]*matrix[2] == 1
    assert all(residue(q-i, n) == 0 and F(q).denominator & (F(q).denominator-1) == 0
               for q, i in zip(matrix, I))
    assert matrix[0]*a+matrix[1]*b == target and matrix[2]*a+matrix[3]*b == 0
    return folding


def physical(p, r, x, z):
    raw = [F(x)]*p+[r*F(z)-x]*p+[-p*F(z)]*r
    checks = 0
    for s in (r, r-2):
        ledger = Ledger(raw, p)
        groups = list(range(p)), list(range(p, 2*p)), list(range(2*p, 2*p+r))
        first = triple_return(ledger, groups, p, r, s)
        d = (p*r-(2*p+r)*s)//2
        assert ledger.state[first[0][0]] == F(d*z, p)
        assert ledger.state[first[2][0]] == x
        last = triple_return(ledger, first, p, r, s)
        for group, value in zip(last, (x, r*z-x, -p*z)):
            assert all(ledger.state[index] == F(-d, p*p)*value for index in group)
        ledger.independent_replay(raw)
        checks += 1
    ledger = Ledger(raw, p)
    a, b = list(range(p)), list(range(p, 2*p))
    half = (p+1)//2
    first, second = a[:half]+b[:p-half], a[half:]+b[p-half:]
    ledger.average(first)
    ledger.average(second)
    assert ledger.state[first[0]] == F(x, p)+F(r*(p-1)*z, 2*p)
    assert ledger.state[2*p:] == raw[2*p:]
    ledger.independent_replay(raw)
    return checks+1


def main():
    rng = Random(2026091414)
    pairs, replays, transports, folds, entries = 0, 0, 0, 0, 0
    for p in (5, 7, 11, 13, 17, 19, 23, 31, 43):
        for r in range(3, p, 2):
            v = core_algebra(p, r)
            pairs += 1
            for x, z in ((1, 0), (0, 1)):
                replays += physical(p, r, x, z)
            for _ in range(4):
                while True:
                    x, z = rng.randrange(-500, 501), rng.randrange(-500, 501)
                    if gcd(x, z) == gcd(x+p*z, 2*p+r) == 1:
                        break
                folds += transport(x, z, p, r, v)
                transports += 1
            primes = prime_divisors(2*p+r)
            if r >= len(primes) and sum((F(1, carrier_period(p, q)) for q in primes), F(0)) < 1:
                while True:
                    raw = [rng.randrange(-100, 101) for _ in range(2*p+r-1)]
                    raw.append(-sum(raw))
                    common = gcd(*raw)
                    if common:
                        raw = [x//common for x in raw]
                        if all(len({x % q for x in raw}) > 1 for q in primes):
                            break
                band_reduce(raw, p, r)
                entries += 1
    inverse_checks = [inverse_activation(p, r) for p, r in ((5, 3), (7, 3), (7, 5), (11, 3), (11, 7), (13, 3))]
    print('odd middle core parameter systems: PASS', pairs)
    print('odd middle literal return checks: PASS', replays)
    print('odd middle exact terminal transports: PASS', transports, folds)
    print('CRT principal inverse activation: PASS', len(inverse_checks))
    print('odd middle existing full-input entries: PASS', entries)
    out = {'parameter_systems': pairs, 'literal_returns': replays,
           'terminal_transports': transports, 'dyadic_folds': folds,
           'inverse_activation_checks': inverse_checks, 'full_input_entries': entries,
           'scope': 'Finite checks of symbolic constructions; no universal input-entry or threshold claim.'}
    (Path(__file__).parent/'uniform_odd_middle_core_records.json').write_text(json.dumps(out, indent=2)+'\n', encoding='utf-8')
    print('uniform odd middle core theorem: PASS')


if __name__ == '__main__':
    main()
