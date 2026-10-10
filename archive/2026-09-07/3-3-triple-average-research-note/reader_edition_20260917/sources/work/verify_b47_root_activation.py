"""Verify a fixed acyclic positive-inverse certificate, without discovery.

Every node is a universal physical B47 macro. A trace-zero product of a
known reversible flank, an available root, and that macro supplies its
positive inverse. This does not certify a congruence subgroup or consensus.
"""

from collections import Counter
from fractions import Fraction as F
import json
from pathlib import Path

from compile_bn_integer_templates import compile_returns
from verify_bn_integer_templates import replay, physical_matrix, normalized_matrix
from verify_b47_extra_involutions import INTEGER, EXTRA, CYCLES, verify as verify_seeds


I = (F(1),F(0),F(0),F(1))
CERTIFICATE = Path(__file__).with_name('b47_root_activation_certificate.json')


def multiply(x,y):
    a,b,c,d = x
    e,f,g,h = y
    return a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h


def inverse(x):
    a,b,c,d = x
    determinant = a*d-b*c
    assert determinant
    return d/determinant,-b/determinant,-c/determinant,a/determinant


def projective(x):
    return normalized_matrix(tuple(F(t) for t in x))


def trace_root_allowed(t):
    quotient = t/47
    denominator = quotient.denominator
    for prime in (2,3):
        while denominator % prime == 0:
            denominator //= prime
    return denominator == 1


def positive_seed_words(actual):
    words = {name:name for name in INTEGER}
    words.update({name.lower():name for name in EXTRA})
    for cycle in CYCLES:
        chronological = cycle[::-1]
        for offset,name in enumerate(chronological):
            rotated = chronological[offset:]+chronological[:offset]
            words.setdefault(name.lower(),rotated[1:]+rotated)

    def evaluate(word):
        value = I
        for name in word:
            assert name.isupper()
            value = multiply(actual[name],value)
        return value

    for name in INTEGER:
        product = multiply(evaluate(words[name.lower()]),actual[name])
        assert product[1] == product[2] == 0 and product[0] == product[3] != 0
    return words,evaluate


def verify():
    verify_seeds()
    data = json.loads(CERTIFICATE.read_text(encoding='utf-8'))
    assert data['schema_version'] == 1 and data['n'] == 47
    rows,_ = compile_returns(47,True,True,True)
    assert len(rows) == 167 and len(data['nodes']) == 170
    matrices,levels,actual_by_matrix,seen = [],[],{},set()
    depth_counts = Counter()

    for index,node in enumerate(data['nodes']):
        integer = tuple(node['matrix'])
        assert integer not in seen
        seen.add(integer)
        if 'seed' in node:
            name = node['seed']
            assert integer == INTEGER[name]
            row = EXTRA[name] if name in EXTRA else rows[integer]
            level = 0
        else:
            row = rows[integer]
            level = 1
        replay(47,row)
        actual = physical_matrix(row)
        assert projective(actual) == integer
        a,b,c,d = actual
        assert all(t.denominator % 47 for t in actual)
        assert (a+b-1).numerator % 47 == (c+d-1).numerator % 47 == 0
        assert (a*d-b*c).numerator % 47

        if 'seed' not in node:
            flank = I
            for reference,sign in node['flank']:
                assert 0 <= reference < index and sign in (-1,1)
                value = matrices[reference]
                if sign == -1:value = inverse(value)
                flank = multiply(value,flank)
                level = max(level,levels[reference]+1)
            numerator,denominator = node['parameter']
            assert denominator > 0
            t = F(numerator,denominator)
            assert trace_root_allowed(t)
            product = multiply(flank,actual)
            assert product[1] and t == -(product[0]+product[3])/product[1]
            bridge = multiply((1,0,t,1),flank)
            cycle = multiply(bridge,actual)
            scalar = -(cycle[0]*cycle[3]-cycle[1]*cycle[2])
            assert scalar and cycle[0]+cycle[3] == 0
            assert multiply(cycle,cycle) == (scalar,0,0,scalar)
            positive_inverse = multiply(multiply(bridge,actual),bridge)
            assert multiply(positive_inverse,actual) == (scalar,0,0,scalar)
            assert multiply(actual,positive_inverse) == (scalar,0,0,scalar)
            depth_counts[level] += 1

        matrices.append(actual)
        actual_by_matrix[integer] = actual
        levels.append(level)

    assert seen == set(rows) | set(INTEGER.values())
    assert depth_counts == {1:46,2:113,3:2}
    assert sum(level == 0 for level in levels) == 9
    print('B47 fixed acyclic root-activation certificate: PASS 170 46 113 2')
    print('B47 universal replay, legal mod47 interfaces and all old positive inverses: PASS 167')

    actual_seeds = {name:actual_by_matrix[m] for name,m in INTEGER.items()}
    positive,evaluate = positive_seed_words(actual_seeds)

    def expand(word):
        return ''.join(positive[letter] for letter in word)

    # H^-1 U(-47) H = U(47/2), all words chronological.
    root_word = expand('bL'+'ALBabL'+'lB')
    assert projective(evaluate(root_word)) == projective((1,0,F(47,2),1))
    bridge_word = expand('la')+root_word
    theta = (-9,5,162,-72)
    assert theta in actual_by_matrix
    macro = actual_by_matrix[theta]
    assert macro == tuple(F(-2,243)*x for x in theta)
    formal_bridge = multiply(multiply((1,0,F(47,2),1),inverse(actual_seeds['A'])),
                             inverse(actual_seeds['L']))
    assert formal_bridge == (F(57,2),F(15,8),F(2781,4),F(783,16))
    formal_cycle = multiply(formal_bridge,macro)
    assert multiply(formal_cycle,formal_cycle) == I
    bridge = evaluate(bridge_word)
    assert projective(bridge) == projective(formal_bridge)
    conjugate = multiply(multiply(bridge,macro),bridge)
    target = (-72,-5,-162,-9)
    assert projective(conjugate) == projective(target)
    scalar = multiply(conjugate,macro)[0]
    assert multiply(conjugate,macro) == (scalar,0,0,scalar)
    assert scalar and (scalar-1).numerator % 47 == 0
    assert scalar.denominator % 47
    print('B47 quadratic conjugate expanded positive macro word: PASS',2*len(bridge_word)+1)

    # N has b=-1 and det=-9, so both transported root ideals remain 47R.
    n = tuple(F(x) for x in (-26,-1,381,15))
    assert tuple(int(x) for x in n) in seen
    p = tuple(F(x) for x in (0,-1,1,15))
    e21 = tuple(F(x) for x in (0,0,1,0))
    upper = multiply(multiply(inverse(p),e21),p)
    lower = multiply(multiply(multiply(multiply(inverse(p),n),e21),inverse(n)),p)
    assert upper == (0,-1,0,0)
    assert lower == (0,0,F(-1,9),0)
    print('B47 two transverse complete localized root groups: PASS 2')
    print('Root-activation certificate alone does not establish B47 terminal orbit coverage')


if __name__ == '__main__':
    verify()
