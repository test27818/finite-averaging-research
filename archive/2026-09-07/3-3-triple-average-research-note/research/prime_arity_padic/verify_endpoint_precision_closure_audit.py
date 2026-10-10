"""Exact audits of endpoint closure obstructions and positive repair witnesses."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from math import gcd
from pathlib import Path
import argparse
import json
import random
from probe_endpoint_bounded_precision import integral_selections,safe
from verify_critical_endpoint_precision_return import primes

HERE=Path(__file__).resolve().parent
SOURCES=HERE/'endpoint_precision_literature_20260930'
RECORD=HERE/'endpoint_precision_closure_audit_verification.json'


def next_state(state,group,p):
    assert len(group)==p and sum(group)%p==0
    hist=Counter(state)
    hist.subtract(Counter(group))
    assert all(c>=0 for c in hist.values())
    mean=sum(group)//p
    hist[mean]+=p
    return tuple(v for v,c in sorted(hist.items()) for _ in range(c))


def obstruction(state):
    g=gcd(*state)
    return 1 if not g else gcd(*(v-state[0] for v in state))//g


def selection_checks():
    rng=random.Random(30930)
    count=0
    for p in [2,3,5,7]:
        for _ in range(12 if p<7 else 4):
            state=tuple(sorted(rng.randint(-8,8) for _ in range(2*p+1)))
            expected={tuple(state[i] for i in ids) for ids in combinations(range(len(state)),p)
                      if sum(state[i] for i in ids)%p==0 and len({state[i] for i in ids})>1}
            actual={tuple(sorted(g)) for g in integral_selections(state,p)}
            assert actual==expected
            count+=1
    return count


def stagnation_family():
    out=[]
    for p in primes(499):
        if p%15!=7:
            continue
        r=(p-1)//2
        X=tuple(sorted([-p]*p+[p]*p+[0]))
        group=tuple([-p]*((p+1)//2)+[p]*((p-3)//2)+[0])
        Y=next_state(X,group,p)
        assert Y==tuple(sorted([-p]*r+[-2]*p+[p]*(r+2)))
        assert obstruction(Y)==1 and max(Counter(Y).values())==p
        groups=list(integral_selections(Y,p))
        assert len(groups)==2
        outcomes=[]
        for selected in groups:
            nxt=next_state(Y,selected,p)
            outcomes.append(obstruction(nxt))
            assert not safe(nxt,p)
        assert sorted(outcomes)==[3,5]
        out.append(p)
    return out


def greedy_counter():
    p=7
    X=tuple(sorted([63]*7+[-49]*7+[-98]))
    choices=[]
    initial_energy=sum(x*x for x in X)
    for group in integral_selections(X,p):
        nxt=next_state(X,group,p)
        choices.append((initial_energy-sum(x*x for x in nxt),tuple(sorted(group)),nxt))
    choices.sort(reverse=True)
    maximum=choices[0][0]
    best=[c for c in choices if c[0]==maximum]
    assert len(best)==1 and maximum==29834
    group=tuple(sorted([-98]+[63]*4+[-49]*2))
    assert best[0][1]==group
    Y=best[0][2]
    assert safe(Y,p)
    successors=[next_state(Y,g,p) for g in integral_selections(Y,p)]
    assert len(successors)==2
    assert sorted(obstruction(x) for x in successors)==[3,5]
    for k in range(7):
        g=[-98]+[63]*k+[-49]*(6-k)
        nxt=next_state(X,g,p)
        drop=initial_energy-sum(x*x for x in nxt)
        assert drop==-1792*k*k+14112*k+2058
    return {'p':p,'unique_max_drop_scaled':maximum,'first_group_scaled':group,
            'trap_G_values':[3,5],'second_best_drop_scaled':choices[1][0]}


def recurrence_checks():
    count=0
    for p in primes(43):
        if p<3:
            continue
        rho=F(1)-F(1,p)+F(1,p*p)
        for j in range(1,p+1):
            alpha=F(2*j-p-1,p)
            beta=F(j,p*p)
            assert abs(alpha)+beta<=1
            if j<p:
                assert abs(alpha)+beta<=rho<1
            for a,b in [(2,-3),(5,7),(F(1,p),F(2,p))]:
                c=-p*(a+b)
                new_a=-F((p+1-j)*a+j*b,p)
                assert new_a==alpha*a+beta*c
                count+=1
        # Both blocks fractional, with different p-adic first digits.
        A,B=1,2
        a,b=F(A,p),F(B,p)
        for j in range(1,p+1):
            new_a=-F((p+1-j)*a+j*b,p)
            new_b=F((p-j)*a+j*b,p)
            assert new_a.denominator>p or new_b.denominator>p
        for r in range(-p+2,p,2):
            k=(p+r)//2
            new_a=F(k*a+(p-k)*b,p)
            assert new_a.denominator==p*p
    return count


def vp(x,p):
    x=F(x)
    if not x:
        return 10**9
    a,b=x.numerator,x.denominator
    order=0
    while a%p==0:
        a//=p
        order+=1
    while b%p==0:
        b//=p
        order-=1
    return order


def padic_menu_checks():
    count=0
    for p in primes(43):
        if p<3:
            continue
        for a,b in [(1,2),(p,1),(1,p),(p,2*p),(F(1,p*p),F(p+1,p))]:
            x,y=F(a),F(a-b)
            initial=min(vp(x,p),vp(y,p))
            assert initial==min(vp(a,p),vp(b,p),vp(-p*(a+b),p))
            for j in range(1,p+1):
                xx=(-(p+1)*x+j*y)/p
                yy=(-(2*p+1)*x+2*j*y)/p
                after=min(vp(xx,p),vp(yy,p))
                assert after<=initial
                if j<p:
                    assert after==initial-1
                count+=1
            for r in range(-p,p+1,2):
                xx=x+F(r-p,2*p)*y
                yy=F(r,p)*y
                assert min(vp(xx,p),vp(yy,p))<=initial
                count+=1
    return count


def browkin_obstructions():
    count=0
    examples=[]
    for p in primes(97):
        if p<3:
            continue
        n=2*p+1
        ell=next(q for q in primes(n) if n%q==0)
        for e in (1,2,5):
            x=1+ell*p**e
            assert x%p==1
            initial=[x]*p+[x-1]*p+[-p*(2*x-1)]
            assert obstruction(initial)==1
            new_x,new_y=1,x-1
            output=[new_x]*p+[new_x-new_y]*p+[-p*(2*new_x-new_y)]
            assert obstruction(output)==gcd(new_y,n)>1
            count+=1
            if p==7 and e==1:
                examples.append({'p':p,'n':n,'input_column':[x,1],
                                 'formal_output':[1,x-1],'output_G':obstruction(output)})
    return {'cases':count,'examples':examples}


def replay_positive_probes():
    out=[]
    for path in sorted(SOURCES.glob('probe_*.json')):
        data=json.loads(path.read_text())
        if data.get('status')!='found':
            continue
        p,e=data['p'],data['precision']
        state=list(map(F,data['input']))
        for ids in data['positions']:
            assert len(ids)==p and len(set(ids))==p
            mean=sum(state[i] for i in ids)/p
            for i in ids:
                state[i]=mean
            assert all(p**e%x.denominator==0 for x in state)
            nums=tuple(int(p**e*x) for x in state)
            assert safe(nums,p)
        assert not any(state)
        out.append({'file':path.name,'p':p,'length':len(data['positions']),'precision':e})
    repair=next(x for x in out if x['file']=='probe_7_greedy_repaired.json')
    assert repair['length']==8
    return out


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--write',action='store_true')
    args=parser.parse_args()
    result={'status':'PASS','selection_generator_independent_cases':selection_checks(),
            'stagnation_family_primes':stagnation_family(),'unique_greedy_counter':greedy_counter(),
            'actual_carrier_recurrence_cases':recurrence_checks(),
            'padic_nondecreasing_precision_cases':padic_menu_checks(),
            'browkin_marking_obstruction':browkin_obstructions(),
            'positive_one_digit_replays':replay_positive_probes(),
            'scope':'General family and obstructions have written proofs. Positive probes are finite examples; no new full endpoint proof or all-input precision bound.'}
    if args.write:
        RECORD.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    elif RECORD.exists():
        assert result==json.loads(RECORD.read_text(encoding='utf-8'))
    print(json.dumps(result,ensure_ascii=False))


if __name__=='__main__':
    main()
