"""Exact checks linking seven-entry averaging, cusps, norm, and physical words."""
from fractions import Fraction as F
from itertools import combinations
from math import gcd,isqrt
from pathlib import Path
from random import Random
from collections import Counter
import sys,json

sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'work'))
import verify_seven_endpoint_structure as old

I=(1,0,0,1)
S=(0,-1,1,0)
T=(1,1,0,1)

def egcd(a,b):
    if b==0:return (abs(a),1 if a>=0 else -1,0)
    g,x,y=egcd(b,a%b)
    return g,y,x-(a//b)*y

def mul(X,Y):return old.mul(X,Y)
def mv(M,z):return (M[0]*z[0]+M[1]*z[1],M[2]*z[0]+M[3]*z[1])
def det(M):return M[0]*M[3]-M[1]*M[2]
def q(x,y):return 7*x*x-7*x*y+2*y*y
def core(x,y):return (x,)*3+(x-y,)*3+(-3*(2*x-y),)
def G(state):return gcd(*(state[i]-state[0] for i in range(1,len(state))))

def cusp_matrix(x,y):
    g,a,b=egcd(x,y);assert g==1
    if y%7:
        k=-a*pow(y,-1,7)%7
        a,b=a+k*y,b-k*x
        H=(y,-x,a,b);target=(0,1)
    else:H=(a,b,-y,x);target=(1,0)
    assert det(H)==1 and H[2]%7==0 and mv(H,(x,y))==target
    return H

def decompose_sl2(M):
    """Right factors S,T^n in PSL2(Z), via Euclid; no word search."""
    factors=[]
    def rec(X):
        a,b,c,d=X
        if c==0:
            assert a==d and abs(a)==1
            if a*b:factors.append(('T',a*b))
            return
        k=a//c
        Y=mul((1,-k,0,1),X)
        Y=mul((0,1,-1,0),Y)
        factors.append(('T',k));factors.append(('S',1));rec(Y)
    rec(M)
    X=I
    for typ,n in factors:X=mul(X,S if typ=='S' else (1,n,0,1))
    assert old.normalize(X)==old.normalize(M)
    return factors

def compile_gamma0(M):
    """Rewrite an arbitrary integer Gamma0(7) matrix using the established 8-coset proof."""
    label=None;chronological=()
    reps={None:I,**{j:(0,-1,1,j) for j in range(-3,4)}}
    for typ,n in decompose_sl2(M):
        letters=[S] if typ=='S' else [(1,1 if n>0 else -1,0,1)]*abs(n)
        for generator in letters:
            candidate=mul(reps[label],generator)
            c,d=int(candidate[2])%7,int(candidate[3])%7
            next_label=None if not c else old.signed(d*pow(c,-1,7))
            edge=old.normalize(mul(candidate,old.inverse(reps[next_label])))
            if edge==I:ew=()
            elif edge==old.normalize(T):ew=old.upper_word(1)
            elif edge==old.normalize((1,-1,0,1)):ew=old.upper_word(-1)
            elif edge==old.normalize((1,0,7,1)):ew=old.lower_word(7)
            elif edge==old.normalize((1,0,-7,1)):ew=old.lower_word(-7)
            else:
                assert generator==S and label not in (None,0)
                j=label;k=old.signed(-pow(j,-1,7))
                ew=old.upper_word(F(1,k))+old.diag_word(F(1,k*k))+old.lower_word(F(-j*k-1,k))
            assert old.word_matrix(ew)==edge
            chronological=ew+chronological
            label=next_label
    assert label is None and old.word_matrix(chronological)==old.normalize(M)
    return chronological

def norm_and_cusps():
    checked=legal=bad=0
    for x in range(-35,36):
        for y in range(-35,36):
            if gcd(x,y)!=1:continue
            state=core(x,y);m=q(x,y)
            assert sum(state)==0 and gcd(*state)==1 and sum(t*t for t in state)==6*m
            assert G(state)==gcd(y,7)
            assert m%7==2*y*y%7
            valuation=0;temp=m
            while temp%7==0:temp//=7;valuation+=1
            assert valuation==(0 if y%7 else 1)
            # x-(2x-y)omega, Norm(omega)=2, Tr(omega)=1.
            z=2*x-y
            assert x*x-x*z+2*z*z==m
            cusp_matrix(x,y)
            legal+=bool(y%7);bad+=not bool(y%7);checked+=1
    assert mul(mul(S,(1,7,0,1)),old.inverse(S))==(1,0,-7,1)
    return {'primitive_core_and_cusp_checks':checked,'legal':legal,'obstructed':bad,
            'cusp_widths':{'zero':7,'infinity':1}}

def safe_entry(state):
    assert len(state)==7 and sum(state)==0 and gcd(*state)==1 and G(state)==1
    first=[0,1,2];second=[3,4,5];singleton=6
    delta=2*sum(state[i] for i in first)+state[singleton]
    if delta%7==0:
        i,j=next((i,j) for i in first for j in second if (state[i]-state[j])%7)
        first[first.index(i)]=j;second[second.index(j)]=i
    a=F(sum(state[i] for i in first),3);b=F(sum(state[i] for i in second),3)
    assert -3*(a+b)==state[singleton]
    actual=list(map(F,state))
    for selected in (first,second):
        mean=sum(actual[i] for i in selected)/3
        for i in selected:actual[i]=mean
    assert all(actual[i]==a for i in first) and all(actual[i]==b for i in second)
    assert actual[singleton]==-3*(a+b)
    X=int(3*a);Y=int(3*(a-b));g=gcd(X,Y)
    assert Y%7 and (Y//g)%7
    return a,b

def replay_checks():
    rng=Random(7172026);states=[]
    while len(states)<12:
        state=[rng.randrange(-9,10) for _ in range(6)];state.append(-sum(state))
        g=gcd(*state)
        if not g:continue
        state=tuple(v//g for v in state)
        if G(state)==1:states.append(state)
    states.append((-3,0,1,1,1,0,0))
    cases=[(F(1),F(0)),(F(1),F(-1)),(F(7),F(2)),(F(-4),F(2))]
    cases.extend(safe_entry(s) for s in states)
    lengths=[]
    for a,b in cases:
        x,y=a,a-b
        denom=__import__('math').lcm(x.denominator,y.denominator)
        X,Y=int(x*denom),int(y*denom);g=gcd(X,Y);X,Y=X//g,Y//g
        H=cusp_matrix(X,Y);w=compile_gamma0(H)
        replay=old.Replay(a,b);replay.word(w);replay.finish()
        assert not any(replay.state)
        lengths.append(len(replay.operations))
    return {'literal_core_paths':len(cases),'safe_two_average_entries':len(states),
            'maximum_atomic_steps':max(lengths),'all_final_states_zero':True}

def localized_group_reduction():
    checked=0
    scalars=[F(1),F(2,3),F(-9,4),F(1,36),F(24)]
    for x,y in ((1,7),(2,7),(-3,14),(5,-21),(1,0)):
        h=cusp_matrix(x,y);assert y%7==0
        for scale in scalars:
            for t in (F(0),F(5,12),F(-7,9)):
                upper=(scale,t,0,1/scale)
                g=mul(old.inverse(h),upper)
                assert det(g)==1 and (g[2]/7).denominator in (1,2,3,4,6,8,9,12,18,24,27,36)
                assert mul(h,g)==upper
                assert mv(g,(1,0))==(scale*x,scale*y)
                d=(scale,0,0,1/scale)
                assert mul(d,(1,t/scale,0,1))==upper
                checked+=1
    return {'localized_first_column_reductions':checked,
            'scope':'R-point inclusion proved in text; samples check fractional scale bookkeeping.'}

def padic_full_coverage():
    counts=[]
    for m in range(1,7):
        modulus=3**m
        reps=[(t,1) for t in range(modulus)]+[(1,3*t) for t in range(modulus//3)]
        for u,v in reps:
            y=v+modulus*((1-v)*pow(modulus,-1,7)%7)
            x=u;g=gcd(x,y);x,y=x//g,y//g
            assert y%7 and gcd(x,y)==1
            assert (x*v-y*u)%modulus==0 and (x%3 or y%3)
        counts.append({'precision':m,'all_projective_classes':len(reps)})
    state=list(map(F,(-3,0,1,1,1,0,0)))
    for selected in ((0,1,5),(0,2,6),(1,3,6),(5,4,6)):
        mean=sum(state[i] for i in selected)/3
        for i in selected:state[i]=mean
    assert not any(state)
    return {'full_local_cover':counts,'five_failure_plus_two_zeros_steps':4}

def theta_checks(limit=1200):
    bound=isqrt(2*limit)+3;counts=Counter();primitive=Counter()
    for a in range(-bound,bound+1):
        for b in range(-bound,bound+1):
            m=a*a-a*b+2*b*b
            if m<=limit:
                counts[m]+=1
                if gcd(a,b)==1:primitive[m]+=1
    chi=lambda a:0 if a%7==0 else (1 if a%7 in (1,2,4) else -1)
    for m in range(1,limit+1):
        divsum=0
        for d in range(1,isqrt(m)+1):
            if m%d==0:
                divsum+=chi(d)
                if d*d!=m:divsum+=chi(m//d)
        assert counts[m]==2*divsum
        t=m;omega=0;ok=True;ell=2
        while ell*ell<=t:
            exponent=0
            while t%ell==0:t//=ell;exponent+=1
            if exponent:
                if ell==7:ok &= exponent<=1
                elif chi(ell)==-1:ok=False
                else:omega+=1
            ell+=1
        if t>1:
            if t!=7 and chi(t)==-1:ok=False
            elif t!=7:omega+=1
        assert primitive[m]==(2**(omega+1) if ok else 0),(m,primitive[m])
    return {'theta_coefficients':limit,'primitive_representation_coefficients':limit,
            'scope':'Identities proved generally via Euclidean norm and ideal factorization; finite checks detect errors.'}

if __name__=='__main__':
    if not __debug__:raise RuntimeError('Assertions required')
    result={'norm_cusps':norm_and_cusps(),'physical_paths':replay_checks(),
            'theta':theta_checks(),'localized_group':localized_group_reduction(),
            'padic_coverage':padic_full_coverage(),
            'scope':'Seven-entry geometric synthesis; no new general-dimension theorem claimed.'}
    Path(__file__).with_name('seven_arithmetic_geometry_verification.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))
