"""Punctured projective order-three averaging on p original positions.

Finite diagnostics only. The missing projective point is bookkeeping,
never an extra physical position or an available zero-valued input.
"""

from fractions import Fraction as F
from explore_gaussian_period_layers import prime, determinant
from verify_flat_star_arithmetic import identity, multiply


def mobius(x,p):
    if x == p:
        return 0
    if x == p-1:
        return p
    return -pow(x+1,-1,p) % p


def orbit_data(p):
    assert prime(p) and p % 3 == 2 and p >= 5
    unused = set(range(1,p-1))
    orbits = []
    while unused:
        a = min(unused)
        orbit = tuple(sorted((a,mobius(a,p),mobius(mobius(a,p),p))))
        assert len(set(orbit)) == 3 and p not in orbit
        orbits.append(orbit)
        unused.difference_update(orbit)
    lookup = {x:i for i,orbit in enumerate(orbits) for x in orbit}
    assert mobius(mobius(mobius(p,p),p),p) == p
    return orbits,lookup


def layer_matrix(p,c):
    orbits,lookup = orbit_data(p)
    rank = len(orbits)+1
    values = [[int(i==j) for j in range(rank)] for i in range(rank)]
    point = {x:values[index] for x,index in lookup.items()}
    point[0] = values[-1]
    point[p-1] = [-3]*(rank-1)+[-1]
    rows = [[sum(point[(x+c)%p][j] for x in orbit) for j in range(rank)] for orbit in orbits]
    rows.append([3*x for x in point[c % p]])
    return [[F(x,3) for x in row] for row in rows]


def rank(matrix):
    a = [list(map(F,row)) for row in matrix]
    pivot_row = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(pivot_row,len(a)) if a[i][j]),None)
        if pivot is None:
            continue
        a[pivot_row],a[pivot] = a[pivot],a[pivot_row]
        value = a[pivot_row][j]
        for i in range(pivot_row+1,len(a)):
            factor = a[i][j]/value
            a[i] = [x-factor*y for x,y in zip(a[i],a[pivot_row])]
        pivot_row += 1
        if pivot_row == len(a):
            break
    return pivot_row


def physical_layers(p,shifts):
    orbits,lookup = orbit_data(p)
    width = len(orbits)+1
    basis = [tuple(F(i==j) for j in range(width)) for i in range(width)]
    state = [None]*p
    for point,index in lookup.items():
        state[point] = basis[index]
    state[0] = basis[-1]
    state[-1] = tuple(F(-3) for _ in orbits)+(F(-1),)
    locations = list(range(p))
    matrix = identity(width)
    operations = 0
    for c in shifts:
        for orbit in orbits:
            selected = [locations[(x+c)%p] for x in orbit]
            mean = tuple(sum(state[x][j] for x in selected)/3 for j in range(width))
            for x in selected:
                state[x] = mean
            operations += 1
        locations = [locations[(x+c)%p] for x in range(p)]
        matrix = multiply(layer_matrix(p,c),matrix)
        for x,index in lookup.items():
            assert state[locations[x]] == tuple(matrix[index])
        assert state[locations[0]] == tuple(matrix[-1])
        assert state[locations[-1]] == tuple(-3*sum(matrix[i][j] for i in range(width-1))-matrix[-1][j]
                                             for j in range(width))
        assert sorted(locations) == list(range(p))
    return operations


def investigate(p):
    matrices = [layer_matrix(p,c) for c in range(p)]
    determinants = [determinant(matrix) for matrix in matrices]
    comm = [[x-y for x,y in zip(a,b)] for a,b in zip(multiply(matrices[1],matrices[2]),
                                                   multiply(matrices[2],matrices[1]))]
    scalar = identity(len(matrices[0]))
    for matrix in matrices[1:]:
        scalar = multiply(matrix,scalar)
    scalar_cycle = all(value == scalar[0][0]*int(i==j)
                       for i,row in enumerate(scalar) for j,value in enumerate(row))
    operations = physical_layers(p,(1,2,p-1))
    print('p',p,'rank',len(matrices[0]),'singular shifts',[c for c,d in enumerate(determinants) if not d],
          'commutator rank',rank(comm),'all-shift scalar',scalar_cycle,'physical averages',operations)
    if p <= 11:
        print('P1',matrices[1])
    return determinants,rank(comm),scalar_cycle


if __name__ == '__main__':
    for p in (5,11,17,23,29):
        investigate(p)
