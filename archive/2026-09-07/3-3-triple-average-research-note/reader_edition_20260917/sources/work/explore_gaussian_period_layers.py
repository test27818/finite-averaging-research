"""Original-position averaging layers from order-three finite-field orbits."""

from fractions import Fraction as F
from itertools import combinations
from math import isqrt

from verify_flat_star_arithmetic import identity, multiply


def prime(value):
    return value >= 2 and all(value % d for d in range(2,isqrt(value)+1))


def orbit_data(p):
    assert prime(p) and p % 3 == 1
    omega = next(pow(a,(p-1)//3,p) for a in range(2,p) if pow(a,(p-1)//3,p) != 1)
    subgroup = (1,omega,omega*omega % p)
    unused = set(range(1,p))
    orbits = []
    while unused:
        representative = min(unused)
        orbit = tuple(sorted(representative*h % p for h in subgroup))
        orbits.append(orbit)
        unused.difference_update(orbit)
    lookup = {x:i for i,orbit in enumerate(orbits) for x in orbit}
    return subgroup,orbits,lookup


def layer_matrix(p,c):
    _,orbits,lookup = orbit_data(p)
    r = len(orbits)
    matrix = [[0]*r for _ in range(r)]
    for i,orbit in enumerate(orbits):
        for point in orbit:
            source = (point+c) % p
            if source:
                matrix[i][lookup[source]] += 1
            else:
                matrix[i] = [x-3 for x in matrix[i]]
    assert [sum(row[j] for row in matrix) for j in range(r)] == [-int(j==lookup[c]) for j in range(r)]
    return matrix


def determinant(matrix):
    a = [list(map(F,row)) for row in matrix]
    result = F(1)
    for j in range(len(a)):
        pivot = next((i for i in range(j,len(a)) if a[i][j]),None)
        if pivot is None:
            return F(0)
        if pivot != j:
            a[pivot],a[j] = a[j],a[pivot]
            result = -result
        value = a[j][j]
        result *= value
        for i in range(j+1,len(a)):
            ratio = a[i][j]/value
            for k in range(j,len(a)):
                a[i][k] -= ratio*a[j][k]
    return result


def physical_layer(p,c,values):
    _,orbits,lookup = orbit_data(p)
    r = len(orbits)
    state = [F(-3*sum(values))]+[F(values[lookup[i]]) for i in range(1,p)]
    output = []
    operations = []
    for orbit in orbits:
        triple = tuple((point+c)%p for point in orbit)
        mean = sum(state[i] for i in triple)/3
        for i in triple:
            state[i] = mean
        output.append(triple)
        operations.append(triple)
    following = [state[triple[0]] for triple in output]
    assert state[c] == values[lookup[c]]
    matrix = layer_matrix(p,c)
    assert following == [sum((F(a)*x for a,x in zip(row,values)),F(0))/3 for row in matrix]
    assert -3*sum(following) == state[c]
    assert sorted([c]+[i for triple in operations for i in triple]) == list(range(p))
    return following,operations


def investigate(p):
    _,orbits,_ = orbit_data(p)
    r = len(orbits)
    matrices = [layer_matrix(p,orbit[0]) for orbit in orbits]
    result = identity(r)
    for matrix in matrices:
        result = multiply(matrix,result)
    norm = result[0][0]
    assert result == [[norm*int(i==j) for j in range(r)] for i in range(r)]
    assert norm == determinant(matrices[0]) and norm > 0
    assert int(norm) % p == pow(3,r,p)
    sparse = []
    for i,j in combinations(range(r),2):
        vector = [row[i]-row[j] for row in matrices[0]]
        if sum(bool(x) for x in vector) <= 2:
            sparse.append((i,j,vector))
    values = list(range(1,r+1))
    original = values.copy()
    for orbit in orbits:
        values,_ = physical_layer(p,orbit[0],values)
    assert values == [F(norm,3**r)*x for x in original]
    print('p',p,'rank',r,'Gaussian norm',norm,'scalar',F(norm,3**r),
          'sparse root images',len(sparse),'averages',r*r)
    if r <= 6:
        print('K',matrices[0],'root samples',sparse[:4])
    return matrices,norm


if __name__ == '__main__':
    for p in (7,13,19,31,37,43):
        investigate(p)
