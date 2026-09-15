from collections import Counter
from itertools import combinations_with_replacement
from math import gcd
from construct_five_exception_core import build

def prim_g(values):
    g=0
    for x in values:g=gcd(g,abs(x))
    vals=[x//g for x in values] if g else values
    h=0
    for x in vals[1:]:h=gcd(h,abs(x-vals[0]))
    return g,h

def main():
    n,u,e,F=build(); c=Counter(e); c[u]=n-5
    vals=sorted(c)
    for inds in combinations_with_replacement(range(len(vals)),3):
        s=tuple(vals[i] for i in inds)
        need=Counter(s)
        if any(c[x]<k for x,k in need.items()) or len(set(s))==1 or sum(s)%3:continue
        q=sum(s)//3
        out=c.copy()
        for x,k in need.items():out[x]-=k
        out[q]+=3
        cg,h=prim_g([x for x,k in out.items() if k>0])
        if h==1:
            print('G-preserving candidate',s,'q',q,'common',cg)
        else:
            print('changes G',s,'q',q,'common',cg,'G',h)

if __name__=='__main__':main()
