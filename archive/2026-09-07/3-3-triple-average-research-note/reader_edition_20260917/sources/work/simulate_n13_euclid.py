from fractions import Fraction as F
from random import Random

def run(u,v,limit=200):
    x=F(u); y=F(9*u+4*v)
    for it in range(limit):
        if x==0:return 'terminal',it,x,y
        if y==0:return 'illegal_axis',it,x,y
        # Choose the one-step return A or three-step return R by exact energy.
        ar=-y/3
        ax=x
        rr=(y-x)/12
        ry=(13*x+3*y)/4
        qa=117*ax*ax+3*ar*ar
        qr=117*rr*rr+3*ry*ry
        if qa < qr:
            x,y=ax,ar
        else:
            x,y=rr,ry
        if x==0:return 'terminal',it+1,x,y
        if y==0:return 'illegal_axis',it+1,x,y
    return 'long',limit,x,y

R=Random(11)
counts={}
for _ in range(20000):
    u=R.randrange(-1000,1001);v=R.randrange(-1000,1001)
    if (not u and not v) or (u-v)%13==0:continue
    typ,it,x,y=run(u,v)
    counts[typ]=counts.get(typ,0)+1
    if typ!='terminal':
        print('cutoff sample',u,v,it,'status',typ)
        break
print(counts)
