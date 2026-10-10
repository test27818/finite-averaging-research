"""Positive modular identity words with exact primitive-height growth."""

from fractions import Fraction as F
from math import gcd


def order_scalar(modulus):
    scalar = -pow(3,-1,modulus) % modulus
    value,order = scalar,1
    while value != 1:
        value = value*scalar % modulus
        order += 1
    return order


def verify():
    checked = operations = 0
    for n in (17,35,41,47):
        r = (n-2)//3
        m = r
        while m % 3 == 0:m //= 3
        modulus = n*m
        order = order_scalar(modulus)
        for multiple in (1,2,3):
            length = 2*multiple*order
            state = [F(1)]*(n-2)+[F(0),F(-(n-2))]
            triple = [0,1,2]
            carrier = n-2
            previous = sum(x*x for x in state)
            for step in range(1,length+1):
                selected = triple[:2]+[carrier]
                mean = sum(state[i] for i in selected)/3
                for i in selected:state[i] = mean
                carrier = triple[2]
                triple = selected
                energy = sum(x*x for x in state)
                assert energy < previous
                previous = energy
                assert state[triple[0]] == F(3,4)+F((-1)**step,4*3**step)
                assert state[carrier] == F(3,4)-F(3*(-1)**step,4*3**step)
            denominator = 3**length
            numerator = [x*denominator for x in state]
            assert all(x.denominator == 1 for x in numerator)
            numerator = [int(x) for x in numerator]
            assert gcd(*numerator) == gcd(*(x-numerator[0] for x in numerator)) == 1
            a = (3**(length+1)+1)//4
            b = (3**(length+1)-3)//4
            assert numerator[triple[0]] == a and numerator[carrier] == b and a-b == 1
            assert max(abs(x) for x in numerator) > n-2
            height = sum(x*x for x in numerator)
            constant = 4*(n-2)**2+4*n-11
            assert height == (constant*3**(2*length)+3)//4
            assert height > (n-2)**2+n-2
            assert pow(3,length,modulus) == 1
            assert all(numerator[i] % modulus == 1 for i in range(n-2) if i not in triple and i != carrier)
            assert numerator[triple[0]] % modulus == 1 and numerator[carrier] % modulus == 0
            assert numerator[-1] % modulus == -(n-2) % modulus
            assert F(height,denominator*denominator) == sum(x*x for x in state)
            checked += 1
            operations += length
    print('positive modular identities: real energy decreases, primitive height grows: PASS',checked,operations)
    print('exact adelic height formula and unchanged primitive residue classes: PASS')


if __name__ == '__main__':
    verify()
