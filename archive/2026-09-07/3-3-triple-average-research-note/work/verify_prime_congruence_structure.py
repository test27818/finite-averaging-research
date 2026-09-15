"""Exact finite checks for the prime stabilizer and physical-scale lemmas."""

from fractions import Fraction as F

from explore_b17_integral_return_cover import mul,I
from verify_b17_positive_arithmetic import word_matrix as word17
from verify_nineteen_arithmetic_group import word_matrix as word19
from verify_nineteen_arithmetic_group import ACTUAL as ACTUAL19, inverse
from verify_twenty_three_arithmetic_group import word_matrix as word23, ACTUAL as ACTUAL23


def order_three(modulus):
    value = 1
    for exponent in range(1,modulus):
        value = 3*value % modulus
        if value == 1:
            return exponent
    raise AssertionError('a prime-to-three unit must have finite order')


def verify():
    expected = {7:6,11:5,13:3,17:16,19:18,23:11}
    for prime,order in expected.items():
        assert order_three(prime) == order
        negative = [k for k in range(1,order+1) if pow(3,k,prime) == prime-1]
        assert negative == ([order//2] if order % 2 == 0 else [])
        # The integral Iwahori image has p(p-1) elements inside SL2(Fp).
        stabilizer = {(a,b,0,pow(a,-1,prime)) for a in range(1,prime) for b in range(prime)}
        assert len(stabilizer) == prime*(prime-1)
        assert prime*(prime*prime-1)//len(stabilizer) == prime+1
        for a,b,c,d in stabilizer:
            # Conjugate by C=[[1,0],[1,1]].
            x,y,z,t = mul((1,0,1,1),mul((a,b,c,d),(1,0,-1,1)))
            assert (x+y-z-t) % prime == 0
    print('prime Iwahori labels and exact 3-unit cycle periods: PASS 6')
    A13 = (F(1),F(0),F(-3),F(-1,3))
    R13 = (F(2,3),F(1,3),F(1),F(0))
    m = I
    for generator in (A13,R13)*3:
        m = mul(generator,m)
    assert m == (F(1,27),0,0,F(1,27))
    for prime,matrix in ((13,m),(17,word17('AQUAQU')),(19,word19('ACACAC'))):
        scalar = matrix[0]
        assert matrix == (scalar,0,0,scalar)
        assert (scalar.numerator-scalar.denominator) % prime == 0
    assert pow(3,11,23) == 1 and all(pow(3,k,23) != 22 for k in range(11))
    print('physical scalar congruences for n13/n17/n19 and negative-unit exclusion at23: PASS')
    for word,scalar in (('JJ',F(4,27)),('NPNP',F(2,2187))):
        assert word23(word) == (scalar,0,0,scalar)
        assert (scalar.numerator-scalar.denominator) % 23 == 0
    assert mul(ACTUAL19['T'],inverse(ACTUAL19['Q'])) == ACTUAL19['A']
    assert mul(ACTUAL23['J'],inverse(ACTUAL23['N'])) == (1,0,20,4)
    print('non-unit B23 scalar cycles and shared-row affine identities: PASS')


if __name__ == '__main__':
    verify()
