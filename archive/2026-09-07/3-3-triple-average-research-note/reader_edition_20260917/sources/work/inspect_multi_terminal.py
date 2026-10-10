from collections import Counter
from itertools import combinations_with_replacement
from math import gcd

def pdiv(n):
    out=[]; d=2
    while d*d<=n:
        if n%d==0:
            if d!=3: out.append(d)
            while n%d==0: n//=d
        d+=1
    if n>1 and n!=3: out.append(n)
    return out

def is3(g):
    if not g:return False
    while g%3==0:g//=3
    return g==1

def safe(v, ps):
    n=len(v)
    from itertools import combinations
    for S in combinations(range(n),3):
        if sum(v[i] for i in S)%3:continue
        if len({v[i] for i in S})==1:continue
        rem=[i for i in range(n) if i not in S]
        if all(len({v[i]%p for i in rem})>=2 for p in ps):return True
    return False

for n in range(7,31):
    ps=pdiv(n)
    if not ps:continue
    total=0; mins={}; examples={}
    for v in combinations_with_replacement(range(-3,4),n):
        if sum(v)!=0 or not any(v):continue
        g=gcd(*(abs(v[i]-v[0]) for i in range(1,n)))
        if not is3(g) or safe(v,ps):continue
        total+=1
        d=sum(max(Counter(x%p for x in v).values())>=n-3 for p in ps)
        m=max(Counter(v).values())
        mins[d]=min(mins.get(d,n+1),m)
        examples.setdefault(d,v)
    if total:
        print(n, ps, 'terminal', total, 'mins', mins, 'bounds', {d:n-3*d-1 for d in mins})
        for d,v in examples.items(): print('  d',d,'max',max(Counter(v).values()),v)
