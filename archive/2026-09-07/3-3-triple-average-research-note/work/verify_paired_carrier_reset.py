"""Equal-carrier entry and a rank-preserving uniform2-adic reset.

All physical operations use the original3r+2 positions. The normalized
reset is R-unimodular; it is not asserted to have a positive inverse.
"""

from fractions import Fraction as F
from math import gcd,lcm
from itertools import permutations
from random import Random

from verify_flat_star_arithmetic import identity,multiply,inverse
from explore_gaussian_period_layers import determinant
from verify_fifteen_via_subblocks import centered_g


K4 = ((1,2,0,0),(0,1,1,1),(0,0,2,1),(2,0,0,1))


def reset_roles(r):
    assert r >= 5 and r % 2
    result = []
    for a in range(1,r,2):
        b = a+1
        spectator = next(i for i in range(r) if i not in (0,a,b))
        result.append((spectator,0,a,b))
    for a in range(1,r,2):
        b = a+1
        spectator = next(i for i in range(r) if i not in (0,a,b))
        result.append((spectator,a,b,0))
    return result


def reduced_pair_exchange(r,index):
    result = identity(r)
    result[index] = [F(-2,3) if j == index else F(-1) for j in range(r)]
    return result


def reset_leaf_matrix(r):
    result = identity(r)
    for roles in reset_roles(r):
        matrix = identity(r)
        for i,row in enumerate(K4):
            for j,value in enumerate(row):
                matrix[roles[i]][roles[j]] = F(value,3)
        result = multiply(matrix,result)
    return result


def natural_coordinates(r):
    # Parameters (u_0,...,u_(r-2),a); u_last=-sum(u_i)-2a/3.
    q = identity(r)
    q[-1] = [F(-1)]*(r-1)+[F(-2,3)]
    return q,inverse(q)


def power_three_denominators(matrix):
    for row in matrix:
        for value in row:
            d = value.denominator
            while d % 3 == 0:d //= 3
            if d != 1:return False
    return True


def verify_matrix_reset():
    checked = 0
    assert determinant(K4) == 6
    assert all(sum(row) == 3 for row in K4)
    assert all(sum(row[j] for row in K4) == 3 for j in range(4))
    for r in (5,7,9,11,13,15):
        leaf = reset_leaf_matrix(r)
        assert all(value.numerator*pow(value.denominator,-1,2) % 2 == 1
                   for row in leaf for value in row)
        assert determinant(leaf) == F(2,27)**(r-1)
        q,qi = natural_coordinates(r)
        gram = multiply(list(map(list,zip(*q))),q)
        gram = [[3*x+2*int(i==r-1 and j==r-1) for j,x in enumerate(row)] for i,row in enumerate(gram)]
        assert determinant(gram) == 2*(3*r+2)*3**(r-2)
        raw = multiply(multiply(qi,multiply(reduced_pair_exchange(r,0),leaf)),q)
        normalized = [[value/2 for value in row] for row in raw]
        assert power_three_denominators(normalized)
        assert power_three_denominators(inverse(normalized))
        assert determinant(normalized) == -F(1,3**(3*r-2))
        assert determinant(raw) == -F(2**r,3**(3*r-2))
        trace = sum(normalized[i][i] for i in range(r))
        assert (trace**r/determinant(normalized)).denominator != 1
        print('reset n',3*r+2,'operations',4*r-3,'normalized trace',trace)
        checked += 1
    print('uniform paired reset: parity matrix and R-unimodular normalization: PASS',checked)
    print('paired lattice discriminant and reset trace finite-order obstruction: PASS',checked)


def verify_permuted_reset_torsion():
    checked = 0
    for r in (5,7):
        raw = multiply(reduced_pair_exchange(r,0),reset_leaf_matrix(r))
        normalized = [[x/2 for x in row] for row in raw]
        det = determinant(normalized)
        for perm in permutations(range(r)):
            matrix = [normalized[i] for i in perm]
            # Changing the sign of det cannot change integrality.
            trace = sum(matrix[i][i] for i in range(r))
            if (trace**r/det).denominator == 1:
                square = multiply(matrix,matrix)
                trace = sum(square[i][i] for i in range(r))
                assert (trace**r/(det*det)).denominator != 1
            checked += 1
    print('all post-reset leaf permutations excluded by trace integrality: PASS',checked)


def verify_physical_reset():
    operations = 0
    for r in (5,7,9,15):
        n = 3*r+2
        q,qi = natural_coordinates(r)
        state = [tuple(row) for row in q for _ in range(3)]
        carrier = tuple(F(i==r-1) for i in range(r))
        state += [carrier,carrier]
        groups = [list(range(3*i,3*i+3)) for i in range(r)]
        pair = [n-2,n-1]
        for roles in reset_roles(r):
            available = [groups[index].copy() for index in roles]
            output = []
            for row in K4:
                triple = [available[j].pop() for j,count in enumerate(row) for _ in range(count)]
                assert len(triple) == len(set(triple)) == 3
                mean = tuple(sum(state[position][i] for position in triple)/3 for i in range(r))
                for position in triple:state[position] = mean
                output.append(triple)
                operations += 1
            assert all(not entries for entries in available)
            for index,positions in zip(roles,output):groups[index] = positions
        previous = groups[0]
        triple = pair+[previous[0]]
        mean = tuple(sum(state[position][i] for position in triple)/3 for i in range(r))
        for position in triple:state[position] = mean
        pair = previous[1:]
        groups[0] = triple
        operations += 1
        output = multiply(multiply(reduced_pair_exchange(r,0),reset_leaf_matrix(r)),q)
        for i,group in enumerate(groups):
            assert all(state[position] == tuple(output[i]) for position in group)
        expected_pair = tuple(-F(3,2)*sum(output[i][j] for i in range(r)) for j in range(r))
        assert all(state[position] == expected_pair for position in pair)
        assert sorted(pair+[position for group in groups for position in group]) == list(range(n))
    print('paired reset full coefficient replay on original positions: PASS',operations)


def ideal_generator(values):
    denominator = lcm(*(value.denominator for value in values))
    result = F(gcd(*(int(value*denominator) for value in values)),denominator)
    numerator,denominator = result.numerator,result.denominator
    while numerator and numerator % 3 == 0:numerator //= 3
    while denominator % 3 == 0:denominator //= 3
    return F(numerator,denominator)


def verify_ideal_and_scalar_constraints():
    random = Random(472023)
    checked = 0
    for r in (5,7,9,15):
        q,qi = natural_coordinates(r)
        raw = multiply(multiply(qi,multiply(reduced_pair_exchange(r,0),reset_leaf_matrix(r))),q)
        for _ in range(30):
            z = [F(random.randrange(-100,101)*random.choice((1,2,4,5,7)),
                   3**random.randrange(4)) for _ in range(r)]
            out = [sum(a*b for a,b in zip(row,z)) for row in raw]
            def expand(params):
                leaves = [sum(a*b for a,b in zip(row,params)) for row in q]
                return [value for value in leaves for _ in range(3)]+[params[-1]]*2
            before,after = expand(z),expand(out)
            assert sum(before) == sum(after) == 0
            assert ideal_generator(after) == 2*ideal_generator(before)
            assert ideal_generator([x-after[0] for x in after]) == 2*ideal_generator([x-before[0] for x in before])
            assert centered_g(before) == centered_g(after)
            checked += 1
        for resets in range(2*r+1):
            for exchanges in range(2*r+1):
                v2 = r*resets+exchanges
                v3 = -(3*r-2)*resets-exchanges
                assert (v2 % r == v3 % r == 0) == (resets % r == exchanges % r == 0)
    print('exact coordinate/difference ideals and scalar-word divisibility: PASS',checked)


def verify_safe_entry_and_no_cycles():
    checked = 0
    for n in (17,23,29,35,41,47,65,95,119):
        r = (n-2)//3
        u = [1,-1]+[n*(i+1) for i in range(r-2)]
        w = 1+n
        z = -3*sum(u)-w
        selected = 2
        mean = F(w+z+u[selected],3)
        before = [F(x) for x in u for _ in range(3)]+[F(w),F(z)]
        after_u = list(map(F,u))
        after_u[selected] = mean
        after = [x for value in after_u for x in [value]*3]+[F(u[selected])]*2
        assert sum(before) == sum(after) == 0 and centered_g(before) == centered_g(after) == 1
        parity_state = [F(1),F(-1)]+[F(0)]*(r-2)
        parity = [int(x) % 2 for x in parity_state]
        for i in range(r):
            output = [sum(a*b for a,b in zip(row,parity_state))
                      for row in reduced_pair_exchange(r,i)]
            assert [x.numerator*pow(x.denominator,-1,2) % 2 for x in output] == parity
        checked += 1
    print('safe equal-carrier entry and invariant nonzero leaf parity: PASS',checked)


def verify_virtual_mass_boundary():
    checked = 0
    for p in (11,17,23,29,41,47):
        for a in (F(-3),F(1),F(5,9)):
            for scalar in (F(1,3),F(-1,9),F(4,27)):
                ghost = a*(1+p*scalar)/(p+1)
                physical_sum = a-ghost
                assert physical_sum == F(p,p+1)*(1-scalar)*a != 0
                checked += 1
    print('virtual-point deletion violates the conserved physical sum: PASS',checked)


def verify():
    verify_matrix_reset()
    verify_permuted_reset_torsion()
    verify_physical_reset()
    verify_ideal_and_scalar_constraints()
    verify_safe_entry_and_no_cycles()
    verify_virtual_mass_boundary()


if __name__ == '__main__':
    verify()
