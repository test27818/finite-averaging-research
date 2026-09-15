from fractions import Fraction as F
from collections import deque
from math import gcd
for p in [7,10,11,13,17,19,23]:
 m=p-4
 targets={F(0),F(-m,3)} # infinity separately represented None
 seen=set(targets)|{None};q=deque([(z,0) for z in seen])
 # inverse A and B; B undefined at z=0? maps infinity maybe
 while q:
  z,d=q.popleft()
  if d>=10: continue
  zs=[]
  if z is None: # infinity: A inf, B=-2
   zs=[None,F(-2)]
  else:
   zs=[-m-3*z]
   if z!=0: zs.append(F(3,1)/z-2)
   else: zs.append(None)
  for zz in zs:
   if zz not in seen:seen.add(zz);q.append((zz,d+1))
 miss=[]
 B=30
 for den in range(1,B+1):
  for num in range(-B,B+1):
   if gcd(num,den)!=1:continue
   z=F(num,den)
   if (den-num)%p==0:continue
   if z not in seen:miss.append((num,den,z))
 print(p,'covered',len(seen),'miss',len(miss),'ex',miss[:5])
