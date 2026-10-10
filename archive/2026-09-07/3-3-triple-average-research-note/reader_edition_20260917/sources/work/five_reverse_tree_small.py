from math import gcd

def norm(u,v):
 d=gcd(abs(u),abs(v));u//=d;v//=d
 return (u,v) if (u>0 or (u==0 and v>=0)) else (-u,-v)

level={(1,-1)}
for d in range(9):
 print('d',d,'count',len(level))
 for p in sorted(level,key=lambda z:abs(z[0])+abs(z[1]))[:8]:
  print(p,'sum',abs(p[0])+abs(p[1]),'ratio',round(p[0]/p[1],3) if p[1] else 'inf')
 nxt=set()
 for u,v in level:
  nxt.add(norm(-3*v,u-v));nxt.add(norm(u-v,-3*v))
 level=nxt
