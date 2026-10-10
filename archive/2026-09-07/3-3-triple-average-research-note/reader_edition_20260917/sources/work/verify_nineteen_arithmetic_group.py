"""B19: universal 15-point calls, positive inverses, and index 20.

The selected generator templates use only sizes 3, 9, and the already
proved size 15. Their internal 15-point words can depend on parameters.
"""

from collections import deque
from fractions import Fraction as F
from math import gcd

from compile_bn_integer_templates import compile_returns
from verify_bn_integer_templates import physical_matrix, normalized_matrix, replay
from explore_b17_integral_return_cover import mul,image,I
from explore_b17_nine_thirteen_bridges import points,projective
from explore_thirteen_modular import Fold,modular_word,S,U as MODULAR_U
from verify_seventeen_arithmetic_group import bezout
from b17_universal_atomic_words import average,nine_word
from verify_fifteen_via_subblocks import centered_g


INTEGER = {'A':(-3,0,15,1), 'C':(-4,-1,21,12), 'Q':(-8,-1,43,5),
           'P':(-23,-4,123,21), 'R':(-71,-10,379,53),
           'T':(-24,-3,77,10), 'U':(-38,-15,189,81)}
DENOMINATOR = {'A':3,'C':81,'Q':9,'P':27,'R':81,'T':27,'U':243}
ACTUAL = {name:tuple(F(-x,DENOMINATOR[name]) for x in matrix)
          for name,matrix in INTEGER.items()}
INVERSE_WORD = {'a':'CACAC','c':'ACACA','q':'QQQQQ',
                'p':'RPR','r':'PRP','t':'UTU','u':'TUT'}
CERTIFICATE = (
    ('APc',(-2,1,-1,0)), ('pRq',(-5,-1,11,2)),
    ('tqa',(-3,-1,-17,-6)), ('AQT',(-6,1,17,-3)),
    ('QQ',(-7,-1,43,6)), ('apQAqP',(-103,-31,525,158)),
)


def inverse(matrix):
    a,b,c,d = matrix
    determinant = a*d-b*c
    return tuple(x/determinant for x in (d,-b,-c,a))


def word_matrix(word,positive=False):
    if positive:
        word = ''.join(INVERSE_WORD.get(letter,letter) for letter in word)
    result = I
    for letter in word:
        matrix = ACTUAL[letter.upper()]
        if letter.islower():
            matrix = inverse(matrix)
        result = mul(matrix,result)
    return result


def verify_templates():
    rows,_ = compile_returns(19,True)
    u,v = (F(1),F(0)),(F(0),F(1))
    for name,matrix in INTEGER.items():
        row = rows[matrix]
        calls = replay(19,row)
        assert all(size in (3,9,15) for size,_,_ in calls)
        assert physical_matrix(row) == ACTUAL[name]
        a,b,mu = (entry[2] for entry in calls)
        if name == 'A':
            expected = u
        elif name == 'C':
            expected = tuple(u[j]+F(4,9)*(a[j]-u[j])+F(1,9)*(v[j]-u[j]) for j in (0,1))
        elif name in ('Q','P','R'):
            factor = {'Q':F(1),'P':F(4,3),'R':F(10,3)}[name]
            expected = tuple(u[j]+factor*(b[j]-u[j]) for j in (0,1))
        elif name == 'T':
            expected = tuple(u[j]+F(1,3)*(a[j]-u[j]) for j in (0,1))
        else:
            expected = tuple(u[j]+F(10,27)*(a[j]-u[j])+F(5,27)*(v[j]-u[j]) for j in (0,1))
        assert mu == expected
    scalar = F(-1,3**9)
    for word in ('PRPR','QQQQQQ','TUTU','ACACAC'):
        assert word_matrix(word) == (scalar,0,0,scalar)
    for letter,word in INVERSE_WORD.items():
        assert mul(word_matrix(word),ACTUAL[letter.upper()]) == (scalar,0,0,scalar)
    for word,matrix in CERTIFICATE:
        assert normalized_matrix(word_matrix(word)) == matrix
        assert normalized_matrix(word_matrix(word,True)) == matrix
        a,b,c,d = matrix
        assert a*d-b*c == 1 and (a+b-c-d) % 19 == 0
    print('B19 seven universal templates, positive inverse cycles and six integer words: PASS')


def verify_cosets():
    fold = Fold()
    for _,matrix in CERTIFICATE:
        fold.loop(modular_word(matrix))
        fold.close()
    table = fold.close()
    nodes = {fold.root(i) for i in range(len(fold.parent))}
    assert len(nodes) == 20
    assert all((node,letter) in table for node in nodes for letter in 'su')
    base = fold.root(0)
    labels = {base:projective((1,-1),19)}
    representatives = {base:I}
    queue = deque([base])
    while queue:
        node = queue.popleft()
        for letter,matrix in (('s',S),('u',MODULAR_U)):
            target = table[node,letter]
            x,y = labels[node]
            a,b,c,d = matrix
            label = projective((x*a+y*c,x*b+y*d),19)
            if target not in labels:
                labels[target] = label
                representatives[target] = mul(representatives[node],matrix)
                queue.append(target)
            else:
                assert labels[target] == label
    assert len(labels) == 20 and set(labels.values()) == set(points(19))
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
        m = representatives[start]
        cusps.append((len(cycle),(m[0]-m[2]) % 19 != 0))
    assert sorted(cusps) == [(1,False),(19,True)]
    assert sum(table[node,'s'] == node for node in nodes) == 0
    assert sum(table[node,'u'] == node for node in nodes) == 2
    print('B19 exact modular folding and independent mod-19 labels: PASS 20')
    print('B19 cusps width1 illegal and width19 legal, genus1: PASS')
    return fold,table


def verify_transport(fold,table):
    checked = 0
    for u in range(-24,25):
        for v in range(-24,25):
            if gcd(u,v) != 1 or (u-v) % 19 == 0:
                continue
            c,d = bezout(u,v)
            shift = ((v-u-c-d)*pow(v-u,-1,19)) % 19
            c,d = c+v*shift,d-u*shift
            matrix = v,-u,c,d
            assert v*d+u*c == 1 and (v-u-c-d) % 19 == 0
            assert image(matrix,(u,v)) == (0,1)
            assert fold.contains(modular_word(matrix),table)
            checked += 1
    state = [F(0)]*15+[F(1)]*3+[F(-3)]
    word = nine_word((0,1,2,3,4,15,16,17,18))
    for indices in word:
        average(state,indices)
    assert len(word) == 6 and not any(state)
    print('B19 explicit cusp transport and six-step terminal: PASS',checked)


def verify_bridge():
    checked = 0
    for u in range(-4,5):
        for a in range(-5,6):
            for b in range(-5,6):
                exceptional = [a,b,-16*u-a-b]
                if gcd(u,*exceptional) != 1 or all((x-u) % 19 == 0 for x in exceptional):
                    continue
                last = next(i for i,x in enumerate(exceptional) if (x-u) % 19)
                remainder = [x for i,x in enumerate(exceptional) if i != last]
                c = exceptional[last]
                state = [F(u)]*16+list(map(F,remainder))+[F(c)]
                v = (u+sum(remainder))/F(3)
                average(state,(15,16,17))
                assert state == [F(u)]*15+[v]*3+[F(c)]
                assert c == -15*u-3*v and centered_g(state) == 1
                checked += 1
    print('n19 safe-core to legal B19 one-step bridge: PASS',checked)


def verify():
    verify_templates()
    fold,table = verify_cosets()
    verify_transport(fold,table)
    verify_bridge()


if __name__ == '__main__':
    verify()
