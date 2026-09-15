from math import gcd

def step(u,v):
    # choose the representative with |u| >= |v|; this is valid up to the A/B swap
    if abs(u) < abs(v): u,v=v,u
    if u*v < 0:
        c=abs(u-v); s=1
    else:
        c=abs(u-v); s=-1
    x,y=3*abs(v),c
    if x<y:x,y=y,x
    # choose signs only through the relation; encode canonical pair
    # reconstruct a pair whose product sign is s and difference has the sign needed
    if s<0:
        return x,-y
    return x,y

for K in range(1,9):
    best=(1e99,None)
    for a in range(1,1000):
      for b in range(1,a+1):
       for s in (-1,1):
        u,v=(a,-b) if s<0 else (a,b)
        L=a+b
        for _ in range(K):u,v=step(u,v)
        r=(abs(u)+abs(v))/L
        if r<best[0]:best=(r,(a,b,s,(u,v)))
    print(K,best)
