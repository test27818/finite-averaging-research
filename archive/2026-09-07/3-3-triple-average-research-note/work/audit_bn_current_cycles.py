"""Audit short positive cycles without an expanding word search.

The A^j B test is exhaustive for all j>=0: finite projective order gives
five quadratic trace equations in t=(-1/3)^j, solved over the rationals.
"""

import argparse
from fractions import Fraction
from math import isqrt

from compile_bn_integer_templates import compile_returns, primitive_matrix
from explore_b17_integral_return_cover import mul
from verify_twenty_five_arithmetic_group import finite_order


def rational_roots(a,b,c):
    if not a:
        if b:
            return {Fraction(-c,b)}
        return {Fraction(1)} if not c else set()
    discriminant = b*b-4*a*c
    if discriminant < 0:
        return set()
    root = isqrt(discriminant)
    if root*root != discriminant:
        return set()
    return {Fraction(-b+root,2*a),Fraction(-b-root,2*a)}


def triadic_exponent(value):
    if abs(value.numerator) != 1:
        return None
    denominator = value.denominator
    exponent = 0
    while denominator % 3 == 0:
        denominator //= 3
        exponent += 1
    if denominator != 1 or value.numerator != (-1)**exponent:
        return None
    return exponent


def a_power_candidates(n,matrix):
    a,b,c,d = matrix
    r = n-4
    upper,lower = 4*a-r*b,4*d+r*b
    determinant = a*d-b*c
    exponents = set()
    for k in range(5):
        for root in rational_roots(lower*lower,2*upper*lower-16*k*determinant,upper*upper):
            exponent = triadic_exponent(root)
            if exponent is not None:
                exponents.add(exponent)
    result = []
    A = (-3,0,r,1)
    power = (1,0,0,1)
    previous = 0
    for exponent in sorted(exponents):
        for _ in range(exponent-previous):
            power = primitive_matrix(mul(A,power))
        previous = exponent
        order = finite_order(mul(power,matrix))
        if order:
            result.append((exponent,order))
    return result


def audit(n):
    rows,_ = compile_returns(n,True,True)
    keys = sorted(set(rows)|{(-3,0,n-4,1)})
    pairs = []
    for i,a in enumerate(keys):
        for b in keys[i:]:
            order = finite_order(mul(a,b))
            if order:
                pairs.append((a,b,order))
    powers = [(matrix,result) for matrix in rows
              if (result := a_power_candidates(n,matrix))]
    print('current B library',n,'templates',len(rows),'pair tests',len(keys)*(len(keys)+1)//2)
    print('finite positive two-factor cycles',len(pairs))
    print('finite A^j B cycles for all j>=0',len(powers))
    if n == 29:
        assert len(rows) == len(keys) == 1195 and not pairs and not powers
        print('B29 current-library two-factor and all-exponent A-power boundary: PASS 1195 714610')
    return pairs,powers


def verify_trace_solver():
    n,r = 29,25
    inverse = (1,0,-r,-3)
    for exponent in (0,1,2,14,57,100):
        matrix = (1,0,0,1)
        for _ in range(exponent):
            matrix = primitive_matrix(mul(inverse,matrix))
        assert (exponent,1) in a_power_candidates(n,matrix)
    off_diagonal = (4*r,16,-r*r-1,-4*r)
    assert (0,2) in a_power_candidates(n,off_diagonal)
    print('all-exponent trace solver scalar and involution controls: PASS 7')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--n',type=int,default=29)
    verify_trace_solver()
    audit(parser.parse_args().n)
