from math import gcd
from random import Random

def val3(x):
 x=abs(x);k=0
 while x and x%3==0:k+=1;x//=3
 return k

def step(u,v):
 # A successful recursive step. The divisible coordinate becomes the
 # second coordinate, so a cascade subsequently uses B until it is spent.
 if u and u%3==0 and v%3:
  q=u//3
  return v-q,-q
 if v and v%3==0 and u%3:
  q=v//3
  return u-q,-q
 return None

def cascade(u,v):
 # exact recursion until the active divisible coordinate has been consumed
 first=step(u,v)
 if first is None:
  return None
 u,v=first
 k=1
 while v and v%3==0:
  following=step(u,v)
  assert following is not None
  u,v=following
  k+=1
 return u,v,k

R=Random(10)
samples=[(u,v) for u in range(-300,301) for v in range(-300,301)]
samples += [(R.randrange(-100000,100001), R.randrange(-100000,100001)) for _ in range(10000)]
for u,v in samples:
 if (u,v)==(0,0) or gcd(abs(u),abs(v))!=1:continue
 if u%3 and v%3:continue
 result=cascade(u,v)
 if result is None:continue
 x,y,k=result
 # If a=3^k t is the active coordinate and b is the other coordinate,
 # C_k(a,b)=(b-d_k t,(-1)^k t).
 active,other=(u,v) if u%3==0 else (v,u)
 t=active//(3**k)
 d=(3**k+(-1)**(k-1))//4
 assert (x,y)==(other-d*t,(-1)**k*t)
 # if continuation exists, apply next cascade and test 7/9 bound
 next_result=cascade(x,y)
 if next_result is not None:
  z,w,l=next_result
  assert max(abs(z),abs(w))*9 <= 7*max(abs(u),abs(v))
print('correct cascade formula and two-cascade bound passed')
