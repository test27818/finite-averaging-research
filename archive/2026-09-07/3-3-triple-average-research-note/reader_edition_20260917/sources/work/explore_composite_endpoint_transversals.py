"""Finite CRT Schreier transversal diagnostics, not averaging-word search.

This reports whether fixed simple Gauss pivots cover all loops. A failure does
not disprove group containment or reachability. Exact certificates can be
checked by a separate verifier.
"""

from collections import deque,Counter
from fractions import Fraction as F
from math import gcd,prod

from verify_prime_power_endpoint_completion import I,S,T,mul,inv
from verify_composite_arity_transfer import factors


def label(c,d,moduli):
    return tuple((1,d*pow(c,-1,m)%m) if c%p else (c*pow(d,-1,m)%m,1)
                 for p,m in moduli)


def transversal(n):
    moduli=[(p,p**a) for p,a in factors(n).items()]
    root=label(0,1,moduli)
    reps={root:I}
    queue=deque([root])
    gens=(S,T,inv(T))
    while queue:
        key=queue.popleft()
        for g in gens:
            z=mul(reps[key],g)
            target=label(z[2],z[3],moduli)
            if target not in reps:
                reps[target]=z
                queue.append(target)
    assert len(reps)==prod(m+m//p for p,m in moduli)
    return moduli,reps


def unit(x,n,p):
    x=F(x)
    if not x or gcd(x.numerator,n)>1 or gcd(x.denominator,n)>1:
        return False
    return all(ell<=p for z in (abs(x.numerator),x.denominator) for ell in factors(z))


def choose_pivot(matrix,n,p):
    a,b,c,d=matrix
    if unit(a,n,p):
        return 'a',F(0)
    if unit(d,n,p):
        return 'd',F(0)
    for den in (1,2,4,8,16):
        for k in (-1,1,-2,2,-3,3,-4,4,-5,5,-6,6,-7,7,-8,8):
            t=F(k,den)
            if unit(a+t*c,n,p):
                return 'shear',t
    return None


def audit(n):
    p=(n-1)//2
    moduli,reps=transversal(n)
    counts=Counter()
    failed=[]
    bounds=[0,0]
    for key,r in reps.items():
        for g in (S,T,inv(T)):
            z=mul(r,g)
            target=label(z[2],z[3],moduli)
            loop=mul(z,inv(reps[target]))
            assert loop[2]%n==0
            bounds[0]=max(bounds[0],abs(loop[0]))
            bounds[1]=max(bounds[1],min(abs(loop[0]),abs(loop[3])))
            pivot=choose_pivot(loop,n,p)
            if pivot:
                counts[pivot[0]]+=1
            else:
                failed.append(loop)
    return len(reps),dict(counts),failed,bounds


def main():
    for n in (15,35,39,55,63,75,87,91,95,111,115,119,123,135,143,155,
              159,175,183,187,195,203,207,215,219,231,255,315,399,435,455,1155):
        count,stats,failed,bounds=audit(n)
        print(n,'primes',len(factors(n)),'cosets',count,'pivots',stats,
              'failure',len(failed),'max/min pivot',bounds,flush=True)
        if failed:
            print('sample',failed[:3],flush=True)


if __name__=='__main__':
    main()
