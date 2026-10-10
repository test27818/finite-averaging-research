from fractions import Fraction as F
from itertools import combinations_with_replacement
from collections import Counter,deque

def choices(st):
 vals=sorted(set(st))
 for inds in combinations_with_replacement(range(len(vals)),3):
  sig=tuple(vals[i] for i in inds);c=Counter(sig)
  if all(st.count(x)>=k for x,k in c.items()) and len(c)>1:yield sig

def step(st,sig):
 q=sum(sig,F(0))/3;a=list(st)
 for x in sig:a.remove(x)
 a.extend([q]*3);return tuple(sorted(a))
def search(p,D):
 st=tuple([F(1)]*(p-4)+[F(-(p-4)),F(0),F(0),F(0)])
 q=deque([(st,())]);seen={st}
 while q:
  s,path=q.popleft()
  if all(x==0 for x in s): return len(path),path,len(seen)
  if len(path)>=D:continue
  for sig in choices(s):
   ns=step(s,sig)
   if ns not in seen: seen.add(ns);q.append((ns,path+(sig,)))
 return None,None,len(seen)
for p in [7,11,13,17,19]:
 for d in [4,6,8]:
  out=search(p,d);print(p,d,out[0],out[2])
  if out[0]:print(out[1]);break
