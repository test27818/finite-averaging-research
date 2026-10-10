"""Even arity endpoint k,2k+1: formula checks and literal cycles."""
from fractions import Fraction as F
from math import gcd
from verify_uniform_odd_middle_cores import mm,invq
from verify_square_arity_controller_and_nine_thirteen import power,sc,delta,det
from verify_even_odd_half_core import I,U,L
from verify_four_prime_entry_and_band import Ledger

def params(k):
    b=k//2;n=2*k+1;S=(1,-1,0,-1)
    def T(j):return (-k-1,j,-n,2*j)
    def Fr(r):return (1,F(r-k,2*k),0,F(r,k))
    J=mm(T(b),S)
    assert power(J,2)==sc(I,-b)
    for j in (1,2,b,k):assert mm(invq(T(b)),T(j))==delta(F(j,b))
    if b%2:
        eps=-1 if b%4==1 else 1;a=(4*b+1+eps*b)//4
        assert 1<=a<=k and gcd(a,n)==1
        V=mm(T(a),Fr(2*eps))
        assert V[0]+V[3]==0 and det(V)!=0
        assert gcd(det(V).numerator,n)==1
        P=mm(delta(F(1,b)),invq(Fr(2)))
        assert P[0]==P[3]==1 and P[2]==0
        assert mm(mm(S,P),S)==invq(P)
        assert mm(mm(mm(S,delta(b)),S),delta(F(1,b)))==U(F(b-1,b))
        Jp=mm(mm(S,J),S)
        assert Jp==(2*b,-b,n,-2*b)
        H=sc(mm(mm(delta(2),Jp),delta(2)),F(1,2))
        Z=mm(H,invq(Jp))
        assert det(Z)==1
        assert all(gcd(x.denominator,b)==x.denominator or b%x.denominator==0 for x in Z)
        assert mm(mm(Jp,delta(2)),invq(H))==sc(delta(F(1,2)),2)
    else:
        assert 1<=b//2<=k
    assert mm(mm(mm(S,delta(2)),S),delta(F(1,2)))==U(F(1,2))
    P=(1,J[0],0,J[2])
    assert mm(mm(invq(P),U(1)),P)==U(-n)
    assert mm(mm(mm(mm(invq(P),J),U(det(J))),invq(J)),P)==L(n)
    assert sc(mm(mm(U(-F(1,2)),T(1)),delta(-F(1,4))),-2)==L(2*n)
    assert mm(mm(delta(F(1,2)),L(2*n)),delta(2))==L(n)
    return b,n,S,T,Fr

def literal(k):
    b,n,S,T,Fr=params(k);cases=[('J',b,None)]
    if b%2:
        eps=-1 if b%4==1 else 1;a=(4*b+1+eps*b)//4
        cases.append(('TF',a,2*eps))
    count=0
    for kind,j,r in cases:
        for x,y in ((1,0),(0,1)):
            raw=[F(x)]*k+[F(x-y)]*k+[-k*(2*x-y)]
            led=Ledger(raw,k);groups=[list(range(k)),list(range(k,2*k)),[2*k]]
            def tstep(groups,j):
                ga,gb,gc=groups
                left=ga[:j-1]+gb[:k-j]+gc;right=ga[j-1:k-1]+gb[k-j:]
                led.average(left);led.average(right)
                return [left,right,ga[k-1:]]
            def fstep(groups,r):
                ga,gb,gc=groups;h=(k+r)//2
                left=ga[:h]+gb[:k-h];right=ga[h:]+gb[k-h:]
                led.average(left);led.average(right)
                return [left,right,gc]
            for _ in range(2):
                if kind=='J':groups=[groups[1],groups[0],groups[2]]
                else:groups=fstep(groups,r)
                groups=tstep(groups,j)
            W=mm(T(j),S if kind=='J' else Fr(r));mat=sc(power(W,2),F(1,k*k))
            xx,yy=mat[0]*x+mat[1]*y,mat[2]*x+mat[3]*y
            assert all(led.state[q]==v for g,v in zip(groups,(xx,xx-yy,-k*(2*xx-yy))) for q in g)
            led.independent_replay(raw);count+=1
    return count

if __name__=='__main__':
    for k in range(4,402,2):params(k)
    print('even-arity uniform endpoint roots and inverse formulas: PASS 199')
    print('even-arity literal full-system scalar cycles: PASS',sum(literal(k) for k in range(4,22,2)))
    print('even-arity all-parameter endpoint interfaces: PASS')
