"""Exact diagnostics for the common root-lattice interpretation, not a new total proof."""
from fractions import Fraction as F
from itertools import product,combinations
from math import gcd
from pathlib import Path
from random import Random
from collections import Counter
import json,sys

sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'work'))
import verify_all_dimensions_double_triple_invariant as direct

def gram(d):return [[int(i==j)+1 for j in range(d)] for i in range(d)]
def rank_mod(M,p):
    M=[row[:] for row in M];r=0
    for c in range(len(M[0])):
        pivot=next((i for i in range(r,len(M)) if M[i][c]%p),None)
        if pivot is None:continue
        M[r],M[pivot]=M[pivot],M[r]
        inv=pow(M[r][c],-1,p);M[r]=[v*inv%p for v in M[r]]
        for i in range(len(M)):
            if i!=r:
                a=M[i][c]%p;M[i]=[(x-a*y)%p for x,y in zip(M[i],M[r])]
        r+=1
        if r==len(M):break
    return r

def lattice_radicals():
    rng=Random(3072026);checks=0;radical_checks=0
    for n in range(3,46):
        B=gram(n-1)
        for p in (2,3,5,7,11,13):
            assert rank_mod(B,p)==n-1-int(n%p==0)
            radical_checks+=1
        for _ in range(20):
            z=[rng.randrange(-20,21) for _ in range(n-1)]
            X=z+[-sum(z)]
            if not any(X):continue
            g=gcd(*X);z=[v//g for v in z];X=[v//g for v in X]
            pairings=[z[i]+sum(z) for i in range(n-1)]
            G=gcd(*pairings)
            assert G==gcd(*(v-X[-1] for v in X)) and n%G==0
            for p in (2,3,5,7,11,13):
                in_radical=all(v%p==0 for v in pairings)
                diagonal=len({v%p for v in X})==1
                assert in_radical==diagonal==(G%p==0)
            checks+=1
    return {'primitive_pairing_identity_checks':checks,'gram_radical_rank_checks':radical_checks}

def projection_identities():
    rng=Random(713)
    count=0
    for n in (5,6,7,8,10,11,15,21):
        for _ in range(25):
            X=[F(rng.randrange(-12,13),3) for _ in range(n-1)];X.append(-sum(X))
            inds=rng.sample(range(n),3);a,b,c=(X[i] for i in inds);mean=(a+b+c)/3
            Y=X[:]
            for i in inds:Y[i]=mean
            delta=sum(x*x for x in X)-sum(y*y for y in Y)
            assert delta==((a-b)**2+(a-c)**2+(b-c)**2)/3
            root1=[int(i==inds[0])-int(i==inds[2]) for i in range(n)]
            root2=[int(i==inds[1])-int(i==inds[2]) for i in range(n)]
            d1=a-c;d2=b-c
            t1=(2*d1-d2)/3;t2=(2*d2-d1)/3
            assert Y==[X[i]-t1*root1[i]-t2*root2[i] for i in range(n)]
            count+=1
    return count

def norm_and_window_counterexamples():
    X=(1,-1,3,-3,1,-1,0,0,0,0,0)
    assert len(X)==11 and sum(X)==0 and gcd(*X)==1
    assert gcd(*(v-X[0] for v in X))==1 and sum(v*v for v in X)==22
    steps,_=direct.solve(X)
    # A scalar return about a 7-position window's mean is affine on the whole state.
    window=X[:7];mu=F(sum(window),7);lam=F(-1,27)
    Y=tuple(mu+lam*(F(x)-mu) for x in window)+tuple(map(F,X[7:]))
    assert mu==0  # Use a second explicit window with nonzero mean.
    Z=(-7,1,1,1,1,1,1,1)
    mu=F(sum(Z[:7]),7);assert mu==F(-1,7)
    Y=tuple(mu+lam*(F(x)-mu) for x in Z[:7])+(F(Z[7]),)
    assert sum(Y)==0 and Y!=tuple(lam*x for x in Z)
    assert Y[7]==Z[7]
    return {'G1_norm_divisible_by11_input':X,'energy':22,'actual_solution_steps':steps,
            'nonzero_window_mean':str(mu),'local_scalar_not_global_scalar':True}

def border_resource_failure():
    X=(-5,-5,-5,3,4,4,4);moves=set()
    for inds in combinations(range(7),3):
        vals=tuple(X[i] for i in inds)
        if len(set(vals))==1 or sum(vals)%3:continue
        Y=list(X);mean=sum(vals)//3
        for i in inds:Y[i]=mean
        assert len([v for v,k in Counter(Y).items() if k>=3])==1
        moves.add(tuple(sorted(vals)))
    assert moves=={(-5,-5,4),(-5,4,4)}
    return {'seven_entry':X,'nontrivial_integer_move_types':sorted(moves),
            'all_lose_two_distinct_triples':True}

def direct_routes():
    rng=Random(20260918);rows=[]
    for n in (11,12,14,15,18,21,25,30,35):
        while True:
            X=[rng.randrange(-3,4) for _ in range(n-1)];X.append(-sum(X))
            if not any(X):continue
            g=gcd(*X);X=tuple(v//g for v in X)
            if direct.incongruent(Counter(X),n):break
        steps,branches=direct.solve(X)
        rows.append({'n':n,'steps':steps,'branch_types':sorted(branches)})
    return rows

if __name__=='__main__':
    if not __debug__:raise RuntimeError('Assertions required')
    result={'root_lattice':lattice_radicals(),'A2_projection_checks':projection_identities(),
            'limits_of_norm_and_window':norm_and_window_counterexamples(),
            'seven_resource_counterexample':border_resource_failure(),'direct_n_ge11_paths':direct_routes(),
            'scope':'Uniform interpretation and independently replayed existing direct construction; no new all-n modular controller claimed.'}
    Path(__file__).with_name('triple_all_n_geometric_synthesis_verification.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))
