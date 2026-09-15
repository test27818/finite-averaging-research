from math import gcd

def kids(u,v): return [(-3*v,u-v),(u-v,-3*v)]
def norm(u,v):
 d=gcd(abs(u),abs(v));u//=d;v//=d
 return (u,v) if (u>0 or (u==0 and v>=0)) else (-u,-v)
for k in range(1,5):
 best=(1e9,None)
 for u in range(-100,101):
  for v in range(-100,101):
   if (u,v)==(0,0) or gcd(abs(u),abs(v))!=1 or (u-v)%3==0:continue
   s=abs(u)+abs(v); L=[(u,v)]
   for _ in range(k):L=[norm(*z) for x in L for z in kids(*x)]
   r=min((abs(x)+abs(y))/s for x,y in L)
   if r<best[0]:best=(r,((u,v),L[0]))
 print(k,best)
