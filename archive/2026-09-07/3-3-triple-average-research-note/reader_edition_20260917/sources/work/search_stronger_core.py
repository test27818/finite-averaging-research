from collections import Counter
from itertools import combinations, combinations_with_replacement
from math import gcd

def ps(n):
    out=[]; d=2; x=n
    while d*d<=x:
        if x%d==0:
            if d!=3: out.append(d)
            while x%d==0:x//=d
        d+=1
    if x>1 and x!=3:out.append(x)
    return out

def is3(g):
    if not g:return False
    while g%3==0:g//=3
    return g==1

def safe(v,P):
    n=len(v)
    for S in combinations(range(n),3):
        if sum(v[i] for i in S)%3 or len({v[i] for i in S})==1:continue
        rem=[i for i in range(n) if i not in S]
        if all(len({v[i]%p for i in rem})>1 for p in P):return True
    return False

for n in [7,8,10,11,12,13,14,15,16,18,20]:
    P=ps(n); best=n; bv=None; total=0
    for v in combinations_with_replacement(range(-4,5),n):
        if sum(v)!=0 or not any(v):continue
        g=gcd(*(abs(v[i]-v[0]) for i in range(1,n)))
        if not is3(g) or safe(v,P):continue
        total+=1;m=max(Counter(v).values())
        if m<best:best=m;bv=v
    if total:print(n,P,'terminal',total,'best',best,'n-3',n-3,'example',bv, flush=True)
