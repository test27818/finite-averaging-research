"""Fixed B47 involutions with one extra atom and positive inverse cycles.

This expands the old167-template alphabet. It is not a complete B47
certificate, and its inverse words do not imply a finite-index subgroup.
"""

from fractions import Fraction as F

from compile_bn_integer_templates import compile_returns
from verify_bn_integer_templates import replay,physical_matrix,normalized_matrix
from explore_b17_integral_return_cover import mul,I


SOURCE = ((-43,-3,1),(0,1,3),(1,0,43))
EXTRA = {
    'J': dict(
        source=SOURCE,first=dict(counts=(1,0,2),scale=(1,3)),
        middle=dict(counts=(1,2,6),scale=(1,9)),
        after_first=((-41,-3,3),(0,3,3),(3,0,41)),
        before_extra=((-369,-27,2),(-23,3,9),(0,27,1),(27,0,35)),
        extra=dict(counts=(2,0,0,1),scale=(3,3)),
        before_final=((-237,-18,3),(-23,3,9),(0,27,1),(27,0,34)),
        final=dict(counts=(2,8,1,34),singleton=1),
        raw=(156,9,-2029,-156),denominator=27),
    'K': dict(
        source=SOURCE,first=dict(counts=(1,0,2),scale=(1,3)),
        middle=dict(counts=(2,1,6),scale=(1,9)),
        after_first=((-41,-3,3),(0,3,3),(3,0,41)),
        before_extra=((-369,-27,1),(-64,-3,9),(0,27,2),(27,0,35)),
        extra=dict(counts=(0,0,2,1),scale=(3,3)),
        before_final=((-369,-27,1),(-64,-3,9),(9,18,3),(27,0,34)),
        final=dict(counts=(1,8,2,34),singleton=2),
        raw=(33,-9,-554,-33),denominator=27),
    'L': dict(
        source=SOURCE,first=dict(counts=(0,1,8),scale=(1,9)),
        middle=dict(counts=(0,1,4,4),scale=(1,9)),
        after_first=((-387,-27,1),(0,9,2),(8,1,9),(9,0,35)),
        before_extra=((-3483,-243,1),(0,81,1),(68,13,9),(72,9,5),(81,0,31)),
        extra=dict(counts=(0,0,0,2,1),scale=(3,3)),
        before_final=((-3483,-243,1),(0,81,1),(68,13,9),(72,9,3),(75,6,3),(81,0,30)),
        final=dict(counts=(0,1,8,2,2,30),singleton=2),
        raw=(228,15,-3336,-228),denominator=3),
}
INTEGER = {
    'J':(-156,-9,2029,156),'K':(-33,9,554,33),'L':(-76,-5,1112,76),
    'A':(-3,0,43,1),'B':(-76,-5,1116,72),'C':(-78,-3,1118,70),
    'D':(-227,-16,3321,243),'E':(-357,18,6323,12),'F':(-228,-15,3326,238),
}
CYCLES = ('LBC','LAD','LEF')


def word_matrix(word,actual):
    result = I
    for letter in word:
        matrix = actual[letter.upper()]
        if letter.islower():
            a,b,c,d = matrix
            determinant = a*d-b*c
            matrix = d/determinant,-b/determinant,-c/determinant,a/determinant
        result = mul(matrix,result)
    return result


def verify():
    rows,_ = compile_returns(47,True,True,True)
    assert len(rows) == 167
    actual = {}
    for name,matrix in INTEGER.items():
        row = EXTRA[name] if name in EXTRA else rows[matrix]
        calls = replay(47,row)
        assert all(size in (3,9,27,43,44,45) for size,_,_ in calls)
        actual[name] = physical_matrix(row)
        assert normalized_matrix(actual[name]) == matrix
        a,b,c,d = actual[name]
        assert (a+b-1).numerator % 47 == (c+d-1).numerator % 47 == 0
        assert (a*d-b*c).numerator % 47
        if name in EXTRA:
            assert matrix not in rows
            assert sum(row['extra']['counts']) == 3
    expected_scalars = {'J':F(25,2187),'K':F(25,2187),'L':F(8,243)}
    for name,scalar in expected_scalars.items():
        assert mul(actual[name],actual[name]) == (scalar,0,0,scalar)
        assert (scalar.numerator-scalar.denominator) % 47 == 0
    print('B47 one-extra-atom universal involutions and exact physical squares: PASS 3')
    covered = set(EXTRA)
    inverses = {name.lower():name for name in EXTRA}
    for cycle in CYCLES:
        chronological = cycle[::-1]
        value = word_matrix(chronological,actual)
        assert value[0]+value[3] == 0
        square = mul(value,value)
        scalar = square[0]
        assert square == (scalar,0,0,scalar) and 0 < abs(scalar) < 1
        assert (scalar.numerator-scalar.denominator) % 47 == 0
        for offset,name in enumerate(chronological):
            rotated = chronological[offset:]+chronological[:offset]
            inverse_word = rotated[1:]+rotated
            assert mul(word_matrix(inverse_word,actual),actual[name]) == square
            covered.add(name)
            inverses.setdefault(name.lower(),inverse_word)
    assert covered == set(INTEGER)
    # In particular, the universal A0 macro now has a positive inverse
    # in the expanded alphabet, despite the old library's short-cycle gap.
    assert actual['A'] == (F(1),F(0),F(-43,3),F(-1,3))
    print('B47 expanded alphabet positive cycles and universal A0 inverse: PASS 9 3')
    for word,sign in (('LBAbLa',1),('ALBabL',-1)):
        assert normalized_matrix(word_matrix(word,actual)) == normalized_matrix((F(1),F(0),F(sign*47),F(1)))
        positive = ''.join(inverses.get(letter,letter) for letter in word)
        assert positive.isupper()
        assert normalized_matrix(word_matrix(positive,actual)) == normalized_matrix((F(1),F(0),F(sign*47),F(1)))
    a = actual['A']
    ai = word_matrix('a',actual)
    checked = 0
    for k in range(8):
        for j in (-3,-1,1,2):
            matrix = (F(1),F(0),F(47*j*(-1)**k),F(1))
            for _ in range(k):matrix = mul(mul(a,matrix),ai)
            assert matrix == (1,0,F(47*j,3**k),1)
            checked += 1
    print('B47 exact positive parabolic roots at all triadic scales: PASS',checked)
    dilation = word_matrix('bL',actual)
    assert dilation == (1,0,-44,-2)
    inverse_dilation = word_matrix('lB',actual)
    for exponent in range(6):
        value = (F(1),F(0),F(47*(-1)**exponent),F(1))
        for _ in range(exponent):value = mul(mul(inverse_dilation,value),dilation)
        assert value == (1,0,F(47,2**exponent),1)
    print('B47 second dilation and positive Z[1/6] root group: PASS 6')
    pencil_checked = 0
    for n in (17,29,41,47,53,65):
        def pencil(t):
            return (1-t,t,F(6-n,3)-t,t-1)
        for t,s in ((F(5,81),F(4,81)),(F(1,27),F(2,27)),(F(7,243),F(8,243))):
            first,second = pencil(t),pencil(s)
            delta_t,delta_s = 1-F(n,3)*t,1-F(n,3)*s
            assert mul(first,first) == (delta_t,0,0,delta_t)
            q = (F(3-n,3),F(-1),F(3-n,3),F(-1))
            expected = tuple(delta_s*x+(t-s)*y for x,y in zip(I,q))
            assert mul(first,second) == expected
            # Fixed eigenlines (1,1) and (3,3-n), independent of t,s.
            for vector,eigen in (((1,1),delta_t),((3,3-n),delta_s)):
                a,b,c,d = expected
                x,y = vector
                assert (a*x+b*y,c*x+d*y) == (eigen*x,eigen*y)
            pencil_checked += 1
    print('general involution pencil and common split-torus product identities: PASS',pencil_checked)


if __name__ == '__main__':
    verify()
