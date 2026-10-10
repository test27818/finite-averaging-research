"""Finite diagnostic of maximum-energy-loss safe integer averaging.

Only arithmetic-safe candidates are admitted. A found trap disproves this
policy for the saved tie rule; positive samples do not prove global closure.
"""
from collections import Counter
from math import gcd
from pathlib import Path
import argparse
import json
import random
import sys
import time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from probe_endpoint_bounded_precision import integral_selections,safe

def probe(p, bound, cases):
    rng=random.Random(9030+p)
    pairs=[(a,b) for a in range(1,bound+1) for b in range(-bound,bound+1)
           if a!=b and gcd(a,b)==1 and gcd(a-b,2*p+1)==1]
    rng.shuffle(pairs)
    checked=0
    begin=time.monotonic()
    for a,b in pairs[:cases]:
        state=tuple(sorted([p*a]*p+[p*b]*p+[-p*p*(a+b)]))
        history=[]
        for step in range(600):
            if not any(state):
                break
            best=None
            for group in integral_selections(state,p):
                mean=sum(group)//p
                c=Counter(state)
                c.subtract(Counter(group))
                c[mean]+=p
                nxt=tuple(v for v,m in sorted(c.items()) for _ in range(m))
                if not safe(nxt,p):
                    continue
                item=(sum(v*v for v in nxt),max(Counter(nxt).values()),nxt,group)
                if best is None or item<best:
                    best=item
            if best is None:
                return {'status':'counterexample','p':p,'a':a,'b':b,'checked':checked,
                        'terminal_scaled':state,'selected_scaled_groups':history,
                        'tie_rule':'min (output energy, maximum multiplicity, sorted output, selected values)',
                        'seconds':round(time.monotonic()-begin,3)}
            _,_,state,group=best
            history.append(group)
        else:
            return {'status':'unknown_step_limit','p':p,'checked':checked,'a':a,'b':b}
        checked+=1
    return {'status':'no_counterexample_in_sample','p':p,'checked':checked,
            'seconds':round(time.monotonic()-begin,3)}

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--p',type=int,required=True)
    parser.add_argument('--bound',type=int,default=30)
    parser.add_argument('--cases',type=int,default=100)
    args=parser.parse_args()
    out=probe(args.p,args.bound,args.cases)
    (Path(__file__).parent/f'greedy_{args.p}.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out))
