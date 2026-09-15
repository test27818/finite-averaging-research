from fractions import Fraction as F
import math

Q=((90,27),(27,12))
Ms={
 'A':((F(1),F(0)),(F(-3),F(-1,3))),
 'A2':((F(1),F(0)),(F(-2),F(1,9))),
 'A3':((F(1),F(0)),(F(F(-7,3)),F(-1,27))),
 'A4':((F(1),F(0)),(F(-20,9),F(1,81))),
 'R':((F(2,3),F(1,3)),(F(1),F(0))),
 'M1':((F(-1,3),F(-1,9)),(F(1),F(0))),
 'M2':((F(-1,9),F(-1,3)),(F(0),F(1))),
 'M3':((F(2,3),F(1,3)),(F(-7,3),F(-1))),
}

def q(m,t):
    a,b=m[0];c,d=m[1]
    x=a+b*t;y=c+d*t
    return 90*x*x+54*x*y+12*y*y

for name,m in Ms.items():
    roots=[]
    # sample sign changes on a dense rational grid; exact polynomial sign at samples.
    vals=[]
    grid=[-100+i/100 for i in range(20001)]
    for t in grid:
        vals.append(q(m,t)-q(((F(1),F(0)),(F(0),F(1))),t))
    intervals=[];inside=False;start=None
    for i,v in enumerate(vals):
        ok=v<0
        if ok and not inside:start=grid[i];inside=True
        if inside and (not ok or i==len(vals)-1):
            intervals.append((start,grid[i-1] if not ok else grid[i]));inside=False
    print(name,intervals)

print('coverage sample')
for t in [-100,-10,-3,-2,-1,-.5,0,.5,1,2,3,10,100]:
    good=[name for name,m in Ms.items() if q(m,t)<q(((F(1),F(0)),(F(0),F(1))),t)]
    print(t,good)
