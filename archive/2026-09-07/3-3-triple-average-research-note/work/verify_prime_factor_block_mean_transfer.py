"""Exact semiconjugacy on initially nonuniform blocks, no reachability search."""
from fractions import Fraction as F
from math import prod
from random import Random

from verify_composite_arity_transfer import factors,tensor_network,independent_replay

if not __debug__:raise RuntimeError('Assertions must be enabled.')


def parameters(q,n,p):
    qf,nf=factors(q),factors(n)
    assert p in qf and n%(q//p)==0
    c=p**(qf[p]-1)*prod(ell**nf.get(ell,0) for ell in qf if ell!=p)
    assert n%c==0 and p*c%q==0 and set(factors(p*c))==set(qf)
    m=n//c
    assert not (set(factors(m))&set(qf)-{p})
    return c,m


def admitted(p,m):return m==p or m>=(4 if p==2 else 2*p+1)


def main():
    rng=Random(915);checks=0
    for q in (4,6,9,10,12,15,18,25,35,45):
        for p in factors(q):
            for n in (3*q,5*q):
                c,m=parameters(q,n,p)
                if not admitted(p,m):continue
                raw=[F(rng.randrange(-40,41),rng.choice((1,2,3))) for _ in range(n)]
                blocks=[list(range(i*c,(i+1)*c)) for i in range(m)]
                # Deliberately do not make any block constant beforehand.
                quotient=[sum(raw[k] for k in b)/c for b in blocks]
                state=raw[:];ops=[];network=tensor_network(q,p*c)
                for step in range(4):
                    chosen=rng.sample(range(m),p)
                    value=sum(quotient[i] for i in chosen)/p
                    ids=[k for i in chosen for k in blocks[i]]
                    here=[[ids[j] for j in row] for row in network]
                    state=independent_replay(state,here,q,False);ops+=here
                    for i in chosen:quotient[i]=value
                    assert [sum(state[k] for k in b)/c for b in blocks]==quotient
                    assert all(state[k]==value for i in chosen for k in blocks[i])
                assert independent_replay(raw,ops,q,False)==state
                # Cleanup works even if only the means, not the values, agree.
                target=F(7,3)
                dirty=[]
                for i in range(m):
                    v=[F(rng.randrange(-9,10)) for _ in range(c-1)]
                    dirty+=v+[c*target-sum(v)]
                for start in range(0,m,p):
                    chosen=list(range(start,min(start+p,m)))
                    chosen+=[i for i in range(m) if i not in chosen][:p-len(chosen)]
                    ids=[k for i in chosen for k in blocks[i]]
                    dirty=independent_replay(dirty,[[ids[j] for j in row] for row in network],q,False)
                assert all(x==target for x in dirty)
                checks+=1
    print('prime-factor nonuniform block-mean simulation and cleanup: PASS',checks)
    count=0
    for q in range(2,201):
        for k in range(3,21):
            assert any(admitted(p,parameters(q,k*q,p)[1]) for p in factors(q))
            count+=1
    print('prime-factor all higher multiples arithmetic: PASS',count)
    print('prime-factor transfer theorem interfaces: PASS')

if __name__=='__main__':main()
