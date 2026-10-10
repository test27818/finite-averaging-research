"""Exact checks of new teaching examples; not a full theorem verification."""
from fractions import Fraction as F
from math import gcd
from functools import reduce
from pathlib import Path
import json

def average(state,ids):
    out=list(state); v=sum(state[i] for i in ids)/len(ids)
    for i in ids:out[i]=v
    return out

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def inv(A):
    a,b=A[0];c,d=A[1];D=a*d-b*c
    return [[F(d,D),F(-b,D)],[F(-c,D),F(a,D)]]

checks={}
raw=list(map(F,[3]*5+[1,-16]));out=average(raw,(0,5,6))
assert sum(raw)==0 and reduce(gcd,(int(x-raw[0]) for x in raw))==1
assert out.count(F(3))==4 and out.count(F(-4))==3
assert all((int(x)-3)%7==0 for x in out)
checks['unsafe_move']=True
Kp=[[0,3,2],[1,2,2],[4,0,1]];Km=[[2,1,2],[3,0,2],[0,4,1]]
for K in (Kp,Km):
    assert all(sum(row)==5 for row in K)
    assert all(sum(K[i][j] for i in range(3))==5 for j in range(3))
E=[[1,0],[1,-1],[-2,1]]
assert mm(Kp,E)==[[-1,-1],[-1,0],[2,1]]
assert mm(Km,E)==[[-1,1],[-1,2],[2,-3]]
checks['five_by_fifteen_shears']=True
assert mm([[-4,5],[-5,6]],[[2],[3]])==[[7],[8]]
assert (-4)*6-5*(-5)==1
checks['exact_fiber_matrix']=True
for s,g,target in [(1,1,(1,6)),(16,2,(8,3)),(21,3,(7,2)),(6,6,(1,1))]:
    assert s%5==1 and gcd(s,1)==1 and gcd(s,6)==g
    assert (s//g,6//g)==target
checks['content_branches']=True
J0=[[F(-5,2),1],[F(55,4),F(5,2)]]
J1=[[F(-5,2),-3],[F(55,4),F(5,2)]]
assert mm(J0,J0)==[[20,0],[0,20]]
assert mm(J1,J1)==[[-35,0],[0,-35]]
T=mm(J1,inv(J0));S=[[1,0],[0,-1]]
assert T==[[F(-7,4),F(-1,2)],[0,1]]
assert mm(mm(mm(S,T),S),inv(T))==[[1,1],[0,1]]
checks['odd_return_p5_r1']=True
p,m,q=5,6,576;u,v=1,5;a=8
assert (2*a-u)%v==0
u1,v1=-a,p*v-m*a
assert (u1,v1)==(-8,-23) and gcd(u1,v1)==1 and gcd(v1,q)==1
b,eps,a1=5,-1,1997
assert (b*v1-eps)%m==0 and (2*a1-u1)%v1==0
assert (a1-(b*v1-eps)//m)%(q//m)==0 and gcd(a1,b)==1
u2,v2=-a1,b*v1-m*a1
assert (u2,v2)==(-1997,-12097) and gcd(u2,v2)==1 and (v2+1)%q==0
assert u2+307*v2==-3715776==-6451*q
checks['two_carrier_crt']=True
Jf=[[-8,383],[-1,8]];Jg=[[-8,9],[-1,8]]
assert mm(Jf,Jf)==[[-319,0],[0,-319]]
assert mm(Jg,Jg)==[[55,0],[0,55]]
Sigma=[[-1,12],[0,1]];T=mm(inv(Jf),Jg)
assert mm(mm(mm(Sigma,T),Sigma),inv(T))==[[1,F(-136,5)],[0,1]]
checks['eleven_by_thirtyfour']=True
p,s,a=83,10,14;r=p+s;n=3*p+s
source=(2*a,a,p-3*a)
stock=(p-2*source[0],p-2*source[1],r-2*source[2],p-s)
assert source==(28,14,41) and stock==(27,55,11,73)
for e,want in [(-9,(23,50,0,10)),(-8,(22,49,2,10))]:
    row=(a-e,p-3*a-e,2*a-s+2*e,s)
    assert row==want and sum(row)==p and all(0<=v<=b for v,b in zip(row,stock))
assert [3*n*x-2*p*p for x in (14,15)]==[-2900,-2123]
assert gcd(-2900,-2123)==1
checks['upper_capacity_p83']=True
x,y=7,3
assert (3*x+3*y,2*x-4*y)==(30,2)
assert (30//2,2//2)==(15,1)
assert (16*5-(5+25),-(10-30),16-(5+9))==(50,20,2)
checks['eight_descent_and_ten_quadratic']=True
assert 5+1+sum([-7,4,4,4,4])==15
checks['collision_sum']=True
result={'exact_teaching_examples':len(checks),'checks':checks,
        'scope':'Only the explicit examples newly added in the pedagogical rewrite.'}
Path(__file__).with_name('example_checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
