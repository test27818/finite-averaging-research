"""Independent Fraction replay for the integer B_n template compiler."""

from collections import Counter
from fractions import Fraction as F
from math import gcd, lcm

from compile_bn_integer_templates import compile_returns, solved_size, away_three
from explore_b17_universal_subblocks import universal_call
from b17_universal_atomic_words import nine_word


def physical_matrix(row):
    scalar = F(1)
    for key in ('first','middle')+(('extra',) if 'extra' in row else ()):
        a,b = row[key]['scale']
        scalar *= F(a,b)
    return tuple(scalar*x/row['denominator'] for x in row['raw'])


def normalized_matrix(matrix):
    denominator = lcm(*(x.denominator for x in matrix))
    integer = tuple(int(x*denominator) for x in matrix)
    divisor = gcd(*integer)
    primitive = tuple(x//divisor for x in integer)
    return min(primitive,tuple(-x for x in primitive))


def replay(n, row):
    r = n-4
    u,v,w = (F(1),F(0)),(F(0),F(1)),(F(-r),F(-3))
    state = [u]*r+[v]*3+[w]
    scalar = F(1)
    normalized = row['source']
    calls = []

    def select(counts):
        indices = []
        for (x,y,c),count in zip(normalized,counts):
            value = scalar*x,scalar*y
            for _ in range(count):
                indices.append(next(i for i,t in enumerate(state) if t == value and i not in indices))
        return indices

    def average(indices):
        mean = tuple(sum(state[i][j] for i in indices)/len(indices) for j in (0,1))
        for i in indices:
            state[i] = mean
        return mean

    def call(indices,first=False):
        counts = Counter(state[i] for i in indices)
        size = len(indices)
        mean = tuple(sum(state[i][j] for i in indices)/size for j in (0,1))
        assert universal_call(tuple(counts.items()),mean)
        if first and size == 6:
            assert counts == Counter({u:4,v:2})
            remaining = list(indices)
            for _ in range(2):
                triple = []
                for value in (u,u,v):
                    index = next(i for i in remaining if state[i] == value)
                    remaining.remove(index)
                    triple.append(index)
                average(triple)
        elif size in (3,9):
            for triple in ((tuple(indices),) if size == 3 else nine_word(tuple(indices))):
                average(triple)
        else:
            assert solved_size(size) and size < n
            average(indices)
        assert all(state[i] == mean for i in indices)
        calls.append((size,tuple(counts.items()),mean))
        return mean

    stages = (('first','after_first'),('middle','before_final'))
    if 'extra' in row:
        stages = (('first','after_first'),('middle','before_extra'),('extra','before_final'))
    for key,following in stages:
        call(select(row[key]['counts']),first=(key == 'first'))
        a,b = row[key]['scale']
        scalar *= F(a,b)
        normalized = row[following]
        expected = Counter({(scalar*x,scalar*y):c for x,y,c in normalized})
        assert Counter(state) == expected
    indices = select(row['final']['counts'])
    remainder = [i for i in range(n) if i not in indices]
    x,y,_ = normalized[row['final']['singleton']]
    singleton = next(i for i in remainder if state[i] == (scalar*x,scalar*y))
    first = call(indices)
    repair = [i for i in remainder if i != singleton]+indices[:len(indices)-r]
    assert len(repair) == 3
    second = average(repair)
    tail = tuple(-r*first[j]-3*second[j] for j in (0,1))
    expected = Counter({first:r,second:3,tail:1})
    assert Counter(state) == expected
    assert first+second == physical_matrix(row)
    return calls


def verify():
    from explore_b17_two_stage_universal import compile_returns as legacy
    old,_ = legacy()
    rows17,stats = compile_returns(17)
    assert set(rows17) == set(old) and stats['prefixes'] == 289
    for matrix,row in rows17.items():
        replay(17,row)
        assert normalized_matrix(physical_matrix(row)) == matrix
    print('integer compiler independent n17 replay and 95-matrix equality: PASS')
    rows19,stats = compile_returns(19,True)
    assert len(rows19) == 222 and stats['prefixes'] == 343
    for matrix,row in rows19.items():
        replay(19,row)
        assert normalized_matrix(physical_matrix(row)) == matrix
        m = physical_matrix(row)
        for value in (m[0]+m[1]-1,m[2]+m[3]-1):
            assert value.numerator % 19 == 0
    print('integer compiler independent n19 universal interfaces: PASS 222')
    rows23,_ = compile_returns(23,True)
    assert len(rows23) == 60
    for matrix,row in rows23.items():
        replay(23,row)
        assert normalized_matrix(physical_matrix(row)) == matrix
    print('integer compiler independent n23 universal interfaces: PASS 60')


if __name__ == '__main__':
    verify()
