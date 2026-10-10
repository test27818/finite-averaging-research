"""Small exact audits of the structural claims in the strategy review.

The proof uses formulas for arbitrary parameters; no averaging-word search.
"""

from fractions import Fraction as F
from itertools import combinations, product
from math import gcd


def mul(a, b):
    return (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
            a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3])


def verify_modular_preparation_obstruction():
    p, r, modulus = 61, 28, 30
    labels = [0, 0]+[0]*20+[16]+[21]*4+[25]*2+[-150]
    weights = [p, p]+[1]*r
    assert len(labels) == r+2
    assert sum(weights) == 150 and sum(w*x for w, x in zip(weights, labels)) == 0
    assert gcd(*labels) == gcd(*(x-labels[0] for x in labels)) == 1
    for q in (2, 3, 5):
        assert len({x % q for x in labels}) > 1
    assert {x % modulus for x in labels} == {0, 16, 21, 25}
    assert all(gcd(x-y, modulus) > 1 for x, y in combinations(labels, 2))
    inverse = pow(p, -1, modulus)
    checked = 0
    for block in (0, 1):
        for carrier in range(2, len(labels)):
            result = list(labels)
            result[block] = ((p-1)*labels[block]+labels[carrier])*inverse % modulus
            result[carrier] = labels[block] % modulus
            assert sorted(x % modulus for x in result) == sorted(x % modulus for x in labels)
            checked += 1
    print('multiprime unit-separation obstruction: PASS', checked)


def verify_two_step_pair_alphabet():
    letters = 0
    types = {(1, b, 0, d) for b, d in product((0, 1), repeat=2)}
    for a, b in product(types, repeat=2):
        c = tuple(x % 2 for x in mul(a, b))
        assert c in types
        assert c[3] == a[3]*b[3]
    for p in range(3, 60, 2):
        for s in (0, 1, 2):
            for i in range(p-1):
                if p-s-i < 0 or p-2-i < 0 or s+i > p:
                    continue
                # Leaves two old a positions; s carriers in first averaged block.
                # Acts on (u,v) with actual factor 1/p.
                matrix = (-1, -1, (1-s)*(p+1), 2*i-p+s+1)
                assert tuple(x % 2 for x in matrix) in types
                assert matrix[3] % 2 == (s == 1)
                assert matrix[0]*matrix[3]-matrix[1]*matrix[2] != 0
                letters += 1
        for k in range(p+1):
            matrix = p, 0, 0, 2*k-p
            assert tuple(x % 2 for x in matrix) == (1, 0, 0, 1)
            letters += 1
    print('uniform pair-return two-adic semigroup character: PASS', letters, len(types)**2)


def verify_general_coalescence():
    count = 0
    for p in (3, 5, 7, 11, 13):
        for r in range(1, p+1):
            for a, b in ((2, -1), (0, 3), (-5, 7)):
                singles = list(range(r-1))
                singles.append(-p*(a+b)-sum(singles))
                averaged = (F((p-r)*a+sum(singles), p), b, a)
                assert averaged[0] == -b-F(r, p)*a
                assert p*averaged[0]+p*averaged[1]+r*averaged[2] == 0
                for ell in range(2, 2*p+r+1):
                    if (2*p+r) % ell or gcd(p, ell) > 1 or any(ell % d == 0 for d in range(2, int(ell**.5)+1)):
                        continue
                    residues = [int(F(x).numerator*pow(F(x).denominator, -1, ell) % ell)
                                for x in averaged]
                    assert (len(set(residues)) == 1) == ((a-b) % ell == 0)
                count += 1
    print('general r-carrier one-step compression identities: PASS', count)


if __name__ == '__main__':
    verify_modular_preparation_obstruction()
    verify_two_step_pair_alphabet()
    verify_general_coalescence()
    print('strategy interface structural audits: PASS')
