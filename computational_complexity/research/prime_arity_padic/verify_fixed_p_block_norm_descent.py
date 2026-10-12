"""Exact checks of three-value norm descent; NOT a full fixed-p solver.

norm_slice returns outside_class when its promised norm shell does not hold.
reduce_double_core returns boundary at the unresolved split interface.
The independent oracle is the earlier full integer DAG with no depth bound
and no G pruning; it is imported only for finite verification.
"""
from math import gcd,isqrt
from random import Random
from pathlib import Path
from collections import Counter
import json
from verify_subcritical_uniform_np_hard import integer_oracle,primitive


def Q(p,m,u,v):
    return (p-m+1)*u*u+(m-2)*u*v+v*v


def matmul(A,B):
    return (A[0]*B[0]+A[1]*B[2],A[0]*B[1]+A[1]*B[3],
            A[2]*B[0]+A[3]*B[2],A[2]*B[1]+A[3]*B[3])


def matpow(A,e):
    out=(1,0,0,1)
    while e:
        if e&1:out=matmul(A,out)
        A=matmul(A,A);e//=2
    return out


def apply(A,z):
    return A[0]*z[0]+A[1]*z[1],A[2]*z[0]+A[3]*z[1]


def B(p,m):return (-1,1,-(p-m+1),-(m-1))
def C(p,m):return (-(m-1),-1,p-m+1,-1)


def valuation(x,p):
    assert x
    e=0
    while x%p==0:x//=p;e+=1
    return e


def physical(p,m,z):
    u,v=z;n=p+m+1
    assert (m*u+v)%n==0
    a=-(m*u+v)//n
    return tuple(sorted((a,)*p+(a+u,)*m+(a+v,)))


def strip_mixed(p,m,u,v):
    assert gcd(u,v)==1 and (m*u+v)%(p+m+1)==0
    value=Q(p,m,u,v)
    assert value and value%p==0
    e=valuation(value,p)
    if (v+(m-1)*u)%p:
        assert (v-u)%p==0
        return {'status':'no','forced':0}
    power=p**e
    z=apply(matpow(C(p,m),e),(u,v))
    assert z[0]%power==z[1]%power==0
    z=(z[0]//power,z[1]//power)
    assert gcd(*z)==1 and Q(p,m,*z)==value//power
    assert (m*z[0]+z[1])%(p+m+1)==0
    return {'status':'reduced','forced':e,'pair':z}


def base_distance(p,m,u,v):
    n=p+m+1;D=4*p-m*m
    assert gcd(u,v)==1 and Q(p,m,u,v)==n and (m*u+v)%n==0
    t=(m*u+v)//n
    if not t:
        assert (u,v) in ((1,-m),(-1,m))
        return 1
    assert D in (3,4) and abs(t)==1
    uu=u*t
    if D==4:
        assert uu==(m+2)//2
        return None
    if uu==(m+1)//2:return 2
    assert uu==(m+3)//2
    return 4 if (p,m)==(7,5) else None


def norm_slice(p,m,u,v):
    assert p>=5 and 2<=m<=p-2 and m*m<4*p
    d=gcd(u,v)
    if not d:return {'status':'yes','distance':0}
    u,v=u//d,v//d;n=p+m+1
    if (m*u+v)%n:return {'status':'no','reason':'G_obstruction'}
    value=Q(p,m,u,v)
    assert value>0 and value%n==0
    rem=value//n;L=0
    while rem%p==0:rem//=p;L+=1
    if rem!=1:return {'status':'outside_class','p_free_norm':value//p**L}
    if L:
        reduced=strip_mixed(p,m,u,v)
        if reduced['status']=='no':return reduced
        assert reduced['forced']==L
        u,v=reduced['pair']
    d0=base_distance(p,m,u,v)
    return {'status':'no'} if d0 is None else {'status':'yes','distance':L+d0,'base':(u,v)}


def reduce_double_core(p,u,v):
    """Complete forced-prefix reduction for p+3 three-value cores only."""
    assert p>=5 and gcd(u,v)==1 and (2*u+v)%(p+3)==0
    forced=0;runs=[]
    while True:
        if 2*u+v==0:return {'status':'yes','distance':forced+1,'runs':runs}
        if u%p==0:return {'status':'boundary','pair':(u,v),'forced':forced,'runs':runs}
        if v%p==0:
            assert v
            e=valuation(v,p);P=p**e;sgn=(-1)**e
            old=Q(p,2,u,v)
            u,v=u-(v//P)*((P-sgn)//(p+1)),sgn*(v//P)
            assert gcd(u,v)==1 and (2*u+v)%(p+3)==0
            assert p*Q(p,2,u,v)<=(p+1)*old
            forced+=e;runs.append(('S',e))
            continue
        if Q(p,2,u,v)%p:
            return {'status':'no','forced':forced,'runs':runs}
        reduced=strip_mixed(p,2,u,v)
        if reduced['status']=='no':return {'status':'no','forced':forced,'runs':runs}
        u,v=reduced['pair'];forced+=reduced['forced'];runs.append(('T',reduced['forced']))


def norm_shell(p,m,L):
    n=p+m+1;D=4*p-m*m;target=p**L
    found=set()
    for t in range(-isqrt(4*target//D),isqrt(4*target//D)+1):
        value=4*target-D*t*t
        z=isqrt(value)
        if z*z!=value:continue
        for zz in {z,-z}:
            if ((m+2)*t+zz)%2:continue
            u=((m+2)*t+zz)//2;v=n*t-m*u
            if gcd(u,v)!=1:continue
            pair=(u,v)
            if next(x for x in pair if x)<0:pair=tuple(-x for x in pair)
            found.add(pair)
    return found


def shell_oracle_checks():
    totals=Counter();specials=[]
    for p in (5,7,11,13,17,19,31,43):
        for m in range(2,p-1):
            D=4*p-m*m
            if D<=0:continue
            n=p+m+1;children,distance=integer_oracle(p,n)
            roots=norm_shell(p,m,0)
            expected_roots=1 if D>4 else 2 if D==4 else 3
            assert len(roots)==expected_roots
            base_rows=[]
            for L in range(5):
                exact=norm_shell(p,m,L)
                expected=set()
                for root in roots:
                    for matrix in (B(p,m),C(p,m)):
                        z=apply(matpow(matrix,L),root)
                        if next(x for x in z if x)<0:z=tuple(-x for x in z)
                        expected.add(z)
                assert exact==expected,(p,m,L,exact,expected)
                for z in exact:
                    d=distance(primitive(physical(p,m,z)))
                    result=norm_slice(p,m,*z)
                    assert result['status']!='outside_class'
                    assert (result['status']=='yes')==(d is not None)
                    if d is not None:assert result['distance']==d
                    if L==0:base_rows.append({'pair':z,'distance':d})
                    totals['directions']+=1
                totals['shells']+=1
            totals['parameter_pairs']+=1
            totals['oracle_states']+=distance.cache_info().currsize
            if D<=4:specials.append({'p':p,'m':m,'D':D,'bases':base_rows})
    return {'totals':dict(totals),'special_bases':specials}


def literal_tower(p,m,L):
    z=apply(matpow(B(p,m),L),(1,-m));u,v=z;n=p+m+1
    assert gcd(u,v)==1 and (m*u+v)%n==0
    a=-(m*u+v)//n
    state=[a]*p+[a+u]*m+[a+v]
    heavy=list(range(p));repeat=list(range(p,p+m));last=p+m
    for step in range(L):
        assert (v+(m-1)*u)%p==0 and u%p and v%p
        valid=[]
        for j in range(m+1):
            for eps in (0,1):
                if j+eps and (j*u+eps*v)%p==0:valid.append((j,eps))
        assert valid==[(m-1,1)]
        selected=heavy[:p-m]+repeat[:m-1]+[last]
        remain_heavy=heavy[p-m:];remain_repeat=repeat[-1]
        assert len(selected)==len(set(selected))==p
        avg=sum(state[i] for i in selected)//p
        assert sum(state[i] for i in selected)%p==0
        for i in selected:state[i]=avg
        old_a=a
        a=avg;u,v=old_a-a,old_a+u-a
        heavy=selected;repeat=remain_heavy;last=remain_repeat
        assert all(state[i]==a for i in heavy)
        assert all(state[i]==a+u for i in repeat) and state[last]==a+v
        assert gcd(u,v)==1 and Q(p,m,u,v)==n*p**(L-step-1)
    assert a==0 and (u,v)==(1,-m)
    selected=repeat+[last]+heavy[:p-m-1]
    assert len(selected)==len(set(selected))==p and sum(state[i] for i in selected)==0
    for i in selected:state[i]=0
    assert not any(state)
    return L+1


def reduction_oracle_checks():
    rng=Random(20261013);counts=Counter();max_runs=0
    for p in (5,7,11,13):
        children,distance=integer_oracle(p,p+3)
        for _ in range(900):
            a=rng.randrange(-40,41);u=rng.randrange(-150,151);v=-(p+3)*a-2*u
            if gcd(u,v)!=1:continue
            result=reduce_double_core(p,u,v)
            d=distance(primitive(physical(p,2,(u,v))))
            if result['status']=='yes':assert result['distance']==d
            elif result['status']=='no':assert d is None
            else:
                d0=distance(primitive(physical(p,2,result['pair'])))
                assert (d is None)==(d0 is None)
                if d0 is not None:assert d==result['forced']+d0
            counts[result['status']]+=1
            counts['inputs']+=1
            max_runs=max(max_runs,len(result['runs']))
        counts['oracle_states']+=distance.cache_info().currsize
    return {'counts':dict(counts),'maximum_runs_in_samples':max_runs}


def identities_and_large_cases():
    rng=Random(271012);identities=0
    for p in (5,7,11,17,43):
        for m in range(2,p-1):
            for _ in range(20):
                z=(rng.randrange(-100,101),rng.randrange(-100,101))
                assert Q(p,m,*apply(B(p,m),z))==p*Q(p,m,*z)
                assert Q(p,m,*apply(C(p,m),z))==p*Q(p,m,*z)
                assert matmul(B(p,m),C(p,m))==(p,0,0,p)
                identities+=1
    rows=[]
    for p,m,L in ((5,2,2000),(5,3,1000),(137,20,500)):
        good=apply(matpow(B(p,m),L),(1,-m))
        bad=apply(matpow(C(p,m),L),(1,-m))
        assert norm_slice(p,m,*good)['distance']==L+1
        assert norm_slice(p,m,*bad)['status']=='no'
        rows.append({'p':p,'m':m,'L':L,'coordinate_bits':max(abs(x).bit_length() for x in good),
                     'yes_distance':L+1,'conjugate_rejected':True})
    return {'identity_checks':identities,'large_cases':rows}


def main():
    result={'scope':'Complete polynomial decision only for the stated positive-definite norm shells; mixed-run compression and p+3 forced-prefix reduction are exact, but boundary means unresolved, not no.',
            'shell_oracles':shell_oracle_checks(),
            'literal_tower_atoms':sum(literal_tower(p,m,L) for p,m in ((5,2),(5,3),(7,5),(11,9),(17,8),(19,17)) for L in range(1,41)),
            'double_core_reductions':reduction_oracle_checks(),
            'algebraic_checks':identities_and_large_cases()}
    path=Path(__file__).with_name('fixed_p_block_norm_descent_verification.json')
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'shell_oracles':result['shell_oracles']['totals'],
                      'literal_tower_atoms':result['literal_tower_atoms'],
                      'double_core_reductions':result['double_core_reductions'],
                      'algebraic_checks':result['algebraic_checks'],'record':str(path)},ensure_ascii=False,indent=2))


if __name__=='__main__':main()
