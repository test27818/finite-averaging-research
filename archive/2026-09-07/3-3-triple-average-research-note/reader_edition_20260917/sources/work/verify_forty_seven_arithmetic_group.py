"""Positive B47 congruence containment by two-root Gaussian elimination.

The only discovered word is a fixed width-one cusp generator. The full
Gamma_0(47) containment is verified through an independent Schreier table
and exact elementary decompositions, not inferred from finite images.
"""

from collections import Counter,deque
from fractions import Fraction as F
from math import gcd
import json

from verify_b47_root_activation import (CERTIFICATE,verify as verify_activation,
                                        multiply,inverse,projective,I)
from compile_bn_integer_templates import compile_returns
from verify_bn_integer_templates import physical_matrix
from verify_b47_extra_involutions import INTEGER,EXTRA
from explore_thirteen_modular import S,U,Fold,modular_word
from verify_seventeen_arithmetic_group import bezout
from b17_universal_atomic_words import average,nine_word
from verify_fifteen_via_subblocks import centered_g


C = (F(1),F(0),F(1),F(1))
CUSP_WORD = (4,-79,67)
CUSP_ROOT = F(329,27)
CUSP_MATRIX = (0,-1,1,-2)


def upper(t):return (F(1),F(t),F(0),F(1))


def lower(t):return (F(1),F(0),F(t),F(1))


def in_ring(t):
    d = F(t).denominator
    for prime in (2,3):
        while d % prime == 0:d//=prime
    return d == 1


def is_unit(t):return bool(t) and in_ring(t) and in_ring(1/F(t))


def verify_cusp_and_roots():
    data = json.loads(CERTIFICATE.read_text(encoding='utf-8'))
    rows,_ = compile_returns(47,True,True,True)
    matrices = []
    for node in data['nodes']:
        key = tuple(node['matrix'])
        row = EXTRA[node['seed']] if node.get('seed') in EXTRA else rows[key]
        matrices.append(physical_matrix(row))
    assert [tuple(data['nodes'][abs(i)-1]['matrix']) for i in CUSP_WORD] == [
        (-3,0,43,1),(-78,-3,1145,43),(-27,0,301,1)]
    word = I
    for index in CUSP_WORD:
        m = matrices[abs(index)-1]
        word = multiply(m if index>0 else inverse(m),word)
    cusp = multiply(lower(CUSP_ROOT),word)
    assert projective(cusp) == projective(CUSP_MATRIX)
    assert projective(multiply(multiply(inverse(C),cusp),C)) == projective(upper(1))
    a = matrices[3]
    assert projective(a) == INTEGER['A']
    h = (F(1),F(0),F(-44),F(-2))
    d3 = multiply(multiply(inverse(C),multiply(lower(F(47,3)),a)),C)
    d2 = multiply(multiply(inverse(C),multiply(lower(47),h)),C)
    assert d3 == (1,0,0,F(-1,3))
    assert d2 == (1,0,0,-2)
    assert multiply(multiply(inverse(d3),upper(1)),d3) == upper(F(-1,3))
    assert multiply(multiply(d2,upper(1)),inverse(d2)) == upper(F(-1,2))
    assert multiply(multiply(inverse(C),lower(47)),C) == lower(47)
    print('B47 fixed width-one cusp and opposite full root group: PASS')


def label(row):
    x,y = (t % 47 for t in row)
    assert x or y
    return (1,y*pow(x,-1,47)%47) if x else (0,1)


def schreier_generators():
    base = (1,46)
    representatives = {base:tuple(int(x) for x in I)}
    queue = deque([base])
    while queue:
        current = queue.popleft()
        for generator in (S,U):
            value = multiply(representatives[current],generator)
            following = label((value[0]-value[2],value[1]-value[3]))
            if following not in representatives:
                representatives[following] = value
                queue.append(following)
    assert len(representatives) == 48
    assert set(representatives) == {(0,1)} | {(1,t) for t in range(47)}
    generators = set()
    for current,representative in representatives.items():
        for generator in (S,U):
            value = multiply(representative,generator)
            following = label((value[0]-value[2],value[1]-value[3]))
            loop = projective(multiply(value,inverse(tuple(F(x) for x in representatives[following]))))
            assert loop[0]*loop[3]-loop[1]*loop[2] == 1
            assert (loop[0]+loop[1]-loop[2]-loop[3]) % 47 == 0
            if loop != (-1,0,0,-1):generators.add(loop)
    assert len(generators) == 18
    return sorted(generators)


def decompose(matrix):
    a,b,c,d = matrix
    assert a*d-b*c == 1 and in_ring(c/47)
    if not c:
        assert is_unit(a)
        return upper(0),lower(0),(a,0,0,1/a),upper(b/a)
    assert is_unit(c/47)
    residues = {}
    for exponent in range(23):
        for sign in (1,-1):residues.setdefault(sign*pow(3,exponent,47)%47,sign*3**exponent)
    assert len(residues) == 46
    # Input here is integral; the lemma in the document also allows R entries.
    unit = F(residues[int(a)%47])
    t = (unit-a)/c
    assert in_ring(t) and is_unit(unit)
    v = c/unit
    w = (b+t*d)/unit
    assert in_ring(v/47) and in_ring(w)
    factors = upper(-t),lower(v),(unit,0,0,1/unit),upper(w)
    result = I
    for factor in factors:result = multiply(result,factor)
    assert result == matrix
    return factors


def verify_group():
    generators = schreier_generators()
    lower_entries = Counter()
    for m in generators:
        matrix = multiply(multiply(inverse(C),tuple(F(x) for x in m)),C)
        lower_entries[int(matrix[2])] += 1
        decompose(matrix)
    assert lower_entries == {0:2,47:12,94:2,141:2}
    fold = Fold()
    for m in generators:fold.loop(modular_word(m))
    table = fold.close()
    nodes = {fold.root(i) for i in range(len(fold.parent))}
    assert len(nodes) == 48 and all((node,l) in table for node in nodes for l in 'su')
    labels = {fold.root(0):(1,46)}
    todo = deque(labels)
    while todo:
        node = todo.popleft()
        x,y = labels[node]
        for letter,m in (('s',S),('u',U)):
            dest = table[node,letter]
            next_label = label((x*m[0]+y*m[2],x*m[1]+y*m[3]))
            if dest not in labels:
                labels[dest] = next_label
                todo.append(dest)
            else:assert labels[dest] == next_label
    assert len(set(labels.values())) == 48
    e2 = sum(table[v,'s'] == v for v in nodes)
    e3 = sum(table[v,'u'] == v for v in nodes)
    remaining = set(nodes)
    cusp_widths = []
    while remaining:
        start = min(remaining)
        node,width = start,0
        while node in remaining:
            remaining.remove(node)
            width += 1
            node = table[table[node,'s'],'u']
        assert node == start
        cusp_widths.append(width)
    assert (e2,e3,sorted(cusp_widths)) == (0,0,[1,47])
    assert F(1)+F(48,12)-F(e2,4)-F(e3,3)-len(cusp_widths)/F(2) == 4
    print('B47 all Schreier generators exact positive root decompositions: PASS 18')
    print('B47 complete conjugate Gamma0(47), independent labels and cusp widths: PASS 48 1 47')
    return fold,table


def verify_transport(fold,table):
    checked = 0
    for u in range(-24,25):
        for v in range(-24,25):
            if gcd(u,v) != 1 or (v-u)%47 == 0:continue
            c,d = bezout(u,v)
            k = (v-u-c-d)*pow(v-u,-1,47)%47
            c,d = c+v*k,d-u*k
            matrix = (v,-u,c,d)
            assert (matrix[0]+matrix[1]-matrix[2]-matrix[3]) % 47 == 0
            assert (v*u-u*v,c*u+d*v) == (0,1)
            assert fold.contains(modular_word(matrix),table)
            checked += 1
    state = [F(0)]*43+[F(1)]*3+[F(-3)]
    terminal = nine_word((0,1,2,3,4,43,44,45,46))
    for triple in terminal:average(state,triple)
    assert len(terminal) == 6 and not any(state)
    print('B47 legal Bezout transports and six-step terminal: PASS',checked)


def verify_bridge_and_catalog():
    checked = 0
    for u in range(-4,5):
        for a in range(-5,6):
            for b in range(-5,6):
                exceptions = [a,b,-44*u-a-b]
                if gcd(u,*exceptions) != 1 or all((x-u)%47 == 0 for x in exceptions):continue
                last = next(i for i,x in enumerate(exceptions) if (x-u)%47)
                rest = [x for i,x in enumerate(exceptions) if i != last]
                state = [F(u)]*44+list(map(F,rest))+[F(exceptions[last])]
                v = (u+sum(rest))/F(3)
                average(state,(43,44,45))
                assert state == [F(u)]*43+[v]*3+[F(-43*u-3*v)]
                assert centered_g(state) == 1
                checked += 1
    from compile_bn_integer_templates import solved_size,certificate_size
    sizes = (47,94,141,235,47**2,31*47,41*47,2*5*47**2)
    assert all(solved_size(size) for size in sizes)
    assert solved_size(53) and solved_size(59) and not solved_size(71)
    assert not certificate_size(47)
    print('n47 safe-core bridge and factor catalog integration: PASS',checked,len(sizes))


def verify():
    verify_activation()
    verify_cusp_and_roots()
    fold,table = verify_group()
    verify_transport(fold,table)
    verify_bridge_and_catalog()


if __name__ == '__main__':verify()
