"""Four existing upper-band involutions give opposite localized root groups.

Only closed capacity formulas and exact matrix arithmetic are used. Literal
returns are independently replayed on the original positions. No terminal
coverage or new solved dimension is asserted by these checks.
"""

from fractions import Fraction as F
from math import gcd

from verify_four_prime_entry_and_band import Ledger, factors
from verify_uniform_odd_middle_cores import mm, invq
from verify_upper_band_descent_boundary import apply_return
from verify_upper_band_three_value_reduction import core_state

if not __debug__:
    raise RuntimeError('Assertions are required.')


def ranges(p, r):
    a = ((2*p-r+5)//6, min((2*p-r)//4, p//3))
    b = (max(0, (2*p-3*r+5)//6), (p-r)//3)
    return a, b


def system(p, r):
    (j, ja), (k, kb) = ranges(p, r)
    assert ja >= j+1 and kb >= k+1
    n = 3*p+r
    d, e = p*p-n*j, p*p-n*(j+1)
    b = n*k-p*p+r*p
    mu, nu = r*r+2*b, r*r+2*(b+n)
    aj, aq = (0, -d, -1, 0), (0, -e, -1, 0)
    bk, bq = (r, b, 2, -r), (r, b+n, 2, -r)
    assert d*e*mu*nu and gcd(d, e) == 1
    assert gcd(mu, nu) == (1 if r % 2 else 2)
    assert all(gcd(value, n) == 1 for value in (d, e, mu, nu))
    assert r % 2 or d*e % 2 == 0
    for matrix, scalar in zip((aj, aq, bk, bq), (d, e, mu, nu)):
        assert mm(matrix, matrix) == (scalar, 0, 0, scalar)
    diagonal = mm(invq(aj), aq)
    affine = mm(invq(bk), bq)
    assert diagonal == (1, 0, 0, F(e, d))
    assert affine == (1, F(r*n, mu), 0, F(nu, mu))
    upper = mm(mm(mm(diagonal, affine), invq(diagonal)), invq(affine))
    parameter = F(r*n*n, e*nu)
    assert upper == (1, parameter, 0, 1)
    lower = mm(mm(aj, upper), invq(aj))
    assert lower == (1, 0, parameter/d, 1)
    # Upper-affine translations cancel when conjugating a root.
    assert mm(mm(affine, upper), invq(affine)) == (1, parameter*F(mu, nu), 0, 1)
    return [(name, index, matrix, scalar) for name, index, matrix, scalar in (
        ('A', j, aj, d), ('A', j+1, aq, e), ('B', k, bk, mu), ('B', k+1, bq, nu))]


def physical(p, r, returns):
    checked = 0
    for a, z in ((1, 0), (0, 1)):
        y = a+p*z
        raw = core_state(p, r, y, z)
        for carrier, j, matrix, scalar in returns:
            s = p-3*j if carrier == 'A' else p-r-3*j
            i = p-j-s
            assert 0 <= 2*s <= r and i >= 0
            assert 2*i <= 2*p-(r if carrier == 'A' else 0)
            assert 2*j <= p-(r if carrier == 'B' else 0)
            groups = [list(range(2*p)), list(range(2*p, 3*p)), list(range(3*p, 3*p+r))]
            ledger = Ledger(raw, p)
            groups = apply_return(ledger, groups, carrier, j, s)
            aa = F(matrix[0]*a+matrix[1]*z, p)
            zz = F(matrix[2]*a+matrix[3]*z, p)
            expected = (aa, -2*aa+r*zz, -p*zz)
            assert [ledger.state[group[0]] for group in groups] == list(expected)
            assert all(ledger.state[index] == value
                       for group, value in zip(groups, expected) for index in group)
            groups = apply_return(ledger, groups, carrier, j, s)
            scale = F(scalar, p*p)
            assert [ledger.state[group[0]] for group in groups] == [scale*a, scale*(-2*a+r*z), -scale*p*z]
            ledger.independent_replay(raw)
            checked += 1
    return checked


def main():
    parameters = uniform_capacities = literal = 0
    for p in range(5, 160):
        if factors(p) != {p: 1}:
            continue
        for r in range(1, p):
            intervals = ranges(p, r)
            available = all(high >= low+1 for low, high in intervals)
            if p >= 13 and 10 <= r <= p-3:
                assert available
                uniform_capacities += 1
            if available:
                returns = system(p, r)
                parameters += 1
                if p <= 29:
                    literal += physical(p, r, returns)
        a, b = ranges(p, 1)
        assert a[1] < a[0]
        assert max(0, b[1]-b[0]+1) == (1 if p % 3 == 1 else 0)
    print('upper-band four-return matrix systems: PASS', parameters)
    print('upper-band uniform interior capacities: PASS', uniform_capacities)
    print('upper-band literal four-return checks: PASS', literal)
    print('upper-band first-fringe capacity boundary: PASS')
    print('upper-band deep congruence interface: PASS')


if __name__ == '__main__':
    main()
