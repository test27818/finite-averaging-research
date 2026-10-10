from collections import Counter, deque
from itertools import combinations, product
from math import gcd
import support_first_lift_search as sf
primitive, step, support, shortest_paths, enumerate_states, inspect_path = (sf.primitive, sf.step, sf.support, sf.shortest_paths, sf.enumerate_states, sf.inspect_path)

for n,bound in [(6,2),(7,2)]:
    ctr=Counter(); examples={}
    for start in enumerate_states(n,bound):
        result=shortest_paths(start,8)
        if result is None: continue
        info=inspect_path(start,result[1])
        if info:
            k,chosen,kind,current,nxt=info
            ctr[(k,kind)]+=1
            examples.setdefault((k,kind),(start,result,info))
    print('n,bound',n,bound,'counts',ctr)
    for key,value in sorted(examples.items()): print(key,value)
