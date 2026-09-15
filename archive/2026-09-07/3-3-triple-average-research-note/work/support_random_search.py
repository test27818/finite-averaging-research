from collections import deque
from itertools import combinations
from math import gcd
from random import Random

CHOICES={n:list(combinations(range(n),3)) for n in range(5,8)}
def prim(s):
 d=0
 for x in s:d=gcd(d,abs(x))
 if d:s=tuple(x//d for x in s)
 t=tuple(-x for x in s)
 return min(s,t)
def step(s,c):
 z=sum(s[i] for i in c);C=set(c)
 return prim(tuple(z if i in C else 3*s[i] for i in range(len(s)))),z%3==0
def supp(s):return {i for i,x in enumerate(s) if x%3}
def shortest(s,limit=7):
 init=supp(s); Q=deque([(s,0)]);D={(s,0):0};P={};
 while Q:
  x,p=Q.popleft();d=D[(x,p)]
  if not any(x):
   path=[]; k=(x,p)
   while k in P:path.append(P[k][1]);k=P[k][0]
   return d,list(reversed(path))
  if d==limit:continue
  for c in CHOICES[len(s)]:
   y,l=step(x,c);q=p or l;key=(y,int(q))
   if key not in D:
    D[key]=d+1;P[key]=((x,p),c);Q.append(key)
 return None
def first(s,path):
 x=s;T=supp(s)
 for j,c in enumerate(path,1):
  y,l=step(x,c)
  if l:return j,c,'T' if set(c)==T else 'disj' if not (set(c)&T) else 'mixed'
  x=y
for n in (6,7):
 R=Random(4);count={}
 for _ in range(300):
  while True:
   vals=[R.randrange(-15,16) for _ in range(n-1)];vals.append(-sum(vals));s=tuple(vals)
   if gcd(*[abs(x) for x in s])!=1 or len(supp(s))!=3:continue
   break
  z=shortest(prim(s),8)
  if z:
   k=first(prim(s),z[1]);count[k[2]]=count.get(k[2],0)+1
   if k[2]=='mixed':print('MIXED',n,s,z,k);break
 print(n,count)
