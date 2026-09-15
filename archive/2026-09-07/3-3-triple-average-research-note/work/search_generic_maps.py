from fractions import Fraction as F
from itertools import combinations_with_replacement
from collections import Counter,deque

def bstate(n):
 m=n-4;return tuple(sorted([(F(1),F(0))]*m+[(F(0),F(1))]*3+[(F(-m),F(-3))]))
def add(s):return(sum(x for x,y in s),sum(y for x,y in s))
def step(st,sig):
 q=tuple(x/3 for x in add(sig));a=list(st)
 for x in sig:a.remove(x)
 a += [q]*3;return tuple(sorted(a))
def choices(st):
 vals=sorted(set(st))
 for inds in combinations_with_replacement(range(len(vals)),3):
  sig=tuple(vals[i] for i in inds);c=Counter(sig)
  if len(c)>1 and all(st.count(x)>=k for x,k in c.items()):yield sig
def params(n,st):
 c=Counter(st);m=n-4
 us=[x for x,k in c.items() if k==m]
 vs=[x for x,k in c.items() if k==3]
 if len(us)==1 and len(vs)==1 and len(c)==3:return us[0],vs[0]
 return None
def search(n,D):
 st=bstate(n);q=deque([(st,())]);seen={st};out={}
 while q:
  s,p=q.popleft();bp=params(n,s)
  if p and bp:out.setdefault(bp,p)
  if len(p)>=D:continue
  for sig in choices(s):
   ns=step(s,sig)
   if ns not in seen:seen.add(ns);q.append((ns,p+(sig,)))
 return out,len(seen)
for n in [13,17,19,23]:
 out,c=search(n,4);print('N',n,'states',c,'returns',len(out))
 # print only maps with x coefficient not 0/1 and depth <=4
 for (u,v),path in list(out.items())[:100]:
  if len(path)<=4 and (u not in [(F(1),F(0)),(F(0),F(1))]): print(' ',len(path),u,v)
