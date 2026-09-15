from fractions import Fraction as F
from itertools import combinations_with_replacement
from collections import deque,Counter

def b_state(n):
 m=n-4;u=(F(1),F(0));v=(F(0),F(1));w=(F(-m),F(-3));return tuple(sorted([u]*m+[v]*3+[w]))
def add(vals):return(sum(x for x,y in vals),sum(y for x,y in vals))
def step(st,sig):
 q=(add(sig)[0]/3,add(sig)[1]/3);a=list(st)
 for x in sig:a.remove(x)
 a.extend([q]*3);return tuple(sorted(a))
def sigs(st):
 vals=sorted(set(st));
 for inds in combinations_with_replacement(range(len(vals)),3):
  sig=tuple(vals[i] for i in inds); c=Counter(sig)
  if all(st.count(x)>=k for x,k in c.items()) and len(c)>1:yield sig
def bparam(n,st):
 m=n-4;c=Counter(st)
 if sorted(c.values()) != sorted([1,3,m]): return None
 u=[x for x,k in c.items() if k==m][0];v=[x for x,k in c.items() if k==3][0]
 return (u,v)
for n,depth in [(13,6),(17,5)]:
 st=b_state(n);q=deque([(st,())]);seen={st};found=[]
 while q:
  s,p=q.popleft(); bp=bparam(n,s)
  if p and bp is not None and bp not in [(F(1),F(0)),(F(0),F(1))]:found.append((len(p),bp,p))
  if len(p)>=depth:continue
  for sig in sigs(s):
   ns=step(s,sig)
   if ns not in seen:
    seen.add(ns);q.append((ns,p+(sig,)))
 print('N',n,'seen',len(seen),'found',len(found))
 for x in found[:30]: print(x)
