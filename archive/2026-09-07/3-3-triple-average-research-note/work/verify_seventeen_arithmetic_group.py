"""Exact n=17 certificate: positive words, index 18, one legal cusp.

The general safe-core theorem and triadic lifting are proved separately.
All arithmetic-group generators here have explicit positive atomic words.
"""

from collections import deque
from fractions import Fraction as F
from math import gcd, lcm

from explore_thirteen_modular import Fold, modular_word, S, U
from explore_b17_integral_return_cover import mul, image, I
from explore_b17_nine_thirteen_bridges import projective, points
from verify_b17_positive_arithmetic import verify as verify_positive, word_matrix, expand, apply_word
from b17_universal_atomic_words import nine_word, average
from verify_fifteen_via_subblocks import centered_g


CERTIFICATE = (
    ('uQa', (-9,-2,5,1)),
    ('pUa', (-5,-1,-19,-4)),
    ('auq', (-3,-1,10,3)),
    ('QQ', (-9,-1,37,4)),
    ('qUA', (-25,-6,71,17)),
    ('bUAbQ', (-56,-15,239,64)),
)


def normalize(matrix):
    denominator = lcm(*(F(x).denominator for x in matrix))
    values = tuple(int(x*denominator) for x in matrix)
    content = gcd(*values)
    values = tuple(x//content for x in values)
    return min(values,tuple(-x for x in values))


def row_action(row, matrix):
    x,y = row
    a,b,c,d = matrix
    return projective((x*a+y*c,x*b+y*d),17)


def verify_generators():
    for word,matrix in CERTIFICATE:
        assert normalize(word_matrix(word,physical=False)) == matrix
        physical = word_matrix(expand(word))
        assert normalize(physical) == matrix
        a,b,c,d = matrix
        assert a*d-b*c == 1 and (a+b-c-d) % 17 == 0
        for pair in ((1,0),(0,1),(2,-7)):
            x,y = image(physical,pair)
            assert apply_word(word,pair) == [x]*13+[y]*3+[-13*x-3*y]
    print('B17 six integral generators with positive atomic realization: PASS')


def verify_cosets():
    fold = Fold()
    for _,matrix in CERTIFICATE:
        fold.loop(modular_word(matrix))
        fold.close()
    table = fold.close()
    nodes = {fold.root(i) for i in range(len(fold.parent))}
    assert len(nodes) == 18
    assert all((node,letter) in table for node in nodes for letter in 'su')
    for node in nodes:
        assert table[table[node,'s'],'s'] == node
        assert table[table[table[node,'u'],'u'],'u'] == node
    base = fold.root(0)
    labels = {base:projective((1,-1),17)}
    representatives = {base:I}
    queue = deque([base])
    while queue:
        node = queue.popleft()
        for letter,generator in (('s',S),('u',U)):
            target = table[node,letter]
            label = row_action(labels[node],generator)
            if target not in labels:
                labels[target] = label
                representatives[target] = mul(representatives[node],generator)
                queue.append(target)
            else:
                assert labels[target] == label
    assert set(labels.values()) == set(points(17)) and len(labels) == 18
    translation = {node:table[table[node,'s'],'u'] for node in nodes}
    unused = set(nodes)
    cusps = []
    while unused:
        start = min(unused)
        node = start
        cycle = []
        while node not in cycle:
            cycle.append(node)
            unused.remove(node)
            node = translation[node]
        assert node == start
        matrix = representatives[start]
        vector = matrix[0],matrix[2]
        cusps.append((cycle,vector,(vector[0]-vector[1]) % 17 != 0))
    assert sorted((len(cycle),legal) for cycle,_,legal in cusps) == [(1,False),(17,True)]
    assert sum(table[node,'s'] == node for node in nodes) == 2
    assert sum(table[node,'u'] == node for node in nodes) == 0
    assert fold.contains(modular_word((0,-1,1,-2)),table)
    print('B17 modular folding and independent local labels: PASS 18')
    print('B17 cusps: width1 illegal, width17 legal; genus1: PASS')
    return fold,table


def bezout(u,v):
    a,b = abs(u),abs(v)
    x0,x1,y0,y1 = 1,0,0,1
    while b:
        q = a//b
        a,b = b,a-q*b
        x0,x1 = x1,x0-q*x1
        y0,y1 = y1,y0-q*y1
    assert a == 1
    return x0 if u >= 0 else -x0, y0 if v >= 0 else -y0


def terminal_transport(u,v):
    c,d = bezout(u,v)
    shift = ((v-u-c-d)*pow(v-u,-1,17)) % 17
    c,d = c+v*shift,d-u*shift
    return v,-u,c,d


def verify_transport(fold,table):
    checked = 0
    for u in range(-24,25):
        for v in range(-24,25):
            if gcd(u,v) != 1 or (u-v) % 17 == 0:
                continue
            matrix = terminal_transport(u,v)
            a,b,c,d = matrix
            assert a*d-b*c == 1 and (a+b-c-d) % 17 == 0
            assert image(matrix,(u,v)) == (0,1)
            assert fold.contains(modular_word(matrix),table)
            checked += 1
    state = [F(0)]*13+[F(1)]*3+[F(-3)]
    word = nine_word((0,1,2,3,4,13,14,15,16))
    for triple in word:
        average(state,triple)
    assert len(word) == 6 and not any(state)
    print('B17 explicit legal-cusp transport and six-step terminal: PASS',checked)


def verify_safe_core_bridge():
    checked = 0
    for u in range(-4,5):
        for a in range(-5,6):
            for b in range(-5,6):
                exceptions = [a,b,-14*u-a-b]
                if gcd(u,*exceptions) != 1 or all((x-u) % 17 == 0 for x in exceptions):
                    continue
                preserved = next(i for i,x in enumerate(exceptions) if (x-u) % 17)
                c = exceptions[preserved]
                remaining = [x for i,x in enumerate(exceptions) if i != preserved]
                state = [F(u)]*14+list(map(F,remaining))+[F(c)]
                mean = (u+sum(remaining))/F(3)
                average(state,(13,14,15))
                assert state == [F(u)]*13+[mean]*3+[F(c)]
                assert c == -13*u-3*mean
                assert centered_g(state) == 1
                checked += 1
    print('n17 safe-core to legal B17 one-step bridge: PASS',checked)


def verify():
    verify_positive()
    verify_generators()
    fold,table = verify_cosets()
    verify_transport(fold,table)
    verify_safe_core_bridge()


if __name__ == '__main__':
    verify()
