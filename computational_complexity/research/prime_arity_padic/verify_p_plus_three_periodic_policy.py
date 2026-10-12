"""Independent finite integer-policy replay and recurrence checks."""
from itertools import product
from math import gcd
from pathlib import Path
from random import Random
import json
from p_plus_three_periodic_policy import (decide_periodic_core,zero_in_recurrence,
                                          multiply,determinant3,second_coefficient)
from five_eight_rank_clock import step_matrix,valuation


def primitive(u):
    g=gcd(*u)
    return tuple(x//g for x in u) if g else u


def literal_step(u,mask,p):
    a=-sum(u)//(p+3)
    old=(a,)*p+tuple(a+x for x in u)
    chosen=tuple(range(p-mask.bit_count()))+tuple(p+i for i in range(3) if mask>>i&1)
    selected=[old[i] for i in chosen]
    if len(set(selected))==1:return u
    if sum(selected)%p:return None
    mean=sum(selected)//p
    # Reassign one unselected old common position to each selected exception slot.
    raw=tuple(a-mean if mask>>i&1 else a+u[i]-mean for i in range(3))
    normalized=primitive(raw)
    if any(normalized) and sum(normalized)%(p+3):return None
    return normalized


def policy_oracle(u,word,p):
    u=primitive(u)
    if sum(u)%(p+3):return False
    seen=set();index=0
    while True:
        if not sum(u):return True
        state=(u,index)
        if state in seen:return False
        seen.add(state)
        child=literal_step(u,word[index],p)
        if child is None:return False
        u=child;index=(index+1)%len(word)


def main():
    rng=Random(20261016);cases=atoms=recurrences=0
    for p in (5,7,11):
        words=[(mask,) for mask in range(1,7)]
        words += [(1,)*3,(1,2),(1,2,4),(1,4,2,1)]
        words += [tuple(rng.randrange(1,7) for _ in range(rng.randrange(1,7))) for _ in range(80)]
        for word in words:
            for _ in range(30):
                u=(rng.randrange(-150,151),rng.randrange(-150,151),0)
                u=u[:2]+(-sum(u)+(p+3)*rng.randrange(-20,21),)
                answer=decide_periodic_core(u,word,p)
                assert answer['possible']==policy_oracle(u,word,p),(p,u,word,answer)
                if answer['possible']:
                    state=primitive(u)
                    for mask in answer['word']:
                        state=literal_step(state,mask,p)
                        assert state is not None
                        atoms+=1
                    assert not any(state)
                cases+=1
    for trace in range(-15,16):
        if trace%5==0:continue
        for determinant in (-125,-25,-5,5,25,125):
            for _ in range(20):
                f0,f1=rng.randrange(-50,51),rng.randrange(-50,51)
                answer=zero_in_recurrence(trace,determinant,f0,f1)
                values=[f0,f1]
                for k in range(2,40):values.append(trace*values[-1]-determinant*values[-2])
                expected=next((k for k,x in enumerate(values) if x==0),None)
                assert answer==expected,(trace,determinant,f0,f1,answer,expected)
                recurrences+=1
    # Force very large repetition indices in a second-order p-adic clock.
    large=[]
    for k in (100,1000):
        # f(j)=5**j-5**k, roots 1 and 5.
        f0=1-5**k;f1=5-5**k
        answer=zero_in_recurrence(6,5,f0,f1)
        assert answer==k
        large.append({'root_index':k,'input_height_bits':abs(f0).bit_length()})
    # An actual mixed period with an arbitrarily long forced tower.
    # Two alternating pair masks restore the original exception pairing.
    word=(5,3)
    long=[]
    for k in (20,200):
        z=(1,-2)
        # Mixed T has inverse B=(-1,1;-4,-1), integer and norm multiplier 5.
        for _ in range(k):z=(-z[0]+z[1],-4*z[0]-z[1])
        answer=decide_periodic_core((z[0],z[0],z[1]),word,5)
        assert answer['possible']
        state=primitive((z[0],z[0],z[1]))
        for mask in answer['word']:
            state=literal_step(state,mask,5)
            assert state is not None
            atoms+=1
        assert not any(state)
        long.append({'tower_increment':k,'input_height_bits':max(map(abs,z)).bit_length(),
                     'steps':answer['steps']})
    singleton_towers=[]
    for word in ((1,),(1,2),(1,2,4)):
        for k in (20,200):
            u=(1,2,-3)
            for _ in range(k):
                for mask in reversed(word):
                    i=mask.bit_length()-1;selected=u[i]
                    u=tuple(-5*selected if j==i else x-selected for j,x in enumerate(u))
            answer=decide_periodic_core(u,word)
            assert answer['possible']
            state=primitive(u)
            for mask in answer['word']:
                state=literal_step(state,mask,5)
                assert state is not None
                atoms+=1
            assert not any(state)
            singleton_towers.append({'period':word,'inverse_repetitions':k,
                                     'input_height_bits':max(map(abs,u)).bit_length(),
                                     'steps':answer['steps']})
    record={'scope':'Polynomial decision of any prescribed proper periodic policy; not free policy synthesis.',
            'integer_policy_cases':cases,'replayed_atoms':atoms,'recurrence_cases':recurrences,
            'large_recurrence_roots':large,'mixed_towers':long,
            'singleton_towers':singleton_towers}
    Path(__file__).with_name('p_plus_three_periodic_policy_verification.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(record,indent=2))


if __name__=='__main__':main()
