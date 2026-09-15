from itertools import combinations,product
from math import gcd
from random import Random

def safe(v,n,ps):
 for S in combinations(range(n),3):
  if sum(v[i] for i in S)%3 or len({v[i] for i in S})==1:continue
  rem=[i for i in range(n) if i not in S]
  if all(len({v[i]%p for i in rem})>1 for p in ps):return True,S
 return False,None
R=Random(42);n=30
# fixed R outside U 24 positions: A 12 value 0, B12 value10, U6 positions
for trial in range(200000):
 v=[0]*12+[10]*12+[R.randrange(-50,51) for _ in range(6)]
 # arrange zero sum by adjust last
 v[-1]-=sum(v)
 # ensure p dangerous: choose F2/F5 all U? all outside U mod2/5 zero works; exceptions must nonzero in each p class to make F exact
 # if some exception 0 mod p, okay still class can include; require p classes outside U all 0 and at least one exception nonzero each
 if all(x%2==0 for x in v[24:]) or all(x%5==0 for x in v[24:]):continue
 g=gcd(*(abs(x-v[0]) for x in v[1:]))
 gg=g
 while gg%3==0:gg//=3
 if gg!=1:continue
 ok,S=safe(v,n,[2,5])
 if not ok:
  print('FOUND',v,'g',g);break
else:print('none')
