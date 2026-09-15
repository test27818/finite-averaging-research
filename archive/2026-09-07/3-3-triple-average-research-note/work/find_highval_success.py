from math import gcd

def d(u,v):
 seen=set(); k=0
 while (u,v) not in seen and k<100:
  seen.add((u,v))
  if u+v==0:return True,k
  if u%3==0 and u and v%3:
   q=u//3
   if q%3==0: print('high', (u,v),'q',q,'v3',val(q), 'step',k)
   u,v=v-q,-q
  elif v%3==0 and v and u%3:
   q=v//3
   if q%3==0: print('high', (u,v),'q',q,'v3',val(q), 'step',k)
   u,v=u-q,-q
  else:return False,k
  k+=1
 return False,k
def val(q):
 q=abs(q);c=0
 while q and q%3==0:c+=1;q//=3
 return c
for u in range(-1000,1001):
 for v in range(-1000,1001):
  if (u,v)==(0,0) or gcd(abs(u),abs(v))!=1:continue
  ok,k=d(u,v)
