"""Uniform upper-band completion by principal layers and a 2,3-unit descent.

The infinite arithmetic-group statements are external dependencies of the
proof. This verifier checks exact identities, physical returns, input entry,
and the constructive arithmetic stages; it does not extract general group
elements into full averaging words.
"""

from fractions import Fraction as F
from math import gcd, lcm
from pathlib import Path
from random import Random
import json

from verify_four_prime_entry_and_band import factors, Ledger
from verify_upper_band_four_return_congruence import ranges, system, physical
from verify_upper_band_descent_boundary import apply_return
from verify_upper_band_three_value_reduction import core_state, upper_reduce
from verify_uniform_odd_middle_cores import (
    mm, invq, power, residue, bezout, normalize_pair, crt_unit_shift, lift_sl2,
)
from verify_prime_arity_zero_trigger_bridge import GlobalReplay

if not __debug__:
    raise RuntimeError('Assertions are required.')

I = (1, 0, 0, 1)


def small_unit(u, n):
    """Return b<=n/11, (b,6n)=1, and b=multiplier*u modulo n."""
    assert n > 7 and gcd(n, 6) == gcd(u, n) == 1
    b = u % n
    multiplier = F(1)
    if 2*b > n:
        b, multiplier = n-b, -multiplier
    history = []
    while True:
        old = b
        if b % 2 == 0:
            b //= 2
            multiplier /= 2
            branch = 'divide2'
        elif b % 3 == 0:
            b //= 3
            multiplier /= 3
            branch = 'divide3'
        elif 11*b <= n:
            break
        else:
            if 5*b > n:
                coefficient, divisor = 3, 2
            elif 7*b > n:
                coefficient, divisor = (4, 3) if (n-b) % 3 == 0 else (8, 3)
            else:
                coefficient, divisor = 9, 2
            signed = n-coefficient*b
            assert signed % divisor == 0 and signed
            b = abs(signed)//divisor
            multiplier *= F(-coefficient*(1 if signed > 0 else -1), divisor)
            branch = str((coefficient, divisor))
        assert 0 < b < old and gcd(b, n) == 1
        assert residue(multiplier*u, n) == b % n
        history.append(branch)
    assert gcd(b, 6*n) == 1 and 11*b <= n
    return b, multiplier, history


def parameters(p, r):
    assert p >= 13 and 10 <= r <= p-3 and gcd(r, 6) == 2
    n = 3*p+r
    returns = system(p, r)
    (j, ja), (k, kb) = ranges(p, r)
    half = r//2
    if half % 3 == p % 3:
        index = (p-half)//3
        assert j <= index <= ja
        determinant = p*p-n*index
        extra = ('A', index, (0, -determinant, -1, 0), determinant)
    else:
        assert (p-r) % 3 == 0
        index = (p-r)//3
        assert k <= index <= kb
        b = n*index-p*p+r*p
        determinant = r*r+2*b
        extra = ('B', index, (r, b, 2, -r), determinant)
    assert determinant % half == 0
    returns += [extra]
    primes = set()
    for _, _, _, value in returns:
        assert gcd(value, n) == 1
        primes.update(factors(abs(value)))
    assert set(factors(2*r)) <= primes
    return returns, primes


def smith_pair(matrix):
    """Unimodular L,R with L*matrix*R diagonal; divisibility is unnecessary."""
    current, left, right = matrix, I, I
    while current[1] or current[2]:
        a, b, c, d = current
        if c:
            common, s, t = bezout(a, c)
            operation = (s, t, -c//common, a//common)
            current, left = mm(operation, current), mm(operation, left)
        a, b, c, d = current
        if b:
            if b % a == 0:
                operation = (1, -b//a, 0, 1)
            else:
                common, s, t = bezout(a, b)
                operation = (s, -b//common, t, a//common)
            current, right = mm(current, operation), mm(right, operation)
    assert mm(mm(left, matrix), right) == current
    assert all(x[0]*x[3]-x[1]*x[2] == 1 for x in (left, right))
    return left, right


def modular_matrix_power(matrix, exponent, modulus):
    result = I
    matrix = tuple(x % modulus for x in matrix)
    while exponent:
        if exponent & 1:
            result = tuple(x % modulus for x in mm(result, matrix))
        matrix = tuple(x % modulus for x in mm(matrix, matrix))
        exponent //= 2
    return result


def general_inverse_activation(matrix, n):
    determinant = matrix[0]*matrix[3]-matrix[1]*matrix[2]
    assert gcd(determinant, n) == 1
    order = 1
    for ell, exponent in factors(n).items():
        order *= ell**(4*(exponent-1))*(ell*ell-1)*(ell*ell-ell)
    for ell in factors(order):
        while order % ell == 0 and modular_matrix_power(matrix, order//ell, n) == I:
            order //= ell
    # Even exponent keeps the CRT modulus positive.
    order = lcm(order, 2)
    pmat = power(matrix, order)
    delta = pmat[0]*pmat[3]-pmat[1]*pmat[2]
    assert delta > 0 and tuple(x % n for x in pmat) == I
    left, right = smith_pair(pmat)
    g0 = mm(mm(right, (0, 1, -1, 0)), left)
    assert all(x % delta == 0 for x in mm(mm(pmat, g0), pmat))
    modulus = delta*n
    selected = tuple((value+delta*((target-value)*pow(delta, -1, n) % n)) % modulus
                     for value, target in zip(g0, I))
    primes = sorted(set(factors(n)) | set(factors(abs(determinant))))
    g = lift_sl2(selected, modulus, primes)
    h = tuple(F(x, delta) for x in mm(mm(pmat, g), pmat))
    assert all(x.denominator == 1 for x in h)
    assert all(residue(x-target, n) == 0 for x, target in zip(g, I))
    assert all(residue(x-target, n) == 0 for x, target in zip(h, I))
    assert h[0]*h[3]-h[1]*h[2] == 1
    assert mm(mm(g, pmat), invq(h)) == tuple(delta*x for x in invq(pmat))
    return order, max(abs(x).bit_length() for x in pmat)


def half_carrier(p, r, aj):
    t, j = r//2, (p-3)//2
    matrix = ((9-p-r)//2, -3*t, -1, 0)
    assert gcd(-3*t, 3*p+r) == 1
    chart = (0, 1, 1, p)
    y_chart = mm(mm(chart, matrix), invq(chart))
    assert residue(y_chart[2], 3*p+r) == 0
    assert residue(y_chart[3]-F(9, 2), 3*p+r) == 0
    affine = mm(matrix, invq(aj))
    assert affine[2:] == (0, 1) and affine[0] == F(3*t, aj[1]*-1)
    for a, z in ((1, 0), (0, 1)):
        raw = core_state(p, r, a+p*z, z)
        ledger = Ledger(raw, p)
        groups = [list(range(2*p)), list(range(2*p, 3*p)), list(range(3*p, 3*p+r))]
        groups = apply_return(ledger, groups, 'A', j, t)
        aa, zz = F(matrix[0]*a+matrix[1]*z, p), F(-a, p)
        assert [ledger.state[group[0]] for group in groups] == [aa, -2*aa+r*zz, -p*zz]
        ledger.independent_replay(raw)
    return matrix


def principal_layers(p, r, returns):
    n = 3*p+r
    aj, aq, bk, bq = [item[2] for item in returns[:4]]
    d, e, mu, nu = [item[3] for item in returns[:4]]
    diagonal, affine = mm(invq(aj), aq), mm(invq(bk), bq)
    h1 = tuple(value/F(e, d) for value in power(diagonal, 2))
    h2 = tuple(value/F(nu, mu) for value in power(affine, 2))
    h3 = mm(mm(aj, h2), invq(aj))
    tangents = ((F(1, d), 0, 0, F(-1, d)),
                (F(-2, mu), F(2*r, mu), 0, F(2, mu)),
                (F(2, mu), 0, F(2*r, mu*d), F(-2, mu)))
    for matrix, tangent in zip((h1, h2, h3), tangents):
        assert matrix[0]*matrix[3]-matrix[1]*matrix[2] == 1
        assert all(residue(value-delta-n*t, n*n) == 0
                   for value, delta, t in zip(matrix, I, tangent))
    checks = 0
    for ell, valuation in factors(n).items():
        vectors = [tuple(residue(t[i], ell) for i in (0, 1, 2)) for t in tangents]
        a, b, c = vectors
        determinant = (a[0]*(b[1]*c[2]-b[2]*c[1])
                       -a[1]*(b[0]*c[2]-b[2]*c[0])
                       +a[2]*(b[0]*c[1]-b[1]*c[0])) % ell
        assert determinant
        # Work in a finite prime-power ring, not with huge rational matrix powers.
        for exponent in range(3):
            modulus = ell**(valuation+exponent+1)
            for matrix, tangent in zip((h1, h2, h3), tangents):
                current = tuple(residue(value, modulus) for value in matrix)
                result, count = I, ell**exponent
                while count:
                    if count & 1:
                        result = tuple(value % modulus for value in mm(result, current))
                    current = tuple(value % modulus for value in mm(current, current))
                    count //= 2
                assert all((value-delta-n*ell**exponent*residue(t, modulus)) % modulus == 0
                           for value, delta, t in zip(result, I, tangent))
                checks += 1
    v = mm(bk, aj)
    chart = (0, 1, 1, p)
    expected = (p*p, -3*p, 0, p*p)
    assert all(residue(x-y, n) == 0 for x, y in zip(mm(mm(chart, v), invq(chart)), expected))
    return v, checks


def inverse_activation(p, r):
    n = 3*p+r
    phi = n
    for q in factors(n):
        phi = phi//q*(q-1)
    order = phi
    for q in factors(phi):
        while order % q == 0 and pow(p, order//q, n) == 1:
            order //= q
    order = lcm(order, 2)
    delta = p**order
    b = r*(delta-1)//3
    matrix = (1, b, 0, delta)
    assert tuple(value % n for value in matrix) == I
    g0 = (b, 1, -1, 0)
    modulus = delta*n
    selected = tuple((v+delta*((target-v)*pow(delta, -1, n) % n)) % modulus
                     for v, target in zip(g0, I))
    g = lift_sl2(selected, modulus, sorted(set(factors(n)) | {p}))
    h = tuple(F(value, delta) for value in mm(mm(matrix, g), matrix))
    assert all(value.denominator == 1 for value in h)
    assert tuple(value % n for value in g) == tuple(value % n for value in h) == I
    assert h[0]*h[3]-h[1]*h[2] == 1
    assert mm(mm(g, matrix), invq(h)) == tuple(delta*value for value in invq(matrix))
    return order, max(abs(value).bit_length() for value in g)


def transport(a, z, p, r, v):
    n = 3*p+r
    assert gcd(a, z) == gcd(a+p*z, n) == 1
    k = z*pow(residue(F(3, p), n)*(a+p*z), -1, n) % n
    vk = power(v, k)
    a, z = normalize_pair(vk[0]*a+vk[1]*z, vk[2]*a+vk[3]*z)
    assert z % n == 0 and gcd(a, n) == 1
    small, multiplier, history = small_unit(pow(a, -1, n), n)
    epsilon = 1 if p % 3 == 1 else -1
    t = small if small % 3 == p % 3 else -small
    q = t*epsilon
    target = multiplier*(1 if t > 0 else -1)*epsilon
    j = (p-t)//3
    assert 0 <= j <= p//2 and q % 3 == 1
    assert residue(q*a-target, n) == 0
    shift = crt_unit_shift(z, n*a, abs(q)) if abs(q) > 1 else 0
    z += n*shift*a
    assert gcd(z, q) == 1
    a = q*a+r*(1-q)//3*z
    assert gcd(a, z) == 1 and z % n == 0 and residue(a-target, n) == 0
    common, alpha, beta = bezout(a, z)
    assert common == 1
    alpha, beta = target*alpha, target*beta
    adjust = residue(beta, n)*pow(a, -1, n) % n
    alpha, beta = alpha+adjust*z, beta-adjust*a
    matrix = (alpha, beta, -F(z)/target, F(a)/target)
    assert matrix[0]*matrix[3]-matrix[1]*matrix[2] == 1
    assert all(residue(value-delta, n) == 0 for value, delta in zip(matrix, I))
    assert (matrix[0]*a+matrix[1]*z, matrix[2]*a+matrix[3]*z) == (target, 0)
    assert all(set(factors(F(value).denominator)) <= {2, 3} for value in matrix)
    return len(history)


def physical_contraction(p, r):
    epsilon = 1 if p % 3 == 1 else -1
    for a, z in ((1, 0), (0, 1)):
        raw = core_state(p, r, a+p*z, z)
        for t in (epsilon, -2*epsilon, p):
            j = (p-t)//3
            ledger = Ledger(raw, p)
            groups = [list(range(2*p)), list(range(2*p, 3*p)), list(range(3*p, 3*p+r))]
            groups = apply_return(ledger, groups, 'C', j, 0)
            aa = F(t*a+r*j*z, p)
            assert [ledger.state[group[0]] for group in groups] == [aa, -2*aa+r*z, -p*z]
            ledger.independent_replay(raw)
        ft = (F(-2*epsilon, p), F(r*(p+2*epsilon), 3*p), 0, 1)
        fe = (F(epsilon, p), F(r*(p-epsilon), 3*p), 0, 1)
        assert mm(ft, invq(fe)) == (-2, r, 0, 1)


def terminal_tail(p, r):
    raw = [1]*(2*p)+[-2]*p+[0]*r
    replay = GlobalReplay(raw, p)
    j, s = divmod(p, 3)
    group = list(range(2*j))+list(range(2*p, 2*p+j))+list(range(3*p, 3*p+s))
    replay.average(group)
    assert all(replay.state[index] == 0 for index in group)
    replay.three_p_tail()
    assert not any(replay.state)
    return len(replay.operations)


def main():
    small_checks, branches = 0, set()
    for n in range(11, 400):
        if gcd(n, 6) != 1:
            continue
        for u in range(1, n):
            if gcd(u, n) == 1:
                _, _, history = small_unit(u, n)
                branches.update(history)
                small_checks += 1
    rng = Random(2026091434)
    systems = layers = labelled = transports = entries = 0
    half_matrices = {}
    for p in range(13, 100):
        if factors(p) != {p: 1}:
            continue
        for r in range(10, p-2, 2):
            if r % 3 == 0:
                continue
            returns, _ = parameters(p, r)
            v, count = principal_layers(p, r, returns)
            systems += 1
            layers += count
            for _ in range(3):
                while True:
                    a, z = rng.randrange(-1000, 1001), rng.randrange(-1000, 1001)
                    if gcd(a, z) == gcd(a+p*z, 3*p+r) == 1:
                        break
                transport(a, z, p, r, v)
                transports += 1
            if p <= 31:
                labelled += physical(p, r, returns)
                physical_contraction(p, r)
                half_matrices[p, r] = half_carrier(p, r, returns[0][2])
                while True:
                    raw = [rng.randrange(-100, 101) for _ in range(3*p+r-1)]
                    raw.append(-sum(raw))
                    if gcd(*raw) == 1 and all(len({x % q for x in raw}) > 1 for q in factors(3*p+r)):
                        break
                upper_reduce(raw, p)
                entries += 1
    inverse_checks = [inverse_activation(p, r) for p, r in ((19, 16), (23, 16), (23, 20), (31, 28))]
    general_inverses = [general_inverse_activation(half_matrices[p, r], 3*p+r)
                        for p, r in ((13, 10), (19, 10))]
    tails = [terminal_tail(p, r) for p, r in ((19, 16), (23, 16), (23, 20), (31, 28))]
    print('2,3-unit short representative descent: PASS', small_checks, sorted(branches))
    print('upper-band uniform2r localization and3 activation: PASS', systems)
    print('upper-band principal-layer identities: PASS', layers)
    print('upper-band augmented literal returns: PASS', labelled)
    print('upper-band exact all-core target constructions: PASS', transports)
    print('upper-band existing complete input entries: PASS', entries)
    print('upper-band contraction inverse sandwiches: PASS', len(inverse_checks))
    print('upper-band general Smith inverse sandwiches: PASS', len(general_inverses))
    print('upper-band literal terminal tails: PASS', len(tails))
    record = {'scope': 'Finite exact checks of the general proof, not enumeration of input space; '
                       'principal subgroup containment uses external arithmetic-group theorems.',
              'uniform_theorem': 'p prime>=13, 3p+10<=n<=4p-3, gcd(n,6)=1: full G=1 criterion',
              'small_representatives': small_checks, 'descent_branches': sorted(branches),
              'parameter_systems': systems, 'principal_layer_checks': layers,
              'literal_returns': labelled, 'target_constructions': transports,
              'input_entries': entries, 'inverse_activation': inverse_checks,
              'general_inverse_activation': general_inverses, 'tail_lengths': tails}
    (Path(__file__).parent/'upper_band_six_unit_completion_records.json').write_text(
        json.dumps(record, indent=2)+'\n', encoding='utf-8')
    print('uniform upper-band coprime-six dimensions: PASS')


if __name__ == '__main__':
    main()
