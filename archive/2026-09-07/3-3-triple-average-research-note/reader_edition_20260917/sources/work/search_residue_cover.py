from itertools import combinations
from random import Random
from math import prod

def prime_divs(n):
 out=[];d=2;x=n
 while d*d<=x:
  if x%d==0:
   if d!=3:out.append(d)
   while x%d==0:x//=d
  d+=1
 if x>1 and x!=3:out.append(x)
 return out

def safe_res(res3, rp, n):
 ps=list(rp)
 for S in combinations(range(n),3):
  if sum(res3[i] for i in S)%3:continue
  ok=True
  for p,vals in rp.items():
   rem=[i for i in range(n) if i not in S]
   if len(set(vals[i] for i in rem))<2:ok=False;break
  if ok:return S
 return None
R=Random(901)
for n in [14,15,21,22,26,30,35,39,55,70,77,105]:
 ps=prime_divs(n)
 best=None
 for trial in range(200000):
  res3=[R.randrange(3) for _ in range(n)]
  rp={}
  for p in ps:
   # choose f=2 or3 random; dominant residue 0
   f=R.choice([2,3])
   F=set(R.sample(range(n),f))
   vals=[0]*n
   for i in F: vals[i]=R.randrange(1,p)
   rp[p]=vals
  if safe_res(res3,rp,n) is None:
   best=(res3,rp);break
 print('n',n,'ps',ps,'found',bool(best))
 if best:
  print('f',[(p,len(set(v))-1) for p,v in best[1].items()]);break
