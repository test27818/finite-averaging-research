from itertools import combinations
from random import Random
from math import gcd
from collections import Counter

def primes(n):
 out=[];d=2
 while d*d<=n:
  if n%d==0:
   if d!=3:out.append(d)
   while n%d==0:n//=d
  d+=1
 if n>1 and n!=3:out.append(n)
 return out

def safe(v,n):
 ps=primes(n)
 for S in combinations(range(n),3):
  if sum(v[i] for i in S)%3:continue
  if len({v[i] for i in S})==1:continue
  rem=[i for i in range(n) if i not in S]
  if all(len({v[i]%p for i in rem})>=2 for p in ps):return True
 return False
R=Random(129)
for n in [12,14,15,16,18,20,21,22,24,26,28,30,33,35,36,39,40,42]:
 best=n; bv=None; term=0
 for _ in range(300000):
  v=[R.randrange(-20,21) for _ in range(n-1)];v.append(-sum(v));
  g=gcd(*(abs(x-v[0]) for x in v[1:]));
  if g==0:continue
  if g & (g-1): # rough; need power3
   gg=g
   while gg%3==0:gg//=3
   if gg!=1:continue
  if not safe(v,n):
   term+=1;mm=max(Counter(v).values())
   if mm<best:best=mm;bv=v
 print(n,'pr',primes(n),'terminal',term,'bestmax',best,'target n-4',n-4,'v',bv)
