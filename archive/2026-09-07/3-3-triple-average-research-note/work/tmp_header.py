from fractions import Fraction as F
from itertools import combinations
from collections import deque

def b_state(n):
 m=n-4;u=(F(1),F(0));v=(F(0),F(1));w=(F(-m),F(-3));return tuple(sorted([u]*m+[v]*3+[w]))
def add(vals): return (sum(v[0] for v in vals),sum(v[1] for v in vals))
def step(st, sig):
 q=(add(sig)[0]/3,add(sig)[1]/3)
 arr=list(st)
 # remove selected values by index of matching values
 for x in sig: arr.remove(x)
 arr.extend([q]*3)
 return tuple(sorted(arr))
def sigs(st):
 # unique multisets of values size3
 vals=sorted(set(st)); out=[]
 for comb in combinations(range(len(vals)),3):
  s=[vals[i] for i in comb]
  # no repeats here; add repeats separately using combinations_with_replacement
 for i,a in enumerate(vals):
  for j in range(i,len(vals)):
   for k in range(j,len(vals)):
    if [a,j,k] is None: pass
    ss=(a,vals[j],vals[k])
    if len(st)-len([x for x in st if x in ss])<0: pass
    if st.count(a)>= (1 if i!=j and i!=k else 0): pass
 # simpler recursion
 from itertools import combinations_with_replacement
 for inds in combinations_with_replacement(range(len(vals)),3):
  ss=tuple(vals[i] for i in inds)
  need={x:ss.count(x) for x in set(ss)}
  if all(st.count(x)>=c for x,c in need.items()):
   if len(set(ss))>1: out.append(ss)
 return out
def isB(n,st):
 from collections import Counter
 c=Counter(st); m=n-4
 if m==3:
  return any(cnt==3 for cnt in c.values()) and len(c)<=3
 return [x for x,cnt in c.items() if cnt==m] and sum(cnt==3 for cnt in c.values())>=1

