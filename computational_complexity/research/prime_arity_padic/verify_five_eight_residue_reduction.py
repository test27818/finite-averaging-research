"""Exact independent checks; the polynomial reduction is proved in the note."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd
from pathlib import Path
from random import Random
import json
from five_eight_residue_reduction import sector,energy_numerator,reduce_core,reduce_input,canonical,cluster_reduction
from verify_subcritical_uniform_np_hard import integer_oracle,primitive


def physical(u):
    assert sum(u)%8==0
    a=-sum(u)//8
    return (a,)*5+tuple(a+v for v in u)


def residue_table():
    counts=Counter()
    for u in product(range(5),repeat=3):
        q=energy_numerator(u)%5
        kind=sector(u)
        expected={1:'equal',2:'collision',3:'distinct'}[len(set(u))]
        assert kind==expected,(u,q)
        counts[kind]+=1
        if kind=='distinct':
            assert sum(x==0 for x in u)<=1
            assert sum((u[i]+u[j])%5==0 for i,j in ((0,1),(0,2),(1,2)))<=1
    return dict(counts)


def independent_cases():
    edges,distance=integer_oracle(5,8)
    rng=Random(511008)
    counts=Counter();biggest=None
    for _ in range(3000):
        a=rng.randrange(-30,31)
        u=[rng.randrange(-160,161) for _ in range(2)]
        u.append(-8*a-sum(u))
        if not any(u):continue
        u=canonical(tuple(u))
        if sum(u)%8:continue
        result=reduce_core(u)
        expected=distance(primitive(physical(u))) is not None
        if result['immediate'] is not None:
            actual=result['immediate']
        else:
            actual=any(distance(primitive(physical(v))) is not None for v in result['targets'])
        assert actual==expected,(u,result,expected)
        for target in result['targets']:
            assert sector(target)=='collision'
        narrowed=cluster_reduction(result)
        actual=narrowed['immediate']
        if actual is None:
            actual=any(distance(primitive(physical(v))) is not None for v in narrowed['targets'])
        assert actual==expected
        for target in narrowed['targets']:
            assert sum(x%5==0 for x in target)==2
        counts['cluster_reductions']+=1
        counts['cores']+=1
        counts[sector(u)]+=1
        if biggest is None or len(result['targets'])>biggest['target_count']:
            biggest={'core':u,'target_count':len(result['targets']),'stats':result['stats']}
    for _ in range(180):
        x=[rng.randrange(-12,13) for _ in range(7)];x.append(-sum(x))
        expected=distance(primitive(tuple(x))) is not None
        for values in (x,[Fraction(-13,7)*v+Fraction(5,11) for v in x]):
            result=reduce_input(values)
            actual=result['immediate']
            if actual is None:
                actual=any(distance(primitive(physical(v))) is not None for v in result['targets'])
            assert actual==expected
            narrowed=cluster_reduction(result)
            actual=narrowed['immediate']
            if actual is None:
                actual=any(distance(primitive(physical(v))) is not None for v in narrowed['targets'])
            assert actual==expected
            assert all(sum(x%5==0 for x in v)==2 for v in narrowed['targets'])
            counts['full_inputs_and_affine_checks']+=1
    counts['oracle_states']=distance.cache_info().currsize
    return {'counts':dict(counts),'largest_exit_list':biggest}


def algebraic_checks():
    rng=Random(802510);count=0
    for _ in range(1500):
        i=rng.randrange(3)
        u=[rng.randrange(-300,301) for _ in range(3)]
        u[i]*=5
        q=u[i]//5
        v=tuple(-q if j==i else u[j]-q for j in range(3))
        assert energy_numerator(v)==energy_numerator(u)-160*q*q
        count+=1
    for L in (1,10,100,2000):
        u=(1,-1,0)
        for _ in range(L):
            u=(-5*u[0],u[1]-u[0],u[2]-u[0])
        assert gcd(*u)==1 and sum(u)%8==0 and sector(u)=='distinct'
        result=reduce_core(u)
        assert result['immediate'] is True
        assert result['stats']['singleton_steps']==L
        count+=1
    return {'checks':count,'long_spine_steps':2000,
            'long_spine_coordinate_bits':max(abs(x).bit_length() for x in u)}


def main():
    result={'scope':'Exact polynomial disjunctive reduction to seven-position clusters with two differences divisible by 5 and one unit. This does not decide the remaining cluster problems in polynomial time.',
            'residue_table':residue_table(),'independent':independent_cases(),
            'algebra':algebraic_checks()}
    path=Path(__file__).with_name('five_eight_residue_reduction_verification.json')
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
