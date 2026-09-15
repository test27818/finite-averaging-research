"""Exact original-position replay of the all-even-carrier inverse rule.

Uses only the written two-choice formula, never searches for a periodic word.
Both basis inputs and a mixed rational input are checked. Existing proof files
are read only through their frozen-content snapshot.
"""
from fractions import Fraction as F
from math import gcd,isqrt
from pathlib import Path
import json

from verify_square_zero_compiler import check_frozen_files,check_local_links

HERE=Path(__file__).resolve().parent


def prime(p):
    return p>=2 and all(p%d for d in range(2,isqrt(p)+1))


def parameters(p,t):
    s=t if t%2 else t//2
    alpha=int(s%2==0)
    d=p*t-(p+t)*s
    assert d%s==0
    c=d//s
    scalar=F(d*d+alpha*alpha*c*(p+t),p**4)
    assert c%2 and 0<abs(c)<p
    assert scalar and gcd(scalar.numerator,2*(p+t))==1
    return s,alpha,d,c,scalar


def replay(p,t,u,v):
    s,alpha,d,c,scalar=parameters(p,t)
    n=2*p+2*t
    values=[F(t*u+v)]*p+[F(t*u-v)]*p+[F(-p*u)]*(2*t)
    initial=values[:];words=[]
    groups=(list(range(p)),list(range(p,2*p)),list(range(2*p,n)))
    def average(indices):
        assert len(indices)==p and len(set(indices))==p
        mean=sum(values[i] for i in indices)/p
        for i in indices:values[i]=mean
        assert sum(values)==0
        words.append(tuple(indices))
    def mix(groups):
        ga,gb,gc=groups;j=(p+c)//2
        a=ga[:j]+gb[:p-j];b=ga[j:]+gb[p-j:]
        average(a);average(b)
        return a,b,gc
    def rebuild(groups):
        ga,gb,gc=groups
        i=(p-s+alpha)//2;j=(p-s-alpha)//2
        first=ga[:i]+gb[:j]+gc[:s]
        second=ga[i:2*i]+gb[j:2*j]+gc[s:2*s]
        average(first);average(second)
        ga=ga[2*i:];gb=gb[2*j:];gc=gc[2*s:]
        fresh=first+second;kept=fresh[:2*t];fresh=fresh[2*t:]
        x=s-alpha;z=t-s+alpha;w=p-t
        left=ga[:x]+gc[:z]+fresh[:w]
        right=ga[x:]+gb+gc[z:]+fresh[w:]
        assert sorted(left+right+kept)==list(range(n))
        average(left);average(right)
        return left,right,kept
    for stage in (1,2):
        groups=rebuild(mix(groups))
        if stage==1:
            uu=F(-d*u,p*p)-F(alpha*c*v,p**3)
            vv=-F(alpha*(p+t)*u,p)+F(d*v,p*p)
        else:
            uu=scalar*u;vv=scalar*v
        for indices,wanted in zip(groups,(t*uu+vv,t*uu-vv,-p*uu)):
            assert all(values[i]==wanted for i in indices),(p,t,stage,indices,wanted)
    independent=initial[:]
    for indices in words:
        mean=sum(independent[i] for i in indices)/p
        for i in indices:independent[i]=mean
    assert independent==values and len(words)==12
    return 12


def general_normal_form_checks():
    count=0
    # Formula-selected legal cases at the new boundary t=p-1.
    for p in (5,7,11,13,17,29,83):
        t=p-1;s=p-2;alpha=2
        d=-p*p+4*p-2;C=2*(p-1)*(2*p-1)
        lam=d*d-2*C
        assert lam==p*(p**3-8*p*p+12*p-4)
        assert gcd(lam,4*p-2)==1
        assert lam!=0
        # The first p-average count is(2,0,p-2); output is(1,p-1,0,0).
        x,y,z,w=1,p-1,0,0
        assert p*(x-y)+alpha*(w+t)==d
        lower=p*t*(x+y)-p*p*z+(w+t)*d
        assert lower==C
        m=2*p-1
        assert (-m*d+C+p*p*m)%(2*m)==0
        assert (-m*alpha+d+p*p)%(2*m)==0
        count+=1
    return count


def main():
    if not __debug__:raise RuntimeError('Assertions required')
    pairs=cycles=atoms=div4=0
    for p in [p for p in range(3,102,2) if prime(p)]:
        for t in range(1,p):
            pairs+=1;div4+=t%4==0
            for u,v in ((F(1),F(0)),(F(0),F(1)),(F(-7,3),F(11,5))):
                atoms+=replay(p,t,u,v);cycles+=1
    report={
        'status':'PASS',
        'formula_parameter_pairs':pairs,
        'previously_missing_four_divides_t_pairs':div4,
        'twelve_atom_scalar_cycles':cycles,
        'literal_atomic_steps_replayed':atoms,
        'boundary_normal_forms':general_normal_form_checks(),
        'unchanged_existing_documents':check_frozen_files(),
        'scope':'Exact formula-selected literal replays for all odd primes below102 and all1<=t<p. General all-prime inverse theorem is proved in text, not inferred from tests. No new complete-dimension claim and no root/terminal completeness asserted.',
    }
    (HERE/'uniform_even_carrier_inverse_verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
