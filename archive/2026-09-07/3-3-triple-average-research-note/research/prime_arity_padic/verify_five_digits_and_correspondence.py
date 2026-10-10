"""Exact arithmetic checks for the digit obstruction and quotient curve."""
from fractions import Fraction as F
from itertools import product
from math import gcd, isqrt
from pathlib import Path
import json
from verify_subcritical_complement_dynamics import core_distance
from verify_five_padic_fractal import A, B, mv, mod_direction


def w_of(u, v):
    return F((u+v)**2, u*v)


def relation(w, z):
    return 9*(w-4)*z*z+3*(w-4)*(w-25)*z-(4*w-25)**2


def period_table():
    rows = []
    for k in range(1, 13):
        a = (-3)**k
        point = F(4*a, a-5)
        q = abs(a-5)//4
        assert point.denominator == q
        assert q % 3
        assert core_distance(3, a, (a-5)//4) == k+1
        if q == 1:
            period = 1
        else:
            residue, period = 3 % q, 1
            while residue != 1:
                residue = residue*3 % q
                period += 1
        assert (3**period-1) % q == 0
        rows.append({'k': k, 'reduced_denominator': q, 'eventual_ternary_period': period})
    return rows


def finite_digit_diagnostics():
    rows = []
    for k in (5, 7, 9, 11, 13):
        modulus = 3**k
        e = mod_direction((1,-1), modulus)
        seen, todo = {e}, [e]
        while todo:
            x = todo.pop()
            for M in (A, B):
                z = mod_direction(mv(M,x), modulus)
                if z not in seen:
                    seen.add(z)
                    todo.append(z)
        slopes = [u for u,v in seen if v == 1]
        assert len(slopes) == 2**k
        prefix_depth = k//2
        groups = {}
        for z in slopes:
            groups.setdefault(z % (3**prefix_depth), set()).add(z//(3**prefix_depth))
        distinct = len({tuple(sorted(v)) for v in groups.values()})
        rows.append({'depth': k, 'prefix_depth': prefix_depth,
                     'allowed_prefixes': len(groups), 'distinct_finite_continuation_sets': distinct})
    return rows


def curve_identities():
    checked = 0
    for u in range(-65,66):
        for v in range(-65,66):
            if gcd(u,v) != 1 or u*v == 0 or u == v:
                continue
            t, w = F(u,v), w_of(u,v)
            assert w*(w-4) == F((u*u-v*v)**2,(u*v)**2)
            first, second = mv(A,(u,v)), mv(B,(u,v))
            z1, z2 = w_of(*first), w_of(*second)
            assert relation(w,z1) == relation(w,z2) == 0
            assert z1+z2 == (25-w)/3
            assert z1*z2 == -(4*w-25)**2/(9*(w-4))
            z = (t-4)**2/(3*(1-t))
            assert z == z2
            assert 3*(z-5)/(w+3*z-10) == t
            c = -F(u+v,5)
            physical = (c,c,c,c+u,c+v)
            E = sum(x*x for x in physical)
            assert 50*c*c/(20*c*c-E) == w
            assert core_distance(3,u,v) == core_distance(3,v,u)
            assert relation(w,w) == (4*w-25)*(3*w*w-16*w+25)
            # Both projections, their deck involutions and the new relative norm.
            back_discriminant = (9*z*z-87*z+200)**2-4*(3*z-16)*(-36*z*z+300*z-625)
            assert back_discriminant == 81*z*(z-4)*(z-5)**2
            tau = (t+8)/(t-1)
            assert (tau-4)**2/(3*(1-tau)) == z
            Q5 = lambda x,y: x*x+7*x*y+y*y
            assert Q5(v,u) == Q5(u,v)
            assert Q5(u+8*v,u-v) == 9*Q5(u,v)
            checked += 1
    assert relation(F(-5),F(5)) == 0
    assert isqrt(45)**2 != 45
    assert core_distance(3,1,4) is None and relation(F(25,4),F(25,4)) == 0
    assert core_distance(3,-7,2) is None
    return checked


def full_positive_orbit():
    layer = {(1,-1)}
    checked = 0
    for depth in range(11):
        scalar_layer = {w_of(*x) for x in layer}
        assert len(scalar_layer) == (1 if depth == 0 else 2**(depth-1))
        for x in layer:
            w = w_of(*x)
            assert core_distance(3,*x) == depth+1
            for M in (A,B):
                z = w_of(*mv(M,x))
                assert relation(w,z) == 0
                checked += 1
        layer = {mv(M,x) for x in layer for M in (A,B)}
    return checked


if __name__ == '__main__':
    if not __debug__:
        raise RuntimeError('Assertions required.')
    result = {'isolated_point_periods': period_table(),
              'finite_digit_diagnostics': finite_digit_diagnostics(),
              'rational_curve_identities': curve_identities(),
              'positive_orbit_edges': full_positive_orbit(),
              'scope': 'Proof gives nonregularity only for ordinary slope-prefix language; quotient curve retains directed reachability.'}
    Path(__file__).with_name('five_digits_and_correspondence_verification.json').write_text(
        json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))
