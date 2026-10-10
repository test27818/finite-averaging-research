"""Exact checks for minimal field denominators and local indistinguishability."""
from fractions import Fraction as Q
from math import gcd, lcm
from pathlib import Path
import json
from verify_five_torus_twist import lift, EPS, ONE, mul, inv, div, add, neg, J, valuation
from verify_subcritical_complement_dynamics import core_distance


def denominator(alpha):
    A,B=alpha
    return lcm((A-B).denominator,(2*B).denominator)


def power(alpha,k):
    z=ONE
    while k:
        if k&1:z=mul(z,alpha)
        alpha=mul(alpha,alpha)
        k//=2
    return z


def from_alpha(alpha):
    h=div(add(alpha,neg(ONE)),add(alpha,ONE))[1]/3
    a,b=h.numerator,h.denominator
    u,v=b+5*a,5*a-b
    g=gcd(u,v)
    return h,(u//g,v//g)


def q5(u,v):return u*u+7*u*v+v*v


def factor(n):
    primes=[]
    d=2
    while d*d<=n:
        if n%d==0:
            primes.append(d)
            while n%d==0:n//=d
        d+=1
    if n>1:primes.append(n)
    return primes


def run():
    pairs=edges=models=0
    for u in range(-100,101):
        for v in range(-100,101):
            if gcd(u,v)!=1 or (u+v)%5 or (u-v)%3==0:continue
            h=Q(u+v,5*(u-v));alpha=lift(h)
            normform=q5(u,v);D=abs(normform)//5
            assert denominator(alpha)==D and gcd(D,30)==1
            assert all(ell%5 in (1,4) for ell in factor(D))
            A,B=alpha;C,E=2*D*A,2*D*B
            assert C.denominator==E.denominator==1
            C,E=int(C),int(E)
            assert C*C-5*E*E==4*D*D and (C-E)%2==0
            C0,E0,D0=Q(-5*C-8*D,9),Q(-E,3),Q(2*C+5*D,9)
            assert C0.denominator==E0.denominator==D0.denominator==1
            assert abs(D0)==denominator(J(alpha))
            permitted=[]
            for sigma in (1,-1):
                parent=mul(inv(EPS) if sigma==1 else EPS,J(alpha))
                Cp,Ep=(3*C0-5*sigma*E0)/2,(-sigma*C0+3*E0)/2
                assert Cp.denominator==Ep.denominator==1
                assert parent==(Cp/(2*D0),Ep/(2*D0))
                assert denominator(parent)==abs(D0)
                if valuation(parent[0]-1,3)>=1 and valuation(parent[1],3)>=1:
                    permitted.append(sigma)
            if h==0 or valuation(h,3)>0:
                assert not permitted
            else:
                residue=h.numerator*pow(h.denominator,-1,3)%3
                assert permitted==([1] if residue==1 else [-1])
            energy=Q(4*u*u-2*u*v+4*v*v,5)
            assert energy==Q(2*abs(C+D),3)
            signedU,signedV=3*C+5*E+5*D,3*C-5*E+5*D
            assert signedU*signedU-7*signedU*signedV+signedV*signedV+25*D*(signedU+signedV)+55*D*D==0
            child_denominators=[]
            for sigma in (1,-1):
                child=J(mul(EPS if sigma==1 else inv(EPS),alpha))
                DD=denominator(child)
                assert gcd(D,DD)==1
                C1,E1=(3*C+5*sigma*E)//2,(sigma*C+3*E)//2
                CC,EE,D1=-5*C1-8*D,-3*E1,2*C1+5*D
                assert abs(D1)==DD==abs(3*C+5*sigma*E+5*D)
                assert child==(Q(CC,2*D1),Q(EE,2*D1))
                uu,vv=(-3*u,v-u) if sigma==1 else (u-v,-3*v)
                assert abs(q5(uu,vv))//5==DD
                new_energy=Q(4*uu*uu-2*uu*vv+4*vv*vv,5)
                assert new_energy-energy==6*(u*u if sigma==1 else v*v)
                child_denominators.append(DD)
                edges+=1;models+=1
            assert gcd(*child_denominators)==gcd(u+v,11)
            pairs+=1
    # The coprimality is valid for all rational torus points, beyond legal core domain.
    general=0
    for a in range(-45,46):
        for b in range(1,36):
            if gcd(a,b)!=1:continue
            alpha=lift(Q(a,b))
            for sigma in (1,-1):
                child=J(mul(EPS if sigma==1 else inv(EPS),alpha))
                assert gcd(denominator(alpha),denominator(child))==1
                general+=1
    alpha0=lift(Q(1))
    alpha1=mul(power(EPS,4),alpha0)
    assert alpha1==(Q(-349,11),Q(-156,11))
    assert lift(Q(23-3,5*(23+3)))==alpha1
    assert core_distance(3,3,2)==2 and core_distance(3,23,-3) is None
    assert denominator(alpha0)==denominator(alpha1)==11
    eps2=power(EPS,2)
    from verify_five_torus_twist import norm
    assert norm((eps2[0]-4,eps2[1]))==-11
    approximants=[]
    for u,v in ((1,-1),(3,2),(9,1),(11,24),(139,261)):
        h0=Q(u+v,5*(u-v));alpha0=lift(h0)
        L=core_distance(3,u,v)-1
        for m in (L+1,L+2):
            alpha_m=mul(alpha0,power(EPS,4*3**m))
            hm,(um,vm)=from_alpha(alpha_m)
            assert valuation(hm-h0,3)==m
            assert denominator(alpha_m)==denominator(alpha0)
            assert hm.denominator%15 and (um+vm)%5==0 and (um-vm)%3
            assert core_distance(3,um,vm) is None
            approximants.append({'seed':[u,v],'word_length':L,'m':m,
                                 'height_bits':max(abs(um),abs(vm)).bit_length(),
                                 'same_minimal_denominator':denominator(alpha0)})
    result={'primitive_legal_pairs':pairs,'adjacent_denominator_edges':edges,
            'exact_predecessor_denominator_and_local_choice':pairs,
            'sibling_gcd_identity_checks':pairs,
            'exact_integer_conic_updates':models,'unrestricted_torus_edges':general,
            'same_divisor_counterexample':'alpha1=epsilon^4 alpha0, D=11',
            'arbitrarily_close_family_checks':approximants,
            'scope':'No claim that a fixed denominator has finitely many solvable points; no complete static criterion.'}
    Path(__file__).with_name('five_torus_denominators_verification.json').write_text(
        json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    if not __debug__:raise RuntimeError('Assertions required.')
    run()
