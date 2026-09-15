from math import gcd

def norm(p):
 u,v=p; d=gcd(abs(u),abs(v));u//=d;v//=d
 return (u,v) if (u>0 or (u==0 and v>=0)) else (-u,-v)

def kids(p):
 u,v=p
 return (norm((-3*v,u-v)),norm((u-v,-3*v)))

for K in range(1,13):
 best=(10**100,None)
 B=500
 for u in range(-B,B+1):
  for v in range(-B,B+1):
   if (u,v)==(0,0) or gcd(abs(u),abs(v))!=1 or (u-v)%3==0: continue
   level={(u,v)}
   for _ in range(K):
    level={q for p in level for q in kids(p)}
   den=abs(u)+abs(v)
   for x,y in level:
    ratio=(abs(x)+abs(y))/den
    if ratio<best[0]:best=(ratio,((u,v),(x,y)))
 print(K,best)
