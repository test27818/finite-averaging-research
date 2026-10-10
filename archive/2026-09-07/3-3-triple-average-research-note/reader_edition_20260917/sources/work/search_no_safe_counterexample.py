from collections import Counter
from itertools import combinations, combinations_with_replacement
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
    n=len(v)
    for S in combinations(range(n),3):
        if sum(v[i] for i in S)%3 or len({v[i] for i in S})==1:continue
        rest=[v[i] for i in range(n) if i not in S]
        if all(len({x%p for x in rest})>=2 for p in P):return True
    return False

for n,R in [(7,8),(8,8),(9,7),(10,7),(11,6),(12,6)]:
    P=ps(n); count=0; terminal=0; best=n; best_v=None
    for v in combinations_with_replacement(range(-R,R+1),n):
        if sum(v)!=0 or not any(v):continue
        g=gcd(*(abs(v[i]-v[0]) for i in range(1,n)))
        if not is3(g) or max(Counter(v).values())>=n-3:continue
        if not safe(v,P):
            terminal+=1
            m=max(Counter(v).values())
            if m<best:best=m;best_v=v
        count+=1
    print('checked',n,'R',R,'below n-3 legal states',count,'terminal',terminal,'best',best,'example',best_v)
print('search complete')
