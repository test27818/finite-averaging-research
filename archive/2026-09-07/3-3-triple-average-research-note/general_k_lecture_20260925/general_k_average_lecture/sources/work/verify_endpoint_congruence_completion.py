"""Check the explicit algebra in the endpoint congruence completion.

Finite quotient checks are not a proof of the external finite-index or
congruence subgroup theorems. No averaging-word discovery is performed.
"""

from collections import deque
from fractions import Fraction as F
from math import gcd, prod
from pathlib import Path
from random import Random
import json

from verify_prime_power_endpoint_completion import Compiler

if not __debug__:
    raise RuntimeError('Assertions are required.')

I = (1, 0, 0, 1)
ROOT = Path(__file__).resolve().parent


def mm(a, b):
    return (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
            a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3])


def inverse(a):
    assert a[0]*a[3]-a[1]*a[2] == 1
    return a[3], -a[1], -a[2], a[0]


def prime_divisors(n):
    out, d = [], 2
    while d*d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def finite_group(modulus, level):
    seen, queue = {I}, deque([I])
    while queue:
        a, b, c, d = queue.popleft()
        for nxt in ((a, (a+b) % modulus, c, (c+d) % modulus),
                    ((a+level*b) % modulus, b, (c+level*d) % modulus, d)):
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return seen


def quotient_word(matrix, level, modulus):
    assert modulus % level == 0 and modulus % 2
    a, b, c, d = matrix
    assert (a*d-b*c) % modulus == 1
    assert (a-1) % level == (d-1) % level == c % level == 0
    # Choose the pivot modulo each prime without scanning possible shears.
    primes = prime_divisors(modulus)
    radical = prod(primes)
    shear = sum((radical//q)*pow(radical//q, -1, q)
                for q in primes if a % q == 0) % radical
    pivot = (a+shear*c) % modulus
    assert gcd(pivot, modulus) == 1
    reciprocal = pow(pivot, -1, modulus)
    upper_right = (b+shear*d) % modulus
    word = [('U', -shear), ('L', c*reciprocal),
            ('U', 1), ('L', pivot-1), ('U', -reciprocal),
            ('L', -pivot*(pivot-1)), ('U', upper_right*reciprocal)]
    result = I
    for kind, value in word:
        value %= modulus
        if kind == 'L':
            assert value % level == 0
            atom = (1, 0, value, 1)
        else:
            atom = (1, value, 0, 1)
        result = tuple(x % modulus for x in mm(result, atom))
    assert result == matrix
    return shear, word


def small_pivot_representative(n, residue):
    p = (n-1)//2
    u = (residue+p) % n-p
    assert u and abs(u) <= p and gcd(u, n) == 1
    assert all(ell <= p and n % ell for ell in prime_divisors(abs(u)))
    d = pow(u, -1, n)
    b = (u*d-1)//n
    representative = (u, b, n, d)
    assert u*d-b*n == 1
    factors = ((1, 0, F(n, u), 1), (u, 0, 0, F(1, u)),
               (1, F(b, u), 0, 1))
    assert mm(mm(factors[0], factors[1]), factors[2]) == representative
    return representative


def main():
    cases, elements, decompositions = 0, 0, 0
    records = []
    for modulus in (3, 5, 7, 9, 15, 21, 25, 27, 35, 45):
        full = finite_group(modulus, 1)
        expected_order = modulus**3
        for ell in prime_divisors(modulus):
            expected_order = expected_order//(ell*ell)*(ell*ell-1)
        assert len(full) == expected_order
        for level in range(1, modulus+1, 2):
            if modulus % level:
                continue
            target = {g for g in full if (g[0]-1) % level == 0
                      and (g[3]-1) % level == 0 and g[2] % level == 0}
            generated = full if level == 1 else finite_group(modulus, level)
            assert generated == target
            for matrix in sorted(target)[::max(1, len(target)//200)]:
                quotient_word(matrix, level, modulus)
                decompositions += 1
            records.append({'modulus': modulus, 'level': level,
                            'group_size': len(target)})
            cases += 1
            elements += len(target)
    print('finite congruence images: PASS', cases, elements)
    print('constructive quotient decompositions: PASS', decompositions)

    rng, unit_checks, coset_checks = Random(20260914), 0, 0
    for n in list(range(7, 300, 4))+[315, 1155, 15015, 435435, 4849845]:
        residues = list(range(1, n)) if n < 300 else [rng.randrange(1, n) for _ in range(128)]
        for residue in residues:
            if gcd(residue, n) != 1:
                continue
            representative = small_pivot_representative(n, residue)
            unit_checks += 1
            u, b, c, d = representative
            g = mm(representative, mm((1, rng.randrange(-100, 101), 0, 1),
                                     (1, 0, n*rng.randrange(-100, 101), 1)))
            selected = small_pivot_representative(n, g[0])
            residual = mm(inverse(selected), g)
            assert (residual[0]-1) % n == (residual[3]-1) % n == residual[2] % n == 0
            coset_checks += 1
    print('balanced unit and coset reduction: PASS', unit_checks, coset_checks)

    physical = 0
    for p in (3, 5, 7, 13, 17, 19, 31):
        compiler = Compiler(p)
        n = 2*p+1
        for residue in (1, 2, p, n-2):
            if gcd(residue, n) != 1:
                continue
            matrix = small_pivot_representative(n, residue)
            expression = compiler.gauss(matrix)
            compiler.program.check(expression, matrix)
            assert expression.back is not None
            physical += 1
    print('existing positive compiler coset representatives: PASS', physical)
    result = {'scope': 'Finite formula checks; external theorems carry infinite group equality.',
              'finite_cases': cases, 'finite_elements': elements,
              'decompositions': decompositions, 'unit_checks': unit_checks,
              'coset_checks': coset_checks, 'positive_compiler_checks': physical,
              'finite_records': records}
    (ROOT/'endpoint_congruence_completion_records.json').write_text(
        json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print('endpoint congruence completion algebra: PASS')


if __name__ == '__main__':
    main()
