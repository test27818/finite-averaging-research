"""Exact interfaces for uniform localized-root generation of Gamma_0(p).

The all-prime assertion is proved by the explicit Schreier representatives
I,S T^j and unit-pivot elimination in the companion document.
"""

from fractions import Fraction as F
from math import isqrt

from verify_forty_seven_arithmetic_group import upper,lower
from verify_b47_root_activation import multiply,inverse,I


def primes(limit):
    return [p for p in range(2,limit+1) if all(p%d for d in range(2,isqrt(p)+1))]


def unit_over_small_primes(value,p):
    value = F(value)
    if not value:return False
    numerator,denominator = abs(value.numerator),value.denominator
    for q in primes(p-1):
        while numerator % q == 0:numerator//=q
        while denominator % q == 0:denominator//=q
    return numerator == denominator == 1


def verify():
    s = (F(0),F(-1),F(1),F(0))
    checked = 0
    for p in primes(149):
        if p < 5:continue
        for j in range(1,p):
            k = -pow(j,-1,p)%p
            word = I
            for factor in (s,upper(j),s,upper(-k),inverse(s)):
                word = multiply(word,factor)
            a,b,c,d = word
            assert word == (-k,-1,j*k+1,j)
            assert c % p == 0 and unit_over_small_primes(a,p)
            result = multiply(multiply(lower(c/a),(a,0,0,1/a)),upper(b/a))
            assert result == word
            assert (c/a/p).denominator < p
            checked += 1
    print('uniform Iwahori Schreier representatives and unit-pivot decomposition: PASS',checked)

    # General diagonal correction and primitive-cusp scaling, all exact.
    checked = 0
    cbase = (F(1),F(0),F(1),F(1))
    for p in (17,23,29,41,47,53,59,73):
        a = (F(1),F(0),F(-(p-4),3),F(-1,3))
        corrected = multiply(lower(F(p,3)),a)
        diagonal = multiply(multiply(inverse(cbase),corrected),cbase)
        assert diagonal == (1,0,0,F(-1,3))
        assert multiply(multiply(inverse(diagonal),upper(1)),diagonal) == upper(F(-1,3))
        checked += 1
    print('all-prime diagonal correction and cusp-root dilation identities: PASS',checked)

    checked = 0
    for p in (17,23,29,41,47,53,59,73):
        m = p-4
        a = (F(1),F(0),F(-m,3),F(-1,3))
        for exponent in (1,3,5,7):
            t = F(1,3**exponent)
            ret = (1-t,t,F(-m,3)*(1-t)-F(1,3),F(-m,3)*t)
            power = I
            for _ in range(exponent):power = multiply(a,power)
            correction = F(p,4)*(1+t)
            value = multiply(multiply(multiply(lower(correction),power),inverse(ret)),a)
            assert value == (0,1,-1,2)
            assert (correction/p).denominator % 2
            checked += 1
    print('all-prime odd-triadic return to width-one cusp identity: PASS',checked)

    units = {1}
    queue = [1]
    for a in queue:
        for g in (-1,2,3):
            b = a*g%73
            if b not in units:units.add(b);queue.append(b)
    assert len(units) == 36 and 5 not in units
    assert all(pow(a,36,73) == 1 for a in units)
    print('fixed localization need not cover all prime residue units: PASS 73 36 72')
    units = {1}
    queue = [1]
    for a in queue:
        for g in (-1,2,3):
            b = a*g%431
            if b not in units:units.add(b);queue.append(b)
    assert len(units) == 86 and 5 not in units and 431 % 3 == 2
    assert pow(2,43,431) == pow(3,43,431) == 1
    assert pow(5,86,431) != 1
    print('nonsplit fixed-unit lifting boundary: PASS 431 86 430')


if __name__ == '__main__':verify()
