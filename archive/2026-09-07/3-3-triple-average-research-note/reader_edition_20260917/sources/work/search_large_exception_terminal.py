from collections import Counter
from itertools import combinations_with_replacement
from math import gcd

def ps(n):
    out=[];d=2;x=n
    while d*d<=x:
        if x%d==0:
            if d!=3:out.append(d)
            while x%d==0:x//=d
        d+=1
    if x>1 and x!=3:out.append(x)
    return out
def is3(g):
    if not g:return False
    while g%3==0:g//=3
    return g==1
def safe(v,P):
    from itertools import combinations
    n=len(v)
    for S in combinations(range(n),3):
        if sum(v[i] for i in S)%3 or len({v[i] for i in S})==1:continue
        rest=[v[i] for i in range(n) if i not in S]
        if all(len({x%p for x in rest})>1 for p in P):return True
    return False

for n in [10,12,14,15,18,20,21,22,24,26,28,30,35,36,40,42]:
    P=ps(n); max_r=0; ex=None; checked=0
    for r in range(5,min(8,n-1)):
        m=n-r
        for u in range(-5,6):
            for exc in combinations_with_replacement(range(-10,11),r):
                if m*u+sum(exc)!=0:continue
                if u in exc:continue
                v=(u,)*m+exc
                if not is3(gcd(*(abs(v[i]-v[0]) for i in range(1,n)))):continue
                checked+=1
                if not safe(v,P):
                    max_r=max(max_r,r)
                    if ex is None:ex=(r,u,exc)
    print(n,P,'tested',checked,'terminal_r>=5',max_r,'example',ex,flush=True)
