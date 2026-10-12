"""Exact audits of the unlimited-reachability reduction.

The independent oracle enumerates all integer averages, modulo permutation and
nonzero common scale. It has no depth bound, no G pruning, and does not call the
new gate criterion. General completeness of this oracle uses the previously
proved integrality lemma for prime p and n<2p, plus linearity under scaling.
Finite checks supplement, rather than establish, the all-input reduction proof.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
from math import gcd, isqrt
from pathlib import Path
from random import Random
import json


def is_prime(p):
    return p>=2 and all(p%d for d in range(2,isqrt(p)+1))


def next_prime(q):
    while not is_prime(q):q+=1
    return q


def primitive(x):
    d=gcd(*x)
    return tuple(sorted(v//d for v in x)) if d else tuple(x)


def difference_gcd(x):
    return gcd(*(v-x[0] for v in x))


def gate(p,r,values,target):
    assert is_prime(p) and p>=3 and 2<=r<p
    assert len(values)==p-2 and min(values)>=0 and target>0
    k=r-1
    z=tuple(p*p*v+1 for v in values)+(-p*p*target-k,)
    h=tuple(1+p*j for j in range(r))
    tau=-p*sum(z)-sum(h)
    x=tuple(p*v for v in z)+h+(tau,)
    assert len(x)==p+r and sum(x)==0 and all(x) and gcd(*x)==1
    return z,x


def encode_subset_sum(source,target,alpha=None):
    """Return a full many-one reduction with pairwise distinct input values."""
    assert len(source)>=2 and min(source)>0 and target>0
    m=len(source)
    if alpha is None:
        p=next_prime(2*m+7)
        r=(p-1)//2
    else:
        alpha=Fraction(alpha)
        assert 0<alpha<1
        threshold=max(Fraction(m+2)/alpha,Fraction(m+4)/(1-alpha))
        threshold=-(-threshold.numerator//threshold.denominator)
        p=next_prime(threshold)
        r=(alpha*p).numerator//(alpha*p).denominator
    k=r-1
    assert k>=m and p-r>=m+4
    C=1+sum(source)+target
    tags=[C*3**j for j in range(k)]
    encoded=[]
    choices=[]
    for j,t in enumerate(tags):
        no=len(encoded)
        encoded.append(t)
        if j<m:
            yes=len(encoded)
            encoded.append(t+source[j])
        else:
            yes=no
        choices.append((no,yes))
    B=sum(tags)+target
    F=B+max(encoded)+1
    values=encoded+[0]
    forbidden_count=p-2-len(values)
    assert forbidden_count>=2
    values+=list(range(F,F+forbidden_count))
    z,x=gate(p,r,values,B)
    assert len(set(values))==len(values) and len(set(x))==len(x)
    assert difference_gcd(x)==1 and sum(v<0 for v in x)==2
    return {'p':p,'r':r,'k':k,'values':values,'B':B,'z':z,'x':x,
            'choices':choices,'C':C,'tags':tags}


def retained_multisets(x,r):
    """Every positional complement, quotienting only equal-value symmetry."""
    items=tuple(sorted(Counter(x).items()))
    suffix=[0]*(len(items)+1)
    for j in range(len(items)-1,-1,-1):suffix[j]=suffix[j+1]+items[j][1]
    def rec(j,left,prefix):
        if left==0:
            yield prefix
            return
        if j==len(items) or suffix[j]<left:return
        v,count=items[j]
        for t in range(max(0,left-suffix[j+1]),min(count,left)+1):
            yield from rec(j+1,left-t,prefix+(v,)*t)
    yield from rec(0,r,())


def integer_oracle(p,n):
    @lru_cache(None)
    def children(x):
        assert len(x)==n and sum(x)==0
        out=set()
        for retained in retained_multisets(x,n-p):
            total=-sum(retained)
            if total%p:continue
            raw=tuple(sorted((total//p,)*p+retained))
            if raw==x:continue
            y=primitive(raw)
            assert sum(v*v for v in y)<sum(v*v for v in x)
            out.add(y)
        return tuple(sorted(out))

    @lru_cache(None)
    def distance(x):
        if not any(x):return 0
        ds=[distance(y) for y in children(x)]
        ds=[d for d in ds if d is not None]
        return 1+min(ds) if ds else None
    return children,distance


def residue_checks():
    count=0
    for p in range(3,102,2):
        if not is_prime(p):continue
        for r in range(2,p):
            first={(j,e) for j in range(r+1) for e in (0,1) if (j-r*e)%p==0}
            assert first=={(0,0),(r,1)}
            k=r-1
            second={(j,e) for j in range(k+1) for e in (0,1) if (j-k*e)%p==0}
            assert second=={(0,0),(k,1)}
            assert all((t*r)%p for t in range(1,r+1))
            count+=1
    return count


def small_gate_checks():
    rng=Random(20261011)
    instances=[]
    for p in (3,5):
        for values in product(range(3),repeat=p-2):
            for target in range(1,5):
                for r in range(2,p):instances.append((p,r,values,target))
    for r in range(2,7):
        for _ in range(12):
            instances.append((7,r,tuple(rng.randrange(6) for _ in range(5)),rng.randrange(1,16)))
    oracles={}
    counts=Counter()
    for p,r,values,target in instances:
        if (p,r) not in oracles:oracles[p,r]=integer_oracle(p,p+r)
        children,distance=oracles[p,r]
        z,x=gate(p,r,values,target)
        truth=any(sum(values[i] for i in inds)==target for inds in combinations(range(p-2),r-1))
        d=distance(primitive(x))
        assert d==(2 if truth else None),(p,r,values,target,d,truth)
        predicted=set()
        for inds in combinations(range(p-1),r):
            s=sum(z[i] for i in inds)
            y=primitive((-s,)*p+tuple(p*z[i] for i in inds))
            predicted.add(y)
            assert distance(y)==(1 if s==0 else None)
            counts['first_complements']+=1
        assert set(children(primitive(x)))==predicted
        counts['instances']+=1
        counts['yes' if truth else 'no']+=1
    counts['oracle_states']=sum(d.cache_info().currsize for _,d in oracles.values())
    return dict(counts)


def source_truth(source,target):
    return any(sum(source[j] for j in range(len(source)) if mask>>j&1)==target
               for mask in range(1<<len(source)))


def distinct_full_oracles():
    rows=[]
    examples=[([1,3],2),([1,3],3),([2,4],6),([1,2,5],4),([1,2,5],7)]
    for source,target in examples:
        e=encode_subset_sum(source,target)
        p,r,x=e['p'],e['r'],e['x']
        truth=source_truth(source,target)
        codedtruth=any(sum(e['values'][i] for i in inds)==e['B']
                       for inds in combinations(range(p-2),r-1))
        assert codedtruth==truth
        children,distance=integer_oracle(p,p+r)
        assert distance(primitive(x))==(2 if truth else None)
        for inds in combinations(range(p-1),r):
            s=sum(e['z'][i] for i in inds)
            y=primitive((-s,)*p+tuple(p*e['z'][i] for i in inds))
            assert distance(y)==(1 if s==0 else None)
        # Positional first-step enumeration, independent of the gate formula.
        valid=0
        mandatory=set(range(p-1,p+r))
        for retained in combinations(range(p+r),r):
            if sum(x[i] for i in retained)%p:continue
            selected=set(range(p+r))-set(retained)
            assert mandatory.issubset(selected)
            valid+=1
        assert valid==sum(1 for _ in combinations(range(p-1),r))
        rows.append({'source':source,'target':target,'p':p,'n':p+r,'r':r,
                     'answer':truth,'max_input_bits':max(abs(v).bit_length() for v in x),
                     'distinct_values':len(set(x)),'valid_first_groups':valid,
                     'oracle_states':distance.cache_info().currsize})
    return rows


def alpha_encoding_checks():
    rows=[]
    for alpha in (Fraction(1,3),Fraction(1,2),Fraction(2,3)):
        for source,target in [([1,3],2),([1,3],3)]:
            e=encode_subset_sum(source,target,alpha)
            truth=source_truth(source,target)
            codedtruth=any(sum(e['values'][i] for i in inds)==e['B']
                           for inds in combinations(range(e['p']-2),e['k']))
            assert codedtruth==truth
            rows.append({'alpha':str(alpha),'source':source,'target':target,
                         'p':e['p'],'n':e['p']+e['r'],'answer':truth})
    return rows


def replay_witness(e,chosen_source,shift=0):
    p,r=e['p'],e['r']
    I=[e['choices'][j][int(j in chosen_source)] for j in range(e['k'])]
    assert len(set(I))==e['k'] and sum(e['values'][j] for j in I)==e['B']
    J=tuple(I+[p-2])
    x=[v+shift for v in e['x']]
    S=tuple(j for j in range(p+r) if j not in set(J))
    S2=J+S[:p-r]
    for group in (S,S2):
        assert len(group)==len(set(group))==p
        total=sum(x[j] for j in group)
        assert total%p==0 and total//p==shift
        for j in group:x[j]=total//p
    assert x==[shift]*(p+r)
    return 2


def large_witnesses():
    rng=Random(101126)
    rows=[]
    for m,bits in ((2,32),(6,128),(32,256),(64,512)):
        source=[rng.getrandbits(bits)+1 for _ in range(m)]
        chosen=set(range(0,m,2))
        target=sum(source[j] for j in chosen)
        e=encode_subset_sum(source,target)
        replay_witness(e,chosen)
        shift=1-min(e['x'])
        assert min(v+shift for v in e['x'])==1
        replay_witness(e,chosen,shift)
        rows.append({'source_count':m,'source_bits':bits,'p':e['p'],
                     'n':e['p']+e['r'],'output_max_bits':max(abs(v).bit_length() for v in e['x']),
                     'raw_and_positive_shift_certificates':True})
    return rows


def main():
    result={'scope':'Exact finite implementation checks. The unlimited-path exclusion and polynomial reduction are proved in the accompanying note; no fixed-p hardness is claimed.',
            'residue_parameter_pairs':residue_checks(),
            'small_gate_checks':small_gate_checks(),
            'distinct_input_complete_oracles':distinct_full_oracles(),
            'alpha_encoding_checks':alpha_encoding_checks(),
            'large_positive_certificates':large_witnesses()}
    path=Path(__file__).with_name('subcritical_uniform_np_hard_verification.json')
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'residue_parameter_pairs':result['residue_parameter_pairs'],
                      'small_gate_checks':result['small_gate_checks'],
                      'distinct_oracle_cases':len(result['distinct_input_complete_oracles']),
                      'distinct_oracle_states':sum(x['oracle_states'] for x in result['distinct_input_complete_oracles']),
                      'alpha_checks':len(result['alpha_encoding_checks']),
                      'large_witness_cases':len(result['large_positive_certificates']),
                      'record':str(path)},ensure_ascii=False,indent=2))


if __name__=='__main__':main()
