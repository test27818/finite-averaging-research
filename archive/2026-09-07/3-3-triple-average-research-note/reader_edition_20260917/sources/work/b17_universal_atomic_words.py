"""Fixed 17/19-step atomic B17 returns, independent of solved-n oracles.

Inputs use slots u[0:13], v[13:16], w[16]. Each certificate returns an
operation word and an output slot order; the latter only relabels slots.
"""

from fractions import Fraction as F
from functools import lru_cache


def average(state, indices):
    assert len(indices) == len(set(indices)) == 3
    mean = sum((state[i] for i in indices), F(0))/3
    for i in indices:
        state[i] = mean


def pattern_word(reference, triples):
    state = list(map(F, reference))
    word = []
    for triple in triples:
        indices = []
        for value in triple:
            indices.append(next(i for i, x in enumerate(state) if x == value and i not in indices))
        indices = tuple(indices)
        average(state, indices)
        word.append(indices)
    assert not any(state)
    return tuple(word)


def nine_word(indices):
    assert len(indices) == 9
    return (tuple(indices[0:3]), tuple(indices[3:6]), tuple(indices[6:9]),
            tuple(indices[0::3]), tuple(indices[1::3]), tuple(indices[2::3]))


@lru_cache(maxsize=1)
def certificates():
    thirteen = pattern_word([-2]*3+[-1]*8+[7]*2,
                            [(7,7,-2), (4,-2,-2)]+[(4,-1,0)]*2+[(-1,0,1)]*6)
    fifteen = pattern_word([-5]*6+[1]*8+[22],
                           [(22,-5,-5), (4,4,-5), (4,1,1)]
                           +[(-5,1,1)]*3+[(2,-1,-1)]*3+[(-1,0,1)]*3)
    assert len(thirteen) == 10 and len(fifteen) == 12
    result = {}

    nine = tuple(range(8))+(13,)
    block = (8,9,10)+tuple(range(8))+(14,15)
    prefix = nine_word(nine)+tuple(tuple(block[i] for i in triple) for triple in thirteen)
    for name, triple, singleton in (('R',(13,11,12),16), ('B',(11,12,16),13),
                                    ('C',(13,11,16),12)):
        result[name] = prefix+(triple,), block+triple+(singleton,)

    nine = tuple(range(7))+(13,14)
    block = tuple(range(7,13))+tuple(range(7))+(13,15)
    prefix = nine_word(nine)+tuple(tuple(block[i] for i in triple) for triple in fifteen)
    for name, extra, singleton in (('D',14,16), ('E',16,14)):
        triple = block[:2]+(extra,)
        result[name] = prefix+(triple,), block[2:]+triple+(singleton,)
    for name, (word, order) in result.items():
        assert len(word) == (17 if name in ('R','B','C') else 19)
        assert sorted(order) == list(range(17))
    return result


def apply(name, u, v):
    u, v = F(u), F(v)
    state = [u]*13+[v]*3+[-13*u-3*v]
    word, order = certificates()[name]
    for indices in word:
        average(state, indices)
    return tuple(state[i] for i in order)


if __name__ == '__main__':
    for name, (word, order) in certificates().items():
        print(name, len(word), 'atomic averages')
        print('word', word)
        print('output slot order', order)
