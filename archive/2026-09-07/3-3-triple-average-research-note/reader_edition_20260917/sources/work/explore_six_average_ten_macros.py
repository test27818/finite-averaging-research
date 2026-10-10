"""Bounded discovery of physical (6,3,1) returns; no reachability conclusion.

Every candidate has a literal one/two-operation labelled construction. Finite
orders give potential inverse certificates; failed bounded search proves none.
"""

from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, product
from math import gcd,lcm
from pathlib import Path
import json

from explore_composite_minimal_core_periods import finite_order,mul,norm


def normal(matrix):
    d=lcm(*(x.denominator for x in matrix))
    return norm(tuple(int(x*d) for x in matrix))


def avg(state,ids):
    mean=tuple(sum(state[i][j] for i in ids)/6 for j in range(2))
    result=state[:]
    for i in ids:
        result[i]=mean
    return result


def generate():
    initial=[(F(1),F(0))]*6+[(F(1),F(-1))]*3+[(F(-9),F(3))]
    table={}
    for countv,carrier in product(range(4),range(2)):
        countu=6-countv-carrier
        if not 0 <= countu <=6:
            continue
        first=list(range(countu))+list(range(6,6+countv))+([9] if carrier else [])
        state=avg(initial,first)
        classes=defaultdict(list)
        for i,v in enumerate(state):
            classes[v].append(i)
        for v,ids in classes.items():
            if len(ids)<3:
                continue
            for w,js in classes.items():
                remaining=ids[:3]
                singles=[j for j in js if j not in remaining]
                if not singles:
                    continue
                singleton=singles[0]
                second=[i for i in range(10) if i not in remaining+[singleton]]
                result=avg(state,second)
                u=result[second[0]]
                matrix=(u[0],u[1],u[0]-v[0],u[1]-v[1])
                exactdet=matrix[0]*matrix[3]-matrix[1]*matrix[2]
                if not exactdet:
                    continue
                canonical=normal(matrix)
                a,b,c,d=canonical
                if (a*d-b*c)%5==0 or c%5:
                    continue
                # Ignore a first identity atom for the shorter original return.
                word=[second] if countu==6 else [first,second]
                entry={'matrix':canonical,'physical_matrix':[str(x) for x in matrix],
                       'operations':word,'u':second,'v':remaining,'w':singleton,
                       'first_type':[countu,countv,carrier]}
                old=table.get(canonical)
                if old is None or len(word)<len(old['operations']):
                    table[canonical]=entry
    return sorted(table.values(),key=lambda x:(len(x['operations']),x['matrix']))


def main():
    macros=generate()
    found=[]
    print('legal distinct one/two-atom core returns',len(macros),flush=True)
    for i,e in enumerate(macros):
        order=finite_order(e['matrix'])
        if order:
            found.append({'word':[i],'order':order})
            print('finite macro',i,order,e['matrix'],e['first_type'],flush=True)
    for i,a in enumerate(macros):
        for j,b in enumerate(macros):
            m=mul(a['matrix'],b['matrix'])
            order=finite_order(m)
            if order:
                found.append({'word':[i,j],'order':order})
    print('one/two-macro finite periods',len(found),flush=True)
    print('sample periods',found[:15],flush=True)
    target=Path(__file__).with_name('six_average_ten_macro_discovery.json')
    target.write_text(json.dumps({'macros':macros,'periods':found},indent=2)+'\n',encoding='utf-8')


if __name__=='__main__':
    main()
