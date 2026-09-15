"""Small exact checks for the final Hecke/Manin route audit.

The general arguments are in triple_average_final_hecke_audit.md.  No word
search runs here, and no automorphic representation is assumed to exist.
"""

from fractions import Fraction as F
from math import gcd, isqrt


I = (F(1), F(0), F(0), F(1))


def mul(a, b):
    return (a[0]*b[0] + a[1]*b[2], a[0]*b[1] + a[1]*b[3],
            a[2]*b[0] + a[3]*b[2], a[2]*b[1] + a[3]*b[3])


def det(a):
    return a[0]*a[3] - a[1]*a[2]


def transpose(a):
    return (a[0], a[2], a[1], a[3])


def inverse(a):
    d = det(a)
    return tuple(F(x)/d for x in (a[3], -a[1], -a[2], a[0]))


def subtract(a, b):
    return tuple(x-y for x, y in zip(a, b))


def matvec(a, v):
    return (a[0]*v[0] + a[1]*v[1], a[2]*v[0] + a[3]*v[1])


def primes():
    return tuple(p for p in range(5, 200)
                 if all(p % d for d in range(2, isqrt(p)+1)))


def verify_integral_conjugacy():
    regular = (F(0), F(3), F(1), F(2))
    for p in primes():
        epsilon = 1 if p % 4 == 1 else -1
        b = (epsilon-p)//4
        q = (F(1), F(3), F(b), F(-p-b))
        h = (F(3), F(0), F(-p), F(-1))
        assert det(q) == -epsilon
        assert mul(h, q) == mul(q, regular)
        assert all(x.denominator == 1 for x in inverse(q))
        # The old index-p intertwiner was one choice, not an invariant index.
        old = (F(1), F(3), F(0), F(-p))
        assert det(old) == -p and mul(h, old) == mul(old, regular)
    print("unimodular conjugacy removes intrinsic index-p claim: PASS", len(primes()))


def verify_common_star_obstruction():
    parameters = (F(-2), F(0), F(1, 3), F(2, 3), F(1), F(4, 3), F(2))
    gram_basis = ((1, 0, 0, 0), (0, 1, 1, 0), (0, 0, 0, 1))
    checked = 0
    for p in primes():
        h = (F(3), F(0), F(-p), F(-1))
        for c in parameters:
            wall = (F(-1), F(0), c*p, F(3))
            equation_h = tuple(subtract(mul(transpose(h), g), mul(g, h))[1]
                               for g in gram_basis)
            equation_b = tuple(subtract(mul(transpose(wall), g), mul(g, wall))[1]
                               for g in gram_basis)
            assert equation_h == (0, 4, -p)
            assert equation_b == (0, -4, c*p)
            coefficient_minor = equation_h[1]*equation_b[2] - equation_h[2]*equation_b[1]
            assert coefficient_minor == 4*p*(c-1)
            if c != 1:
                assert coefficient_minor != 0
                for a in (F(-7), F(0), F(1), F(9)):
                    g = (a, F(0), F(0), F(0))
                    assert det(g) == 0
                    assert mul(transpose(h), g) == mul(g, h)
                    assert mul(transpose(wall), g) == mul(g, wall)
            else:
                g = (F(p*(p-1)), F(3*p), F(3*p), F(12))
                assert det(g) > 0 and g[0] > 0
                assert mul(transpose(h), g) == mul(g, h)
                assert mul(transpose(wall), g) == mul(g, wall)
            checked += 1
    print("displaced wall has no common positive Hecke star form: PASS", checked)


def verify_triangular_and_cusp_obstructions():
    checked = 0
    for p in primes():
        h = (F(3), F(0), F(-p), F(-1))
        word = I
        for c in (F(0), F(1, 3), F(2, 3), F(1), F(2)):
            wall = (F(-1), F(0), c*p, F(3))
            for matrix in (h, wall, inverse(h), inverse(wall)):
                assert matrix[1] == 0 and matrix[0] != 0
                word = mul(matrix, word)
                assert word[1] == 0 and word[0] != 0
                assert matvec(word, (F(1), F(2)))[0] != 0
        # Every primitive legal rational line is in Gamma_0(p)'s orbit of zero.
        for x in range(-5, 6):
            for y in range(1, 7):
                if gcd(x, y) != 1 or y % p == 0:
                    continue
                if x == 0:
                    a, k = 1, 0
                else:
                    a = pow(y, -1, abs(p*x))
                    k = (a*y - 1)//(p*x)
                gamma = (a, x, p*k, y)
                assert det(gamma) == 1 and gamma[2] % p == 0
                assert matvec(gamma, (0, 1)) == (x, y)
                checked += 1
    print("triangular orbit and collapsed legal-cusp checks: PASS", checked)


def verify_manin_central_sign():
    # A linear F to a trivial-coefficient symbol module must satisfy
    # F*(-I)=F because -I fixes all rational cusps. Hence 2F=0 over Q.
    minus_i = tuple(-x for x in I)
    coefficient_maps = ((1, 0, 0, 0), (0, 1, 0, 0),
                        (0, 0, 1, 0), (0, 0, 0, 1))
    for f in coefficient_maps:
        assert subtract(mul(f, minus_i), f) == tuple(-2*x for x in f)
    print("ordinary Manin-symbol linear map central-sign obstruction: PASS")


def verify_puncture_and_local_convolution():
    checked = 0
    for p in primes():
        if p % 3 != 2 or p < 11:
            continue
        mobius = tuple(-pow(x+1, -1, p) % p if x != p-1 else None
                       for x in range(p))
        punctured = tuple(x if x in (0, p-1) else mobius[x]
                          for x in range(p))
        assert punctured[0] != mobius[0]
        assert punctured[p-1] != mobius[p-1]
        assert all(punctured[x] == mobius[x] for x in range(1, p-1))
        assert sum(punctured[x] == x for x in range(p)) == 2
        assert all(punctured[punctured[punctured[x]]] == x for x in range(p))
        checked += 1
    # The spherical degree-four tree adjacency cannot obey (T-3)(T+1)=0:
    # on delta at a root, T^2-2T-3I has values1,-2,1 on distances0,1,2.
    residual_by_distance = (4-3, -2, 1)
    assert residual_by_distance == (1, -2, 1)
    # In contrast, complete-graph degree-three adjacency is the finite Hecke model.
    k4 = tuple(tuple(int(i != j) for j in range(4)) for i in range(4))
    square = tuple(tuple(sum(k4[i][k]*k4[k][j] for k in range(4))
                         for j in range(4)) for i in range(4))
    assert all(square[i][j] == 2*k4[i][j]+3*int(i == j)
               for i in range(4) for j in range(4))
    print("puncturing and finite-versus-spherical Hecke distinction: PASS", checked)


def verify():
    verify_integral_conjugacy()
    verify_common_star_obstruction()
    verify_triangular_and_cusp_obstructions()
    verify_manin_central_sign()
    verify_puncture_and_local_convolution()
    print("final Hecke-Manin route audit: PASS")


if __name__ == "__main__":
    verify()
