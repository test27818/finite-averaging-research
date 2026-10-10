from itertools import combinations_with_replacement,combinations
from collections import Counter
from math import gcd

def power3(g):
 if g==0:return False
 while g%3==0:g//=3
 return g==1

def safe(v):
 n=len(v);ps=[];x=n;d=2
 while d*d<=x:
  if x%d==0:
   if d!=3:ps.append(d)
   while x%d==0:x//=d
  d+=1
 if x>1 and x!=3:ps.append(x)
 for S in combinations(range(n),3):
  if sum(v[i] for i in S)%3 or len({v[i] for i in S})==1:continue
  rem=[i for i in range(n) if i not in S]
  if all(len({v[i]%p for i in rem})>1 for p in ps):return True
 return False
for n in [12,14,15,16,18,20,21,22,24,25,26,28,30]:
 cnt=term=0;best=n;bv=None
 for v in combinations_with_replacement(range(-3,4),n):
  if sum(v)!=0 or not any(v):continue
  g=gcd(*(abs(v[i]-v[0]) for i in range(1,n)))
  if not power3(g):continue
  cnt+=1
  if not safe(v):
   term+=1;m=max(Counter(v).values())
   if m<best:best=m;bv=v
 print(n,'legal',cnt,'terminal',term,'best',best,'target',n-4,bv)
