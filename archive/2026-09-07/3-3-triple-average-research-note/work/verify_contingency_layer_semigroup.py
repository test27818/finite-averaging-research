"""Weighted contingency matrices exactly encode original-position layers.

Only size-three output blocks are averaged, so all letters are universally
executable with no child solver. The proposed terminal coverage is open.
"""

from fractions import Fraction as F
from itertools import combinations,product
from random import Random

from verify_flat_star_arithmetic import identity,multiply
from verify_two_carrier_modular_bridge import carrier


def matrix_from_orders(weights,order):
    owners = [j for j,w in enumerate(weights) for _ in range(w)]
    assert sorted(order) == list(range(len(owners)))
    count = [[0]*len(weights) for _ in weights]
    offset = 0
    for i,w in enumerate(weights):
        for position in order[offset:offset+w]:count[i][owners[position]]+=1
        offset += w
    return count


def build_positions(weights,count):
    pools = []
    offset = 0
    for w in weights:
        pools.append(list(range(offset,offset+w)))
        offset += w
    used = [0]*len(weights)
    blocks = []
    for row in count:
        block = []
        for j,c in enumerate(row):
            block += pools[j][used[j]:used[j]+c]
            used[j] += c
        blocks.append(block)
    assert used == weights
    return blocks


def quotient(weights,count):
    return [[F(c,weights[i]) for c in row] for i,row in enumerate(count)]


def natural_restriction(r,q):
    # Independent u_0,...,u_(r-1),w; last carrier=-3sum(u)-w.
    embedding = identity(r+1)+[[F(-3)]*r+[F(-1)]]
    return multiply(q,embedding)[:r+1]


def matrix_rank(matrix):
    rows = [list(map(F,row)) for row in matrix]
    rank = 0
    for column in range(len(rows[0])):
        pivot = next((i for i in range(rank,len(rows)) if rows[i][column]),None)
        if pivot is None:continue
        rows[rank],rows[pivot] = rows[pivot],rows[rank]
        value = rows[rank][column]
        rows[rank] = [x/value for x in rows[rank]]
        for i in range(rank+1,len(rows)):
            value = rows[i][column]
            rows[i] = [a-value*b for a,b in zip(rows[i],rows[rank])]
        rank += 1
    return rank


def verify_layers():
    rng = Random(20260910)
    cases,atoms = 0,0
    for r,delta in ((1,2),(2,1),(3,2),(5,2),(17,2)):
        weights = [3]*r+[1]*delta
        dimension = len(weights)
        n = sum(weights)
        for _ in range(12):
            order = list(range(n))
            rng.shuffle(order)
            count = matrix_from_orders(weights,order)
            assert list(map(sum,count)) == weights
            assert [sum(row[j] for row in count) for j in range(dimension)] == weights
            blocks = build_positions(weights,count)
            state = [row[:] for j,w in enumerate(weights) for row in [identity(dimension)[j]]*w]
            q = quotient(weights,count)
            for i,block in enumerate(blocks):
                assert len(block) == weights[i]
                if len(block) == 3:
                    mean = [sum(state[j][k] for j in block)/3 for k in range(dimension)]
                    for j in block:state[j] = mean[:]
                    atoms += 1
                assert all(state[j] == q[i] for j in block)
            # Transpose reversal is the exact weighted adjoint letter.
            reverse_count = [list(row) for row in zip(*count)]
            reverse_q = quotient(weights,reverse_count)
            assert all(reverse_q[i][j] == q[j][i]*F(weights[j],weights[i])
                       for i in range(dimension) for j in range(dimension))
            cases += 1
    print('original-position contingency layers and weighted adjoint reversal: PASS',cases,atoms)


def verify_carriers():
    checked = 0
    for r in range(2,8):
        weights = [3]*r+[1,1]
        for i in range(r):
            for which,column in (('w',r),('z',r+1)):
                count = [[weights[a]*int(a==b) for b in range(r+2)] for a in range(r+2)]
                count[i][i],count[i][column] = 2,1
                count[column][i],count[column][column] = 1,0
                assert natural_restriction(r,quotient(weights,count)) == carrier(r,i,which)
                checked += 1
    print('all carrier macros are explicit letters of the same contingency semigroup: PASS',checked)


def verify_terminal_hyperplanes():
    r = 3
    weights = [3]*r+[1,1]
    patterns = [s for s in product(range(4),repeat=r+2)
                if sum(s) == 3 and all(a<=b for a,b in zip(s,weights))]
    assert len(patterns) == 25
    support_patterns = {tuple(sum(j==owner for owner in choice) for j in range(r+2))
                        for choice in combinations([j for j,w in enumerate(weights) for _ in range(w)],3)}
    assert set(patterns) == support_patterns
    count = [[w*int(i==j) for j in range(r+2)] for i,w in enumerate(weights)]
    chosen = patterns[7]
    capacities = [w-s for w,s in zip(weights,chosen)]
    count[0] = list(chosen)
    for i,w in enumerate(weights[1:],1):
        count[i] = [0]*(r+2)
        needed = w
        for j,c in enumerate(capacities):
            take = min(c,needed)
            count[i][j] = take
            capacities[j] -= take
            needed -= take
        assert not needed
    assert not any(capacities)
    assert list(map(sum,count)) == weights
    assert [sum(row[j] for row in count) for j in range(r+2)] == weights
    print('finite terminal hyperplanes and extension to a full layer: PASS',len(patterns))


def verify_overlap_rank():
    from verify_reynolds_hodge_structure import triple_projection
    checked = 0
    for n in range(5,10):
        first = {0,1,2}
        # Zero-sum basis for the first triple-equality subspace.
        embedding = [[F(1) if j==0 else F(0) for j in range(n-3)] for _ in range(3)]
        embedding += [[F(j==i+1) for j in range(n-3)] for i in range(n-4)]
        embedding += [[F(-3)]+[F(-1)]*(n-4)]
        assert matrix_rank(embedding) == n-3
        for second in combinations(range(n),3):
            overlap = len(first.intersection(second))
            rank = matrix_rank(multiply(triple_projection(n,second),embedding))
            assert rank == n-3-max(0,2-overlap)
            checked += 1
    print('exact single-triple stratum ranks by overlap zero/one/two/three: PASS',checked)


if __name__ == '__main__':
    verify_layers()
    verify_carriers()
    verify_terminal_hyperplanes()
    verify_overlap_rank()
