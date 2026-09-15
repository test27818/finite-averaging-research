"""Two analytic three-atom reflections; core resource only, not termination."""
from fractions import Fraction as F
from math import gcd
from verify_uniform_odd_middle_cores import mm
from verify_even_odd_half_core import I
from verify_four_prime_entry_and_band import Ledger

def reflection(p,s,keep):
    assert p>=5 and s>=(p-1)*(p-2)
    k=p*s*s;r=p*s;n=k+r+1
    d=(p-1)*s+1;j=r-d
    c=p-2 if keep=='u' else p-1
    b=d-c
    h=p*((p-1)*s+1-(s+1)*c) if keep=='u' else p*(p*s+1-(s+1)*c)
    a=h-b
    assert 0<=j<=r and 0<=a<=j+1 and 0<=b<=d and 0<=k-h<=k
    assert (j+1-a>=1 if keep=='u' else d-b>=1)
    alpha=n*h-k*(r+1);beta=k*(d-b)-d*h
    z=0 if keep=='u' else k*k
    J=(-r*alpha-k*k,-r*beta+z,-(r+k)*alpha-k*k,-(r+k)*beta+z)
    assert J[0]+J[3]==0
    lam=J[0]**2+J[1]*J[2]
    assert mm(J,J)==tuple(lam*x for x in I) and lam and gcd(lam,n)==1
    assert lam%n==pow(k,6,n)
    return (k,r,n),(j,a,b,h),(alpha,beta),J,lam

def literal(p,s,keep):
    (k,r,n),(j,a,b,h),_,J,lam=reflection(p,s,keep)
    for x,y in ((1,0),(0,1)):
        raw=[F(x)]*k+[F(x-y)]*r+[-k*x-r*(x-y)]
        led=Ledger(raw,k);groups=[list(range(k)),list(range(k,k+r)),[n-1]]
        for turn in(1,2):
            ga,gb,gc=groups
            first=ga[:k-j-1]+gb[:j]+gc;led.average(first)
            ga,gb=ga[k-j-1:],gb[j:]
            second=ga[:a]+gb[:b]+first[:k-h];led.average(second)
            ga,gb,fresh=ga[a:],gb[b:],first[k-h:]
            if keep=='u':single=ga[:1];ga=ga[1:]
            else:single=gb[:1];gb=gb[1:]
            kept=second[:r];third=ga+gb+fresh+second[r:]
            assert len(third)==k and sorted(third+kept+single)==list(range(n))
            led.average(third);groups=[third,kept,single]
            xx,yy=(F(J[0]*x+J[1]*y,k**3),F(J[2]*x+J[3]*y,k**3)) if turn==1 else (F(lam*x,k**6),F(lam*y,k**6))
            assert all(led.state[v]==value for group,value in zip(groups,(xx,xx-yy,-k*xx-r*(xx-yy))) for v in group)
        led.independent_replay(raw)

if __name__=='__main__':
    count=0
    for p in(5,7,11,13,17,19,23,29,31):
        for exponent in(2,3,4):
            for keep in('u','v'):reflection(p,p**exponent,keep);count+=1
    for keep in('u','v'):literal(5,25,keep)
    print('large-prime high-odd-exponent three-atom reflections: PASS',count)
    print('large-prime high-odd-exponent literal cycles: PASS 4')
    print('scope: reversible core resources only; roots and full reachability not proved')
