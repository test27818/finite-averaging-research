"""Bounded (q,16-q,1) return discovery for arities10 and12.

Records literal one/two-atom returns and finite-order products. This is not
the final proof verifier; failure within the finite search has no force.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import lcm
from pathlib import Path
import json

from explore_composite_minimal_core_periods import norm,mul,finite_order


def normalized(m):
    d=lcm(*(x.denominator for x in m))
    return norm(tuple(int(x*d) for x in m))


def avg(state,ids,q):
    value=tuple(sum(state[i][j] for i in ids)/q for j in (0,1))
    after=state[:]
    for i in ids:after[i]=value
    return after


def generate(q):
    r=16-q
    initial=[(F(1),F(0))]*q+[(F(1),F(-1))]*r+[(F(-16),F(r))]
    table={}
    for v,w in product(range(r+1),range(2)):
        u=q-v-w
        if not 0<=u<=q:continue
        first=list(range(u))+list(range(q,q+v))+([16] if w else [])
        state=avg(initial,first,q)
        classes=defaultdict(list)
        for i,x in enumerate(state):classes[x].append(i)
        for vv,indices in classes.items():
            if len(indices)<r:continue
            remaining=indices[:r]
            for singles in classes.values():
                available=[i for i in singles if i not in remaining]
                if not available:continue
                singleton=available[0]
                second=[i for i in range(17) if i not in remaining+[singleton]]
                after=avg(state,second,q)
                uu=after[second[0]]
                exact=(uu[0],uu[1],uu[0]-vv[0],uu[1]-vv[1])
                if exact[0]*exact[3]==exact[1]*exact[2]:continue
                matrix=normalized(exact)
                a,b,c,d=matrix
                if c%17 or (a*d-b*c)%17==0:continue
                operations=[second] if u==q else [first,second]
                entry={'matrix':matrix,'actual':[str(x) for x in exact],
                       'first_type':[u,v,w],'operations':operations,
                       'u':second,'v':remaining,'w':singleton}
                if matrix not in table or len(operations)<len(table[matrix]['operations']):
                    table[matrix]=entry
    return sorted(table.values(),key=lambda x:(len(x['operations']),x['matrix']))


def main():
    data=[]
    for q in (10,12):
        macros=generate(q)
        periods=[]
        for i,m in enumerate(macros):
            order=finite_order(m['matrix'])
            if order:periods.append({'word':[i],'order':order})
        for i,a in enumerate(macros):
            for j,b in enumerate(macros):
                order=finite_order(mul(a['matrix'],b['matrix']))
                if order:periods.append({'word':[i,j],'order':order})
        print('arity',q,'returns',len(macros),'periods',len(periods),flush=True)
        for i,m in enumerate(macros):print(i,m['matrix'],m['actual'],m['first_type'],flush=True)
        print('cycles',periods,flush=True)
        data.append({'arity':q,'macros':macros,'periods':periods})
    Path(__file__).with_name('seventeen_arity_return_discovery.json').write_text(
        json.dumps(data,indent=2)+'\n',encoding='utf-8')


if __name__=='__main__':main()
