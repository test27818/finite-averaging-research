from math import gcd

def kids(u,v): return [(-3*v,u-v),(u-v,-3*v)]
def norm(u,v):
 d=gcd(abs(u),abs(v));u//=d;v//=d
 return (u,v) if (u>0 or (u==0 and v>=0)) else (-u,-v)
best={1:(1e9,None),2:(1e9,None),3:(1e9,None),4:(1e9,None)}
for u in range(-2000,2001):
 for v in range(-2000,2001):
  if (u,v)==(0,0) or gcd(abs(u),abs(v))!=1 or (u-v)%3==0:continue
  s=abs(u)+abs(v);L=[(u,v)]
  for k in range(1,5):
   L=[norm(*z) for x in L for z in kids(*x)]
   # use minimum among branches; they actually agree up to swap
   r=min((abs(x)+abs(y))/s for x,y in L)
   if r<best[k][0]:best[k]=(r,((u,v),L[0]))
print(best)
