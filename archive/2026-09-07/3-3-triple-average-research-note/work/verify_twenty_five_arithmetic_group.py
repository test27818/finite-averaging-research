"""Exact B25 certificate using universal solved-child templates.

Inverse templates are checked individually; the modular coset certificate
is fixed and independent of the exploratory integral-word enumeration.
"""

from collections import deque
from fractions import Fraction as F
from functools import lru_cache
from math import gcd

from compile_bn_integer_templates import compile_returns
from verify_bn_integer_templates import replay,physical_matrix,normalized_matrix
from explore_b17_integral_return_cover import mul,image,I
from explore_thirteen_modular import Fold,modular_word,S,U
from verify_seventeen_arithmetic_group import bezout
from b17_universal_atomic_words import average,nine_word
from verify_fifteen_via_subblocks import centered_g


INTEGER = {'A':(-2,0,1,-3),'B':(-8,-1,-7,-2),'C':(-5,-1,-8,2),
           'E':(-4,-2,-13,7),'F':(-16,-2,-7,-11),
           'I':(-2,0,17,6),'J':(-2,0,20,3),'K':(-2,0,21,2),
           'L':(-8,-1,59,7),'M':(-71,-10,-70,-11),
           'N':(-7,1,76,-7),'Q':(-24,-3,175,23)}
CERTIFICATE = (
    ('AIlJ',(0,-1,1,-2)), ('lKi',(-7,-1,15,2)),
    ('ACBi',(-5,-1,16,3)), ('alfB',(-11,-1,12,1)),
    ('eeNI',(-1,0,-25,-1)), ('bFQABnL',(-23,-29,165,208)),
    ('cNmeBnL',(-41,-48,293,343)),
)


def finite_order(matrix):
    a,b,c,d = matrix
    if b == c == 0 and a == d:
        return 1
    trace,determinant = a+d,a*d-b*c
    if trace == 0:
        return 2
    if determinant > 0 and trace*trace % determinant == 0:
        return {1:3,2:4,3:6}.get(trace*trace//determinant)
    return None


def power(matrix,exponent):
    result = I
    for _ in range(exponent):
        result = mul(matrix,result)
    return result


@lru_cache(maxsize=1)
def library():
    rows,_ = compile_returns(25,True)
    assert len(rows) == 235
    inverses = {}
    checked = set()
    for name,matrix in INTEGER.items():
        candidates = []
        for partner in rows:
            order = finite_order(mul(partner,matrix))
            if order:
                candidates.append((2*order-1,max(map(abs,partner)),partner,order))
        _,_,partner,order = min(candidates)
        for selected in (matrix,partner):
            if selected not in checked:
                calls = replay(25,rows[selected])
                assert all(size in (3,9,21) for size,_,_ in calls)
                checked.add(selected)
        actual,other = physical_matrix(rows[matrix]),physical_matrix(rows[partner])
        cycle = power(mul(other,actual),order)
        scalar = cycle[0]
        assert scalar and cycle == (scalar,0,0,scalar)
        assert (scalar.numerator-scalar.denominator) % 25 == 0
        sequence = (partner,)+(matrix,partner)*(order-1)
        inv = I
        for selected in sequence:
            inv = mul(physical_matrix(rows[selected]),inv)
        assert mul(inv,actual) == cycle
        inverses[name.lower()] = inv
    return rows,inverses,len(checked)


def inverse(matrix):
    a,b,c,d = matrix
    det = a*d-b*c
    return tuple(x/det for x in (d,-b,-c,a))


def word_matrix(word,positive):
    rows,inverses,_ = library()
    result = I
    for letter in word:
        actual = physical_matrix(rows[INTEGER[letter.upper()]])
        if letter.islower():
            actual = inverses[letter] if positive else inverse(actual)
        result = mul(actual,result)
    return result


def projective25(pair):
    x,y = (int(value) % 25 for value in pair)
    if x % 5:
        return 1,y*pow(x,-1,25) % 25
    assert y % 5
    return x*pow(y,-1,25) % 25,1


def verify_words():
    _,_,checked = library()
    for word,matrix in CERTIFICATE:
        assert normalized_matrix(word_matrix(word,False)) == matrix
        assert normalized_matrix(word_matrix(word,True)) == matrix
        a,b,c,d = matrix
        assert a*d-b*c == 1 and (a+b-c-d) % 25 == 0
    print('B25 universal template inverse partners and seven positive integer words: PASS',checked)


def verify_cosets():
    fold = Fold()
    for _,matrix in CERTIFICATE:
        fold.loop(modular_word(matrix))
        fold.close()
    table = fold.close()
    nodes = {fold.root(i) for i in range(len(fold.parent))}
    assert len(nodes) == 30 and all((node,letter) in table for node in nodes for letter in 'su')
    base = fold.root(0)
    labels = {base:projective25((1,-1))}
    reps = {base:I}
    queue = deque([base])
    while queue:
        node = queue.popleft()
        for letter,matrix in (('s',S),('u',U)):
            target = table[node,letter]
            a,b,c,d = matrix
            x,y = labels[node]
            label = projective25((x*a+y*c,x*b+y*d))
            if target not in labels:
                labels[target] = label
                reps[target] = mul(reps[node],matrix)
                queue.append(target)
            else:
                assert labels[target] == label
    expected = {(1,t) for t in range(25)}|{(5*t,1) for t in range(5)}
    assert set(labels.values()) == expected and len(labels) == 30
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
        m = reps[start]
        cusps.append((len(cycle),(m[0]-m[2]) % 5 != 0))
    assert sorted(cusps) == [(1,False)]*5+[(25,True)]
    assert sum(table[node,'s'] == node for node in nodes) == 2
    assert sum(table[node,'u'] == node for node in nodes) == 0
    print('B25 complete modular folding and independent projective Z/25 labels: PASS 30')
    print('B25 six cusps, unique legal width25 cusp, genus0: PASS')
    return fold,table


def verify_transport(fold,table):
    checked = 0
    for u in range(-20,21):
        for v in range(-20,21):
            if gcd(u,v) != 1 or (u-v) % 5 == 0:
                continue
            c,d = bezout(u,v)
            shift = ((v-u-c-d)*pow(v-u,-1,25)) % 25
            c,d = c+v*shift,d-u*shift
            matrix = v,-u,c,d
            assert v*d+u*c == 1 and (v-u-c-d) % 25 == 0
            assert image(matrix,(u,v)) == (0,1)
            assert fold.contains(modular_word(matrix),table)
            checked += 1
    state = [F(0)]*21+[F(1)]*3+[F(-3)]
    for triple in nine_word((0,1,2,3,4,21,22,23,24)):
        average(state,triple)
    assert not any(state)
    print('B25 explicit legal transport and six-step terminal: PASS',checked)
    checked = 0
    for u in range(-3,4):
        for a in range(-4,5):
            for b in range(-4,5):
                tail = [a,b,-22*u-a-b]
                if gcd(u,*tail) != 1 or all((x-u) % 5 == 0 for x in tail):
                    continue
                last = next(i for i,x in enumerate(tail) if (x-u) % 5)
                selected = [x for i,x in enumerate(tail) if i != last]
                state = [F(u)]*22+list(map(F,selected))+[F(tail[last])]
                average(state,(21,22,23))
                assert centered_g(state) == 1
                checked += 1
    print('n25 safe-core to legal B25 bridge: PASS',checked)


def verify():
    verify_words()
    fold,table = verify_cosets()
    verify_transport(fold,table)


if __name__ == '__main__':
    verify()
