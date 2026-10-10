"""Fixed positive cycles and an independent index30 B29 certificate.

No floating search or unbounded word enumeration runs in this verifier.
Child averaging calls are exact, universally admissible, and at most27.
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
    'A':(-3,-3,7,16), 'B':(-3,-3,16,7), 'C':(-1,-1,18,9),
    'D':(0,-2,9,18), 'E':(-24,-3,-25,-2), 'F':(-1,3,0,-27),
    'G':(-8,-1,69,9), 'H':(-20,-3,153,27), 'I':(-24,-3,209,25),
    'J':(-25,-2,216,18), 'K':(-26,-1,225,9), 'L':(-30,-3,-236,-29),
    'M':(-60,-9,347,48), 'N':(-189,-3,-612,-218),
    'O':(-189,3,1332,164), 'P':(-351,-33,-1449,-211),
    'Q':(-189,-3,2061,241), 'R':(-891,-102,3051,364),
}
# Each triple is written in algebraic matrix order, acting right to left.
CYCLES = (('AQC',4),('BQH',4),('CDP',4),('CMN',4),('DDL',4),
          ('DFI',4),('DGE',4),('DOK',2),('DRJ',4))
CERTIFICATE = (
    ('AlbLAb',(-101,-132,-13,-17)), ('BlbL',(-17,-13,-132,-101)),
    ('Ae',(-1,-2,9,17)), ('jKCd',(-28,-3,103,11)),
    ('bCkIAb',(-106,-49,13,6)), ('EbEb',(-64,-7,119,13)),
    ('GbLFDg',(-197,-26,341,45)),
)


def inverse(matrix):
    a,b,c,d = matrix
    det = a*d-b*c
    return tuple(F(x)/det for x in (d,-b,-c,a))


def word_matrix(word,actual):
    result = I
    for letter in word:
        matrix = actual[letter.upper()]
        result = mul(inverse(matrix) if letter.islower() else matrix,result)
    return result


def expanded(word,inverses):
    return ''.join(inverses.get(letter,letter) for letter in word)


@lru_cache(maxsize=1)
def library():
    rows,_ = compile_returns(29,True)
    assert len(rows) == 1194
    actual = {}
    sizes = set()
    for name,matrix in INTEGER.items():
        row = rows[matrix]
        calls = replay(29,row)
        sizes.update(size for size,_,_ in calls)
        assert all(size <= 27 for size,_,_ in calls)
        actual[name] = physical_matrix(row)
        assert normalized_matrix(actual[name]) == matrix
        a,b,c,d = actual[name]
        assert (a*d-b*c).numerator % 29 != 0
        for value in (actual[name][0]+actual[name][1]-1,
                      actual[name][2]+actual[name][3]-1):
            assert value.numerator % 29 == 0 and value.denominator % 29
    inverses = {}
    for algebraic,order in CYCLES:
        chronological = algebraic[::-1]
        cycle = word_matrix(chronological,actual)
        power = I
        for step in range(1,order+1):
            power = mul(cycle,power)
            scalar = power[0]
            if step < order:
                assert power != (scalar,0,0,scalar)
        assert power == (scalar,0,0,scalar) and 0 < abs(scalar) < 1
        assert (scalar.numerator-scalar.denominator) % 29 == 0
        for offset,letter in enumerate(chronological):
            rotation = chronological[offset:]+chronological[:offset]
            tail = rotation[1:]+rotation*(order-1)
            assert mul(word_matrix(tail,actual),actual[letter]) == power
            inverses.setdefault(letter.lower(),tail)
    assert set(inverses) == {name.lower() for name in INTEGER}
    return actual,inverses,tuple(sorted(sizes))


def verify_words():
    actual,inverses,sizes = library()
    for word,matrix in CERTIFICATE:
        assert normalized_matrix(word_matrix(word,actual)) == matrix
        positive = expanded(word,inverses)
        assert normalized_matrix(word_matrix(positive,actual)) == matrix
        a,b,c,d = matrix
        assert a*d-b*c == 1 and (a+b-c-d) % 29 == 0
    print('B29 universal templates and independent child-call replay: PASS',len(INTEGER),sizes)
    print('B29 exact positive scalar cycles and all generator inverses: PASS',len(CYCLES))
    print('B29 fixed positive integral matrix words: PASS',len(CERTIFICATE))


def verify_cosets():
    fold = Fold()
    for _,matrix in CERTIFICATE:
        fold.loop(modular_word(matrix))
        fold.close()
    table = fold.close()
    nodes = {fold.root(i) for i in range(len(fold.parent))}
    assert len(nodes) == 30 and all((node,letter) in table for node in nodes for letter in 'su')
    base = fold.root(0)
    labels = {base:projective((1,-1),29)}
    representatives = {base:I}
    queue = deque([base])
    while queue:
        node = queue.popleft()
        for letter,matrix in (('s',S),('u',U)):
            target = table[node,letter]
            a,b,c,d = matrix
            x,y = labels[node]
            label = projective((x*a+y*c,x*b+y*d),29)
            if target not in labels:
                labels[target] = label
                representatives[target] = mul(representatives[node],matrix)
                queue.append(target)
            else:
                assert labels[target] == label
    assert set(labels.values()) == set(points(29)) and len(labels) == 30
    assert all(table[table[node,'s'],'s'] == node for node in nodes)
    assert all(table[table[table[node,'u'],'u'],'u'] == node for node in nodes)
    e2 = sum(table[node,'s'] == node for node in nodes)
    e3 = sum(table[node,'u'] == node for node in nodes)
    assert (e2,e3) == (2,0)
    unused = set(nodes)
    cusps = []
    while unused:
        start = min(unused)
        node = start
        length = 0
        while node in unused:
            unused.remove(node)
            length += 1
            node = table[table[node,'s'],'u']
        assert node == start
        representative = representatives[start]
        cusps.append((length,(representative[0]-representative[2]) % 29 != 0))
    assert sorted(cusps) == [(1,False),(29,True)]
    assert F(1)+F(30,12)-F(e2,4)-F(e3,3)-F(len(cusps),2) == 2
    print('B29 independent modular folding and projective labels: PASS 30')
    print('B29 cusp widths1/29 and unique legal cusp, genus2: PASS')
    return fold,table


def verify_transport(fold,table):
    checked = 0
    for u in range(-24,25):
        for v in range(-24,25):
            if gcd(u,v) != 1 or (u-v) % 29 == 0:
                continue
            c,d = bezout(u,v)
            k = ((v-u-c-d)*pow(v-u,-1,29)) % 29
            c,d = c+v*k,d-u*k
            matrix = v,-u,c,d
            assert v*d+u*c == 1 and (v-u-c-d) % 29 == 0
            assert image(matrix,(u,v)) == (0,1)
            assert fold.contains(modular_word(matrix),table)
            checked += 1
    state = [F(0)]*25+[F(1)]*3+[F(-3)]
    word = nine_word((0,1,2,3,4,25,26,27,28))
    for triple in word:
        average(state,triple)
    assert len(word) == 6 and not any(state)
    print('B29 explicit legal Bezout transport and six-step terminal: PASS',checked)


def verify_bridge():
    checked = 0
    for u in range(-4,5):
        for a in range(-5,6):
            for b in range(-5,6):
                exceptions = [a,b,-26*u-a-b]
                if gcd(u,*exceptions) != 1 or all((x-u) % 29 == 0 for x in exceptions):
                    continue
                last = next(i for i,x in enumerate(exceptions) if (x-u) % 29)
                remainder = [x for i,x in enumerate(exceptions) if i != last]
                state = [F(u)]*26+list(map(F,remainder))+[F(exceptions[last])]
                v = (u+sum(remainder))/F(3)
                average(state,(25,26,27))
                assert state == [F(u)]*25+[v]*3+[F(-25*u-3*v)]
                assert centered_g(state) == 1
                checked += 1
    print('n29 safe-core to legal B29 bridge: PASS',checked)


def verify_catalog():
    from compile_bn_integer_templates import certificate_size,solved_size
    sizes = (29,58,87,145,203,29**2,29*31,2*29*37)
    assert all(solved_size(size) for size in sizes)
    assert not certificate_size(29)
    assert solved_size(53) and solved_size(59) and not solved_size(71)
    print('n29 factor closure with frozen historical child library: PASS',len(sizes))


def verify():
    verify_words()
    fold,table = verify_cosets()
    verify_transport(fold,table)
    verify_bridge()
    verify_catalog()


if __name__ == '__main__':
    verify()
