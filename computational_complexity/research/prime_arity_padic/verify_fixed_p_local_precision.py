"""Independent literal checks; infinite statements require the written proof."""
from math import gcd
from pathlib import Path
from random import Random
import json
from fixed_p_local_precision import synthesize,params,pairs,rho
from fixed_p_plus_three_solver import Solver,escape_filter,local_zero_in_range
from verify_subcritical_uniform_np_hard import integer_oracle,primitive


def actions(plan):
    tau,_=params(plan['p'])
    for t in plan['returns']+[tau]*plan['padding']:
        yield from [1]*(t-1)
        yield 2
    yield from [1]*plan['tail']


def literal_replay(plan,global_check=False):
    p=plan['p'];L=plan['L'];d=plan['digits']
    state=[0]*p+[1,1];den=1;scale=p**L
    outside=9-2*scale if global_check else None
    atoms=0
    for count in actions(plan):
        chosen=list(range(p-count))+list(range(p,p+count))
        chosen_set=set(chosen)
        selected_sum=sum(state[j] for j in chosen)
        assert len({state[j] for j in chosen})>1
        state=[selected_sum]*p+[p*state[j] for j in range(p+2) if j not in chosen_set]
        den*=p;scale//=p;atoms+=1
        assert sum(state)==2*den and state[0]%p
        if atoms==1:assert state[0] in (1,2)
        else:assert (p-1)*(den//p**2)<=state[0]<=2*(den//p)
        if global_check:
            assert p==7
            actual=[-1+scale*v for v in state]+[outside]
            assert sum(actual)==0
            # Literal full-state normalization, independently checking G=1.
            content=gcd(*actual)
            difference_content=gcd(*(v-actual[0] for v in actual))
            assert difference_content==content
    assert atoms==L and state[0]%p**d==plan['target']
    if global_check:
        assert actual[0]!=0 and actual[0]%p**d==0
    return atoms


def residue_checks():
    count=atoms=0
    for p in (5,7):
        tau,_=params(p)
        H={1,2,4} if p==7 else {1,2,3,4}
        for d in (1,2):
            for extra in range(tau):
                reference=synthesize(p,d,1)
                L=reference['T']+extra
                for target in range(1,p**d):
                    if target%p==0:continue
                    plan=synthesize(p,d,target,L)
                    # First digit of A_L is (-1)^(L-1)*2^s.
                    allowed=target%p in {((-1)**(L-1)*h)%p for h in H}
                    assert bool(plan)==allowed
                    if plan:
                        atoms+=literal_replay(plan);count+=1
    rng=Random(202610112)
    for p in (5,7):
        for d in (3,4,5):
            for _ in range(4):
                reference=synthesize(p,d,1)
                target=rng.randrange(1,p**d)
                while not target%p or (p==7 and target%p not in (1,2,4)):
                    target=rng.randrange(1,p**d)
                plan=synthesize(p,d,target,reference['L']+params(p)[0]*3)
                assert plan
                atoms+=literal_replay(plan);count+=1
    return {'words':count,'literal_local_atoms':atoms}


def global_no_checks():
    edges,oracle=integer_oracle(7,10)
    small=[]
    for L in (3,5,7):
        U=7**L;x=(-1,)*7+(U-1,U-1,9-2*U)
        assert oracle(primitive(x)) is None
        unfiltered=Solver(7,False)
        assert unfiltered.solve_input(x) is None
        fast=Solver(7,True)
        assert fast.solve_input(x) is None and fast.stats['queries']==1
        small.append({'L':L,'unfiltered_states':dict(unfiltered.stats)})
    rows=[]
    for d in range(1,6):
        plan=synthesize(7,d,1);L=plan['L']
        assert L%4==1 and escape_filter(7,-1,7**L)
        assert not local_zero_in_range(7,-1,1,L)
        atoms=literal_replay(plan,global_check=True)
        rows.append({'d':d,'L':L,'g_checked_literal_atoms':atoms,
                     'source_height_bits':(2*7**L-9).bit_length()})
    return {'small_independent_no_instances':small,
            'oracle_states':oracle.cache_info().currsize,'precision_no_examples':rows}


def identity_checks():
    count=0
    for p in (5,7):
        tau,_=params(p)
        for k in range(1,31):
            t=tau*k
            assert gcd(rho(p,t),p+3)==1
            a,b,c=2,-p,-p
            for _ in range(t-1):a,b,c=(p-1)*a+b,p*a,p*c
            a,b,c=(p-2)*a+b+c,p*a,p*a
            assert (a,b,c)==tuple(rho(p,t)*v for v in (2,-p,-p))
            count+=1
        for d in range(1,31):
            A,B,ps=pairs(p,d)
            for W,V in ps:
                assert all(t%tau==0 for t in W+V)
                assert sum(W)==sum(V)
            count+=len(ps)
    return count


def main():
    result={'scope':'Finite literal and independent-oracle checks. Quadratic precision synthesis and the infinite no family are proved in the note; general fixed-p P remains unresolved.',
            'identity_checks':identity_checks(),'residues':residue_checks(),
            'global_no':global_no_checks()}
    path=Path(__file__).with_name('fixed_p_local_precision_verification.json')
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
