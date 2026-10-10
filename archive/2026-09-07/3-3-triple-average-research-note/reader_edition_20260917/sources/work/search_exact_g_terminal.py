from collections import Counter
from itertools import combinations, combinations_with_replacement
from math import gcd

def ps(n):
    out=[];d=2;x=n
    while d*d<=x:
        if x%d==0:
            if d!=3:out.append(d)
            while x%d==0:x//=d
        d+=1
    if x>1 and x!=3:out.append(x)
    return out
def is3(g):
    if not g:return False
    while g%3==0:g//=3
    return g==1
def norm_g(values):
    d=0
    for x in values:d=gcd(d,abs(x))
    if not d:return 0
    w=[x//d for x in values]
    h=0
    for x in w[1:]:h=gcd(h,abs(x-w[0]))
    return h
def has_g_move(v):
    n=len(v); vals=sorted(set(v)); c=Counter(v)
    for inds in combinations_with_replacement(range(len(vals)),3):
        s=tuple(vals[i] for i in inds); need=Counter(s)
        if len(set(s))==1 or sum(s)%3:continue
        if any(c[x]<k for x,k in need.items()):continue
        out=c.copy()
        for x,k in need.items():out[x]-=k
        out[sum(s)//3]+=3
        w=[]
        for x,k in out.items():
            if k>0:w.append(x)
        if is3(norm_g(w)):return True,s,norm_g(w)
    return False,None,None

for n,R in [(7,8),(8,8),(9,7),(10,7),(11,7),(12,6),(13,6),(14,5),(15,5)]:
    count=0; terminal=0; ex=None
    for v in combinations_with_replacement(range(-R,R+1),n):
        if sum(v)!=0 or not any(v):continue
        if not is3(norm_g(v)):continue
        count+=1
        ok,s,g=has_g_move(v)
        if not ok:
            terminal+=1
            if ex is None:ex=v
    print(n,'legal',count,'exact G-terminal',terminal,'example',ex,flush=True)
