"""Fixed positive B41 certificate with a complete index42 subgroup.

Signed integers label generators; words are executed from left to right.
The selected templates only call already proved sizes below41.
"""

from collections import deque
from fractions import Fraction as F
from functools import lru_cache
from math import gcd

from compile_bn_integer_templates import compile_returns
from verify_bn_integer_templates import replay,physical_matrix,normalized_matrix
from explore_b17_integral_return_cover import mul,image,I
from explore_thirteen_modular import Fold,modular_word,S,U
from explore_b17_nine_thirteen_bridges import points,projective
from verify_seventeen_arithmetic_group import bezout
from verify_fifteen_via_subblocks import centered_g
from b17_universal_atomic_words import average,nine_word


INTEGER = {
    1:(-1,2,26,-25), 2:(-3,0,-35,-9), 3:(-3,0,37,1),
    4:(-3,0,70,9), 5:(-9,0,74,-1), 6:(-75,-6,-74,-7),
    7:(-3,6,-82,-79), 8:(-3,-6,-125,-7), 10:(-24,51,296,100),
    11:(-25,-2,317,25), 12:(-21,-6,634,77), 13:(-30,3,709,2),
    14:(-159,-6,908,-7), 17:(-75,-6,947,79), 19:(-76,-5,963,63),
    20:(-77,-4,973,53), 21:(-77,-4,975,51), 22:(-79,-2,999,27),
    26:(-224,-19,2838,240), 27:(-225,-18,2849,229),
    28:(-228,-15,2891,187),
}
# Algebraic matrix order, so the last factor acts first.
CYCLES = ((1,2,6),(11,17,27),(1,8,21),(2,3,14),(2,4,5),
          (11,19,13),(11,21,12),(7,28,11),(10,11,22),(11,26,20))
CERTIFICATE = (
    ((1,19,1,13,-12,-1),(-25,-13,2,1)),
    ((-21,-1),(-25,-2,13,1)),
    ((-3,-19,17,-3,1,13,-12,-1),(-81,-10,-8,-1)),
    ((8,-14,-6,28,1,13,-12,-1),(-150,-41,11,3)),
    ((-26,6,-26,6),(-59,-5,130,11)),
    ((2,-27,19,-4),(-74,-9,255,31)),
    ((-22,-1,-22,-1),(-489,-40,-110,-9)),
    ((-5,-21,11,-4),(-173,-18,644,67)),
    ((-17,-19,11,-8),(-26,-1,53,2)),
    ((21,1,1,6,11,-21),(-153,-8,899,47)),
)


def inverse(matrix):
    a,b,c,d = matrix
    determinant = a*d-b*c
    return tuple(F(x)/determinant for x in (d,-b,-c,a))


def word_matrix(word,actual):
    result = I
    for index in word:
        matrix = actual[abs(index)]
        result = mul(matrix if index > 0 else inverse(matrix),result)
    return result


@lru_cache(maxsize=1)
def library():
    rows,_ = compile_returns(41,True,True,True)
    assert len(rows) == 169
    actual = {}
    sizes = set()
    for index,matrix in INTEGER.items():
        row = rows[matrix]
        calls = replay(41,row)
        sizes.update(size for size,_,_ in calls)
        assert all(size in (3,9,18,27,37,38,39) for size,_,_ in calls)
        actual[index] = physical_matrix(row)
        assert normalized_matrix(actual[index]) == matrix
        a,b,c,d = actual[index]
        assert (a+b-1).numerator % 41 == (c+d-1).numerator % 41 == 0
        assert (a*d-b*c).numerator % 41 != 0
        assert all(value.denominator % 41 for value in actual[index])
    inverses = {}
    for cycle in CYCLES:
        chronological = tuple(reversed(cycle))
        value = word_matrix(chronological,actual)
        assert value[0]+value[3] == 0
        square = mul(value,value)
        scalar = square[0]
        assert square == (scalar,0,0,scalar) and 0 < abs(scalar) < 1
        assert (scalar.numerator-scalar.denominator) % 41 == 0
        for offset,index in enumerate(chronological):
            rotation = chronological[offset:]+chronological[:offset]
            tail = rotation[1:]+rotation
            assert mul(word_matrix(tail,actual),actual[index]) == square
            inverses.setdefault(-index,tail)
    assert set(inverses) == {-i for i in INTEGER}
    return actual,inverses,tuple(sorted(sizes))


def verify_words():
    actual,inverses,sizes = library()
    for word,matrix in CERTIFICATE:
        assert normalized_matrix(word_matrix(word,actual)) == matrix
        positive = tuple(i for index in word for i in inverses.get(index,(index,)))
        assert all(i > 0 for i in positive)
        assert normalized_matrix(word_matrix(positive,actual)) == matrix
        a,b,c,d = matrix
        assert a*d-b*c == 1 and (a+b-c-d) % 41 == 0
    print('B41 universal templates and independent child-call replay: PASS',len(INTEGER),sizes)
    print('B41 exact three-factor involutions and positive inverses: PASS',len(CYCLES))
    print('B41 fixed positive integral matrix words: PASS',len(CERTIFICATE))


def verify_cosets():
    fold = Fold()
    for _,matrix in CERTIFICATE:
        fold.loop(modular_word(matrix))
        fold.close()
    table = fold.close()
    nodes = {fold.root(i) for i in range(len(fold.parent))}
    assert len(nodes) == 42 and all((v,letter) in table for v in nodes for letter in 'su')
    base = fold.root(0)
    labels = {base:projective((1,-1),41)}
    representatives = {base:I}
    queue = deque([base])
    while queue:
        node = queue.popleft()
        for letter,matrix in (('s',S),('u',U)):
            target = table[node,letter]
            a,b,c,d = matrix
            x,y = labels[node]
            label = projective((x*a+y*c,x*b+y*d),41)
            if target not in labels:
                labels[target] = label
                representatives[target] = mul(representatives[node],matrix)
                queue.append(target)
            else:
                assert labels[target] == label
    assert len(labels) == 42 and set(labels.values()) == set(points(41))
    assert all(table[table[v,'s'],'s'] == v for v in nodes)
    assert all(table[table[table[v,'u'],'u'],'u'] == v for v in nodes)
    e2 = sum(table[v,'s'] == v for v in nodes)
    e3 = sum(table[v,'u'] == v for v in nodes)
    assert (e2,e3) == (2,0)
    unused = set(nodes)
    cusps = []
    while unused:
        start = min(unused)
        v,length = start,0
        while v in unused:
            unused.remove(v)
            length += 1
            v = table[table[v,'s'],'u']
        assert v == start
        m = representatives[start]
        cusps.append((length,(m[0]-m[2]) % 41 != 0))
    assert sorted(cusps) == [(1,False),(41,True)]
    assert F(1)+F(42,12)-F(e2,4)-F(e3,3)-F(len(cusps),2) == 3
    print('B41 independent modular folding and projective labels: PASS 42')
    print('B41 cusp widths1/41 and unique legal cusp, genus3: PASS')
    return fold,table


def verify_transport(fold,table):
    checked = 0
    for u in range(-24,25):
        for v in range(-24,25):
            if gcd(u,v) != 1 or (u-v) % 41 == 0:continue
            c,d = bezout(u,v)
            k = ((v-u-c-d)*pow(v-u,-1,41)) % 41
            c,d = c+v*k,d-u*k
            m = v,-u,c,d
            assert image(m,(u,v)) == (0,1)
            assert v*d+u*c == 1 and (v-u-c-d) % 41 == 0
            assert fold.contains(modular_word(m),table)
            checked += 1
    state = [F(0)]*37+[F(1)]*3+[F(-3)]
    tail = nine_word((0,1,2,3,4,37,38,39,40))
    for triple in tail:average(state,triple)
    assert len(tail) == 6 and not any(state)
    print('B41 explicit legal Bezout transport and six-step terminal: PASS',checked)


def verify_bridge():
    checked = 0
    for u in range(-4,5):
        for a in range(-5,6):
            for b in range(-5,6):
                exceptions = [a,b,-38*u-a-b]
                if gcd(u,*exceptions) != 1 or all((x-u) % 41 == 0 for x in exceptions):continue
                last = next(i for i,x in enumerate(exceptions) if (x-u) % 41)
                remaining = [x for i,x in enumerate(exceptions) if i != last]
                state = [F(u)]*38+list(map(F,remaining))+[F(exceptions[last])]
                v = (u+sum(remaining))/F(3)
                average(state,(37,38,39))
                assert state == [F(u)]*37+[v]*3+[F(-37*u-3*v)]
                assert centered_g(state) == 1
                checked += 1
    print('n41 safe-core to legal B41 bridge: PASS',checked)


def verify():
    verify_words()
    fold,table = verify_cosets()
    verify_transport(fold,table)
    verify_bridge()
    from compile_bn_integer_templates import solved_size,certificate_size
    sizes = (41,82,123,205,41**2,29*41,31*41)
    assert all(solved_size(size) for size in sizes)
    assert solved_size(53) and solved_size(59) and not solved_size(71)
    assert not certificate_size(41)
    print('n41 factor closure and frozen historical-library boundary: PASS',len(sizes))


if __name__ == '__main__':
    verify()
