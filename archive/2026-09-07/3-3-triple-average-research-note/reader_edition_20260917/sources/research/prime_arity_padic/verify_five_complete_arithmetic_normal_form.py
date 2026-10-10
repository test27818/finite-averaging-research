"""Exact audit of the complete arithmetic form, not a new closed-form oracle."""
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement
from math import gcd
from pathlib import Path
import json
from verify_subcritical_complement_dynamics import core_distance, initial_distance


def normal_form(u, v):
    if not (u or v):
        return ('zero', (), 0)
    d = gcd(u, v)
    u, v = u//d, v//d
    if u+v == 0:
        return ('terminal', (), 1)
    if not u or not v:
        return None
    swapped = False
    if u % 3:
        if v % 3:
            return None
        u, v = v, u
        swapped = True
    digits = []
    while u+v != 0:
        if not u or u % 3:
            return None
        k, quotient = 0, u
        while quotient % 3 == 0:
            quotient //= 3
            k += 1
        a = (-3)**k
        gamma = (a-1)//4
        # Inverse of P_k: (v - gamma*u/a, u/a).
        second = u//a
        assert u % a == 0
        u, v = v-gamma*second, second
        assert gcd(u, v) == 1
        digits.append(k)
    return (swapped, tuple(digits), 1+sum(digits))


def evaluate(digits):
    value = F(-1)
    for k in reversed(digits):
        a = (-3)**k
        b = (a-1)//4
        value = a/(b+value)
    return value


def compositions(total):
    if not total:
        yield ()
    else:
        for k in range(1, total+1):
            for rest in compositions(total-k):
                yield (k,)+rest


def multiply(A, B):
    return tuple(sum(A[2*i+k]*B[2*k+j] for k in range(2))
                 for i in range(2) for j in range(2))


def determinant4(rows):
    a = [list(map(F, row)) for row in rows]
    out = F(1)
    for i in range(4):
        j = next(j for j in range(i, 4) if a[j][i])
        if j != i:
            a[i], a[j] = a[j], a[i]
            out = -out
        z = a[i][i]
        out *= z
        a[i] = [t/z for t in a[i]]
        for j in range(i+1, 4):
            z = a[j][i]
            a[j] = [x-z*y for x, y in zip(a[j], a[i])]
    return out


def run():
    pairs = 0
    successes = 0
    for u in range(-150, 151):
        for v in range(-150, 151):
            result = normal_form(u, v)
            oracle = core_distance(3, u, v)
            assert (result is not None) == (oracle is not None), (u, v)
            if result is not None:
                assert result[2] == oracle
                if result[0] not in ('zero', 'terminal'):
                    oriented = F(v, u) if result[0] else F(u, v)
                    assert evaluate(result[1]) == oriented
                successes += 1
            pairs += 1
    fractions = 0
    distinct = set()
    for total in range(1, 13):
        for digits in compositions(total):
            value = evaluate(digits)
            assert value not in distinct
            distinct.add(value)
            result = normal_form(value.numerator, value.denominator)
            assert result == (False, digits, total+1)
            fractions += 1
    inputs = 0
    for x in combinations_with_replacement(range(-5, 6), 5):
        S = sum(x)
        # Integral centered representative, valid also when mean is fractional.
        centered = tuple(5*t-S for t in x)
        actual = initial_distance(3, centered) is not None
        expected = False
        for i, j in combinations(range(5), 2):
            U = 4*x[i]+x[j]-S
            V = x[i]+4*x[j]-S
            c = F(S-x[i]-x[j], 3)
            assert F(U, 3) == x[i]-c and F(V, 3) == x[j]-c
            if normal_form(U, V) is not None:
                expected = True
        assert expected == actual, x
        inputs += 1
    A, B, I = (-3, 0, -1, 1), (1, -1, 0, -3), (1, 0, 0, 1)
    AB, BA = multiply(A, B), multiply(B, A)
    assert determinant4([I, A, B, AB]) == 15
    bracket = tuple(a-b for a, b in zip(AB, BA))
    assert multiply(bracket, bracket) == (-15, 0, 0, -15)
    assert (A[0]+4*A[1], A[2]+4*A[3]) == (-3, 3)
    assert core_distance(3, 1, 4) is None
    P, Pinv = (1, 0, 4, 1), (1, 0, -4, 1)
    assert multiply(multiply(Pinv, A), P) == (-3, 0, 15, 1)
    assert multiply(multiply(Pinv, B), P) == (-3, -1, 0, 1)
    for matrix in (A, B):
        assert tuple(a+2*b-3*c for a, b, c in
                     zip(multiply(matrix, matrix), matrix, I)) == (0,)*4
    assert tuple(a+b+2*c+2*d+9*e for a,b,c,d,e in zip(AB,BA,A,B,I)) == (0,)*4
    C = tuple(a+2*b for a,b in zip(A,I))
    assert C == (-1,0,-1,3) and multiply(A,C) == (3,0,0,3)
    assert (C[0]-C[1],C[2]-C[3]) == (-1,-4)
    # Integer module image has index5, while positive orbit is strictly smaller.
    assert 1*(-2)-(-1)*(-3) == -5
    basis_module_checks = 0
    for u in range(-30,31):
        for v in range(-30,31):
            if (u+v) % 5:
                continue
            beta = -(u+v)//5
            alpha = u+3*beta
            assert (alpha-3*beta,-alpha-2*beta) == (u,v)
            basis_module_checks += 1
    # Exact conjugation into signed ternary Stern--Brocot-type coordinates.
    H = (4,-1,1,-4)
    Hinv = tuple(F(x,15) for x in H)
    assert multiply(multiply(H,A),Hinv) == (-3,1,0,1)
    assert multiply(multiply(H,B),Hinv) == (1,0,1,-3)
    result = {'integer_pairs_checked': pairs, 'solvable_pairs': successes,
              'all_compositions_up_to_total_12': fractions,
              'original_input_multisets': inputs,
              'integer_module_image_checks': basis_module_checks,
              'matrix_algebra_and_group_false_positive': 'PASS',
              'scope': 'Complete arithmetic reformulation, still not a fixed gcd-style criterion.'}
    Path(__file__).with_name('five_complete_arithmetic_normal_form_verification.json').write_text(
        json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    if not __debug__:
        raise RuntimeError('Assertions required.')
    run()
