"""Fixed positive inverses and integral unipotents for B17.

All named generators are expanded into atomic triples on 17 fixed slots.
No solved-subproblem oracle is used in this certificate replay.
"""

from fractions import Fraction as F
from functools import lru_cache
from math import gcd

from b17_universal_atomic_words import certificates as old_certificates, nine_word, pattern_word, average
from explore_b17_two_stage_universal import compile_returns
from explore_b17_integral_return_cover import mul, image, I


INTEGER = {
    'A': (3,0,-13,-1), 'B': (7,2,-33,-9),
    'P': (-65,-16,303,75), 'Q': (-8,-1,37,5),
    'T': (-24,-3,109,17), 'U': (-22,-5,103,23),
}
ACTUAL = {
    'A': tuple(F(x,3) for x in INTEGER['A']),
    'B': tuple(F(x,9) for x in INTEGER['B']),
    'P': tuple(F(-x,81) for x in INTEGER['P']),
    'Q': tuple(F(-x,9) for x in INTEGER['Q']),
    'T': tuple(F(-x,27) for x in INTEGER['T']),
    'U': tuple(F(-x,27) for x in INTEGER['U']),
}
INVERSE_WORD = {'a':'QUAQU', 'b':'QTBQT', 'p':'QPQ',
                'q':'UAQUA', 't':'BQTBQ', 'u':'AQUAQ'}
PATTERNS = {
    'P': (81, [(-16,2,2),(-4,2,2)]+[(-4,1,0)]*2+[(-1,0,1)]*6),
    'Q': (9, [(8,-1,-1)]+[(2,-1,-1)]*3+[(-1,0,1)]*2),
    'T': (9, [(2,-1,-1)]*2+[(3,0,0)]*2+[(-1,0,1)]*6),
    'U': (27, [(22,-5,-5),(4,4,-5),(4,1,1)]
              +[(-5,1,1)]*2+[(2,-1,-1)]*3+[(-1,0,1)]*2),
}


def inverse(matrix):
    a,b,c,d = matrix
    determinant = a*d-b*c
    return tuple(F(x,determinant) for x in (d,-b,-c,a))


def expand(word):
    return ''.join(INVERSE_WORD.get(letter,letter) for letter in word)


def word_matrix(word, physical=True):
    matrix = I
    for letter in word:
        if physical:
            generator = ACTUAL[letter]
        else:
            generator = ACTUAL[letter.upper()]
            if letter.islower():
                generator = inverse(generator)
        matrix = mul(generator,matrix)
    return matrix


@lru_cache(maxsize=1)
def atomic_certificates():
    rows,_ = compile_returns()
    result = {'A': (((14,15,16),), tuple(range(13))+(14,15,16,13)),
              'B': old_certificates()['B']}
    for name in PATTERNS:
        row = rows[INTEGER[name]]
        state = [(F(1),F(0))]*13+[(F(0),F(1))]*3+[(F(-13),F(-3))]
        operations = []

        def select(block):
            selected = []
            for value,count in block:
                for _ in range(count):
                    selected.append(next(i for i,x in enumerate(state) if x == value and i not in selected))
            return tuple(selected)

        def symbolic_average(indices):
            mean = tuple(sum(state[i][j] for i in indices)/3 for j in (0,1))
            for i in indices:
                state[i] = mean
            operations.append(indices)

        for key in ('first','middle'):
            indices = select(row[key])
            word = (indices,) if len(indices) == 3 else nine_word(indices)
            for triple in word:
                symbolic_average(triple)
        indices = select(row['final'])
        denominator, triples = PATTERNS[name]
        mean = row['matrix'][:2]
        unit = (F(-1,denominator),F(1,denominator))
        reference = []
        for i in indices:
            coefficient = (state[i][0]-mean[0])/unit[0]
            assert coefficient.denominator == 1
            assert state[i] == tuple(mean[j]+coefficient*unit[j] for j in (0,1))
            reference.append(int(coefficient))
        for triple in pattern_word(reference,triples):
            symbolic_average(tuple(indices[i] for i in triple))
        symbolic_average(select(row['repair']))
        x,y = row['matrix'][:2],row['matrix'][2:]
        singleton = tuple(-13*x[j]-3*y[j] for j in (0,1))
        order = tuple(i for value in (x,y,singleton) for i,z in enumerate(state) if z == value)
        assert [state.count(value) for value in (x,y,singleton)] == [13,3,1]
        assert row['matrix'] == ACTUAL[name]
        result[name] = tuple(operations),order
    assert {name:len(word) for name,(word,_) in result.items()} == {
        'A':1,'B':17,'P':23,'Q':9,'T':13,'U':18}
    return result


def apply_word(word, pair):
    u,v = map(F,pair)
    state = [u]*13+[v]*3+[-13*u-3*v]
    for letter in expand(word):
        operations,order = atomic_certificates()[letter]
        for triple in operations:
            average(state,triple)
        state = [state[i] for i in order]
    return state


def verify():
    certificates = atomic_certificates()
    for name in ACTUAL:
        for pair in ((1,0),(0,1),(1,1),(2,-7),(F(1,9),F(-4,3))):
            x,y = image(ACTUAL[name],pair)
            assert apply_word(name,pair) == [x]*13+[y]*3+[-13*x-3*y]
    print('B17 additional atomic macros P23 Q9 T13 U18: PASS')
    scalar = F(-1,3**8)
    for cycle in ('PQPQ','BQTBQT','AQUAQU'):
        assert word_matrix(cycle) == (scalar,0,0,scalar)
    for letter,word in INVERSE_WORD.items():
        matrix = word_matrix(word)
        assert mul(matrix,ACTUAL[letter.upper()]) == (scalar,0,0,scalar)
        for pair in ((1,0),(0,1),(2,-7)):
            x,y = image(matrix,pair)
            assert apply_word(word,pair) == [x]*13+[y]*3+[-13*x-3*y]
    assert sum(len(certificates[x][0]) for x in INVERSE_WORD['a']) == 55
    assert sum(len(certificates[x][0]) for x in INVERSE_WORD['b']) == 61
    print('B17 positive inverses of A and B (55 and 61 atomic steps): PASS')

    k_word = 'AAqT'
    K = word_matrix(k_word,physical=False)
    assert K == (1,0,F(2,3),F(1,3))
    lower_word = k_word+k_word+'aa'
    lower = word_matrix(lower_word,physical=False)
    assert lower == (1,0,34,1)
    physical = word_matrix(expand(lower_word))
    assert physical == tuple(F(x,3**32) for x in lower)
    assert sum(len(certificates[x][0]) for x in expand(lower_word)) == 234
    for pair in ((1,0),(0,1),(2,-7)):
        x,y = image(physical,pair)
        assert apply_word(lower_word,pair) == [x]*13+[y]*3+[-13*x-3*y]
    assert mul(K,mul(lower,inverse(K))) == (1,0,F(34,3),1)
    C = (2,0,-9,1)
    assert mul(inverse(C),mul(lower,C)) == (1,0,68,1)
    opposite = mul(ACTUAL['B'],mul(lower,inverse(ACTUAL['B'])))
    assert mul(inverse(C),mul(opposite,C)) == (1,F(-68,3),0,1)
    print('B17 positive integral unipotent and opposite level-68 root groups: PASS')


if __name__ == '__main__':
    verify()
