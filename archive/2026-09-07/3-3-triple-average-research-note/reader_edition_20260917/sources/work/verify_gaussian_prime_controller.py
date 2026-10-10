"""Exact positive Gaussian-period controller for primes p=1 modulo3.

The proof of the uniform primitive shear lemma is in the document.
Physical replays keep one fixed set of p positions throughout each word.
"""

from fractions import Fraction as F
from itertools import combinations
from math import gcd, lcm
from random import Random
from collections import Counter

from explore_gaussian_period_layers import orbit_data, layer_matrix, determinant
from verify_flat_star_arithmetic import identity, inverse, multiply, rank_one
from b17_universal_atomic_words import nine_word, average


def rational_gcd(values):
    denominator = lcm(*(value.denominator for value in values))
    numerator = gcd(*(int(value*denominator) for value in values))
    return F(numerator,denominator)


def verify_eisenstein_identities():
    def rotate(z):
        a,b = z
        return -b,a-b
    def period(z):
        result = Counter()
        for _ in range(3):
            result[z] += 1
            z = rotate(z)
        return dict(result)
    def combine(a,b,sign=1):
        result = a.copy()
        for z,value in b.items():
            result[z] = result.get(z,0)+sign*value
        return {z:value for z,value in result.items() if value}
    def convolution(a,b):
        result = Counter()
        for (x,y),value in a.items():
            for (u,v),other in b.items():
                result[x+u,y+v] += value*other
        return {z:value for z,value in result.items() if value}
    def ring_multiply(x,y):
        a,b = x
        c,d = y
        return a*c-b*d,a*d+b*c-b*d
    theta = period
    lhs = convolution(theta((-1,0)),combine(theta((1,0)),theta((-2,0)),-1))
    assert lhs == combine({(0,0):3},theta((-3,0)),-1)
    lhs = convolution(theta((-1,0)),combine(theta((-1,1)),theta((1,-1)),-1))
    assert lhs == combine(theta((-2,1)),theta((1,-2)),-1)
    norm_unit = combine(convolution(theta((1,0)),theta((-1,0))),{(0,0):1},-1)
    product = {(0,0):1}
    z = (-1,1)
    for _ in range(3):
        product = convolution(product,{(0,0):1,z:1})
        z = rotate(z)
    assert norm_unit == product
    for z,cube in (((-1,1),(3,6)),((-2,1),(-1,18)),((1,-2),(-19,-18))):
        assert ring_multiply(ring_multiply(z,z),z) == cube
    print('Eisenstein lattice convolution and exceptional-prime identities: PASS 4')


def controller_data(p):
    subgroup,orbits,lookup = orbit_data(p)
    omega = subgroup[1]
    r = len(orbits)
    K = layer_matrix(p,1)
    Km = layer_matrix(p,p-1)
    base,opposite = lookup[1],lookup[p-1]
    a,b = lookup[(omega-1)%p],lookup[(1-omega)%p]
    i,j = lookup[(omega-2)%p],lookup[(1-2*omega)%p]
    source = [int(k==a)-int(k==b) for k in range(r)]
    target = [int(k==i)-int(k==j) for k in range(r)]
    assert [sum(x*y for x,y in zip(row,source)) for row in K] == target
    unit_a,unit_b,unit_i = base,lookup[-2%p],lookup[-3%p]
    assert [row[unit_a]-row[unit_b] for row in K] == [-int(k==unit_i) for k in range(r)]
    gram = [[int(k==ell)+3 for ell in range(r)] for k in range(r)]
    assert multiply(list(map(list,zip(*K))),gram) == multiply(gram,Km)
    unit = multiply(Km,K)
    for k in range(r):
        unit[k][k] -= 1
    assert determinant(unit) == 1
    Ki = inverse(K)
    h = [Ki[a][k]-Ki[b][k]-int(k==i)+int(k==j) for k in range(r)]
    outside = [k for k in range(r) if k not in (i,j)]
    divisor = rational_gcd([h[k]-h[ell] for k,ell in combinations(outside,2)])
    assert divisor.numerator == 1
    assert h[i] == h[j]
    if p > 13:
        assert a != base and b != base and i not in (base,opposite) and j not in (base,opposite)
        assert all(value in (0,1) for row in (K[i],K[j]) for value in row)
    return K,Ki,orbits,lookup,(a,b,i,j,h),divisor


class PhysicalFlat:
    def __init__(self,p):
        self.p = p
        _,self.orbits,self.lookup = orbit_data(p)
        self.r = len(self.orbits)
        self.locations = list(range(p))
        basis = [tuple(F(i==j) for j in range(self.r)) for i in range(self.r)]
        self.state = [tuple(F(-3) for _ in range(self.r))]
        self.state += [basis[self.lookup[i]] for i in range(1,p)]
        self.operations = 0

    def layer(self,c):
        for orbit in self.orbits:
            positions = [self.locations[(x+c)%self.p] for x in orbit]
            mean = tuple(sum(self.state[x][j] for x in positions)/3 for j in range(self.r))
            for position in positions:
                self.state[position] = mean
            self.operations += 1
        self.locations = [self.locations[(x+c)%self.p] for x in range(self.p)]

    def swap(self,i,j):
        for x,y in zip(self.orbits[i],self.orbits[j]):
            self.locations[x],self.locations[y] = self.locations[y],self.locations[x]

    def apply(self,word):
        for token in word:
            if token[0] == 'swap':
                self.swap(*token[1:])
            elif token[0] == 'P':
                self.layer(1)
            elif token[0] == 'inverse':
                for orbit in self.orbits:
                    if 1 not in orbit:
                        self.layer(orbit[0])
            else:
                raise ValueError(token)

    def check(self,matrix,scale):
        assert sorted(self.locations) == list(range(self.p))
        expected = [tuple(scale*x for x in row) for row in matrix]
        for i,orbit in enumerate(self.orbits):
            assert all(self.state[self.locations[x]] == expected[i] for x in orbit)
        carrier = tuple(-3*sum(row[j] for row in expected) for j in range(self.r))
        assert self.state[self.locations[0]] == carrier


def verify_cycles():
    checked = operations = 0
    for p in (7,13,19,31,37,43):
        _,orbits,_ = orbit_data(p)
        r = len(orbits)
        result = identity(r)
        physical = PhysicalFlat(p)
        for orbit in orbits:
            result = multiply(layer_matrix(p,orbit[0]),result)
            physical.layer(orbit[0])
        norm = determinant(layer_matrix(p,1))
        assert norm.denominator == 1 and 0 < norm < 3**r
        assert result == [[norm*int(i==j) for j in range(r)] for i in range(r)]
        assert int(norm) % p == pow(3,r,p)
        physical.check(identity(r),F(norm,3**r))
        assert physical.operations == r*r
        operations += physical.operations
        checked += 1
    print('Gaussian norm cycles on fixed physical positions: PASS',checked,operations)


def verify_unit_and_affine_bridge():
    checked = 0
    for p in (13,19,31,37,43,61,67,73,79,97):
        K,Ki,orbits,lookup,_,_ = controller_data(p)
        r = len(orbits)
        i = lookup[-3%p]
        excluded = {i,lookup[-1%p]}
        k,ell = [x for x in range(r) if x not in excluded][:2]
        v = [F(x==lookup[1])-F(x==lookup[-2%p]) for x in range(r)]
        f = [K[k][x]-K[ell][x] for x in range(r)]
        transvection = rank_one(v,f)
        assert sum(v) == sum(f) == sum(a*b for a,b in zip(v,f)) == 0
        assert all(sum(row) == 1 for row in transvection)
        assert all(sum(row[x] for row in transvection) == 1 for x in range(r))
        target = identity(r)
        target[i][k] -= 1
        target[i][ell] += 1
        assert multiply(multiply(K,transvection),Ki) == target
        assert set(K[x][lookup[1]] for x in range(r) if x != lookup[-1%p]) == {0,1}
        checked += 1
    print('Gaussian root identities, norm-one defect, primitive shear and affine bridge: PASS',checked)


def verify_positive_unit_shears():
    total = 0
    for p in (13,19,31):
        K,_,orbits,_,data,_ = controller_data(p)
        a,b,i,j,h = data
        outside = [k for k in range(len(orbits)) if k not in (i,j)]
        options = []
        for k,ell in combinations(outside,2):
            delta = h[k]-h[ell]
            if abs(delta.numerator) == 1:
                if delta < 0:
                    k,ell = ell,k
                options.append((delta.denominator,k,ell))
        repeats,k,ell = min(options)
        u = [('inverse',),('swap',a,b),('P',),('swap',i,j)]
        ui = [('swap',i,j),('inverse',),('swap',a,b),('P',)]
        word = [('swap',k,ell)]+ui+[('swap',k,ell)]+u
        physical = PhysicalFlat(p)
        for _ in range(repeats):
            physical.apply(word)
        expected = identity(len(orbits))
        expected[i][k] += 1
        expected[i][ell] -= 1
        expected[j][k] -= 1
        expected[j][ell] += 1
        scalar = F(determinant(K),3**len(orbits))**(2*repeats)
        physical.check(expected,scalar)
        assert physical.operations == 2*len(orbits)**2*repeats
        total += physical.operations
    print('positive integer balanced shears with full coefficient replay: PASS',total)


def matvec(matrix,values):
    return [sum(a*x for a,x in zip(row,values)) for row in matrix]


def row_fixed_normalizer(values):
    r = len(values)
    y = [x-values[-1] for x in values[:-1]]
    assert any(y)
    matrix = [[int(i==j) for j in range(r)] for i in range(r)]
    for j in range(1,r-1):
        while y[j]:
            quotient = y[0]//y[j]
            y[0] -= quotient*y[j]
            matrix[0] = [a-quotient*b for a,b in zip(matrix[0],matrix[j])]
            y[0],y[j] = y[j],y[0]
            matrix[0],matrix[j] = matrix[j],matrix[0]
    if y[0] < 0:
        y[0] = -y[0]
        matrix[0] = [-x for x in matrix[0]]
    divisor = y[0]
    common = values[-1] % divisor
    quotient = (common-values[-1])//divisor
    matrix[-1] = [a+quotient*b for a,b in zip(matrix[-1],matrix[0])]
    q = [[int(i==j) for j in range(r)] for i in range(r)]
    qi = [row.copy() for row in q]
    for i in range(r-1):
        q[i][-1] = 1
        qi[i][-1] = -1
    result = multiply(multiply(q,matrix),qi)
    assert all(value.denominator == 1 for row in result for value in row)
    assert all(sum(row) == 1 for row in result)
    assert matvec(result,values) == [common+divisor]+[common]*(r-1)
    return result,divisor,common


def verify_global_reduction():
    random = Random(310613)
    checked = 0
    for p in (19,31,37,43,61):
        _,orbits,_ = orbit_data(p)
        r = len(orbits)
        K = layer_matrix(p,1)
        for divisor in (1,2,4,5,7,p-1,p+1,2*p+1):
            for _ in range(8):
                y = [0,1]+[random.randrange(-20,21) for _ in range(r-2)]
                common = next(c for c in range(random.randrange(1,12),divisor+15) if gcd(c,divisor) == 1)
                values = [common+divisor*x for x in y]
                assert gcd(*values) == 1
                first,d,c = row_fixed_normalizer(values)
                assert d == divisor
                following = matvec(K,matvec(first,values))
                assert all(x.denominator == 1 for x in following)
                following = [int(x) for x in following]
                assert gcd(*(x-following[0] for x in following)) == gcd(divisor,p) == 1
                last,_,_ = row_fixed_normalizer(following)
                assert matvec(last,following) == [1]+[0]*(r-1)
                checked += 1
        state = [F(1)]*3+[F(0)]*(p-4)+[F(-3)]
        chosen = (0,1,2,3,4,5,6,7,p-1)
        for triple in nine_word(chosen):
            average(state,triple)
        assert not any(state)
    print('affine normal forms, exact prime-gcd removal and terminal tails: PASS',checked)


def verify_dimension_catalog():
    from compile_bn_integer_templates import solved_size,certificate_size
    solved = (31,37,43,61,97,109,127,139,62,155,31**2,7*31*43,3*29,6*41)
    for size in solved:
        assert solved_size(size)
    for size in (2,4,5,6,71,83,71*31,71**2):
        assert not solved_size(size)
    assert solved_size(53) and solved_size(59)
    assert not certificate_size(31) and not certificate_size(37)
    print('split-prime factor closure and frozen-library boundary: PASS',len(solved))


def verify():
    verify_eisenstein_identities()
    verify_cycles()
    verify_unit_and_affine_bridge()
    verify_positive_unit_shears()
    verify_global_reduction()
    verify_dimension_catalog()


if __name__ == '__main__':
    verify()
