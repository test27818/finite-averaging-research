"""Exact normal-orbit checks and literal original-position certificate replay.

This does NOT decide whether a rank >=2 relation lattice meets the orbit.
Bounded-height oracle completeness uses the proved L1 monotonicity of A_i,
not an arbitrary word-depth cutoff.
"""
from collections import deque
from functools import lru_cache
from itertools import product
from math import gcd
from pathlib import Path
from random import Random
import json
from verify_subcritical_complement_dynamics import core_distance


def normal_step(p,h,J):
    s=sum(h)
    return tuple(-s if j in J else p*h[j] for j in range(len(h)))


def valuation(v,p):
    assert v
    out=0
    while v%p==0:v//=p;out+=1
    return out


def decode_singleton_normal(p,h):
    r=len(h)
    assert 2<=r<p
    d=gcd(*h)
    if not d:return None
    h=tuple(v//d for v in h)
    if 0 in h:return None
    runs=[];norms=[sum(map(abs,h))]
    while h not in ((1,)*r,(-1,)*r):
        units=[i for i,v in enumerate(h) if v%p]
        if len(units)!=1:return None
        i=units[0]
        length=min(valuation(h[j],p) for j in range(r) if j!=i)
        P=p**length;sign=(-1)**length
        Q=sum(h[j]//P for j in range(r) if j!=i)
        assert (sign*P-1)%(p+1)==0
        coeff=(sign*P-1)//(p+1)
        nxt=tuple(sign*h[i]+Q*coeff if j==i else h[j]//P for j in range(r))
        assert sum(map(abs,nxt))<sum(map(abs,h)) and gcd(*nxt)==1
        runs.append((i,length));h=nxt;norms.append(sum(map(abs,h)))
        if len(norms)>=3:assert p*norms[-1]<=2*norms[-3]
        if 0 in h:return None
    return {'runs':runs,'root_sign':h[0],'normalization':d,
            'letter_count':sum(k for i,k in runs)}


def bounded_singleton_orbit(p,r,H):
    root=(1,)*r
    seen={root};queue=deque([root])
    while queue:
        h=queue.popleft()
        for i in range(r):
            z=normal_step(p,h,{i})
            assert sum(map(abs,z))>sum(map(abs,h))
            if sum(map(abs,z))<=H and z not in seen:
                seen.add(z);queue.append(z)
    return seen|{tuple(-x for x in h) for h in seen}


def exhaustive_membership():
    rows=[]
    for p,r,H in ((3,2,40),(5,3,30),(5,4,14),(7,3,30)):
        exact=bounded_singleton_orbit(p,r,H);tested=0
        for h in product(range(-H,H+1),repeat=r):
            if sum(map(abs,h))>H or gcd(*h)!=1:continue
            assert (decode_singleton_normal(p,h) is not None)==(h in exact),(p,h)
            tested+=1
        rows.append({'p':p,'r':r,'height_L1':H,'primitive_candidates':tested,'orbit_normals':len(exact)})
    return rows


def p_plus_two_comparison():
    checked=0
    for p in (3,5,7,11):
        for u,v in product(range(-35,36),repeat=2):
            if not (u or v):continue
            old=core_distance(p,u,v)
            dec=decode_singleton_normal(p,(v,-u))
            got=None if dec is None else dec['letter_count']+1
            assert got==old,(p,u,v,got,old)
            checked+=1
    return checked


def literal_lift(p,u,forward_masks):
    r=len(u);n=p+r
    assert sum(u)%n==0
    a=-sum(u)//n
    state=[a]*p+[a+v for v in u]
    block=list(range(p));exception=list(range(p,n))
    u=list(u);count=0
    for J in forward_masks:
        J=sorted(J);k=len(J)
        q=sum(u[j] for j in J)
        assert q%p==0
        q//=p
        selected=block[:p-k]+[exception[j] for j in J]
        new_exceptions=block[p-k:]
        assert len(selected)==len(set(selected))==p
        total=sum(state[j] for j in selected)
        assert total%p==0 and total//p==a+q
        for j in selected:state[j]=a+q
        for j,pos in zip(J,new_exceptions):exception[j]=pos
        block=selected
        u=[-q if j in J else u[j]-q for j in range(r)]
        a+=q
        assert set(block).isdisjoint(exception) and len(set(block+exception))==n
        assert all(state[j]==a for j in block)
        assert all(state[exception[j]]==a+u[j] for j in range(r))
        count+=1
    assert a==sum(u)==0
    selected=exception+block[:p-r]
    assert len(selected)==len(set(selected))==p and sum(state[j] for j in selected)==0
    for j in selected:state[j]=0
    assert not any(state)
    return count+1


def random_normals_and_lifts():
    rng=Random(20261012)
    stats={'single_normals':0,'general_normals':0,'literal_atoms':0}
    for p,r in ((3,2),(5,3),(5,4),(7,3),(11,6)):
        n=p+r
        for mode in ('single','general'):
            for _ in range(70):
                h=(1,)*r;generation=[]
                length=rng.randrange(1,24)
                for t in range(length):
                    if mode=='single':J={rng.randrange(r)}
                    else:J=set(rng.sample(range(r),rng.randrange(1,r)))
                    raw=normal_step(p,h,J)
                    d=gcd(*raw)
                    assert gcd(d,p*n)==1
                    h=tuple(v//d for v in raw)
                    assert sum(h)%p and 0 not in h
                    assert {j for j,v in enumerate(h) if v%p}==J
                    assert len({h[j] for j in J})==1
                    assert all((v-h[0])%n==0 for v in h) and gcd(h[0],n)==1
                    generation.append(J)
                if mode=='single':
                    dec=decode_singleton_normal(p,h)
                    assert dec is not None
                    decoded=[{i} for i,k in dec['runs'] for _ in range(k)]
                    assert decoded==list(reversed(generation))
                    stats['single_normals']+=1
                else:stats['general_normals']+=1
                b=[rng.randrange(-7,8) for _ in range(r-1)]
                if not any(b):b[0]=1
                u=[h[-1]*v for v in b]+[-sum(h[j]*b[j] for j in range(r-1))]
                assert sum(h[j]*u[j] for j in range(r))==0
                stats['literal_atoms']+=literal_lift(p,u,list(reversed(generation)))
    return stats


def long_run_checks():
    rows=[]
    for p,r,word in ((5,3,[0]*2000),(5,3,[0,1,2]*250),(13,8,[0,2,4,6]*125)):
        h=(1,)*r
        for i in word:h=normal_step(p,h,{i})
        dec=decode_singleton_normal(p,h)
        assert dec is not None and dec['letter_count']==len(word)
        assert [i for i,k in dec['runs'] for _ in range(k)]==list(reversed(word))
        rows.append({'p':p,'r':r,'letters':len(word),'compressed_runs':len(dec['runs']),
                     'maximum_coordinate_bits':max(abs(v).bit_length() for v in h)})
    return rows


def boundary_counterexample():
    h=(1,1,65);p=5;r=3;n=8;u=(13,13,14)
    assert gcd(*h)==1 and sum(h)%p and all((x-h[0])%n==0 for x in h)
    allowed=[mask for mask in range(1,1<<r) if sum(u[j] for j in range(r) if mask>>j&1)%p==0]
    assert allowed==[7]
    a=-sum(u)//n
    assert a==-5 and a+sum(u)//p==3
    # The sole nonidentity result is (3^5,-5^3); its normalized p-leading
    # heavy block has no partial integer interaction.
    assert all(((p-t)*3+t*(-5))%p for t in range(1,r+1))
    path=[(-175,185,214),(35,220,249),(-44,-9,205),(-85,-50,-41),
          (-75,-31,10),(-16,15,25),(-19,-3,22)]
    selected=[-175,220,205,-50,-75,15]
    for old,new,v in zip(path,path[1:],selected):
        i=old.index(v);q=v//p
        assert v%p==0
        assert tuple(sorted(-q if j==i else old[j]-q for j in range(3)))==new
    assert sum(path[-1])==0
    bad=(-212,-37,177)
    assert sum(bad)!=0 and all(v%p for v in bad)
    return {'nonmember_normal':h,'equivalent_core_difference':u,
            'single_greedy_counterexample':path[0],'known_success_length':7}


def main():
    result={'scope':'The given-normal singleton membership problem is polynomial. This does not solve the existence of a suitable normal in a rank>=2 relation lattice, nor full fixed-p averaging reachability.',
            'exhaustive_membership':exhaustive_membership(),
            'p_plus_two_comparisons':p_plus_two_comparison(),
            'normal_lifts':random_normals_and_lifts(),
            'long_runs':long_run_checks(),
            'boundary':boundary_counterexample()}
    path=Path(__file__).with_name('fixed_p_dual_normals_verification.json')
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'normal_candidates':sum(x['primitive_candidates'] for x in result['exhaustive_membership']),
                      'p_plus_two_comparisons':result['p_plus_two_comparisons'],
                      'normal_lifts':result['normal_lifts'],'long_runs':result['long_runs'],
                      'record':str(path)},ensure_ascii=False,indent=2))


if __name__=='__main__':main()
