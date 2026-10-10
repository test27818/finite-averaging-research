"""Bounded labelled return discovery for six-averaging on the (6,4,1) core.

This is a discovery record only. Positive cycles may be extracted and proved
independently. Missing a cycle in the specified finite scope proves nothing.
"""

from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import gcd,lcm
from pathlib import Path
import json

from explore_composite_minimal_core_periods import finite_order,mul,norm


def normal(matrix):
    denominator=lcm(*(x.denominator for x in matrix))
    return norm(tuple(int(x*denominator) for x in matrix))


def average(state,ids):
    value=tuple(sum(state[i][j] for i in ids)/6 for j in range(2))
    result=state[:]
    for i in ids:
        result[i]=value
    return result


def generate():
    initial=[(F(1),F(0))]*6+[(F(1),F(-1))]*4+[(F(-10),F(4))]
    table={}
    for fv,fw in product(range(5),range(2)):
        fu=6-fv-fw
        if not 0<=fu<=6:
            continue
        first=list(range(fu))+list(range(6,6+fv))+([10] if fw else [])
        state=average(initial,first)
        classes=defaultdict(list)
        for i,x in enumerate(state):
            classes[x].append(i)
        for v,ids in classes.items():
            if len(ids)<4:
                continue
            four=ids[:4]
            for w,singles in classes.items():
                remainder=[i for i in singles if i not in four]
                if not remainder:
                    continue
                singleton=remainder[0]
                second=[i for i in range(11) if i not in four+[singleton]]
                after=average(state,second)
                u=after[second[0]]
                physical=(u[0],u[1],u[0]-v[0],u[1]-v[1])
                if physical[0]*physical[3]==physical[1]*physical[2]:
                    continue
                matrix=normal(physical)
                a,b,c,d=matrix
                if (a*d-b*c)%11==0 or c%11:
                    continue
                operations=[second] if fu==6 else [first,second]
                entry={'matrix':matrix,'physical_matrix':[str(x) for x in physical],
                       'operations':operations,'u':second,'v':four,'w':singleton,
                       'first_type':[fu,fv,fw]}
                if matrix not in table or len(operations)<len(table[matrix]['operations']):
                    table[matrix]=entry
    return sorted(table.values(),key=lambda x:(len(x['operations']),x['matrix']))


def main():
    macros=generate()
    periods=[]
    for i,m in enumerate(macros):
        order=finite_order(m['matrix'])
        if order:
            periods.append({'word':[i],'order':order})
    for i,a in enumerate(macros):
        for j,b in enumerate(macros):
            order=finite_order(mul(a['matrix'],b['matrix']))
            if order:
                periods.append({'word':[i,j],'order':order})
    print('legal one/two-atom returns:',len(macros))
    for i,m in enumerate(macros):
        print(i,m['matrix'],m['first_type'],m['operations'],m['u'],m['v'],m['w'])
    print('periods:',periods)
    Path(__file__).with_name('six_average_eleven_macro_discovery.json').write_text(
        json.dumps({'macros':macros,'periods':periods},indent=2)+'\n',encoding='utf-8')


if __name__=='__main__':
    main()
