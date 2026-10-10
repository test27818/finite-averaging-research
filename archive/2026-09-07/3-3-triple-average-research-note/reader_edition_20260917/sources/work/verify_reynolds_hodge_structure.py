"""Exact interfaces for Reynolds semigroups and discriminant duality.

All-n statements are proved in the companion document. Matrix-algebra
generation does not imply positive-product reachability, and the Hodge
operator is a formal duality that fails legal-domain preservation.
"""

from fractions import Fraction as F
from itertools import combinations
from math import comb,gcd

from verify_flat_star_arithmetic import identity,multiply,inverse


def add(*matrices):
    return [[sum(m[i][j] for m in matrices) for j in range(len(matrices[0][0]))]
            for i in range(len(matrices[0]))]


def scale(c,m):return [[F(c)*x for x in row] for row in m]


def transpose(m):return [list(row) for row in zip(*m)]


def outer(x,y):return [[F(a)*b for b in y] for a in x]


def triple_projection(n,indices):
    matrix = identity(n)
    for i in indices:
        matrix[i] = [F(j in indices,3) for j in range(n)]
    return matrix


def cycle_matrix(n,indices):
    permutation = list(range(n))
    for offset,i in enumerate(indices):permutation[i] = indices[(offset+1)%3]
    return [[F(i == permutation[j]) for j in range(n)] for i in range(n)]


def root(n,i,j):return [F(k==i)-F(k==j) for k in range(n)]


def verify_reynolds():
    atom_count = 0
    for n in range(4,10):
        eye = identity(n)
        projections = {}
        for indices in combinations(range(n),3):
            sigma = cycle_matrix(n,indices)
            actual = triple_projection(n,indices)
            assert scale(F(1,3),add(eye,sigma,multiply(sigma,sigma))) == actual
            assert multiply(actual,actual) == actual == transpose(actual)
            projections[indices] = actual
            atom_count += 1
        mean = scale(F(1,len(projections)),add(*projections.values()))
        rho = F(n-3,n-1)
        expected = add(scale(rho,eye),scale(F(1,1)-rho,[[F(1,n)]*n for _ in range(n)]))
        assert mean == expected
    print('Reynolds atoms and exact convex scalar averages: PASS',atom_count)


def verify_full_algebra():
    recovered,pairs = 0,0
    for n in range(5,10):
        eye = identity(n)
        triangles = {s:scale(3,add(eye,scale(-1,triple_projection(n,s))))
                     for s in combinations(range(n),3)}
        total_edges = scale(F(1,n-2),add(*triangles.values()))
        incident = {i:scale(F(1,n-3),add(*[v for s,v in triangles.items() if i in s],
                                        scale(-1,total_edges))) for i in range(n)}
        edges = {}
        for i,j in combinations(range(n),2):
            through = add(*[v for s,v in triangles.items() if i in s and j in s])
            value = scale(F(1,n-4),add(through,scale(-1,incident[i]),scale(-1,incident[j])))
            r = root(n,i,j)
            assert value == outer(r,r)
            edges[i,j] = value
            recovered += 1
        for i in range(n-1):
            for j in range(n-1):
                ri,rj = root(n,i,n-1),root(n,j,n-1)
                product = multiply(edges[i,n-1],edges[j,n-1])
                assert product == scale(2 if i==j else 1,outer(ri,rj))
                pairs += 1
    print('triangle Laplacians recover all roots and rank-one endomorphisms: PASS',recovered,pairs)


def determinant(m):return m[0][0]*m[1][1]-m[0][1]*m[1][0]


def gram(p):
    m = p-4
    return [[F(m*(m+1)),F(3*m)],[F(3*m),F(12)]]


def hodge(p):return multiply(inverse(gram(p)),[[F(0),F(1)],[F(-1),F(0)]])


def vector_image(m,x):return [sum(a*b for a,b in zip(row,x)) for row in m]


def primitive(values):
    from math import lcm
    d = lcm(*(x.denominator for x in values))
    integers = [int(x*d) for x in values]
    g = gcd(*integers)
    return tuple(x//g for x in integers)


def verify_hodge():
    identities,legal_images,duality = 0,0,0
    for p in (5,7,11,17,23,47,53,59,73):
        m = p-4
        g = gram(p)
        delta = determinant(g)
        k = hodge(p)
        assert delta == 3*p*m
        assert multiply(k,k) == scale(-1/delta,identity(2))
        assert multiply(multiply(transpose(k),g),k) == scale(1/delta,g)
        p0 = [[F(1),F(0)],[F(-m,4),F(1)]]
        gd = multiply(multiply(transpose(p0),g),p0)
        assert gd == [[F(p*m,4),0],[0,F(12)]]
        w = scale(12*p,multiply(multiply(inverse(p0),k),p0))
        unit = F(48,m)
        assert w == [[0,unit],[-p,0]]
        assert multiply(w,w) == scale(-p*unit,identity(2))

        for a in ([[F(2),F(1)],[F(3),F(2)]],
                  [[F(1),F(2,3)],[F(0),F(-1,3)]],
                  [[F(4),F(-3)],[F(1),F(2)]]):
            adjoint = multiply(multiply(inverse(g),transpose(a)),g)
            value = multiply(multiply(k,adjoint),inverse(k))
            assert value == scale(determinant(a),inverse(a))
            identities += 1

        for x in range(-7,8):
            for y in range(-7,8):
                if gcd(x,y) != 1 or (x-y)%p == 0:continue
                transformed = primitive(vector_image(k,(x,y)))
                assert (transformed[0]-transformed[1])%p == 0
                assert transformed[0]%p
                legal_images += 1

        # The formal duality conjugates the entire local Iwahori into itself.
        for b,c in ((1,2),(-3,1),(F(1,3),F(2,3))):
            a = [[F(1),F(b)],[p*F(c),1+p*F(b)*F(c)]]
            conjugate = multiply(multiply(w,a),inverse(w))
            expected = [[a[1][1],-unit*F(c)],[-p*F(b)/unit,a[0][0]]]
            assert conjugate == expected and determinant(conjugate) == 1
            duality += 1
    print('Hodge inverse, energy similarity and local Fricke form: PASS',identities)
    print('Hodge sends every sampled primitive legal direction into illegal residue: PASS',legal_images)
    print('Fricke conjugation preserves the Iwahori while exchanging its boundary sides: PASS',duality)


def verify_discriminant_valuation():
    checked = 0
    for p in (5,7,11,17,23,47,53,59,73):
        for a in range(1,p):
            for b in (0,1,2):
                for c in (0,1):
                    # Diagonal entries unit,p*unit plus a basis shear.
                    base = [[F(a),0],[0,F(p*(b+1))]]
                    change = [[F(1),F(c)],[0,F(1)]]
                    g = multiply(multiply(transpose(change),base),change)
                    k = multiply(inverse(g),[[F(0),F(1)],[F(-1),F(0)]])
                    image = scale(p,k)
                    assert all(x.denominator%p for row in image for x in row)
                    assert any(x.numerator%p for row in image for x in row)
                    assert all(x.numerator%p == 0 for row in multiply(g,image) for x in row)
                    assert determinant(image).numerator % (p*p) != 0
                    checked += 1
    print('valuation-one discriminant forces primitive duality image into radical: PASS',checked)


if __name__ == '__main__':
    verify_reynolds()
    verify_full_algebra()
    verify_hodge()
    verify_discriminant_valuation()
