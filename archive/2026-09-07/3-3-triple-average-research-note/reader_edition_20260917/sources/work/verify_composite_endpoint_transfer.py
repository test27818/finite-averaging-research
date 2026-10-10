"""Independent verification of finite composite endpoint CRT certificates.

Does not import the builder, transversal BFS, or pivot search. The matrix list,
all edge choices and prescribed pivots are treated as untrusted certificate
data. General two-prime entry is checked separately on labelled positions.
"""

from collections import Counter
from fractions import Fraction as F
from math import gcd,prod
from pathlib import Path
from random import Random
import json

from verify_prime_power_endpoint_completion import Compiler
from verify_uniform_endpoint_controller import Replay

I=(1,0,0,1)
GENERATORS=((0,-1,1,0),(1,1,0,1),(1,-1,0,1))


def factors(n):
    result,p={},2
    while p*p<=n:
        while n%p==0:
            result[p]=result.get(p,0)+1
            n//=p
        p+=1
    if n>1:
        result[n]=result.get(n,0)+1
    return result


def mm(a,b):
    return (a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],
            a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3])


def inverse(a):
    assert a[0]*a[3]-a[1]*a[2]==1
    return a[3],-a[1],-a[2],a[0]


def signature(c,d,primepowers):
    out=[]
    for ell,m in primepowers:
        if c%ell:
            out.append(('unit-c',d*pow(c,-1,m)%m))
        else:
            assert d%ell
            out.append(('unit-d',c*pow(d,-1,m)%m))
    return tuple(out)


def supported_unit(value,n,p):
    value=F(value)
    if not value:
        return False
    for number in (abs(value.numerator),value.denominator):
        if gcd(number,n)>1 or any(ell>p for ell in factors(number)):
            return False
    return True


def exact_decomposition(matrix,mode,t,n,p):
    a,b,c,d=map(F,matrix)
    assert a*d-b*c==1 and c%n==0
    if mode=='d':
        assert t==0 and supported_unit(d,n,p)
        factors3=((1,b/d,0,1),(1/d,0,0,d),(1,0,c/d,1))
        assert (c/d/n).denominator>0 and supported_unit((c/d/n).denominator,n,p)
        assert mm(mm(*factors3[:2]),factors3[2])==(a,b,c,d)
        return
    assert mode in ('a','shear')
    if mode=='a':
        assert t==0
    else:
        assert t and supported_unit(t.denominator,n,p)
    u,v=a+t*c,b+t*d
    assert supported_unit(u,n,p)
    factors3=((1,0,c/u,1),(u,0,0,1/u),(1,v/u,0,1))
    adjusted=mm(mm(*factors3[:2]),factors3[2])
    assert adjusted==mm((1,t,0,1),matrix)
    assert mm((1,-t,0,1),adjusted)==(a,b,c,d)


class PhysicalCompiler(Compiler):
    def selected_pivot(self,matrix,mode,t):
        a,b,c,d=map(F,matrix)
        program=self.program
        if mode=='d':
            result=program.mul(self.upper(b/d),self.diagonal(d*d),self.lower(c/d))
        else:
            adjusted=mm((1,t,0,1),matrix)
            result=program.mul(self.upper(-t),self.gauss(adjusted))
        program.check(result,matrix)
        assert result.back is not None


def replay(raw,word,p,consensus=False):
    values=list(map(F,raw))
    target=sum(values)/len(values)
    for atom in word:
        assert len(atom)==len(set(atom))==p
        assert all(type(i) is int and 0<=i<len(values) for i in atom)
        mean=sum(values[i] for i in atom)/p
        for i in atom:
            values[i]=mean
    if consensus:
        assert values==[target]*len(values)
    return values


def residue(x,ell):
    x=F(x)
    return x.numerator*pow(x.denominator,-1,ell)%ell


def finish_entry(raw,p,first):
    n=len(raw)
    assert n==2*p+1 and sum(raw)==0
    primes=tuple(factors(n))
    assert 1<=len(primes)<=2
    word=[first[:]]
    values=replay(raw,word,p)
    block=first[:]
    singles=[i for i in range(n) if i not in block]
    assert all(len({residue(values[i],ell) for i in singles})>1 for ell in primes)
    a=values[block[0]]
    def unit(i):
        return all(residue(values[i]-a,ell) for ell in primes)
    good=next((i for i in singles if unit(i)),None)
    repaired=False
    if good is None:
        assert len(primes)==2
        ell1,ell2=primes
        c=next(i for i in singles if residue(values[i]-a,ell1)==0
               and residue(values[i]-a,ell2)!=0)
        d=next(i for i in singles if residue(values[i]-a,ell2)==0
               and residue(values[i]-a,ell1)!=0)
        newblock=block[:-1]+[c]
        word.append(newblock)
        values=replay(values,[newblock],p)
        singles.remove(c)
        singles.append(block[-1])
        block=newblock
        a=values[block[0]]
        assert unit(d)
        good=d
        repaired=True
    second=[i for i in singles if i!=good]
    word.append(second)
    values=replay(values,[second],p)
    a,b=values[block[0]],values[second[0]]
    assert all(values[i]==a for i in block) and all(values[i]==b for i in second)
    assert values[good]==-p*(a+b)
    assert all(residue(a-b,ell)!=0 for ell in primes)
    assert replay(raw,word,p)==values and len(word)==2+repaired
    return repaired,word


def first_block(raw,p):
    protected=set()
    for ell in factors(len(raw)):
        pair=next((i,j) for i in range(len(raw)) for j in range(i+1,len(raw))
                  if (raw[i]-raw[j])%ell)
        protected.update(pair)
    result=[i for i in range(len(raw)) if i not in protected][:p]
    assert len(result)==p
    return result


class RecordedReplay(Replay):
    def __init__(self,p,a,b):
        super().__init__(p,a,b)
        self.word=[]

    def average(self,indices):
        super().average(indices)
        self.word.append(indices[:])


def main():
    source=Path(__file__).with_name('composite_endpoint_pivot_certificates.json')
    data=json.loads(source.read_text(encoding='utf-8'))
    assert data['schema']==1
    seen_levels=set()
    totals=Counter()
    full,core_only=[],[]
    summaries=[]
    physical=atom_checks=0
    for case in data['cases']:
        n,p=case['level'],case['arity']
        assert n==2*p+1 and p>=3 and p%2==1 and n not in seen_levels
        seen_levels.add(n)
        primepowers=[(ell,ell**exponent) for ell,exponent in factors(n).items()]
        reps=[tuple(r) for r in case['representatives']]
        assert reps[0]==I
        assert all(r[0]*r[3]-r[1]*r[2]==1 for r in reps)
        labels=[signature(r[2],r[3],primepowers) for r in reps]
        assert len(reps)==len(set(labels))==prod(m+m//ell for ell,m in primepowers)
        edge_labels={(e['source'],e['generator']) for e in case['edges']}
        assert len(case['edges'])==len(edge_labels)==3*len(reps)
        assert edge_labels=={(i,j) for i in range(len(reps)) for j in range(3)}
        compiler=PhysicalCompiler(p) if n in (35,39,63,75) else None
        stats=Counter()
        for e in case['edges']:
            r,g=reps[e['source']],GENERATORS[e['generator']]
            assert 0<=e['target']<len(reps)
            following=reps[e['target']]
            intermediate=mm(r,g)
            assert signature(intermediate[2],intermediate[3],primepowers)==labels[e['target']]
            assert (intermediate[2]*following[3]-intermediate[3]*following[2])%n==0
            loop=mm(intermediate,inverse(following))
            mode,t=e['mode'],F(e['shear'])
            exact_decomposition(loop,mode,t,n,p)
            stats[mode]+=1
            if compiler:
                compiler.selected_pivot(loop,mode,t)
                physical+=1
        totals.update(stats)
        if compiler:
            program=compiler.program
            for i,(key,_,_) in enumerate(program.nodes):
                if key[0]=='m':
                    assert key[1]<i and key[2]<i
                elif key[0] in ('t','f'):
                    assert gcd(key[1],n)==1
                    for a,b in ((1,0),(0,1)):
                        check=Replay(p,a,b)
                        check.letter(key)
                        x,y=check.parameters()
                        if key[0]=='t':
                            j=key[1]
                            expected=(F(-(p+1)*a+j*(a-b),p),F(-n*a+2*j*(a-b),p))
                        else:
                            r=key[1]
                            expected=(a+F(r-p,2*p)*(a-b),F(r,p)*(a-b))
                        assert (x,y)==expected
                        atom_checks+=1
        complete=len(primepowers)<=2
        (full if complete else core_only).append([p,n])
        summaries.append({'arity':p,'n':n,'distinct_primes':len(primepowers),
                          'cosets':len(reps),'loops':len(case['edges']),'pivots':dict(stats),
                          'full_input_G_criterion_proved':complete})
    assert {n for n in range(7,220,4) if len(factors(n))==2}<=seen_levels
    assert [p for p in range(3,110,2) if len(factors(2*p+1))>=3]==[97]
    print('composite CRT finite certificates complete loops: PASS',len(data['cases']),sum(totals.values()),flush=True)
    print('composite positive loop DAGs and physical basis leaves: PASS',physical,atom_checks,flush=True)
    rng=Random(21520260912)
    general_entries=forced_entries=0
    for p,n in full:
        primes=tuple(factors(n))
        for _ in range(6):
            while True:
                raw=[rng.randrange(-(1<<72),1<<72) for _ in range(n-1)]
                raw.append(-sum(raw))
                common=gcd(*raw)
                raw=[x//common for x in raw]
                if all(len({x%ell for x in raw})>1 for ell in primes):
                    break
            finish_entry(raw,p,first_block(raw,p))
            general_entries+=1
        if len(primes)==2:
            ell1,ell2=primes
            for a in (-2,0,3):
                differences=[ell1,-ell1,ell2,-ell2]+[0]*(p-3)
                differences[-1]-=n*a
                raw=[a]*p+[a+x for x in differences]
                repaired,_=finish_entry(raw,p,list(range(p)))
                assert repaired
                forced_entries+=1
    print('composite two-prime general and forced entries: PASS',general_entries,forced_entries,flush=True)
    # Five short global-controller words are literally expanded. Their input
    # kernels are explicitly chosen; these are not random-instance statistics.
    paths=[]
    for p in (7,17,19,31,37):
        compiler=Compiler(p)
        program=compiler.program
        record=RecordedReplay(p,-1,-2)
        original=record.state[:]
        for key in program.letters(program.u.node):
            record.letter(key)
        assert record.parameters()[0]==0
        record.finish()
        replay(original,record.word,p,consensus=True)
        paths.append({'arity':p,'n':2*p+1,'input':[str(x) for x in original],
                      'steps':len(record.word),'operations':[[i+1 for i in atom] for atom in record.word]})
    target=Path(__file__).with_name('composite_endpoint_transfer_results.json')
    target.write_text(json.dumps({'scope':'finite certified levels only; no all-level conclusion',
                                 'cases':summaries,'full_input_cases':full,'core_only_cases':core_only,
                                 'literal_controller_paths':paths},indent=2)+'\n',encoding='utf-8')
    print('composite full-input levels and core-only levels: PASS',len(full),len(core_only),flush=True)
    print('composite literal positive controller paths: PASS',len(paths),max(x['steps'] for x in paths),flush=True)
    print('composite endpoint transfer certificates: PASS',flush=True)


if __name__=='__main__':
    main()
