"""Exact interfaces extracted from AI-3/4/5, with independent boundaries.

General Zariski density follows from the rank-one Lie proof in the report;
finite rank checks here only validate the constructive identities.
"""

from fractions import Fraction as F
from itertools import product
from math import gcd,lcm

from verify_burau_power_chain import full_generator,inverse,matrix_power
from explore_weighted_kernel_group import identity,multiply
from verify_ai3_multprime_chain import exchange_blocks,real_exchange
from verify_ai3_bn_template_recursion import template_one_data,template_two_data
from audit_burau_rank4 import rational_matrix_mod,projective_orbits
from explore_weighted_kernel_group import exchange_matrix


def add(a,b,scale=1):
    return tuple(tuple(x+scale*y for x,y in zip(ar,br)) for ar,br in zip(a,b))


def scaled(a,scalar):
    return tuple(tuple(scalar*x for x in row) for row in a)


def outer(v,f):
    return tuple(tuple(x*y for y in f) for x in v)


def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),F(0))


def apply(a,v):
    return tuple(dot(row,v) for row in a)


def bracket(a,b):
    return add(multiply(a,b),multiply(b,a),-1)


def rank(rows):
    basis = {}
    for row in rows:
        row = list(map(F,row))
        for pivot,value in sorted(basis.items()):
            if row[pivot]:
                factor = row[pivot]
                row = [a-factor*b for a,b in zip(row,value)]
        pivot = next((i for i,x in enumerate(row) if x),None)
        if pivot is not None:
            factor = row[pivot]
            basis[pivot] = [x/factor for x in row]
    return len(basis)


def reduced(matrix,weights):
    d = len(weights)-1
    return tuple(tuple(matrix[i][j]-matrix[i][-1]*F(weights[j],weights[-1])
                       for j in range(d)) for i in range(d))


def exchange_projector(weights,i,j):
    assert weights[i] > weights[j]
    size = len(weights)
    s = F(weights[i],weights[j])
    normal = tuple(F(-1,weights[i]) if k == i else F(1,weights[j]) if k == j else F(0)
                   for k in range(size))
    covector = tuple(F(-1) if k == i else F(1) if k == j else F(0) for k in range(size))
    norm = dot(covector,normal)
    covector = tuple(x/norm for x in covector)
    projection = outer(normal,covector)
    macro = add(identity(size),scaled(projection,-1/s-1))
    return normal,covector,projection,macro


def away_gcd(values):
    denominator = lcm(*(x.denominator for x in values))
    result = gcd(*(int(x*denominator) for x in values))
    while result and result % 3 == 0:
        result //= 3
    return result


def affine_ideal(values):
    return away_gcd([x-values[0] for x in values])


def verify_affine_transport():
    checked = 0
    for weights in ((9,3,1),(27,9,3,1),(9,9,3,1),(81,9,1,1)):
        for i in range(len(weights)):
            for j in range(len(weights)):
                if weights[i] <= weights[j]:
                    continue
                _,_,_,matrix = exchange_projector(weights,i,j)
                inv = inverse(matrix)
                assert all(x.denominator == 1 or away_gcd([F(x.denominator)]) == 1
                           for row in inv for x in row)
                for seed in range(6):
                    values = tuple(F((k+1)**2+seed,3**(k % 3)) for k in range(len(weights)))
                    output = apply(matrix,values)
                    assert output == exchange_blocks(weights,values,i,j)
                    assert dot(weights,output) == dot(weights,values)
                    assert affine_ideal(output) == affine_ideal(values)
                    assert away_gcd(output) == away_gcd(values)
                    checked += 1
                physical,_ = real_exchange(weights,values,i,j)
                assert physical == output
    print('exchange preserves full away-from-three coordinate and difference ideals: PASS',checked)


def verify_rank_one_lie():
    cases = ((3,1),(9,3,1),(27,9,3,1),(9,9,3,1),(27,9,3,1,1),(81,27,9,3,1,1))
    identities = 0
    for weights in cases:
        edges = [(i,j) for i in range(len(weights)) for j in range(len(weights)) if weights[i]>weights[j]]
        data = [exchange_projector(weights,*edge) for edge in edges]
        for v,f,p,g in data:
            assert dot(f,v) == 1 and multiply(p,p) == p
            assert dot(weights,v) == 0
            assert sum(f) == 0
        for v,f,p,g in data:
            for w,h,q,k in data:
                alpha,beta = dot(f,w),dot(h,v)
                if not alpha:
                    assert not beta
                    continue
                first = bracket(p,q)
                double = bracket(p,first)
                constructed = scaled(add(add(double,first),scaled(p,2*alpha*beta)),F(1,2*alpha))
                assert constructed == outer(v,h)
                identities += 1
        # All rank-one cross maps arise by walking through the connected
        # line graph and applying [v f_h, v_h f'] + f'(v) P_h = v f'.
        for v,f,p,g in data:
            for w,h,q,k in data:
                reduced_cross = reduced(outer(v,h),weights)
                assert len(reduced_cross) == len(weights)-1
        matrices = [reduced(outer(v,h),weights) for v,_,_,_ in data for _,h,_,_ in data]
        assert rank([sum((list(row) for row in matrix),[]) for matrix in matrices]) == (len(weights)-1)**2
    print('rank-one exchange Lie identities and full reduced matrix spans: PASS',len(cases),identities)


def chain_data(t,s):
    weights = tuple(s**(t-1-i) for i in range(t))
    pi = tuple(tuple(F(w,sum(weights)) for w in weights) for _ in weights)
    generators = [full_generator(t,s,i) for i in range(t-1)]
    coxeter = identity(t)
    for generator in generators:
        coxeter = multiply(generator,coxeter)
    lam = F(1,s**t)
    center = add(pi,scaled(add(identity(t),pi,-1),lam))
    assert matrix_power(coxeter,t) == center
    return weights,pi,generators,coxeter,center


def verify_affine_burau():
    checked = 0
    for t in range(3,7):
        for s in (3,9):
            weights,pi,generators,coxeter,center = chain_data(t,s)
            for selected,generator in enumerate(generators):
                lower,higher = identity(t),identity(t)
                for i in range(selected):
                    lower = multiply(generators[i],lower)
                for i in range(selected+1,t-1):
                    higher = multiply(generators[i],higher)
                positive = multiply(lower,multiply(matrix_power(coxeter,t-1),higher))
                assert positive == multiply(center,inverse(generator))
                values = tuple(F(i+1) for i in range(t))
                assert dot(weights,values) != 0
                assert apply(center,values) == tuple(dot(weights,values)/sum(weights)+
                    F(1,s**t)*(x-dot(weights,values)/sum(weights)) for x in values)
                checked += 1
    w1,pi1,g1,c1,d1 = chain_data(3,3)
    w2,pi2,g2,c2,d2 = chain_data(4,3)
    weights = w1+w2
    zero = F(0)
    pi = tuple(tuple((pi1[i][j] if i<3 and j<3 else pi2[i-3][j-3] if i>=3 and j>=3 else zero)
                      for j in range(7)) for i in range(7))
    lam = F(1,3**12)
    center = add(pi,scaled(add(identity(7),pi,-1),lam))
    assert matrix_power(d1,4) == add(pi1,scaled(add(identity(3),pi1,-1),lam))
    assert matrix_power(d2,3) == add(pi2,scaled(add(identity(4),pi2,-1),lam))
    _,_,_,exchange = exchange_projector(weights,3,0)
    commutator = bracket(exchange,center)
    assert commutator == scaled(bracket(exchange,pi),1-lam)
    assert rank(commutator) == 2
    print('nonzero-mean Burau inverse interface and rank-two cross-chain defect: PASS',checked)


def quotient_layer(counts):
    n = len(counts)
    assert all(sum(row) == 3 for row in counts)
    assert all(sum(counts[i][j] for i in range(n)) == 3 for j in range(n))
    available = [list(range(3*j,3*j+3)) for j in range(n)]
    groups = []
    state = [tuple(F(int(j == k)) for k in range(n)) for j in range(n) for _ in range(3)]
    for row in counts:
        group = []
        for j,count in enumerate(row):
            group.extend(available[j][-count:] if count else [])
            if count:
                del available[j][-count:]
        assert len(group) == len(set(group)) == 3
        mean = tuple(sum(state[i][k] for i in group)/3 for k in range(n))
        for i in group:
            state[i] = mean
        groups.append(group)
    assert all(not bucket for bucket in available)
    for row,group in zip(counts,groups):
        assert all(state[i] == tuple(F(x,3) for x in row) for i in group)
    return counts


def verify_replica_regrouping():
    checked = 0
    for a,b,c,d in product(range(4),repeat=4):
        matrix = ((a,b,3-a-b),(c,d,3-c-d),(3-a-c,3-b-d,a+b+c+d-3))
        if all(x >= 0 for row in matrix for x in row):
            quotient_layer(matrix)
            checked += 1
    assert checked == 55
    for n in range(2,15):
        matrix = tuple(tuple(2*int(i == j)+int(j == (i+1)%n) for j in range(n)) for i in range(n))
        quotient_layer(matrix)
        assert rank(matrix) == n
        assert 2**n-(-1)**n != 0
    print('regrouped replica layers and nonsingular quotient obstruction: PASS 55 13')


def verify_report_boundaries():
    boundary = template_one_data(8,3)
    assert boundary['smith_g'] == 2 and not boundary['child_lattice_ok']
    assert 8 % 4 == 0
    assert template_two_data(11,9)['smith_g'] == 7
    values = [F(1),F(1),F(5),F(0),F(0),F(0),F(-7)]
    mean = sum(values[:3])/3
    following = [mean]*3+values[3:]
    assert away_gcd(following) == 7 and affine_ideal(following) == 7
    # Both coordinate and difference ideals acquire 7, so primitive G=1.
    assert affine_ideal(following)//away_gcd(following) == 1
    print('AI report boundary corrections independently reproduced: PASS')


def verify_rank_four_orbits():
    for prime,expected in ((2,[1,6]),(5,[1,30]),(7,[9,12,36])):
        generators = [rational_matrix_mod(exchange_matrix((27,9,3,1),i,i+1),prime)
                      for i in range(3)]
        orbits = projective_orbits(generators,prime)
        assert sorted(map(len,orbits)) == expected
    print('AI4 projective orbit tables via three generators only: PASS 3')


def verify():
    verify_affine_transport()
    verify_rank_one_lie()
    verify_affine_burau()
    verify_replica_regrouping()
    verify_report_boundaries()
    verify_rank_four_orbits()


if __name__ == '__main__':
    verify()
