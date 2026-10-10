"""Exact original-position checks for the symmetric four-step rebuild.

All selected parameters follow the written formulas. No macro or orbit search.
The output and frozen-document verification stay in this research directory.
"""
from fractions import Fraction as F
from pathlib import Path
import json

from verify_square_zero_compiler import check_frozen_files,check_local_links

HERE=Path(__file__).resolve().parent


def run_rebuild(p,t,s,b,u,v,close):
    assert p%2==1 and 1<=t<p and s%2 and b%2 and 1<=s<=t and 0<abs(b)<=s
    d=p*t-(p+t)*s
    values=[F(t*u+v)]*p+[F(t*u-v)]*p+[F(-p*u)]*(2*t)
    initial=values[:];n=len(values);operations=[]
    ga=list(range(p));gb=list(range(p,2*p));gc=list(range(2*p,n))
    def average(group):
        assert len(group)==p and len(set(group))==p
        mean=sum(values[i] for i in group)/p
        for i in group:values[i]=mean
        operations.append(tuple(group))
        assert sum(values)==0

    k=(p-s)//2
    first=ga[:k]+gb[:k]+gc[:s]
    second=ga[k:2*k]+gb[k:2*k]+gc[s:2*s]
    assert not set(first)&set(second)
    average(first);average(second)
    assert all(values[i]==F(d,p)*u for i in first+second)
    ga=ga[2*k:];gb=gb[2*k:];gc=gc[2*s:]
    fresh=first+second
    kept=fresh[:2*t];fresh=fresh[2*t:]
    ka=(s+b)//2;kb=(s-b)//2
    out_a=ga[:ka]+gb[:kb]+gc[:t-s]+fresh[:p-t]
    out_b=ga[ka:]+gb[kb:]+gc[t-s:]+fresh[p-t:]
    assert sorted(out_a+out_b+kept)==list(range(n))
    average(out_a);average(out_b)
    new_u=-F(d,p*p)*u;new_v=F(b,p)*v
    for indices,wanted in ((out_a,t*new_u+new_v),(out_b,t*new_u-new_v),(kept,-p*new_u)):
        assert all(values[i]==wanted for i in indices)
    if close:
        assert d%b==0
        c=-d//b
        assert c%2 and 0<abs(c)<=p
        j=(p+c)//2
        end_a=out_a[:j]+out_b[:p-j]
        end_b=out_a[j:]+out_b[p-j:]
        average(end_a);average(end_b)
        scalar=-F(d,p*p)
        assert all(values[i]==scalar*(t*u+v) for i in end_a)
        assert all(values[i]==scalar*(t*u-v) for i in end_b)
        assert all(values[i]==scalar*(-p*u) for i in kept)
    # Re-evaluate only literal averaging instructions, no parameter formulas.
    replay=initial[:]
    for group in operations:
        mean=sum(replay[i] for i in group)/p
        for i in group:replay[i]=mean
    assert replay==values
    return len(operations)


def main():
    if not __debug__:raise RuntimeError('Assertions required')
    rebuilds=cycles=cycle_parameters=atoms=0
    for p in (3,5,7,11,13,17,23,31,83):
        for t in range(1,p):
            # Formula checks include t divisible by4; no closure claimed there.
            for s in sorted({1,t if t%2 else t-1}):
                for b in sorted({-s,1,s}):
                    for u,v in ((F(1),F(0)),(F(0),F(1))):
                        atoms+=run_rebuild(p,t,s,b,u,v,False)
                        rebuilds+=1
            if t%2:
                s=b=t
            elif t%4==2:
                s=b=t//2
            else:
                continue
            cycle_parameters+=1
            for u,v in ((F(1),F(0)),(F(0),F(1)),(F(-7,3),F(11,5))):
                atoms+=run_rebuild(p,t,s,b,u,v,True)
                cycles+=1
    report={
        'status':'PASS',
        'four_step_rebuild_replays':rebuilds,
        'closed_cycle_parameter_pairs':cycle_parameters,
        'six_step_scalar_cycle_replays':cycles,
        'literal_atomic_steps_replayed':atoms,
        'unchanged_existing_documents':check_frozen_files(),
        'scope':'Exact original-position replay of the written four-step diagonal rebuild, and the six-step closure for t odd or t=2 mod4. The all-parameter proof is in the note. No roots, full termination, or t=0 mod4 closure is inferred.',
    }
    (HERE/'symmetric_rebuild_verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
