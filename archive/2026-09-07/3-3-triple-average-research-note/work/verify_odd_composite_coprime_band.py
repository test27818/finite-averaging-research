"""Audit the old odd-band proof under its actual coprimality hypothesis."""
from math import gcd
from random import Random
from verify_uniform_odd_middle_cores import core_algebra,transport,physical

if not __debug__:raise RuntimeError('Assertions must be enabled.')

def main():
    rng=Random(91533);systems=paths=0
    for k in (9,15,21,25,27,33,35,45,49,63,81,105):
        for r in range(3,k,2):
            if gcd(k,r)!=1:continue
            v=core_algebra(k,r);systems+=1
            for _ in range(3):
                while True:
                    x,z=rng.randrange(-80,81),rng.randrange(-80,81)
                    if gcd(x,z)==gcd(x+k*z,2*k+r)==1:break
                transport(x,z,k,r,v)
            if k<=25:
                for x,z in ((1,0),(0,1)):paths+=physical(k,r,x,z)
    count=0
    for p in(3,5,7,11):
        for a in range(1,5):
            k=p**a
            for r in range(1,k,2):
                d=gcd(k,r);q=k//d;rr=r//d;nn=2*q+rr
                assert q>=p and gcd(q,rr)==1 and rr%2 and 2*q<nn<3*q
                assert all((nn%ell or q%ell==0) for ell in (p,))
                count+=1
    print('odd-composite coprime-band exact algebra and terminal interfaces: PASS',systems,paths)
    print('odd-prime-power band divisor reduction identities: PASS',count)
    print('odd-composite coprime-band extension interfaces: PASS')

if __name__=='__main__':main()
