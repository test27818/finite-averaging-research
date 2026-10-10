"""Compile fixed atomic words for rank-one final subproblem patterns."""

from fractions import Fraction as F

from b17_universal_atomic_words import nine_word,pattern_word
from verify_bn_integer_templates import physical_matrix


def compile_atomic(n,row,unit_denominator,triples):
    r = n-4
    state = [(F(1),F(0))]*r+[(F(0),F(1))]*3+[(F(-r),F(-3))]
    scalar = F(1)
    normalized = row['source']
    operations = []

    def select(counts):
        indices = []
        for (x,y,c),count in zip(normalized,counts):
            value = scalar*x,scalar*y
            for _ in range(count):
                indices.append(next(i for i,z in enumerate(state) if z == value and i not in indices))
        return tuple(indices)

    def average(indices):
        value = tuple(sum(state[i][j] for i in indices)/3 for j in (0,1))
        for i in indices:
            state[i] = value
        operations.append(tuple(indices))

    for key,following in (('first','after_first'),('middle','before_final')):
        indices = select(row[key]['counts'])
        assert len(indices) in (3,9)
        for triple in ((indices,) if len(indices) == 3 else nine_word(indices)):
            average(triple)
        a,b = row[key]['scale']
        scalar *= F(a,b)
        normalized = row[following]
    indices = select(row['final']['counts'])
    remainder = [i for i in range(n) if i not in indices]
    x,y,_ = normalized[row['final']['singleton']]
    singleton = next(i for i in remainder if state[i] == (scalar*x,scalar*y))
    matrix = physical_matrix(row)
    mean = matrix[:2]
    unit = F(-1,unit_denominator),F(1,unit_denominator)
    reference = []
    for i in indices:
        coefficient = (state[i][0]-mean[0])/unit[0]
        assert coefficient.denominator == 1
        assert state[i] == tuple(mean[j]+coefficient*unit[j] for j in (0,1))
        reference.append(int(coefficient))
    for triple in pattern_word(reference,triples):
        average(tuple(indices[i] for i in triple))
    repair = [i for i in remainder if i != singleton]+list(indices[:len(indices)-r])
    assert len(repair) == 3
    average(repair)
    first,second = matrix[:2],matrix[2:]
    tail = tuple(-r*first[j]-3*second[j] for j in (0,1))
    assert [state.count(value) for value in (first,second,tail)] == [r,3,1]
    order = tuple(i for value in (first,second,tail) for i,z in enumerate(state) if z == value)
    return tuple(operations),order
