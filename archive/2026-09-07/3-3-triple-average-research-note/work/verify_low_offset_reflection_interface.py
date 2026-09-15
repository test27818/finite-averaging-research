"""Exact trace-zero count interface for every low upper remainder.

For each first-row count pair, one modular inverse determines the only possible
fresh-block count. No word search or enumeration of p-subsets is used.
"""
from fractions import Fraction as F
from math import gcd

from verify_four_prime_entry_and_band import factors, Ledger
from verify_uniform_odd_middle_cores import mm, invq, residue


def feasible(p, s):
    n = 3*p+s
    for b in range(1, s+1):
        for t in range(p-b+1):
            alpha, beta = p-3*t-b, s*t-p*b
            if alpha % p == 0:
                continue  # b>0,s<p implies beta !=0 modp here.
            v = beta*pow(alpha, -1, p) % p
            if 2*v > p-s:
                continue
            for u in range((s-b)//2+1):
                num = p*p+p*b-s*t-p*u-(3*t+b)*v
                if num % (3*p):
                    continue
                y = num//(3*p)
                x = p-y-u-v
                if min(x, y) < 0 or 2*x > p+t+b or 2*y > p-t:
                    continue
                q = p*s*y-p*p*u+v*beta
                j = (beta, q, -alpha, -beta)
                lam = beta*beta-alpha*q
                assert mm(j,j) == (lam,0,0,lam) and gcd(lam,n)==1
                assert lam % n == pow(p,4,n)
                assert ((3*t+b)*(3*v+s)-b*s) % p == 0
                yield (b,t,x,y,u,v), j, lam


def replay(p,s,counts,j,lam):
    b,t,x,y,u,v=counts
    n=3*p+s
    for a,z in ((1,0),(0,1)):
        raw=[a]*(2*p)+[-2*a+s*z]*p+[-p*z]*s
        ledger=Ledger(raw,p)
        groups=[list(range(2*p)),list(range(2*p,3*p)),list(range(3*p,n))]
        for stage in range(2):
            ga,gb,gc=groups
            i=p-t-b
            fresh=ga[:i]+gb[:t]+gc[:b]
            ledger.average(fresh)
            ga,gb,gc=ga[i:],gb[t:],gc[b:]
            kept,fresh=fresh[:s],fresh[s:]
            left=ga[:x]+gb[:y]+gc[:u]+fresh[:v]
            right=ga[x:2*x]+gb[y:2*y]+gc[u:2*u]+fresh[v:2*v]
            other=ga[2*x:]+gb[2*y:]+gc[2*u:]+fresh[2*v:]
            assert sorted(left+right+other+kept)==list(range(n))
            for group in (left,right,other): ledger.average(group)
            groups=[left+right,other,kept]
            av,zv=(F(j[0]*a+j[1]*z,p*p),F(j[2]*a+j[3]*z,p*p)) if stage==0 else (F(lam*a,p**4),F(lam*z,p**4))
            assert all(ledger.state[index]==value
                       for group,value in zip(groups,(av,-2*av+s*zv,-p*zv))
                       for index in group)
        ledger.independent_replay(raw)


def main():
    total=literal=0
    rows=[]
    for p in range(11,104):
        if factors(p)!={p:1}: continue
        amounts=[]
        for s in range(1,10):
            candidates=list(feasible(p,s))
            total+=len(candidates)
            amounts.append(len(candidates))
            if p<=23 and candidates:
                replay(p,s,*candidates[0])
                literal+=2
        rows.append((p,amounts))
    for p in (11,13,17,19):
        print("count-interface",next(row for row in rows if row[0]==p))
    print("low-offset modular-hyperbola reflection identities: PASS",total)
    print("low-offset literal four-atom scalar returns: PASS",literal)
    print("low-offset reflection-interface scope only: PASS")


if __name__=="__main__":main()

