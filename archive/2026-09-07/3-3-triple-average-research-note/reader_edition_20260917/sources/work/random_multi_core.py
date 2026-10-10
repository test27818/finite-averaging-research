from random import Random
from itertools import combinations
from collections import Counter
from math import gcd
R=Random(4)
def ps(n):
 a=[];d=2;x=n
 while d*d<=x:
  if x%d==0:
   if d!=3:a.append(d)
   while x%d==0:x//=d
  d+=1
 if x>1 and x!=3:a.append(x)
 return a
def safe(v,n,P):
 for S in combinations(range(n),3):
  if sum(v[i] for i in S)%3 or len({v[i] for i in S})==1:continue
  rem=[i for i in range(n) if i not in S]
  if all(len({v[i]%p for i in rem})>1 for p in P):return 1
 return 0
def pow3(g):
 while g%3==0:g//=3
 return g==1
for n in [14,15,18,20,21,22,24,26,28,30,35,36,40,42,45,60,70,84,90,105]:
 P=ps(n); checked=term=0
 for _ in range(3000):
  v=[R.randrange(-100,101) for _ in range(n-1)];v.append(-sum(v));
  g=gcd(*(abs(x-v[0]) for x in v[1:]));
  if not pow3(g):continue
  checked+=1
  if not safe(v,n,P):
   term+=1
   D=sum(max(Counter(x%p for x in v).values())>=n-3 for p in P)
   assert max(Counter(v).values())>=n-3*D-1,(n,v,D)
 print(n,'checked',checked,'terminal',term)
