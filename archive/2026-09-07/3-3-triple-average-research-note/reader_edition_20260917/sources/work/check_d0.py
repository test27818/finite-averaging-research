from itertools import combinations_with_replacement,combinations
from collections import Counter
from math import gcd
for n in [7,8,9,10,11,12,13]:
 ps=[];x=n;d=2
 while d*d<=x:
  if x%d==0:
   if d!=3:ps.append(d)
   while x%d==0:x//=d
  d+=1
 if x>1 and x!=3:ps.append(x)
 count=0
 for v in combinations_with_replacement(range(-2,3),n):
  if sum(v)!=0:continue
  g=gcd(*(abs(x-v[0]) for x in v[1:]))
  gg=g
  while gg and gg%3==0:gg//=3
  if not gg:continue
  if gg!=1:continue
  safe=False
  for S in combinations(range(n),3):
   if sum(v[i] for i in S)%3 or len({v[i] for i in S})==1:continue
   rem=[i for i in range(n) if i not in S]
   if all(len({v[i]%p for i in rem})>=2 for p in ps):safe=True;break
  if not safe:
   count+=1
   if max(Counter(v).values())<n:print('terminal',n,v,ps);break
 print(n,count)
