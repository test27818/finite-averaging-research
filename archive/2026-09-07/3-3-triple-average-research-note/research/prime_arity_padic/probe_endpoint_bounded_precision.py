"""Exact, budgeted endpoint diagnostics, with modular type-count elimination.

Positive results are literal paths. A depth/node limit is UNKNOWN, not a
counterexample. No common rescaling is performed during the physical path.
"""
from collections import Counter
from fractions import Fraction as F
from math import gcd
from pathlib import Path
from time import perf_counter
import argparse
import json


class Limit(Exception):
    pass


def safe(x,p):
    content=gcd(*x)
    if not content:
        return True
    d=gcd(*(a-x[0] for a in x))//content
    while d%p==0:
        d//=p
    return d==1


def integral_selections(state,p):
    hist=Counter(state)
    vals=sorted(hist,key=lambda v:(hist[v],v))
    pair=next(((i,j) for i in range(len(vals)) for j in range(i)
               if (vals[i]-vals[j])%p),None)
    if pair:
        i,j=pair
        vals=[v for k,v in enumerate(vals) if k not in (i,j)]+[vals[j],vals[i]]
    if len(vals)<2:
        return
    bounds=[hist[v] for v in vals]
    suffix=[0]*(len(vals)+1)
    for j in range(len(vals)-1,-1,-1):
        suffix[j]=suffix[j+1]+bounds[j]
    a,b=vals[-2:]
    diff=(a-b)%p
    inv=pow(diff,-1,p) if diff else None
    partial=[]
    def rec(i,left,total):
        if i==len(vals)-2:
            lo=max(0,left-bounds[-1])
            hi=min(bounds[-2],left)
            if lo>hi:
                return
            target=(-total-left*b)%p
            if inv is not None:
                start=target*inv%p
                start+=max(0,(lo-start+p-1)//p)*p
                candidates=range(start,hi+1,p)
            else:
                if target:
                    return
                candidates=range(lo,hi+1)
            for k in candidates:
                counts=partial+[k,left-k]
                if sum(c>0 for c in counts)<2:
                    continue
                selected=tuple(v for v,c in zip(vals,counts) for _ in range(c))
                yield selected
            return
        lo=max(0,left-suffix[i+1])
        for count in range(lo,min(bounds[i],left)+1):
            partial.append(count)
            yield from rec(i+1,left-count,total+count*vals[i])
            partial.pop()
    yield from rec(0,p,0)


def search(X,p,e,depth,nodes_limit):
    assert len(X)==2*p+1 and sum(X)==0 and safe(tuple(X),p)
    start=tuple(sorted(p**e*x for x in X))
    begin=perf_counter()
    nodes=0
    failed={}
    def dfs(state,left):
        nonzero=[x for x in state if x]
        if not nonzero:
            return []
        if left<=0 or len(nonzero)>p*left:
            return None
        if len(nonzero)<=p:
            selected=tuple(nonzero+[0]*(p-len(nonzero)))
            return [selected]
        if failed.get(state,-1)>=left:
            return None
        nonlocal nodes
        nodes+=1
        if nodes>nodes_limit:
            raise Limit
        nxts={}
        for selected in integral_selections(state,p):
            total=sum(selected)
            assert total%p==0
            mean=total//p
            hist=Counter(state)
            hist.subtract(Counter(selected))
            hist[mean]+=p
            nxt=tuple(v for v,c in sorted(hist.items()) for _ in range(c))
            if not safe(nxt,p):
                continue
            score=(sum(v!=0 for v in nxt),sum(v*v for v in nxt))
            nxts[nxt]=(score,selected)
        for nxt,(score,selected) in sorted(nxts.items(),key=lambda x:x[1][0]):
            tail=dfs(nxt,left-1)
            if tail is not None:
                return [selected]+tail
        failed[state]=left
        return None
    try:
        path=dfs(start,depth)
        status='found' if path is not None else 'unknown_depth_exhausted'
    except Limit:
        path=None
        status='unknown_node_budget'
    result={'p':p,'input':X,'precision':e,'depth_bound':depth,
            'status':status,'expanded_nodes':nodes,'elapsed_seconds':round(perf_counter()-begin,3)}
    if path is not None:
        physical=list(map(F,X))
        positions=[]
        for selected in path:
            used=set()
            for x in selected:
                value=F(x,p**e)
                pos=next(i for i,y in enumerate(physical) if i not in used and y==value)
                used.add(pos)
            mean=sum(physical[i] for i in used)/p
            for i in used:
                physical[i]=mean
            assert all(p**e%x.denominator==0 for x in physical)
            positions.append(sorted(used))
        assert not any(physical)
        result.update(length=len(path),positions=positions)
    return result


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--p',type=int,required=True)
    parser.add_argument('--a',type=int,default=1)
    parser.add_argument('--b',type=int,default=2)
    parser.add_argument('--kind',choices=['core','two-exception'],default='core')
    parser.add_argument('--precision',type=int,default=1)
    parser.add_argument('--depth',type=int,default=18)
    parser.add_argument('--nodes',type=int,default=15000)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    p,a,b=args.p,args.a,args.b
    X=([a]*p+[b]*p+[-p*(a+b)] if args.kind=='core'
       else [a]*(2*p-1)+[b,-((2*p-1)*a+b)])
    result=search(X,p,args.precision,args.depth,args.nodes)
    Path(args.output).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='positions'}))
