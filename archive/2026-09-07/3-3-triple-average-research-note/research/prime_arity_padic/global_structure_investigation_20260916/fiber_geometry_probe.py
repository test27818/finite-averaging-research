"""Explore bounded equal-determinant fibers, never averaging-word search."""
from math import gcd
from fractions import Fraction as F


def fiber(p, r, sources, source, base):
    i, j, k = source
    alpha, beta = i-j, r*j-p*k
    assert 0 < alpha < p and i+j+k == p
    stock = (p-sources*i, p-sources*j, r-sources*k, sources*p-r)
    assert min(stock) >= 0
    assert sum(base) == p and all(0 <= a <= b for a, b in zip(base, stock))
    n = 2*p+r
    A0 = p*alpha-beta
    coeff = (A0, alpha*n-A0, alpha*p)
    value = coeff[0]*base[0]+coeff[1]*base[1]+coeff[2]*base[3]
    points = []
    for x in range(stock[0]+1):
        for y in range(stock[1]+1):
            numerator = value-coeff[0]*x-coeff[1]*y
            if numerator % coeff[2]:
                continue
            v = numerator//coeff[2]
            u = p-x-y-v
            if 0 <= u <= stock[2] and 0 <= v <= stock[3]:
                points.append((x, y, u, v))
    root = F(0)
    g = gcd(alpha, beta)
    step_indices = []
    for point in points:
        X, Y, _, V = (a-b for a, b in zip(point, base))
        shear = -F(p*(X-Y)+alpha*V, alpha)
        index = shear/F(n, g)
        assert index.denominator == 1
        step_indices.append(index.numerator)
    lattice_gcd = gcd(*step_indices)
    differences = [tuple(a-b for a, b in zip(point, base)) for point in points]
    nonzero = next((d for d in differences if any(d)), None)
    dimension = 0 if nonzero is None else 1
    if nonzero is not None:
        for d in differences:
            if any(nonzero[a]*d[b] != nonzero[b]*d[a]
                   for a in range(4) for b in range(a)):
                dimension = 2
                break
    if dimension == 2:
        assert lattice_gcd == 1
    return {'stock': stock, 'points': points, 'dimension': dimension,
            'root_index': lattice_gcd, 'step_indices': step_indices}


if __name__ == '__main__':
    for p, r, source, base in (
            (11, 14, (4, 2, 5), (2, 5, 1, 3)),
            (13, 4, (6, 5, 2), (2, 3, 1, 7)),
            (13, 16, (4, 2, 7), (2, 7, 1, 3)),
            (19, 10, (9, 8, 2), (8, 6, 1, 4))):
        nu = 1 if source[2] == 2 else 2
        result = fiber(p, r, nu, source, base)
        print(p, r, result)
