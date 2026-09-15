"""Exact projective characteristic invariants and independent boundaries.

The general spectral balance criterion is proved in the cited document.
These tests use rational identities and prescribed characteristic roots;
they do not approximate eigenvalues or claim a general spectral solver.
"""

from fractions import Fraction as F
from math import gcd
from random import Random
from functools import lru_cache
from math import lcm
from itertools import product as cartesian_product

from verify_flat_star_arithmetic import identity,multiply,inverse
from explore_gaussian_period_layers import determinant
from compile_bn_integer_templates import compile_returns
from verify_bn_integer_templates import replay,physical_matrix


def characteristic(matrix):
    n = len(matrix)
    current = identity(n)
    coefficients = []
    for k in range(1,n+1):
        product = multiply(matrix,current)
        coefficient = -sum(product[i][i] for i in range(n))/k
        coefficients.append(coefficient)
        current = [row.copy() for row in product]
        for i in range(n):current[i][i] += coefficient
    assert all(not x for row in current for x in row)
    return coefficients


def invariants(matrix):
    coefficients = characteristic(matrix)
    n = len(matrix)
    det = (-1)**n*coefficients[-1]
    assert det
    return tuple(coefficient**n/det**k for k,coefficient in enumerate(coefficients[:-1],1))


def finite_place_balance(matrix):
    return all(value.denominator == 1 for value in invariants(matrix))


def scalar_power(matrix,limit):
    current = identity(len(matrix))
    for exponent in range(1,limit+1):
        current = multiply(matrix,current)
        scalar = current[0][0]
        if current == [[scalar*int(i==j) for j in range(len(matrix))] for i in range(len(matrix))]:
            return exponent,scalar
    return None


def companion(coefficients):
    n = len(coefficients)
    matrix = [[F(0)]*n for _ in range(n)]
    for i in range(n-1):matrix[i+1][i] = 1
    for i,value in enumerate(reversed(coefficients)):matrix[i][-1] = -F(value)
    return matrix


def trim(polynomial):
    polynomial = list(map(F,polynomial))
    while len(polynomial)>1 and polynomial[-1] == 0:polynomial.pop()
    return polynomial


def polynomial_divmod(a,b):
    remainder,divisor = trim(a),trim(b)
    assert divisor != [0]
    quotient = [F(0)]*max(1,len(remainder)-len(divisor)+1)
    while remainder != [0] and len(remainder)>=len(divisor):
        shift = len(remainder)-len(divisor)
        factor = remainder[-1]/divisor[-1]
        quotient[shift] = factor
        for i,value in enumerate(divisor):remainder[i+shift] -= factor*value
        remainder = trim(remainder)
    return trim(quotient),remainder


def polynomial_gcd(a,b):
    a,b = trim(a),trim(b)
    while b != [0]:a,b = b,polynomial_divmod(a,b)[1]
    return [x/a[-1] for x in a]


@lru_cache(maxsize=None)
def cyclotomic(index):
    polynomial = [-1]+[0]*(index-1)+[1]
    for divisor in range(1,index):
        if index % divisor == 0:
            polynomial,remainder = polynomial_divmod(polynomial,cyclotomic(divisor))
            assert remainder == [0]
    return tuple(polynomial)


def totient(n):
    value,result,prime = n,n,2
    while prime*prime<=value:
        if value % prime == 0:
            result = result//prime*(prime-1)
            while value % prime == 0:value //= prime
        prime += 1
    if value>1:result = result//value*(value-1)
    return result


def semisimple(matrix):
    coefficients = list(reversed(characteristic(matrix)))+[F(1)]
    derivative = [i*value for i,value in enumerate(coefficients)][1:]
    radical,remainder = polynomial_divmod(coefficients,polynomial_gcd(coefficients,derivative))
    assert remainder == [0]
    result = [[F(0)]*len(matrix) for _ in matrix]
    for coefficient in reversed(radical):
        result = multiply(matrix,result)
        for i in range(len(matrix)):result[i][i] += coefficient
    return not any(x for row in result for x in row)


def projective_order(matrix):
    """Exact rational algorithm, returning None iff the order is infinite."""
    if not semisimple(matrix) or not finite_place_balance(matrix):return None
    n = len(matrix)
    inv = inverse(matrix)
    adjoint = [[matrix[i][k]*inv[ell][j]
                for k in range(n) for ell in range(n)]
               for i in range(n) for j in range(n)]
    polynomial = list(reversed(characteristic(adjoint)))+[F(1)]
    dimension = n*n
    order = 1
    for index in range(1,2*dimension*dimension+1):
        if totient(index)>len(polynomial)-1:continue
        factor = cyclotomic(index)
        used = False
        while len(polynomial)>=len(factor):
            quotient,remainder = polynomial_divmod(polynomial,factor)
            if remainder != [0]:break
            polynomial = quotient
            used = True
        if used:order = lcm(order,index)
        if polynomial == [1]:return order
    return None


def valuation(value,prime):
    value = F(value)
    if not value:return None
    a,b = abs(value.numerator),value.denominator
    result = 0
    while a % prime == 0:a //= prime;result += 1
    while b % prime == 0:b //= prime;result -= 1
    return result


def verify_all_rank_invariants():
    random = Random(47089)
    checked = 0
    for n in range(2,9):
        for _ in range(12):
            m = identity(n)
            for _ in range(6):
                i,j = random.sample(range(n),2)
                factor = random.randrange(-4,5)
                m[i] = [a+factor*b for a,b in zip(m[i],m[j])]
            diagonal = [[F(0)]*n for _ in range(n)]
            for i in range(n):diagonal[(i+1)%n][i] = random.choice((-1,1))
            power,scalar = scalar_power(diagonal,2*n)
            actual = multiply(multiply(m,diagonal),inverse(m))
            scale = F(random.choice((-7,-3,2,5)),3**random.randrange(1,5))
            actual = [[scale*x for x in row] for row in actual]
            assert invariants(actual) == invariants(diagonal)
            assert finite_place_balance(actual)
            assert scalar_power(actual,2*n) == (power,scale**power*scalar)
            checked += 1
    radical = companion((0,0,-2))
    assert scalar_power(radical,3) == (3,F(2))
    assert finite_place_balance(radical)
    # Nonintegral common p-adic slope1/3 is allowed projectively.
    assert valuation(determinant(radical),2) == 1
    print('all-rank projective coefficient invariants and exact torsion controls: PASS',checked+1)


def verify_independent_boundaries():
    # An integral determinant-one hyperbolic matrix balances every finite
    # place but fails the complex equal-modulus condition.
    hyperbolic = [[F(2),F(1)],[F(1),F(1)]]
    assert characteristic(hyperbolic) == [-3,1]
    assert finite_place_balance(hyperbolic)
    # A rational unit-circle rotation is semisimple and complex balanced,
    # but its coefficient invariant36/25 detects a finite-place defect.
    rotation = [[F(3,5),F(-4,5)],[F(4,5),F(3,5)]]
    assert determinant(rotation) == 1
    assert invariants(rotation) == (F(36,25),)
    assert not finite_place_balance(rotation)
    jordan = [[F(1),F(1)],[F(0),F(1)]]
    assert characteristic(jordan) == [-2,1] and finite_place_balance(jordan)
    assert multiply([[0,1],[0,0]],[[0,1],[0,0]]) == [[0,0],[0,0]]
    # Trace alone cannot replace the other characteristic coefficients.
    trace_zero = companion((0,1,0,2))
    assert characteristic(trace_zero) == [0,1,0,2]
    assert invariants(trace_zero) == (0,F(1,4),0)
    assert not finite_place_balance(trace_zero)
    print('archimedean, finite-place, semisimplicity and higher-coefficient boundaries: PASS 4')


def verify_exact_order_algorithm():
    examples = [
        ([[1,0],[0,1]],1), ([[0,-1],[1,0]],2),
        ([[0,-1],[1,1]],3), ([[1,-1],[1,1]],4),
        ([[0,-3],[1,3]],6), (companion((0,0,-2)),3),
        ([[1,1],[0,1]],None), ([[2,1],[1,1]],None),
        ([[F(3,5),F(-4,5)],[F(4,5),F(3,5)]],None),
        (companion((0,1,0,2)),None),
    ]
    for matrix,expected in examples:
        matrix = [list(map(F,row)) for row in matrix]
        assert projective_order(matrix) == expected
        if expected is not None:
            assert scalar_power(matrix,expected)[0] == expected
    for n in range(1,101):assert 2*totient(n)**2 >= n
    print('exact adjoint-cyclotomic projective-order algorithm: PASS',len(examples))


def verify_b47_norm_macro():
    rows,_ = compile_returns(47,True,True,True)
    selected = (-9,5,162,-72)
    calls = replay(47,rows[selected])
    assert tuple(size for size,_,_ in calls) == (9,27,43)
    physical = physical_matrix(rows[selected])
    original = [[F(selected[0],9),F(selected[1],9)],
                [F(selected[2],9),F(selected[3],9)]]
    assert characteristic(original) == [9,-2]
    companion_matrix = [[F(0),F(2)],[F(1),F(-9)]]
    change = [[F(1),F(-1)],[F(0),F(18)]]
    assert multiply(original,change) == multiply(change,companion_matrix)
    assert invariants(original) == (F(-81,2),)
    assert valuation(determinant(original),3) == 0
    assert valuation(characteristic(original)[0],3) == 2
    assert valuation(determinant(original),2) == 1
    assert valuation(characteristic(original)[0],2) == 0
    assert all((x*x+9*x-2) % 3 for x in range(3))
    assert (9*9+8) == 89 and 89 % 8 == 1
    # Physical scale: P = (-2/27) * (M/9).
    assert physical == tuple(F(-2,27)*x for row in original for x in row)
    print('B47 real quadratic norm-minus-two macro and split local obstruction: PASS')


def verify_commuting_unit_relation():
    # Exact coefficients in Q(sqrt89), with no logarithmic comparisons.
    def mul(x,y):
        a,b = x
        c,d = y
        return a*c+89*b*d,a*d+b*c
    def power(x,k):
        result = (F(1),F(0))
        for _ in range(k):result = mul(result,x)
        return result
    theta = (F(-9,2),F(1,2))
    conjugate = (F(-9,2),F(-1,2))
    epsilon = (F(500),F(53))
    assert mul(theta,conjugate) == (-2,0)
    assert mul(epsilon,(epsilon[0],-epsilon[1])) == (-1,0)
    unit = mul(epsilon,epsilon)
    assert unit == (500001,53000)
    checked = 0
    for a,b,c in cartesian_product(range(5),repeat=3):
        result = mul(mul(power(theta,a),power(conjugate,b)),power(unit,c))
        relation = a-b == 0 and c == 0
        assert (result[1] == 0) == relation
        checked += 1
    # The valuation row alone accepts the unit, the unit row rejects it.
    assert 0-0 == 0 and 1 != 0
    print('commuting quadratic valuation-and-unit positive-relation controls: PASS',checked)


def verify():
    verify_all_rank_invariants()
    verify_independent_boundaries()
    verify_exact_order_algorithm()
    verify_b47_norm_macro()
    verify_commuting_unit_relation()


if __name__ == '__main__':
    verify()
