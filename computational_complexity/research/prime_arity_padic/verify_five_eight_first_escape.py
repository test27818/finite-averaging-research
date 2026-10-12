"""Independent literal search for the outside-interaction subproblem."""
from functools import lru_cache
from itertools import combinations
from math import gcd
from random import Random
from pathlib import Path
import json
from five_eight_first_escape import FirstEscape,primitive,depth,deep_escape,follow,step,EXTERNAL
from verify_subcritical_uniform_np_hard import integer_oracle,primitive as full_primitive
from fixed_p_plus_three_solver import Solver,canonical


def good(values):
    g=gcd(*values)
    return not g or gcd(*(x-values[0] for x in values))==g


def literal_apply(values,inds):
    selected=[values[i] for i in inds]
    if len(set(selected))==1 or sum(selected)%5:return None
    avg=sum(selected)//5;out=list(values)
    for i in inds:out[i]=avg
    if not good(out):return None
    return tuple(out)


@lru_cache(None)
def outside_oracle(local,outside):
    values=local+(outside,)
    for inds in combinations(range(7),4):
        if literal_apply(values,inds+(7,)) is not None:return True
    for inds in combinations(range(7),5):
        child=literal_apply(values,inds)
        if child is None:continue
        if outside_oracle(tuple(sorted(child[:7])),outside):return True
    return False


def replay(state,word):
    a,b,c,d=state
    values=(a,)*5+(b,c,d)
    for pos,letter in enumerate(word):
        if letter=='S1':inds=(0,1,2,3,5)
        elif letter=='S2':inds=(0,1,2,3,6)
        elif letter=='D':inds=(0,1,2,5,6)
        elif letter=='E0':inds=(0,1,2,3,7)
        elif letter=='E1':inds=(0,1,2,5,7)
        elif letter=='E2':inds=(0,1,2,6,7)
        elif letter=='E12':inds=(0,1,5,6,7)
        else:raise AssertionError(letter)
        out=literal_apply(values,inds)
        assert out is not None
        assert (7 in inds)==(pos==len(word)-1)
        if letter=='S1':rest=(4,6,7)
        elif letter=='S2':rest=(5,4,7)
        elif letter=='D':rest=(3,4,7)
        else:rest=tuple(i for i in range(8) if i not in inds)
        values=(out[inds[0]],)*5+tuple(out[i] for i in rest)
    return len(word)


def small_comparison():
    rng=Random(581017);cases=atoms=no=0;max_nodes=0
    _,full_oracle=integer_oracle(5,8)
    solver=Solver(5,filter_first_escape=True)
    for _ in range(900):
        a=rng.choice([i for i in range(-9,10) if i%5])
        s,t=rng.randrange(-35,36),rng.randrange(-35,36)
        state=primitive((a,a+5*s,a+5*t,-7*a-5*s-5*t))
        a,b,c,d=state
        if not good((a,)*5+(b,c,d)):continue
        result=FirstEscape().decide(state)
        expected=outside_oracle(tuple(sorted((a,)*5+(b,c))),d)
        assert result['possible']==expected,(state,result,expected)
        full_answer=full_oracle(full_primitive((a,)*5+(b,c,d)))
        assert solver.solve_input((a,)*5+(b,c,d))==full_answer
        if not expected:assert full_answer is None
        if expected:atoms+=replay(state,result['word'])
        else:no+=1
        max_nodes=max(max_nodes,result['stats'].get('visited_nodes',0))
        cases+=1
    return {'cases':cases,'no_first_escape':no,'replayed_atoms':atoms,
            'oracle_states':outside_oracle.cache_info().currsize,'largest_search_nodes':max_nodes,
            'full_oracle_states':full_oracle.cache_info().currsize,
            'integrated_solver_stats':dict(solver.stats)}


def deep_checks():
    rng=Random(5100811);cases=atoms=0;rows=[]
    for e in (8,9,10,17,50,100):
        for _ in range(24):
            a=rng.choice([i for i in range(-50,51) if i%5])
            s,t=rng.randrange(-60,61),rng.randrange(-60,61)
            if s%5==0 and t%5==0:continue
            state=primitive((a,a+5**e*s,a+5**e*t,-7*a-5**e*(s+t)))
            a,b,c,d=state
            if not good((a,)*5+(b,c,d)):continue
            assert depth(state)>=8
            word=deep_escape(state)
            atoms+=replay(state,word);cases+=1
    for L in (6,7,8,30,300,1000):
        state=(-1,-1+5**L,-1+5**L,7-2*5**L)
        word=deep_escape(state);atoms+=replay(state,word)
        assert len(word)==L+1
        rows.append({'depth':L,'atoms':len(word),'height_bits':(2*5**L-7).bit_length()})
    return {'arbitrary_deep_clusters':cases,'replayed_atoms':atoms,'large_duplicate_examples':rows}


def arbitrary_outside_checks():
    rng=Random(580125);counts={'cases':0,'outside_divisible_by_5':0,'replayed_atoms':0}
    for _ in range(450):
        a,b,c=[rng.randrange(-25,26) for _ in range(3)]
        state=primitive((a,b,c,-5*a-b-c))
        a,b,c,d=state
        if not d or not good((a,)*5+(b,c,d)):continue
        result=FirstEscape().decide(state)
        expected=outside_oracle(tuple(sorted((a,)*5+(b,c))),d)
        assert result['possible']==expected,(state,result,expected)
        counts['cases']+=1
        counts['outside_divisible_by_5']+=d%5==0
        if expected:counts['replayed_atoms']+=replay(state,result['word'])
    return counts


def counterexample():
    state=(3,8,8,-31)
    first=FirstEscape().decide(state)
    assert first['possible']
    assert first['word']==('S1','E0')
    replay(state,first['word'])
    _,distance=integer_oracle(5,8)
    assert distance(full_primitive((3,)*5+(8,8,-31))) is None
    assert distance(full_primitive((-3,)*5+(4,3,8))) is None
    return {'state':state,'outside_word':first['word'],'full_reachability':False,
            'independent_full_oracle_states':distance.cache_info().currsize}


def long_spine():
    N=1000;x=5**N;state=(1,1+x,16,-22-x)
    result=FirstEscape().decide(state)
    assert result['possible']
    assert replay(state,result['word'])==N+1
    assert result['stats']['spine_steps']==N-1
    return {'input_exponent':N,'word_length':N+1,'stats':result['stats']}


def representative_counterexample():
    a=-12;L=6;U=5**L
    state=(a,a+U,a+U,-7*a-2*U)
    targets=set()
    for s in range(L//2+1):
        prefix=('S1','D')*s+('S1',)*(L-2*s)
        landed=follow(state,prefix)
        assert landed is not None
        for letter in EXTERNAL:
            child=step(landed,letter)
            if child is not None:
                targets.add(canonical(tuple(x-child[0] for x in child[1:])))
    expected={(-7481,-7481,-7478),(-7169,-7169,-5606),(-7307,-7127,-7118)}
    assert targets==expected
    edges,distance=integer_oracle(5,8)
    source=full_primitive((a,)*5+(a+U,a+U,-7*a-2*U))
    assert distance(source)==17
    for u in targets:
        mean=-sum(u)//8
        assert distance(full_primitive((mean,)*5+tuple(mean+x for x in u))) is None
    # Recover and replay an actual unscaled integer witness, not just the
    # primitive representatives used by the independent full-state oracle.
    current=source;raw=source;path=[raw];choices=[]
    while distance(current):
        wanted=next(y for y in edges(current)
                    if distance(y) is not None and distance(y)==distance(current)-1)
        for inds in combinations(range(8),5):
            candidate=literal_apply(raw,inds)
            if candidate is not None and full_primitive(candidate)==wanted:
                raw=tuple(sorted(candidate));choices.append(inds);path.append(raw);break
        else:raise AssertionError('literal witness recovery failed')
        current=wanted
    assert len(choices)==17 and not any(raw)
    return {'source':state,'full_distance':17,'all_template_targets':sorted(targets),
            'all_template_targets_unsolvable':True,
            'independent_full_oracle_states':distance.cache_info().currsize,
            'literal_success_choices':choices,'literal_success_path':path}


def main():
    result={'scope':'Polynomial first nonidentity outside interaction with integer and primitive G=1 prefixes. This is strictly weaker than full consensus reachability.',
            'small':small_comparison(),'arbitrary_outside':arbitrary_outside_checks(),
            'deep':deep_checks(),'long_spine':long_spine(),
            'strictness':counterexample(),'representative_counterexample':representative_counterexample()}
    path=Path(__file__).with_name('five_eight_first_escape_verification.json')
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    display={k:v for k,v in result.items() if k!='representative_counterexample'}
    display['representative_counterexample']={k:v for k,v in result['representative_counterexample'].items()
                                            if not k.startswith('literal_')}
    print(json.dumps(display,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
