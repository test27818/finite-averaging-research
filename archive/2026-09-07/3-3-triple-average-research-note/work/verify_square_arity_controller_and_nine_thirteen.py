"""Uniform square-arity scalar cycles and the complete nine/13 interface.

No word search. Exact identities, literal original-position replay, and the
complete finite mod13 unit calculation support the written proof.
"""
from fractions import Fraction as F
from math import gcd
from random import Random

from verify_four_prime_entry_and_band import Ledger
from verify_uniform_odd_middle_cores import mm,invq,residue,bezout
from verify_even_odd_half_core import I,U,L

if not __debug__:raise RuntimeError('Assertions must be enabled.')

def sc(m,a):return tuple(a*x for x in m)
def power(m,k):
    out=I
    for _ in range(k):out=mm(out,m)
    return out
def delta(t):return (1,0,0,F(t))
def det(m):return m[0]*m[3]-m[1]*m[2]


def system(t):
    n=t*t+t+1
    a=(t,-1,0,-1)
    b=(-t-1,t,-n,t*t+t)
    c=(-t-1,1,-n,1)
    sigma=(1,-1,0,-1)
    assert power(c,3)==sc(I,t**3)
    assert power(mm(c,a),2)==sc(I,t**3)
    assert mm(power(c,2),b)==sc(sigma,t**3)
    aa,bb,cc=sc(a,F(1,t)),sc(b,F(1,t*t)),sc(c,F(1,t*t))
    assert power(cc,3)==sc(I,F(1,t**3))
    assert power(mm(cc,aa),2)==sc(I,F(1,t**3))
    assert mm(power(cc,2),bb)==sc(sigma,F(1,t**3))
    assert mm(sigma,aa)==delta(F(1,t))
    assert mm(mm(mm(sigma,delta(t)),sigma),delta(F(1,t)))==U(F(t-1,t))
    pmat=(1,-t-1,0,-n)
    assert mm(mm(invq(pmat),U(1)),pmat)==U(-n)
    assert mm(mm(mm(mm(invq(pmat),c),U(t*t)),invq(c)),pmat)==L(n)
    for j in (0,max(0,t-2),t-1):
        mj=(1,j-t,n,(t+1)*(j-t))
        m0=(1,-t,n,-t*(t+1))
        assert det(mj)==t*t*(t-j)
        assert mm(invq(m0),mj)==delta(F(t-j,t))
    if t%2:
        h=sc(mm(mm(delta(2),c),delta(2)),F(1,2*t))
        assert h==(-F(t+1,2*t),F(1,t),-F(n,t),F(2,t)) and det(h)==1
        assert mm(mm(c,delta(2)),invq(h))==sc(delta(F(1,2)),2*t)
    else:
        assert gcd(2,(t-1)**2*n**3)==1
    # Recompute the commutator after obtaining Delta(2) and its inverse.
    assert mm(mm(mm(sigma,delta(2)),sigma),delta(F(1,2)))==U(F(1,2))
    assert mm(mm(U(-1),cc),delta(t*t))==L(-F(n,t*t))
    return aa,bb,cc,sigma


def core(t,x,y):
    u,v=F(x),F(x-y)
    return [u]*(t*t)+[v]*t+[-t*t*u-t*v]


def atom(led,groups,t,name):
    ga,gb,gc=(list(x) for x in groups);q=t*t
    if name=='A':
        chosen=ga[:q-t]+gb
        led.average(chosen)
        return [chosen,ga[q-t:],gc]
    if name=='B':
        chosen=ga[:q-1]+gc
        led.average(chosen)
        return [chosen,gb,ga[q-1:]]
    if name=='C':
        chosen=ga[:q-t]+gb[:t-1]+gc
        led.average(chosen)
        return [chosen,ga[q-t:],gb[t-1:]]
    raise AssertionError(name)


def m_return(led,groups,t,j):
    ga,gb,gc=(list(x) for x in groups);q=t*t
    first=ga[:q-j-1]+gb[:j]+gc
    led.average(first)
    olda=ga[q-j-1:]
    kept,fresh=first[:t],first[t:]
    singleton=olda[:1]
    second=olda[1:]+gb[j:]+fresh
    assert len(second)==q
    led.average(second)
    return [second,kept,singleton]


def check_physical(t):
    aa,bb,cc,ss=system(t);q=t*t
    count=0
    for x,y in ((1,0),(0,1)):
        raw=core(t,x,y)
        for names,expected in ((['C']*3,sc(I,F(1,t**3))),
                (['A','C']*2,sc(I,F(1,t**3))),
                (['B','C','C'],sc(ss,F(1,t**3)))):
            led=Ledger(raw,q);groups=[list(range(q)),list(range(q,q+t)),[q+t]]
            for name in names:groups=atom(led,groups,t,name)
            xx,yy=expected[0]*x+expected[1]*y,expected[2]*x+expected[3]*y
            values=(xx,xx-yy,-q*xx-t*(xx-yy))
            assert all(led.state[k]==v for group,v in zip(groups,values) for k in group)
            led.independent_replay(raw);count+=1
        for j in (0,max(0,t-2),t-1):
            led=Ledger(raw,q);groups=[list(range(q)),list(range(q,q+t)),[q+t]]
            groups=m_return(led,groups,t,j)
            mat=sc((1,j-t,q+t+1,(t+1)*(j-t)),F(1,t**3))
            xx,yy=mat[0]*x+mat[1]*y,mat[2]*x+mat[3]*y
            values=(xx,xx-yy,-q*xx-t*(xx-yy))
            assert all(led.state[k]==v for group,v in zip(groups,values) for k in group)
            led.independent_replay(raw);count+=1
    return count


def entry_nine(raw):
    q,t,n=9,3,13
    led=Ledger([F(x) for x in raw],q)
    pair=next((i,j) for i in range(n) for j in range(i) if (raw[i]-raw[j])%13)
    outside=list(pair)+[i for i in range(n) if i not in pair][:2]
    inside=[i for i in range(n) if i not in outside]
    led.average(inside);a=led.state[inside[0]]
    w=next(i for i in outside if residue(led.state[i]-a,13))
    second=inside[:q-t]+[i for i in outside if i!=w]
    led.average(second);left=inside[q-t:]
    u,v=led.state[second[0]],led.state[left[0]]
    assert residue(u-v,13)
    assert all(led.state[k]==val for g0,val in zip((second,left,[w]),(u,v,-q*u-t*v)) for k in g0)
    led.independent_replay(raw)


def complete_interface():
    t,q,n=3,9,13
    aa,bb,cc,sigma=system(t)
    assert pow(2,6,13)==12 and len({pow(2,k,13) for k in range(12)})==12
    # After inverting2, U(R),L(13R) yield Gamma_1(13,R). Check the
    # actual diagonal correction for every modular unit, not just direction.
    rng=Random(913);count=0
    for _ in range(250):
        x,y=rng.randrange(-10**8,10**8),rng.randrange(1,10**8)
        if gcd(x,y)!=1 or y%13==0:continue
        d,a,b=bezout(x,y);assert d==1
        k=-a*pow(y,-1,13)%13
        a,b=a+k*y,b-k*x
        h=(y,-x,a,b)
        assert det(h)==1 and a%13==0
        eps=2**next(k for k in range(12) if pow(2,k,13)==y%13)
        g=mm((F(1,eps),0,0,F(eps)),h)
        assert det(g)==1 and residue(g[0],13)==residue(g[3],13)==1 and residue(g[2],13)==0
        assert (h[0]*x+h[1]*y,h[2]*x+h[3]*y)==(0,1)
        count+=1
    raw=core(3,0,1);led=Ledger(raw,9)
    led.average(list(range(9,13))+list(range(5)))
    assert not any(led.state)
    led.independent_replay(raw)
    entries=0
    for _ in range(100):
        raw=[rng.randrange(-10000,10000) for _ in range(12)]
        raw.append(-sum(raw))
        if any((x-raw[0])%13 for x in raw):entry_nine(raw);entries+=1
    print('nine-average13 exact entry and terminal interfaces: PASS',entries,count)


def main():
    for t in range(2,202):system(t)
    print('square-arity uniform positive cycles and dyadic inverse: PASS 200')
    print('square-arity all-parameter full upper and n-lower roots: PASS 200')
    count=sum(check_physical(t) for t in (2,3,4,5,7,9))
    print('square-arity literal original-position cycles and returns: PASS',count)
    complete_interface()
    print('nine-average thirteen-position full criterion interfaces: PASS')

if __name__=='__main__':main()
