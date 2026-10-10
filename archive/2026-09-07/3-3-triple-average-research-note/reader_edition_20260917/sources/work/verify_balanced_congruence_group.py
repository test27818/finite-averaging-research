"""Exact checks for balanced generation and the digit congruence group.

The general generation argument is in the accompanying proof. Finite
quotient orbit checks use short elementary words, not a group enumeration.
"""

from math import gcd
from random import Random

from verify_digit_replica_transvections import (
    balanced_normal_form, digit_matrix, digit_order, difference_gcd,
)


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def multiply(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def matvec(a,x):
    return [sum(c*v for c,v in zip(row,x)) for row in a]


def balanced(n,i,j,k,ell,q=1):
    assert len({i,j,k,ell}) == 4
    matrix = identity(n)
    matrix[i][k] += q
    matrix[i][ell] -= q
    matrix[j][k] -= q
    matrix[j][ell] += q
    return matrix


def lift_row_stochastic(b):
    m = len(b)
    assert all(sum(row) == 1 for row in b)
    return [row+[0] for row in b]+[[1-sum(b[i][j] for i in range(m))
                                  for j in range(m)]+[1]]


def row_fixed_basis(m):
    q = identity(m)
    inverse = identity(m)
    for i in range(m-1):
        q[i][-1] = 1
        inverse[i][-1] = -1
    return q,inverse


def verify_stabilizer_generators():
    checked = 0
    for n in range(5,13):
        m,d = n-1,n-2
        q,qi = row_fixed_basis(m)
        for i in range(d):
            for k in range(d):
                if i == k:
                    continue
                elementary = identity(m)
                elementary[i][k] = 2
                b = multiply(multiply(q,elementary),qi)
                assert lift_row_stochastic(b) == balanced(n,i,n-1,k,m-1,2)
                checked += 1
        for k in range(d):
            ell = (k+1) % d
            r = [int(i==k)-int(i==ell) for i in range(d)]
            s = identity(m)
            s[-1][k] += 1
            s[-1][ell] -= 1
            transformed = multiply(multiply(qi,s),q)
            expected = identity(m)
            for i in range(d):
                for j in range(d):
                    expected[i][j] -= r[j]
            expected[-1][:d] = r
            assert transformed == expected
            # r*1=0 makes I-1*r an integral unipotent.
            cancel = identity(m)
            for i in range(d):
                for j in range(d):
                    cancel[i][j] += r[j]
            translation = multiply(cancel,transformed)
            expected = identity(m)
            expected[-1][:d] = r
            assert translation == expected
            b = identity(m)
            bi = identity(m)
            b[ell][k] = 1
            bi[ell][k] = -1
            unit_translation = multiply(multiply(bi,translation),b)
            expected = identity(m)
            expected[-1][ell] = -1
            assert unit_translation == expected
            assert lift_row_stochastic(s) == balanced(n,m-1,n-1,k,ell)
            checked += 1
    print('column stabilizer elementary blocks and unit translations: PASS',checked)


def root_basis_matrix(full):
    n = len(full)
    return [[full[i][j]-full[i][-1] for j in range(n-1)] for i in range(n-1)]


def lift_root_matrix(b):
    n = len(b)+1
    numerators = [1-sum(row) for row in b]
    assert all(value % n == 0 for value in numerators)
    last = [value//n for value in numerators]
    rows = [[b[i][j]+last[i] for j in range(n-1)]+[last[i]]
    for i in range(n-1)]
    rows.append([1-sum(rows[i][j] for i in range(n-1)) for j in range(n)])
    return rows


def verify_column_reduction():
    random = Random(9134)
    checked = 0
    for n in range(5,13):
        for _ in range(20):
            root_matrix = identity(n-1)
            for _ in range(12):
                i,j = random.sample(range(n-1),2)
                coefficient = n*random.randrange(-4,5)
                root_matrix[i] = [a+coefficient*b for a,b in zip(root_matrix[i],root_matrix[j])]
            root_matrix[0],root_matrix[1] = root_matrix[1],root_matrix[0]
            matrix = lift_root_matrix(root_matrix)
            assert all(sum(row) == 1 for row in matrix)
            assert all(sum(matrix[i][j] for i in range(n)) == 1 for j in range(n))
            b = root_basis_matrix(matrix)
            assert all((sum(row)-1) % n == 0 for row in b)
            assert lift_root_matrix(b) == matrix
            column = [row[-1] for row in matrix]
            assert sum(column) == 1 and difference_gcd(column) == 1
            normal,word,_ = balanced_normal_form(column)
            for i,j,k,ell,power in word:
                matrix = multiply(balanced(n,i,j,k,ell,power),matrix)
            assert [row[-1] for row in matrix] == list(normal)
            position = normal.index(1)
            matrix[position],matrix[-1] = matrix[-1],matrix[position]
            top = [row[:-1] for row in matrix[:-1]]
            assert matrix == lift_row_stochastic(top)
            checked += 1
    print('balanced column reduction and full congruence lift: PASS',checked)


def verify_digit_level():
    checked = 0
    for arity in range(2,10):
        for n in range(max(5,arity+2),32):
            if gcd(n,arity) != 1:
                continue
            matrix = digit_matrix(n,arity)
            b = root_basis_matrix(matrix)
            assert all((sum(row)-arity) % n == 0 for row in b)
            period = digit_order(n,arity)
            # Check the full period using digit counts, already independently
            # replayed by the replica verifier, and sparse modular row actions.
            vector = list(range(n-1))+[-sum(range(n-1))]
            start = vector.copy()
            for _ in range(period):
                vector = matvec(matrix,vector)
            assert vector == start
            assert matvec(b,start[:-1]) == matvec(matrix,start)[:-1]
            q_power = 1
            for _ in range(period):
                q_power = q_power*arity % n
            assert q_power == 1
            checked += 1
    print('digit root-lattice matrices and exact cyclic level extension: PASS',checked)


def divisors(n):
    return [d for d in range(1,n+1) if n % d == 0]


def projective_orbit_label(n,arity,x):
    divisor = gcd(*x)
    x = [v//divisor for v in x]
    d = difference_gcd(x)
    residue = x[0] % d
    orbit = set()
    current = residue
    while current not in orbit:
        orbit.add(current)
        orbit.add(-current % d)
        current = arity*current % d
    return d,min(orbit)


def verify_projective_orbits():
    checked = 0
    random = Random(9307)
    for n in (5,7,8,10,11,13,14,16,17,20,23,25,29):
        arity = 3
        representatives = {}
        for d in divisors(n):
            for c in range(d):
                if gcd(c,d) != 1:
                    continue
                x = [c]*(n-2)+[c+d,-(n-1)*c-d]
                assert sum(x) == 0 and gcd(*x) == 1 and difference_gcd(x) == d
                label = projective_orbit_label(n,arity,x)
                representatives.setdefault(label,x)
        for label,x in representatives.items():
            for _ in range(12):
                i,j,k,ell = random.sample(range(n),4)
                x = matvec(balanced(n,i,j,k,ell,random.randrange(-3,4)),x)
                x = matvec(digit_matrix(n),x)
                assert projective_orbit_label(n,arity,x) == label
                checked += 1
        if n in (7,11,17,23,29):
            assert len(representatives) == 2
        if n == 13:
            assert len(representatives) == 3
    print('primitive rational projective orbit representatives and invariants: PASS',checked)


def verify():
    verify_stabilizer_generators()
    verify_column_reduction()
    verify_digit_level()
    verify_projective_orbits()


if __name__ == '__main__':
    verify()
