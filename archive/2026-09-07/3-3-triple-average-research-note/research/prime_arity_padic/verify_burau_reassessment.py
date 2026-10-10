"""Exact comparisons of old Burau resources with prime-arity critical bands.

No group BFS or word search. General conclusions are proved in the note.
"""
from pathlib import Path
from fractions import Fraction as F
from time import perf_counter
import json,sys
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/'work'))
from verify_burau_power_chain import full_generator,inverse
from explore_weighted_kernel_group import identity,multiply
from verify_four_prime_entry_and_band import Ledger
from verify_square_zero_compiler import check_frozen_files,check_local_links


def power(A,k):
    ans=identity(len(A))
    while k:
        if k&1:ans=multiply(A,ans)
        A=multiply(A,A);k//=2
    return ans


def add(A,B):return tuple(tuple(a+b for a,b in zip(x,y)) for x,y in zip(A,B))
def scale(c,A):return tuple(tuple(c*x for x in row) for row in A)


def expand(ledger,seed,available,s):
    block=[seed]
    while len(block)<s:
        out=[]
        for x in block:
            others=available[-(ledger.p-1):]
            del available[-(ledger.p-1):]
            group=[x]+others
            ledger.average(group);out+=group
        block=out
    assert len(block)==s
    return block


def physical_chain(p,s,t):
    weights=[s**(t-1-i) for i in range(t)]
    raw=[];groups=[]
    for i,w in enumerate(weights):
        groups.append(list(range(len(raw),len(raw)+w)))
        raw += [F(2*i-3)]*w
    led=Ledger(raw,p)
    for i in range(t-1):
        large,small=groups[i],groups[i+1]
        u,v=led.state[large[0]],led.state[small[0]]
        kept=large[:len(small)];pool=large[len(small):]
        new=[]
        for seed in small:new+=expand(led,seed,pool,s)
        assert not pool and len(new)==weights[i] and len(kept)==weights[i+1]
        assert all(led.state[k]==((s-1)*u+v)/s for k in new)
        assert all(led.state[k]==u for k in kept)
        groups[i],groups[i+1]=new,kept
    led.independent_replay(raw)
    return len(led.word)


def main():
    if not __debug__:raise RuntimeError('Assertions required')
    start=perf_counter();braids=centers=inverses=atoms=defects=star_checks=0
    for p in (3,5,7,11):
        assert p*p+p+1>4*p
        for k in (1,2):
            s=p**k
            for t in range(3,7):
                generators=[full_generator(t,s,i) for i in range(t-1)]
                for i in range(t-2):
                    A,B=generators[i:i+2]
                    assert multiply(multiply(A,B),A)==multiply(multiply(B,A),B)
                    braids+=1
                C=identity(t)
                for A in generators:C=multiply(A,C)
                w=[s**(t-1-i) for i in range(t)];N=sum(w)
                P=tuple(tuple(F(w[j],N) for j in range(t)) for i in range(t))
                D=add(P,scale(F(1,s**t),add(identity(t),scale(-1,P))))
                assert power(C,t)==D;centers+=1
                for i,A in enumerate(generators):
                    L,H=identity(t),identity(t)
                    for j in range(i):L=multiply(generators[j],L)
                    for j in range(i+1,t-1):H=multiply(generators[j],H)
                    word=multiply(multiply(L,power(C,t-1)),H)
                    assert word==multiply(D,inverse(A));inverses+=1
                if N<=2000:atoms+=physical_chain(p,s,t)
    for a in (F(1,3),F(1,5),F(1,9),F(2,7)):
        for b in (F(1,3),F(1,5),F(1,9),F(2,7)):
            A=((1-a,a,0),(1,0,0),(0,0,1))
            B=((1,0,0),(0,1-b,b),(0,1,0))
            diff=add(multiply(multiply(A,B),A),scale(-1,multiply(multiply(B,A),B)))
            expected=scale(a-b,((a,-a,0),(-1,1,0),(0,0,0)))
            assert diff==expected;defects+=1
    for p in (2,3,5,7,11,83):
        A=((-F(1,p),0),(-1,1));B=((1,-1),(0,-F(1,p)))
        C=multiply(A,B);Q=scale(p,C)
        assert Q[0][0]+Q[1][1]==p-2
        assert Q[0][0]*Q[1][1]-Q[0][1]*Q[1][0]==1
        if p==3:assert power(C,3)==scale(-F(1,27),identity(2))
        elif p==2:assert power(C,2)==scale(-F(1,4),identity(2))
        else:assert (p-2)**2-4>0
        for x,y in ((F(1),F(0)),(F(0),F(1))):
            carrier=F(2,3)
            raw=[x+carrier]*p+[y+carrier]*p+[carrier]
            led=Ledger(raw,p)
            g1=list(range(p));g2=list(range(p,2*p));c=2*p
            chosen=g1[:p-1]+[c]
            led.average(chosen);newc=g1[-1]
            got=(led.state[chosen[0]]-led.state[newc],led.state[g2[0]]-led.state[newc])
            assert got==(-x/p,y-x)
            led.independent_replay(raw);atoms+=1
        star_checks+=1
    report={'status':'PASS','braid_identities':braids,'full_space_center_identities':centers,
            'positive_inverse_centered_identities':inverses,'literal_general_arity_atoms':atoms,
            'unequal_ratio_defect_identities':defects,'two_block_star_cases':star_checks,
            'frozen_files':check_frozen_files(),'local_links':check_local_links(),
            'seconds':round(perf_counter()-start,3),
            'scope':'Exact relations, nonzero-mean correction and p-ary physical expansion. Does not prove arithmetic index or terminal coverage; no word/group search.'}
    (HERE/'burau_reassessment_verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
