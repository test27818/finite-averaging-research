from fractions import Fraction as F
from math import gcd

def mm(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
T=((F(1),F(0)),(F(9),F(4))); Ti=((F(1),F(0)),(F(-9,4),F(1,4)))
Ms={
 'M1':((F(-1,3),F(-1,9)),(F(1),F(0))),
 'M2':((F(-1,9),F(-1,3)),(F(0),F(1))),
 'M3':((F(2,3),F(1,3)),(F(-7,3),F(-1))),
 'R':((F(2,3),F(1,3)),(F(1),F(0))),
 'A':((F(1),F(0)),(F(-3),F(-1,3))),
}
for name,M in Ms.items():
 print(name,mm(T,mm(M,Ti)))

def prim(a,b):
 g=gcd(abs(a),abs(b)); return (a//g,b//g,g)
def h(x,y):
 d=gcd(4,y-9*x);return 4//d
def Q(x,y):return 117*x*x+3*y*y
for name,M in Ms.items():
 print('---',name)
 for x in range(-20,21):
  for y in range(-20,21):
   if (x,y)==(0,0) or (y- x)%4:continue
   # M in xy
   N=mm(T,mm(M,Ti)); X=N[0][0]*x+N[0][1]*y;Y=N[1][0]*x+N[1][1]*y
   den=1
   for z in [X,Y]:den=max(den,z.denominator)
   a,b,g=prim(int(X*den),int(Y*den))
   # ratio normalized homogeneous use rational output direct; h of prim
   rr=float(F(h(a,b)**2*Q(a,b), h(x,y)**2*Q(x,y)))
   if rr>=1.00001:
    print('nondecrease',x,y,rr,'out',a,b,'h',h(a,b),'den',den);break
