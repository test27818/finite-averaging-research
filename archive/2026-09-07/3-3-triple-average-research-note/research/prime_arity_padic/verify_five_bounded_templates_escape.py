"""Exact checks for bounded-template escape. General finiteness uses ESS, not samples."""
from itertools import product
from math import gcd,isqrt
from pathlib import Path
import json

I=(1,0,0,1)
A=(-3,0,-1,1)
B=(1,-1,0,-3)
J=(4,-1,-1,4)

def mul(X,Y):
    return tuple(sum(X[2*i+k]*Y[2*k+j] for k in range(2))
                 for i in range(2) for j in range(2))

def mv(M,z):return (M[0]*z[0]+M[1]*z[1],M[2]*z[0]+M[3]*z[1])
def transpose(M):return (M[0],M[2],M[1],M[3])
def det(M):return M[0]*M[3]-M[1]*M[2]
def word(s,p=3):
    R=I
    for c in s:R=mul(R,(-p,0,-1,1) if c=='A' else (1,-1,0,-p))
    return R
def power(M,n):
    R=I
    while n:
        if n&1:R=mul(R,M)
        M=mul(M,M);n//=2
    return R
def q(z):return z[0]**2+7*z[0]*z[1]+z[1]**2
def energy(z):return 4*z[0]**2-2*z[0]*z[1]+4*z[1]**2

def spectral_and_energy():
    mixed=pure=0
    for p in (3,5,7,11):
        H=(p+1,-1,-1,p+1)
        delta=p*(p+2)*(p-1)
        for c in 'AB':
            M=word(c,p);K=mul(transpose(M),mul(H,M))
            assert tuple(x-y for x,y in zip(K,H))==((delta,0,0,0) if c=='A' else (0,0,0,delta))
        for length in range(1,9):
            for chars in product('AB',repeat=length):
                s=''.join(chars);M=word(s,p)
                assert (M[0]+M[3])%p==1 and det(M)==(-p)**length
                K=mul(transpose(M),mul(H,M));D=tuple(x-y for x,y in zip(K,H))
                if len(set(s))==2:
                    assert D[0]>0 and det(D)>0
                    # No eigenvalue +1 or -1: strict energy expansion.
                    assert 1-(M[0]+M[3])+det(M)!=0
                    assert 1+(M[0]+M[3])+det(M)!=0
                    mixed+=1
                else:
                    assert det(D)==0
                    pure+=1
    return {'mixed_words_checked':mixed,'pure_words_checked':pure,
            'primes':[3,5,7,11],'scope':'Checks exact positivity, determinant, and mod-p identities.'}

def templates():
    cases=[(('', '', ''),('AB','BA')),
           (('A','BB','A'),('ABA','ABBA')),
           (('AB','BA','A','BB'),('A','B','A')),
           (('BA','A','BA',''),('AB','A','BBA'))]
    checked=raychecks=0
    for connectors,blocks in cases:
        r=len(blocks)
        for exps in product(range(5),repeat=r):
            M=word(connectors[0]);literal=connectors[0]
            for i,(block,n) in enumerate(zip(blocks,exps)):
                M=mul(M,mul(power(word(block),n),word(connectors[i+1])))
                literal+=block*n+connectors[i+1]
            assert M==word(literal)
            z=mv(M,(1,-1));assert gcd(*z)==1 and z[0]*z[1]!=0 and q(z)!=0
            assert (z[0]+z[1])%5==0
            checked+=1
        for direction in product(range(3),repeat=r):
            if not any(direction):continue
            vals=[]
            for t in range(9):
                M=word(connectors[0])
                for i,(block,b) in enumerate(zip(blocks,direction)):
                    M=mul(M,mul(power(word(block),1+t*b),word(connectors[i+1])))
                vals.append(q(mv(M,(1,-1))))
            assert len(set(vals))>1
            raychecks+=1
    return {'template_parameter_instances':checked,'affine_rays_diagnosed':raychecks,
            'scope':'Ray nonconstancy in finite samples is a formula check, not the theorem proof.'}

def exact_norm_symmetry():
    # 3C, C=B^{-1}A; avoids fractions.
    C=(-8,-1,1,-1)
    assert mul(B,C)==tuple(3*x for x in A)
    assert mul(C,C)==tuple(9*x for x in (7,1,-1,0))
    for z in ((1,-1),(9,1),(11,24),(-357,52)):
        assert q(mv(C,z))==9*q(z)
    return {'C':'B^{-1}A=(-8,-1;1,-1)/3','C_square':'(7,1;-1,0)',
            'meaning':'The norm-preserving unit motion is an inverse-containing group word, not a positive return.'}

def symmetric_square(M):
    a,b,c,d=M
    return ((a*a,2*a*b,b*b),(a*c,a*d+b*c,b*d),(c*c,2*c*d,d*d))

def periodic_expansion_checks():
    count=0;types={'real_distinct':0,'complex_pair':0}
    for length in range(2,9):
        for chars in product('AB',repeat=length):
            s=''.join(chars)
            if len(set(s))<2:continue
            M=word(s);trace=M[0]+M[3];d=det(M)
            types['complex_pair' if trace*trace-4*d<0 else 'real_distinct']+=1
            z=(1,-1);seq=[]
            for _ in range(12):seq.append(q(z));z=mv(M,z)
            a=trace*trace-d
            for i in range(3,len(seq)):
                assert seq[i]==a*seq[i-1]-d*a*seq[i-2]+d**3*seq[i-3]
                count+=1
    return {'spectral_types':types,'quadratic_recurrence_checks':count,
            'scope':'Baker lower bound is an external general theorem; numerical samples do not certify its constants.'}

def norm_return_diagnostic(depth):
    """Solve Q(Wx)=+/-Q(x) over rational directions, then use the complete oracle."""
    from verify_subcritical_complement_dynamics import core_distance
    hits=[];words=0
    stack=[(I,'')]
    while stack:
        M,w=stack.pop()
        if w:
            words+=1
            a,b,c,d=M
            aa=a*a+7*a*c+c*c
            bb=2*a*b+7*(a*d+b*c)+2*c*d
            cc=b*b+7*b*d+d*d
            for sign in (1,-1):
                x,y,z=aa-sign,bb-7*sign,cc-sign
                disc=y*y-4*x*z
                if disc<0 or isqrt(disc)**2!=disc:continue
                sq=isqrt(disc)
                candidates=[(1,0)] if x==0 else []
                if x:candidates.extend(((-y+sq,2*x),(-y-sq,2*x)))
                elif y:candidates.append((-z,y))
                seen=set()
                for u,v in candidates:
                    if not (u or v):continue
                    g=gcd(u,v);u,v=u//g,v//g
                    if u<0 or (u==0 and v<0):u,v=-u,-v
                    if (u,v) in seen:continue
                    seen.add((u,v))
                    assert q(mv(M,(u,v)))==sign*q((u,v))
                    if core_distance(3,u,v) is not None:
                        hits.append({'word':w,'sign':sign,'seed':(u,v),'D':abs(q((u,v)))//5})
        if len(w)<depth:
            stack.append((mul(M,A),w+'A'))
            stack.append((mul(M,B),w+'B'))
    return {'depth':depth,'all_nonempty_words_checked':words,'successful_rational_return_roots':hits,
            'scope':'Finite macro-length diagnostic only; does not exclude longer returns or unrelated branches.'}

if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--return-depth',type=int,default=0)
    args=parser.parse_args()
    if not __debug__:raise RuntimeError('Assertions required')
    result={'spectral_energy':spectral_and_energy(),'templates':templates(),
            'norm_symmetry':exact_norm_symmetry(),'periodic_growth':periodic_expansion_checks(),
            'status':'Bounded-template escape proved; arbitrary changing positive words remain open.'}
    if args.return_depth:
        result['finite_norm_return_diagnostic']=norm_return_diagnostic(args.return_depth)
    Path(__file__).with_name('five_bounded_templates_escape_verification.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))
