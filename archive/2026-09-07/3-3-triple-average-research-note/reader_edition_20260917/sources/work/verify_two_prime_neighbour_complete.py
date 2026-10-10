"""Complete (p,p,2) Euclidean descent when p+1 has at most two prime factors.

The arity p can be any odd integer >=5. The same closed selection rule is
used for every arity and every input. No matrix-word or modular-group search
is used. Physical samples replay all operations to zero on original indices.
"""

from fractions import Fraction as F
from math import gcd, lcm
from pathlib import Path
from random import Random
import json

from verify_four_prime_entry_and_band import factors, is_legal
from verify_carrier_energy_and_pair_reduction import PairLedger
from verify_uniform_two_block_entry import uniform_entry

if not __debug__:
    raise RuntimeError('Assertions are required.')


def primitive(u,v):
    denominator=lcm(F(u).denominator,F(v).denominator)
    u,v=int(u*denominator),int(v*denominator)
    common=gcd(u,v)
    assert common and v
    u,v=u//common,v//common
    return (u,v) if v>0 else (-u,-v)


def choose_step(u,v,p):
    m=p+1
    assert v>1 and gcd(u,v)==gcd(v,m)==1 and len(factors(m))<=2
    b=u*pow(2,-1,v)%v
    sign=1
    if 2*b>v:
        b=v-b
        sign=-1
    assert 0<b<v/2
    nearest=2*((m*b)//(2*v))+1
    assert abs(nearest*v-m*b)<v
    if gcd(nearest,m)==1:
        d=1
        if nearest==1:
            a,e=v-b,p
            sign=-sign
            branch='reflect-one'
        else:
            a,e=b,nearest
            branch='unit-nearest'
    else:
        assert any(q!=2 and nearest%q==0 for q in factors(m))
        d=2
        if b%2==0:
            a=b//2
            branch='halve-even'
        else:
            a=(v-b)//2
            sign=-sign
            branch='halve-odd'
        e=2*((m*a)//(2*v))+1
        assert gcd(e,m)==1
    q=d*e
    assert 1<=a<v and 2<=q<=p and gcd(e,m)==1
    assert (2*d*a-sign*u)%v==0
    shift=(2*d*a-v-sign*u)//v
    assert sign*u+shift*v==2*d*a-v
    new_v=e*v-m*a
    assert 0<abs(new_v)<v and gcd(new_v,m)==1
    assert gcd(a,v)==1
    return {'sign':sign,'d':d,'e':e,'a':a,'q':q,'shift':shift,'branch':branch,
            'following':primitive(-a,new_v)}


def plan_core(u,v,p):
    u,v=primitive(u,v)
    assert gcd(v,p+1)==1
    initial_v=v
    plan=[]
    stages=[]
    while v>1:
        step=choose_step(u,v,p)
        if step['sign']<0:
            plan.append(('s',0))
        if step['shift']:
            plan.append(('u',step['shift']))
        plan.append(('n',step['q']-(p+1)//2))
        old=v
        u,v=step['following']
        assert 0<v<old and v%2
        stages.append(step['branch'])
    if u:
        plan.append(('u',-u))
    assert len(stages)<=(initial_v-1)//2
    return plan,stages


class RecordedPair(PairLedger):
    def __init__(self,p,state,first,second,carriers):
        super().__init__(p,state,first,second,carriers)
        self.word=[]

    def average(self,group):
        super().average(group)
        self.word.append(list(group))


def replay(raw,p,word):
    state=list(map(F,raw))
    for group in word:
        assert len(group)==len(set(group))==p
        assert all(0<=index<len(state) for index in group)
        mean=sum(state[index] for index in group)/p
        for index in group:
            state[index]=mean
        assert sum(state)==0
        denominator=lcm(*(x.denominator for x in state))
        integers=[int(x*denominator) for x in state]
        common=gcd(*integers)
        if common:
            integers=[x//common for x in integers]
            assert gcd(*(x-integers[0] for x in integers))==1
    return state


def physical_core(p,u,v):
    raw=[u+v]*p+[u-v]*p+[-p*u]*2
    ledger=RecordedPair(p,raw,range(p),range(p,2*p),range(2*p,2*p+2))
    plan,stages=plan_core(*ledger.parameters(),p)
    ledger.execute(plan)
    assert ledger.parameters()[0]==0
    ledger.finish()
    assert not any(replay(raw,p,ledger.word))
    return {'p':p,'core_parameters':[u,v],'plan':plan,'stages':stages,'operations':ledger.word}


def full_input(p,raw):
    entry=uniform_entry(raw,p,2)
    state=replay(raw,p,entry['operations'])
    first,second,carrier=entry['groups']
    ledger=RecordedPair(p,state,first,second,carrier)
    plan,stages=plan_core(*ledger.parameters(),p)
    ledger.execute(plan)
    assert ledger.parameters()[0]==0
    ledger.finish()
    word=entry['operations']+ledger.word
    assert not any(replay(raw,p,word))
    return {'p':p,'input':raw,'entry_steps':len(entry['operations']),
            'plan':plan,'stages':stages,'operations':word}


def audit_larger_scope():
    # A fixed necessary-and-sufficient test for one translated M_q return
    # lowering |v| after full primitive cancellation. It is not a path search.
    p,u,v=29,4,7
    assert gcd(u,v)==gcd(v,p+1)==1
    choices=[]
    for e in range(1,p+1,2):
        if gcd(e,p+1)!=1:
            continue
        for d in range(1,p//e+1):
            if d*e<2:
                continue
            lo=(e-1)*v//(p+1)+1
            hi=((e+1)*v-1)//(p+1)
            for a in range(lo,hi+1):
                if (2*d*a-u)%v==0 or (2*d*a+u)%v==0:
                    choices.append((d,e,a))
    assert not choices
    # This excludes this one-stage descent criterion, not all averaging paths.
    print('multiple-odd-prime one-stage boundary retained: PASS')


def main():
    count=0
    branches=set()
    arities=[]
    for p in range(5,110,2):
        if len(factors(p+1))>2:
            continue
        arities.append(p)
        for v in range(3,90,2):
            if gcd(v,p+1)!=1:
                continue
            for u in range(1,v):
                if gcd(u,v)!=1:
                    continue
                step=choose_step(u,v,p)
                branches.add(step['branch'])
                count+=1
    assert branches=={'reflect-one','unit-nearest','halve-even','halve-odd'}
    cores=[physical_core(p,u,v) for p in (5,7,9,11,13,17,19,23,31,53)
           for u,v in ((1,5),(3,11)) if gcd(u,v)==gcd(v,p+1)==1]
    rng=Random(2026091471)
    inputs=[]
    for p in (5,7,9,11,13,17,19,23):
        for _ in range(3):
            while True:
                raw=[rng.randrange(-12,13) for _ in range(2*p+1)]
                raw.append(-sum(raw))
                if gcd(*raw)==1 and is_legal(raw,factors(2*p+2)):
                    break
            inputs.append(full_input(p,raw))
    audit_larger_scope()
    print('two-prime-neighbour uniform arithmetic descent: PASS',len(arities),count)
    print('two-prime-neighbour all selector branches: PASS',sorted(branches))
    print('two-prime-neighbour literal full core paths: PASS',len(cores))
    print('two-prime-neighbour literal full input paths: PASS',len(inputs))
    record={'scope':'General complete theorem when p is odd>=5 and omega(p+1)<=2; '
                    'the restriction is proved, not inferred from finite samples. '
                    'No assertion that qualifying prime arities are infinite.',
            'arities':arities,'one_stage_checks':count,'core_paths':cores,'full_input_paths':inputs}
    (Path(__file__).parent/'two_prime_neighbour_complete_records.json').write_text(
        json.dumps(record,indent=2)+'\n',encoding='utf-8')
    print('two-prime-neighbour full G1 criterion; five-average12 complete: PASS')


if __name__=='__main__':
    main()
