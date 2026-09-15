"""Fixed atomic B23 inverses and a complete index-24 congruence certificate."""

from collections import deque
from fractions import Fraction as F
from functools import lru_cache
from math import gcd

from compile_bn_integer_templates import compile_returns
from verify_bn_integer_templates import normalized_matrix,physical_matrix,replay
from bn_atomic_from_template import compile_atomic
from b17_universal_atomic_words import average,nine_word
from explore_b17_integral_return_cover import mul,image,I
from explore_b17_nine_thirteen_bridges import points,projective
from explore_thirteen_modular import Fold,modular_word,S,U
from verify_seventeen_arithmetic_group import bezout
from verify_fifteen_via_subblocks import centered_g


INTEGER = {'J':(-8,-1,52,8),'N':(-8,-1,53,7),'P':(-23,-4,154,26)}
ACTUAL = {name:tuple(F(-x,27 if name == 'P' else 9) for x in matrix)
          for name,matrix in INTEGER.items()}
INVERSE_WORD = {'j':'J','n':'PNP','p':'NPN'}
INVERSE_SCALE = {'j':F(4,27),'n':F(2,2187),'p':F(2,2187)}
PATTERNS = {
    'J':(9,[(8,-1,-1)]+[(2,-1,-1)]*3+[(4,-1,0)]*2+[(-1,0,1)]*6),
    'N':(9,[(2,-1,-1)]+[(-1,0,1)]*8),
    'P':(27,[(23,-4,-4)]*2+[(5,-4,-4)]*2+[(5,-1,-1)]*4
              +[(-4,-1,-1)]+[(-2,1,1)]*5+[(-1,0,1)]*2),
}
CERTIFICATE = (
    ('nJNJpNpJ',(-7,-1,-27,-4)), ('nPJnPJ',(-11,-2,28,5)),
    ('JpNJpN',(-5,-2,28,11)), ('NJpNpN',(-8,-1,33,4)),
    ('nnpNJpNJ',(-23,-4,75,13)), ('JPnPJnJN',(-4,1,27,-7)),
    ('NNJpNpNN',(-12,-1,73,6)),
)


def inverse(matrix):
    a,b,c,d = matrix
    determinant = a*d-b*c
    return tuple(x/determinant for x in (d,-b,-c,a))


def expand(word):
    return ''.join(INVERSE_WORD.get(letter,letter) for letter in word)


def word_matrix(word,positive=False):
    if positive:
        word = expand(word)
    matrix = I
    for letter in word:
        generator = ACTUAL[letter.upper()]
        if letter.islower():
            generator = inverse(generator)
        matrix = mul(generator,matrix)
    return matrix


@lru_cache(maxsize=1)
def certificates():
    rows,_ = compile_returns(23,True)
    result = {}
    for name,matrix in INTEGER.items():
        row = rows[matrix]
        replay(23,row)
        assert physical_matrix(row) == ACTUAL[name]
        result[name] = compile_atomic(23,row,*PATTERNS[name])
    assert {name:len(word) for name,(word,_) in result.items()} == {'J':15,'N':17,'P':24}
    return result


def apply_word(word,pair):
    u,v = map(F,pair)
    state = [u]*19+[v]*3+[-19*u-3*v]
    for letter in expand(word):
        operations,order = certificates()[letter]
        for triple in operations:
            average(state,triple)
        state = [state[i] for i in order]
    return state


def verify_words():
    certificates()
    for name in INTEGER:
        for pair in ((1,0),(0,1),(1,1),(2,-7)):
            x,y = image(ACTUAL[name],pair)
            assert apply_word(name,pair) == [x]*19+[y]*3+[-19*x-3*y]
    for letter,word in INVERSE_WORD.items():
        scalar = INVERSE_SCALE[letter]
        assert mul(word_matrix(word),ACTUAL[letter.upper()]) == (scalar,0,0,scalar)
        assert (scalar.numerator-scalar.denominator) % 23 == 0
    for word,matrix in CERTIFICATE:
        assert normalized_matrix(word_matrix(word)) == matrix
        physical = word_matrix(word,True)
        assert normalized_matrix(physical) == matrix
        a,b,c,d = matrix
        assert a*d-b*c == 1 and (a+b-c-d) % 23 == 0
        for pair in ((1,0),(0,1)):
            x,y = image(physical,pair)
            assert apply_word(word,pair) == [x]*19+[y]*3+[-19*x-3*y]
    print('B23 fixed atomic generators J15 N17 P24 and positive inverses: PASS')
    print('B23 seven positive integral matrix words: PASS')


def verify_cosets():
    fold = Fold()
    for _,matrix in CERTIFICATE:
        fold.loop(modular_word(matrix))
        fold.close()
    table = fold.close()
    nodes = {fold.root(i) for i in range(len(fold.parent))}
    assert len(nodes) == 24 and all((node,letter) in table for node in nodes for letter in 'su')
    base = fold.root(0)
    labels = {base:projective((1,-1),23)}
    representatives = {base:I}
    queue = deque([base])
    while queue:
        node = queue.popleft()
        for letter,matrix in (('s',S),('u',U)):
            target = table[node,letter]
            a,b,c,d = matrix
            x,y = labels[node]
            label = projective((x*a+y*c,x*b+y*d),23)
            if target not in labels:
                labels[target] = label
                representatives[target] = mul(representatives[node],matrix)
                queue.append(target)
            else:
                assert labels[target] == label
    assert len(labels) == 24 and set(labels.values()) == set(points(23))
    for node in nodes:
        assert table[table[node,'s'],'s'] == node
        assert table[table[table[node,'u'],'u'],'u'] == node
    unused = set(nodes)
    cusps = []
    while unused:
        start = min(unused)
        node = start
        cycle = []
        while node not in cycle:
            cycle.append(node)
            unused.remove(node)
            node = table[table[node,'s'],'u']
        assert node == start
        matrix = representatives[start]
        cusps.append((len(cycle),(matrix[0]-matrix[2]) % 23 != 0))
    assert sorted(cusps) == [(1,False),(23,True)]
    assert all(table[node,'s'] != node and table[node,'u'] != node for node in nodes)
    print('B23 exact modular folding and independent mod-23 labels: PASS 24')
    print('B23 cusp widths1/23, one legal cusp, genus2: PASS')
    return fold,table


def verify_transport(fold,table):
    checked = 0
    for u in range(-24,25):
        for v in range(-24,25):
            if gcd(u,v) != 1 or (u-v) % 23 == 0:
                continue
            c,d = bezout(u,v)
            k = ((v-u-c-d)*pow(v-u,-1,23)) % 23
            c,d = c+v*k,d-u*k
            matrix = v,-u,c,d
            assert v*d+u*c == 1 and (v-u-c-d) % 23 == 0
            assert image(matrix,(u,v)) == (0,1)
            assert fold.contains(modular_word(matrix),table)
            checked += 1
    state = [F(0)]*19+[F(1)]*3+[F(-3)]
    word = nine_word((0,1,2,3,4,19,20,21,22))
    for triple in word:
        average(state,triple)
    assert len(word) == 6 and not any(state)
    print('B23 explicit legal transport and six-step terminal: PASS',checked)


def verify_bridge():
    checked = 0
    for u in range(-4,5):
        for a in range(-5,6):
            for b in range(-5,6):
                exceptions = [a,b,-20*u-a-b]
                if gcd(u,*exceptions) != 1 or all((x-u) % 23 == 0 for x in exceptions):
                    continue
                last = next(i for i,x in enumerate(exceptions) if (x-u) % 23)
                remainder = [x for i,x in enumerate(exceptions) if i != last]
                c = exceptions[last]
                state = [F(u)]*20+list(map(F,remainder))+[F(c)]
                v = (u+sum(remainder))/F(3)
                average(state,(19,20,21))
                assert state == [F(u)]*19+[v]*3+[F(c)]
                assert c == -19*u-3*v and centered_g(state) == 1
                checked += 1
    print('n23 safe-core to legal B23 one-step bridge: PASS',checked)


def verify():
    verify_words()
    fold,table = verify_cosets()
    verify_transport(fold,table)
    verify_bridge()


if __name__ == '__main__':
    verify()
