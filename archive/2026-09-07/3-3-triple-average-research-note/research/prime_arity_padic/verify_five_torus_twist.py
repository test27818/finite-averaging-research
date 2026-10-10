"""Exact Q(sqrt5) audit, with no symbolic or floating algebra dependencies."""
from fractions import Fraction as Q
from math import gcd
from pathlib import Path
from random import Random
from itertools import product
import json
from verify_subcritical_complement_dynamics import core_distance

ONE = (Q(1), Q(0))
EPS = (Q(3,2), Q(1,2))


def add(a,b):
    return (a[0]+b[0],a[1]+b[1])


def neg(a):
    return (-a[0],-a[1])


def mul(a,b):
    return (a[0]*b[0]+5*a[1]*b[1],a[0]*b[1]+a[1]*b[0])


def norm(a):
    return a[0]*a[0]-5*a[1]*a[1]


def inv(a):
    n = norm(a)
    return (a[0]/n,-a[1]/n)


def div(a,b):
    return mul(a,inv(b))


def lift(h):
    return div((Q(1),3*h),(Q(1),-3*h))


def J(a):
    return div(neg(add(mul((Q(2),Q(0)),a),ONE)),add(a,(Q(2),Q(0))))


def phi(h,sign):
    return (3*h+sign)/(1+15*sign*h)


def trace(a):
    return 2*a[0]


def reduction5(a):
    # For a norm1 unit, the ramified residue is its rational coefficient mod5.
    assert a[0].denominator % 5
    return a[0].numerator*pow(a[0].denominator,-1,5) % 5


def valuation(x,p):
    x=Q(x)
    if not x:return float('inf')
    num,den=abs(x.numerator),x.denominator
    order=0
    while num%p==0:order+=1;num//=p
    while den%p==0:order-=1;den//=p
    return order


def run():
    assert norm(EPS)==1 and trace(EPS)==3
    assert J(ONE)==neg(ONE)
    assert neg(J(mul(EPS,EPS)))!=(mul(neg(J(EPS)),neg(J(EPS))))
    cases=branches=traces=local5=local3=0
    for a in range(-60,61):
        for b in range(1,61):
            if gcd(a,b)!=1:continue
            h=Q(a,b)
            alpha=lift(h)
            assert norm(alpha)==1 and J(J(alpha))==alpha
            assert J(inv(alpha))==inv(J(alpha))
            s=div(add(alpha,neg(ONE)),add(alpha,ONE))
            assert s==(0,3*h)
            u,v=b+5*a,5*a-b
            common=gcd(u,v)
            legal=(u+v)//common%5==0
            assert legal==(b%5!=0)
            assert (reduction5(alpha)==1)==legal
            local5+=1
            if b%3:
                assert valuation(alpha[0]-1,3)>=1 and valuation(alpha[1],3)>=1
                local3+=1
            # Both torus shifts and all rational branches.
            for sign in (1,-1):
                if 1+15*sign*h==0:continue
                shifted=mul(EPS if sign==1 else inv(EPS),alpha)
                AA=add(mul((Q(2),Q(0)),shifted),ONE)
                BB=add(shifted,(Q(2),Q(0)))
                assert add(mul((Q(2),Q(0)),BB),neg(AA))==(3,0)
                assert add(AA,neg(mul((Q(2),Q(0)),shifted)))==ONE
                child=phi(h,sign)
                assert lift(child)==J(shifted)
                assert reduction5(lift(child))==reduction5(alpha)
                if b%3:
                    assert child.denominator%3
                    assert child.numerator*pow(child.denominator,-1,3)%3==sign%3
                branches+=1
            # Compare with physical difference-coordinate inverse matrices.
            for sign,(uu,vv) in ((1,(-3*u,v-u)),(-1,(u-v,-3*v))):
                if uu==vv:continue
                assert Q(uu+vv,5*(uu-vv))==phi(h,sign)
            if u*v and u!=v:
                w=Q((u+v)**2,u*v)
                X=(10-7*w)/(w+5)
                assert X==trace(alpha)
                t=Q(u,v)
                z=(t-4)**2/(3*(1-t))
                Y=(3*z-10)/(5-z)
                assert Y==trace(mul(inv(EPS),alpha))
                assert X*X+Y*Y-3*X*Y+5==0
                assert (2*Y-3*X)**2-5*X*X==-20
                assert (10-7*z)/(z+5)==-(5*Y+8)/(2*Y+5)
                traces+=1
            cases+=1
    rng=Random(2026091703)
    contraction=0
    for _ in range(2000):
        h=Q(rng.randrange(-10000,10001),rng.randrange(1,10001))
        k=Q(rng.randrange(-10000,10001),rng.randrange(1,10001))
        if h==k or h.denominator%3==0 or k.denominator%3==0:continue
        for sign in (1,-1):
            assert valuation(phi(h,sign)-phi(k,sign),3)==valuation(h-k,3)+1
            contraction+=1
    assert phi(Q(-1,5),1)==Q(-1,5)
    assert phi(Q(1,5),-1)==Q(1,5)
    assert phi(Q(1,3),1)==Q(1,3)
    assert phi(Q(-1,3),-1)==Q(-1,3)
    # Four punctures are distinct in the split torus coordinate.
    assert J((Q(0),Q(0)))==(Q(-1,2),0)
    assert J((Q(-1,2),Q(0)))==(0,0)
    assert core_distance(3,1,24) is None
    # Residue field F9: s²=2; epsilon reduces to -s and has order4.
    e=(0,2)
    residue=lambda z:tuple(int(c)%3 for c in z)
    assert residue(mul(e,e))==(2,0)
    assert residue(mul(mul(e,e),mul(e,e)))==(1,0)
    # Fixed-depth genuine components are rational branches; compare finite matrix double cosets.
    from verify_five_padic_fractal import A, B, I, mul as matmul
    swap=(0,1,1,0)
    def normalized_matrix(M):
        content=gcd(*M)
        M=tuple(t//content for t in M)
        return M if next(t for t in M if t)>0 else tuple(-t for t in M)
    components=[]
    for depth in range(1,8):
        reps=set()
        for word in product((0,1),repeat=depth):
            M=I
            for letter in word:
                M=matmul((A,B)[letter],M)
            rep=min(normalized_matrix(matmul(L,matmul(M,R)))
                    for L in (I,swap) for R in (I,swap))
            reps.add(rep)
        assert len(reps)==2**(depth-1)
        components.append({'depth':depth,'endpoint_map_double_cosets':len(reps)})
    result={'rational_torus_points':cases,'exact_branch_identities':branches,
            'trace_conic_and_gluing_checks':traces,'ramified_prime5_checks':local5,
            'inert_prime3_principal_unit_checks':local3,'local_contraction_checks':contraction,
            'iterated_component_checks':components,
            'scope':'Full common torus structure; no assertion of a closed gcd criterion or torus-group orbit equivalence.'}
    Path(__file__).with_name('five_torus_twist_verification.json').write_text(
        json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    if not __debug__:raise RuntimeError('Assertions required.')
    run()
