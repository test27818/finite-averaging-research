"""Verify exact precision cylinders and formula-based six-step repairs.

No long-word search is performed. Optional probe records are only replayed.
"""
from collections import Counter
from fractions import Fraction as F
from math import gcd
from pathlib import Path
import argparse
import json
from verify_critical_endpoint_precision_return import primes, frozen_family_audit

HERE=Path(__file__).resolve().parent
RECORD=HERE/'padic_return_cylinders_verification.json'


def vp_int(x,p):
    if not x:
        return None
    v=0
    while x % p == 0:
        x//=p
        v+=1
    return v


def depth(x,p):
    denominator=x.denominator
    value=0
    while denominator>1:
        assert denominator % p == 0
        denominator//=p
        value+=1
    return value


def branches(p):
    for u in range(2,p):
        v=p+1-u
        inv=pow(u,-1,p)
        for k in range(1,u):
            l=v*k*inv % p
            q=k+l
            delta=u*l-v*k
            if not 1<=l<v or q>=p or not delta:
                continue
            for s in sorted({2,q}):
                yield u,v,k,l,s


def coefficients(p,u,v,k,l,s):
    q=k+l
    t=p+1-s
    h=(u*l-v*k)//p
    assert 0<abs(h)<p
    ea=p*k-u*(p-q)
    eb=p*l-v*(p-q)
    fa=s*p*u-t*ea
    fb=s*p*v-t*eb
    assert fb % p and fa % p
    assert u*fb-v*fa == -t*p*p*h
    assert ea*fb-eb*fa == -s*p**3*h
    assert vp_int(p*(ea*fb-eb*fa),p)==4
    return ea,eb,fa,fb


def actual_means(p,u,v,k,l,s,A,B):
    U,V,c=F(A,p),F(B,p),F(-A-B)
    q=k+l
    D=((p-u)*U+(p-v)*V+c)/p
    E=(k*U+l*V+(p-q)*D)/p
    Fout=((u-k)*U+(v-l)*V+(q-s)*D+(s-1)*E)/p
    return D,E,Fout


def cylinder_checks():
    count=0
    branch_count=0
    entrances=0
    sample=None
    for p in primes(43):
        if p<7:
            continue
        first={(-u*pow(p+1-u,-1,p*p))%(p*p) for u in range(2,p)}
        assert len(first)==p-2
        assert len({x%p for x in first})==p-2
        assert {x%p for x in first}==set(range(2,p))
        assert F(len(first),p*(p-1))==F(p-2,p*(p-1))
        entrances+=1
        for u,v,k,l,s in branches(p):
            branch_count+=1
            ea,eb,fa,fb=coefficients(p,u,v,k,l,s)
            modulus=p**8
            tau=(-fa*pow(fb,-1,modulus))%modulus
            assert tau%p==(-u*pow(v,-1,p))%p
            for A in (1,1+2*p):
                base=tau*A % modulus
                for nu in range(6):
                    unit=1 if (base+p**nu)%p else 2
                    B=base+unit*p**nu
                    assert A%p and B%p
                    L=fa*A+fb*B
                    assert vp_int(L,p)==nu
                    means=actual_means(p,u,v,k,l,s,A,B)
                    assert means==(F(-(u*A+v*B),p*p),F(ea*A+eb*B,p**3),F(L,p**4))
                    actual=max(1,*(depth(x,p) for x in means))
                    assert actual==max(1,4-nu)
                    assert (all(x.denominator==1 for x in means))==(nu>=4)
                    assert (actual<=1)==(nu>=3)
                    count+=1
                    if sample is None and nu==4:
                        sample={'p':p,'counts':[u,v,k,l,s],
                                'coefficients':[fa,fb],'slope_mod_p4':tau%(p**4)}
            means=actual_means(p,u,v,k,l,s,fb,-fa)
            assert all(x.denominator==1 for x in means) and means[-1]==0
            count+=1
    return {'branches':branch_count,'valuation_instances':count,
            'entrance_counts':entrances,'sample':sample}


def apply_histogram(state, selected, p):
    selected=Counter({x:m for x,m in selected.items() if m})
    assert sum(selected.values())==p
    assert all(m<=state[x] for x,m in selected.items())
    mean=sum(x*m for x,m in selected.items())/p
    before=sum(x*x*m for x,m in state.items())
    out=state.copy()
    out.subtract(selected)
    out[mean]+=p
    out=Counter({x:m for x,m in out.items() if m})
    assert sum(out.values())==2*p+1 and sum(x*m for x,m in out.items())==0
    assert sum(x*x*m for x,m in out.items())<before
    assert all(x.denominator in (1,p) for x in out)
    return out,mean


def six_step_formula(a, physical=False):
    p=6*a-1
    A,B=1-9*a,9*a-2
    U,V,D=F(A,p),F(B,p),F(1,p)
    negative=F(2-3*p)
    state=Counter({F(1):p+2,F(2):p-2,negative:1})
    groups=[{negative:1,F(1):3*a,F(2):3*a-2},
            {F(1):3*a,F(2):3*a-1},
            {U:3*a-1,V:3*a},
            {U:a,V:a-1,D:4*a-1,F(1):1},
            {U:a,V:a,D:a,F(0):3*a-1},
            {U:a,V:a,D:a,F(0):3*a-1}]
    expected=[U,V,D,F(0),F(0),F(0)]
    expanded=([F(1)]*(p+2)+[F(2)]*(p-2)+[negative]) if physical else None
    for index,group in enumerate(groups):
        state,mean=apply_histogram(state,group,p)
        assert mean==expected[index]
        if expanded is not None:
            used=set()
            for value,m in group.items():
                matches=[j for j,x in enumerate(expanded) if j not in used and x==value]
                assert len(matches)>=m
                used.update(matches[:m])
            assert len(used)==p
            actual=sum(expanded[j] for j in used)/p
            for j in used:
                expanded[j]=actual
            assert Counter(expanded)==state
        if index==3:
            assert state==Counter({U:2*a,V:2*a,D:2*a,F(0):p})
    assert state==Counter({F(0):2*p+1})
    if expanded is not None:
        assert not any(expanded)
    return p


def replay_probes():
    count=0
    descriptions=[]
    for path in sorted(HERE.glob('precision_return_p*_probe.json')):
        item=json.loads(path.read_text(encoding='utf-8'))
        if item['status']!='found':
            continue
        p=item['p']
        state=list(map(F,item['initial']))
        for selected in item['positions']:
            assert len(selected)==p and len(set(selected))==p
            mean=sum(state[i] for i in selected)/p
            for i in selected:
                state[i]=mean
            assert all(p%x.denominator==0 for x in state)
            assert sum(state)==0
        assert not any(state)
        count+=1
        descriptions.append([p,len(item['positions'])])
    return {'certificates':count,'p_and_lengths':descriptions,
            'scope':'Only stored positive paths are replayed; search exhaustion is not promoted to a theorem.'}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--write',action='store_true')
    args=parser.parse_args()
    cylinders=cylinder_checks()
    prime_examples=0
    for p in primes(499):
        if p%6==5:
            assert six_step_formula((p+1)//6,physical=(p<=47))==p
            prime_examples+=1
    extra_parameters=[2,4,6,10,10**20,10**50]
    for a in extra_parameters:
        six_step_formula(a)
    frozen=frozen_family_audit()
    frozen['status']='Finite diagnostic cross-check; the follow-up note independently proves exclusion for every odd prime.'
    result={'status':'PASS','precision_cylinders':cylinders,
            'frozen_five_step_finite_crosscheck':frozen,
            'six_step_formula':{'prime_examples':prime_examples,
                                'additional_integer_parameters':extra_parameters,
                                'scope':'Formula proof holds for all arities p=6a-1; prime assumption is used for the matching lower bound.'},
            'independent_positive_replays':replay_probes(),
            'scope':'General valuation formula, all-prime five-step obstruction and sharp six-step family are proved in the note. No all-input bounded-precision or full-band theorem.'}
    if args.write:
        RECORD.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    elif RECORD.exists():
        assert result==json.loads(RECORD.read_text(encoding='utf-8'))
    print(json.dumps(result,ensure_ascii=False))


if __name__=='__main__':
    main()
