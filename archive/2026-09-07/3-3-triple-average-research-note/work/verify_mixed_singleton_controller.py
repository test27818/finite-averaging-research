"""Uniform two-return controller with minimal prime-support localization.

Only matrix identities, triadic positive transport margins, and root
compilation are certified. Original-position realization of the two
returns is an explicit unresolved hypothesis.
"""

from fractions import Fraction as F
from math import gcd,isqrt,prod

from verify_diagonal_resource_reduction import product,upper,lower,diagonal,roots
from verify_b53_inverse_closure import inverse


I = (F(1),F(0),F(0),F(1))
C = (F(1),F(0),F(1),F(1))


def primes(limit):
    return [p for p in range(2,limit+1)
            if all(p%d for d in range(2,isqrt(p)+1))]


def localization_product(p):
    """Prime support not already supplied by the fixed factor 15."""
    return prod(q for q in primes((p-1)//2) if q not in (3,5))


def det(a):return a[0]*a[3]-a[1]*a[2]


def commutator(a,b):return product(a,b,inverse(a),inverse(b))


def change(a):return product(inverse(C),a,C)


def standard(p):return (F(1),F(0),F(4-p,3),F(-1,3))


def mixed_return(p,beta):
    m,n = p-4,2*p+1
    t = F(9+beta,n)
    return (1-t,t,-F(m*(1-t)+1-beta,3),-F(m*t+beta,3))


def strip(value,allowed):
    value = abs(value)
    for q in allowed:
        while value and value%q == 0:value//=q
    return value


def triadic(value):
    return strip(F(value).denominator,(3,)) == 1


def in_ring(value,small,extra):
    d = strip(F(value).denominator,small)
    while d>1:
        common = gcd(d,extra)
        if common == 1:return False
        d//=common
    return True


def scalar_power(a,k):
    value = I
    while k:
        if k&1:value=product(value,a)
        a=product(a,a)
        k//=2
    return value


def verify_family():
    checked = 0
    for p in (11,17,23,47,53,59,71,83,107,431):
        a = standard(p)
        n = 2*p+1
        for beta in (F(0),F(1),F(1,3),F(1,10),F(1,2)):
            r = mixed_return(p,beta)
            r0 = mixed_return(p,F(0))
            k = 9-2*p*beta
            t = F(9+beta,n)
            assert det(r) == F(t-beta,3) == F(k,3*n)
            cycle = product(r,a)
            assert cycle[0]+cycle[3] == 0
            assert product(cycle,cycle) == tuple(F(k,9*n)*x for x in I)
            h = change(product(inverse(r),a))
            assert h == (1,F(9+beta,k),0,F(-n,k))
            h0 = (F(1),F(1),F(0),F(-n,9))
            assert commutator(h0,h) == upper(F(10*beta,n))
            assert change(product(inverse(r0),r)) == (
                F(1), beta, F(0), F(1)-F(2*p*beta,9))
            checked += 1
    print('mixed-singleton symbolic cycles and affine commutator identity: PASS',checked)


def verify_localized_controller():
    count,schreier = 0,0
    for p in [q for q in primes(149) if q>=11 and q%3==2]+[431]:
        b = localization_product(p)
        n,k = 2*p+1,45*b-p
        beta = F(1,10*b)
        a = change(standard(p))
        r0,rb = change(mixed_return(p,F(0))),change(mixed_return(p,beta))
        h0,hb = product(inverse(r0),a),product(inverse(rb),a)
        assert h0 == (1,1,0,F(-n,9))
        assert hb == (1,F(90*b+1,2*k),0,F(-5*b*n,k))
        assert commutator(h0,hb) == upper(F(1,b*n))
        assert gcd(b,k) == gcd(5,k) == gcd(n,9) == 1
        # Removing cancelled factors of a multiplier cannot lose a prime
        # already present in the other multiplier or in B or 5.
        assert gcd(5*b*n,k) == gcd(n,k)
        small = primes((p-1)//2)
        extra = 15*n*k
        for value in (*h0,*hb):assert in_ring(value,small,extra)
        d0 = product(h0,upper(-h0[1]))
        db = product(hb,upper(-hb[1]))
        assert d0 == (1,0,0,h0[3]) and db == (1,0,0,hb[3])
        c0,cb = commutator(a,d0)[2],commutator(a,db)[2]
        assert c0 == F(-2*p*(p+5),27)
        assert cb == F(-p*((10*b-1)*p+50*b),3*k)
        left,right = F(27*(10*b-1),10),F(-3*k,5)
        assert left*c0+right*cb == p
        assert in_ring(left,small,extra) and in_ring(right,small,extra)
        assert product(lower(left*c0),lower(right*cb)) == lower(p)

        # The signed Schreier pivots lie in this proven multiplier ring.
        half = (p-1)//2
        for j in range(-half,half+1):
            if not j:continue
            pivot = -pow(j,-1,p)%p
            if pivot>half:pivot-=p
            entry = j*pivot+1
            assert in_ring(F(1,pivot),small,extra)
            assert in_ring(F(-entry,pivot*p),small,extra)
            assert product(lower(F(-entry,pivot)),diagonal(-pivot),upper(F(1,pivot))) == (
                -pivot,-1,entry,j)
            schreier += 1
        count += 1
    print('two mixed returns give full opposite localized root ideals: PASS',count)
    print('prime-support ring contains all signed Schreier root parameters: PASS',schreier)


def verify_scales():
    count = 0
    max_bits = 0
    for p in [q for q in primes(149) if q>=11 and q%3==2]+[431]:
        b = localization_product(p)
        n = 2*p+1
        mass = 10*b*n
        exponent = 1
        residue = 3*pow(mass,-1,p)%p
        order = next(h for h in range(1,p) if pow(3,h,p)==1)
        while F(mass*residue,3**exponent)>F(1,4*p*p):exponent+=order
        lam = F(mass*residue,3**exponent)
        assert 0<lam<=F(1,4*p*p) and triadic(lam)
        assert triadic((1-lam)/p)
        for beta in (F(0),F(1,10*b)):
            r = mixed_return(p,beta)
            targets = ((lam*r[0],lam*r[1]),(lam*r[2],lam*r[3]),
                       (lam*(1-beta),lam*beta))
            weights = []
            for aa,bb in targets:
                gamma = F(1-aa-bb,p)
                alpha,second = aa+(p-4)*gamma,bb+3*gamma
                row = (alpha,second,gamma)
                assert sum(row) == 1 and min(row)>0 and all(triadic(x) for x in row)
                weights.append(row)
            assert tuple(sum(w*row[j] for w,row in zip((p-4,3,1),weights))
                         for j in range(3)) == (p-4,3,1)
            for row in weights:
                for x in row:max_bits=max(max_bits,x.numerator.bit_length(),x.denominator.bit_length())
            count += 1
    print('both target returns have common legal positive triadic transport margins: PASS',count)
    print('largest checked coefficient bit length',max_bits)


def verify_diagonal_shadow():
    p=431
    subgroup = {pow(-F(1,3).numerator*pow(3,-1,p),i,p) for i in range(p)}
    assert len(subgroup) == 86
    square_image = {a*a%p for a in range(1,p)}
    assert len(square_image) == 215 and len(square_image & subgroup) == 43
    assert pow(5,2,p) not in subgroup
    # Every p-integral beta has the same local slope, so adding the mixed
    # return cannot repair this full-group containment obstruction.
    for beta in (F(0),F(1),F(1,10),F(1,10*localization_product(p))):
        h = change(product(inverse(mixed_return(p,beta)),standard(p)))
        slope = h[0]/h[3]
        assert slope.numerator*pow(slope.denominator,-1,p)%p == -9%p
    print('whole-family diagonal shadow forbids full Gamma0 containment at431: PASS 86 215')
    print('This does not obstruct legal projective orbit coverage; torus absorption applies.')


def verify():
    verify_family()
    verify_localized_controller()
    verify_scales()
    verify_diagonal_shadow()
    print('Original-position realization of the two prescribed returns remains unproved.')


if __name__ == '__main__':verify()
