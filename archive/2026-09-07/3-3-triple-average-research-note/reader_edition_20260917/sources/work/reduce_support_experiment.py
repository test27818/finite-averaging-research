from fractions import Fraction as F
from random import Random
from collections import Counter

def step(v):
    vals=sorted(set(v))
    if len(vals)<=2:return v,None
    s=(vals[0],vals[len(vals)//2],vals[-1])
    q=sum(s,F(0))/3
    a=list(v)
    for x in s:a.remove(x)
    a += [q]*3
    return tuple(sorted(a)),s

R=Random(3)
for n in range(5,16):
    worst=0;bad=0
    for _ in range(1000):
        v=tuple(sorted(F(R.randrange(-10,11)) for _ in range(n)))
        seen=set();d=0
        while len(set(v))>2 and d<1000:
            if v in seen:break
            seen.add(v);v,s=step(v);d+=1
        if len(set(v))>2:bad+=1
        worst=max(worst,d)
    print(n,'bad',bad,'worst',worst)
