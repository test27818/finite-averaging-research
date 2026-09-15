from math import gcd

def prim(u,v):
    d=gcd(abs(u),abs(v)); u//=d;v//=d
    return (u,v) if (u>0 or (u==0 and v>=0)) else (-u,-v)

def run(u,v,limit=100):
    u,v=prim(u,v); start=(u,v); steps=0
    while steps<limit and u+v and ((u%3==0 and u) or (v%3==0 and v)):
        if u%3==0 and u and v%3:
            q=u//3;u,v=prim(v-q,-q)
        elif v%3==0 and v and u%3:
            q=v//3;u,v=prim(u-q,-q)
        else: break
        steps+=1
    return start,(u,v),steps

for B in [30,100,300,1000]:
    best=(-1,None)
    for u in range(-B,B+1):
      for v in range(-B,B+1):
       if not u and not v or gcd(abs(u),abs(v))!=1: continue
       s,t,k=run(u,v)
       if k and t[0]+t[1]!=0:
        ratio=(abs(t[0])+abs(t[1]))/(abs(s[0])+abs(s[1]))
        if ratio>best[0]:best=(ratio,(s,t,k))
    print(B,best)
