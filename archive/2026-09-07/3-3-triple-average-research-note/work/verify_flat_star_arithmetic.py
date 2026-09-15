"""Exact formal-group identities for flat triple blocks and carriers.

Formal inverses are deliberately explicit. These identities do not claim
that the resulting unipotents have positive original-dimension words.
"""

from fractions import Fraction as F
from math import factorial, gcd


def identity(n):
    return [[F(i==j) for j in range(n)] for i in range(n)]


def multiply(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def product(*matrices):
    result = identity(len(matrices[0]))
    for matrix in reversed(matrices):
        result = multiply(matrix,result)
    return result


def inverse(a):
    n = len(a)
    work = [list(map(F,row))+unit for row,unit in zip(a,identity(n))]
    for j in range(n):
        pivot = next(i for i in range(j,n) if work[i][j])
        work[j],work[pivot] = work[pivot],work[j]
        value = work[j][j]
        work[j] = [entry/value for entry in work[j]]
        for i in range(n):
            if i != j:
                value = work[i][j]
                work[i] = [x-value*y for x,y in zip(work[i],work[j])]
    return [row[n:] for row in work]


def commutator(a,b):
    return product(a,b,inverse(a),inverse(b))


def rank_one(u,f,coefficient=1):
    return [[F(i==j)+coefficient*u[i]*f[j] for j in range(len(u))]
            for i in range(len(u))]


def carrier(r,i):
    result = identity(r)
    result[i] = [F(-1,3) if j == i else F(-1) for j in range(r)]
    return result


def elementary(n,i,j,value):
    result = identity(n)
    result[i][j] += value
    return result


def verify_unipotents():
    checked = 0
    for r in range(4,10):
        for i,j,k,ell in ((0,1,2,3),(r-1,r-2,0,1)):
            ti,tj,tk,tl = (carrier(r,a) for a in (i,j,k,ell))
            h = product(ti,tj,inverse(ti))
            other = product(tj,ti,inverse(tj))
            u = product(h,inverse(other))
            v = [F(a==j)-F(a==i) for a in range(r)]
            f = [F(4)+F(2,3)*(int(a==i)+int(a==j)) for a in range(r)]
            assert u == rank_one(v,f)
            wk,wl = commutator(u,tk),commutator(u,tl)
            source = [F(a==k)-F(a==ell) for a in range(r)]
            balanced = product(wk,inverse(wl))
            assert balanced == rank_one(v,source,4)
            row_shear = product(ti,balanced,inverse(ti),inverse(balanced))
            unit = [F(a==i) for a in range(r)]
            assert row_shear == rank_one(unit,source,F(4,3))
            assert product(ti,row_shear,inverse(ti)) == rank_one(unit,source,F(-4,9))
            checked += 1
    print('flat-star homology ratios, balanced commutators and row shears: PASS',checked)


def verify_parabolic_interfaces():
    checked = 0
    for r in range(4,10):
        d = r-1
        n = 3*r+1
        q = identity(r)
        for i in range(d):
            q[i][-1] = 1
        qi = inverse(q)
        generators = [product(qi,carrier(r,i),q) for i in range(r)]
        for a,b in ((F(4),F(4)),(F(-8),F(12)),(F(4),F(16))):
            i,j,k,ell = 0,1,1,2
            v = [F(x==i)-F(x==j) for x in range(d)]+[F(0)]
            rho = [F(1)]*d+[F(0)]
            upper = product(generators[j],elementary(r,i,j,b),inverse(generators[j]))
            axis = [F(-3)]*d+[F(-n)]
            assert upper == rank_one(v,axis,b)
            top = rank_one(v,rho,-3*b)
            upper_translation = product(inverse(top),upper)
            assert upper_translation == rank_one(v,[F(0)]*d+[F(1)],-b*n)
            change = elementary(r,j,i,4)
            unit_upper = product(change,upper_translation,inverse(change),inverse(upper_translation))
            assert unit_upper == elementary(r,j,r-1,-4*b*n)
            if b == 16:
                assert all((top[x][y]-int(x==y)) % 16 == 0 for x in range(d) for y in range(d))

            root = [F(x==i) for x in range(r)]
            f = [F(x==k)-F(x==ell) for x in range(r)]
            x = rank_one(root,f,a)
            y = product(generators[-1],elementary(r,i,j,b),inverse(generators[-1]))
            center = [F(1)+F(x==i) for x in range(d)]+[F(-1)]
            axis = [F(3)+F(x==j) for x in range(d)]+[F(n)]
            assert y == rank_one(center,axis,b)
            comm = commutator(x,y)
            assert comm == rank_one(center,f,-3*a*b)
            top_center = center[:-1]+[F(0)]
            cancel = rank_one(top_center,f,-3*a*b)
            lower = product(inverse(cancel),comm)
            assert lower == rank_one([F(0)]*d+[F(1)],f,3*a*b)
            change = elementary(r,ell,k,4)
            unit_lower = product(inverse(change),lower,change,inverse(lower))
            assert unit_lower == elementary(r,r-1,k,-12*a*b)
            if a == b == 4:
                assert all((cancel[x][y]-int(x==y)) % 16 == 0 for x in range(d) for y in range(d))
            checked += 1
    print('formal upper/lower parabolic extraction identities: PASS',checked)


def verify_two_carrier_gluing():
    checked = 0
    for r in range(4,13):
        d = r-1
        size = d+2
        mass = 3*r+1
        upper_a = [F(0)]*d+[F(1),F(1,mass)]
        upper_b = [F(0)]*d+[F(1,mass),F(1)]
        for i in (0,d-1):
            u = [F(k==i) for k in range(size)]
            left = rank_one(u,upper_a,mass*mass)
            right = rank_one(u,upper_b,-mass)
            assert product(left,right) == elementary(size,i,d,mass*mass-1)
            left = rank_one(u,upper_b,mass*mass)
            right = rank_one(u,upper_a,-mass)
            assert product(left,right) == elementary(size,i,d+1,mass*mass-1)
            assert commutator(elementary(size,d,i,4),elementary(size,i,d+1,4)) == elementary(size,d,d+1,16)
            checked += 1
    print('two-carrier arithmetic block gluing identities: PASS',checked)


def verify_first_local_levels():
    first = identity(3)
    second = identity(3)
    first[0],first[2] = [F(2,3),F(0),F(1,3)],[F(1),F(0),F(0)]
    second[1],second[2] = [F(0),F(2,3),F(1,3)],[F(0),F(1),F(0)]
    result = commutator(first,second)
    assert result == [[0,2,-1],[1,-2,2],[0,3,-2]]
    assert [[value % 2 for value in row] for row in result] == [[0,0,1],[1,0,0],[0,1,0]]
    checked = 0
    for p in (13,17,19,23,29,31,37,41,43,47,53,59,61):
        r,delta = divmod(p,3)
        t = r+delta
        assert r >= 4 and p**((t-2)*(t-3)//2) > factorial(t)//2
        if delta == 2:
            mass = 3*r+1
            assert mass % p == p-1
            size = r+1
            top = elementary(r,r-1,0,1)
            ga = identity(size)
            gb = identity(size)
            for i in range(r):
                ga[i][:r] = gb[i][:r] = top[i]
            row = [F(i==r-1) for i in range(r)]
            gb[-1][:r] = [row[j]-sum(row[i]*top[i][j] for i in range(r)) for j in range(r)]
            assert product(gb,inverse(ga)) == elementary(size,r,0,-1)
        for odd_blocks in range(2,t,2):
            if delta == 1:
                leaves = [1]*(odd_blocks-1)+[0]*(r-odd_blocks+1)
                carriers = [-3*(odd_blocks-1)]
            else:
                leaves = [1]*(odd_blocks-2)+[0]*(r-odd_blocks+2)
                carriers = [-3*(odd_blocks-2)-1,1]
            blocks = leaves+carriers
            physical = [x for value in leaves for x in [value]*3]+carriers
            assert len(physical) == p and sum(physical) == 0
            assert gcd(*physical) == 1 and gcd(*(x-physical[0] for x in physical)) == 1
            assert sum(x % 2 for x in blocks) == odd_blocks
            assert physical.count(0) >= 3
            assert len({x % p for x in blocks}) > 1
            checked += 1
    print('integral three-cycles, first-level Levi gluing and terminal representatives: PASS',checked)


def verify():
    verify_unipotents()
    verify_parabolic_interfaces()
    verify_two_carrier_gluing()
    verify_first_local_levels()


if __name__ == '__main__':
    verify()
