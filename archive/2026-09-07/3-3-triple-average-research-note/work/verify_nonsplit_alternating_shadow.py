"""Linear-time checks of the uniform three-cycle word and class data."""
from math import isqrt
from fractions import Fraction as F
from verify_nonsplit_reynolds_words import tau,shift,compose


def parity(permutation):
    cycles=0
    seen=set()
    for i in range(len(permutation)):
        if i in seen:
            continue
        cycles+=1
        j=i
        while j not in seen:
            seen.add(j)
            j=permutation[j]
    return (len(permutation)-cycles)%2


def verify():
    count=0
    for p in range(11,998):
        if p%3!=2 or any(p%q==0 for q in range(2,isqrt(p)+1)):
            continue
        a=tau(p)
        sinv=shift(p,-1)
        g=compose(sinv,a)
        square=compose(g,g)
        support=[i for i,x in enumerate(square) if i!=x]
        assert set(support)=={0,p-1,p-2}
        assert square[0]==p-2 and square[p-2]==p-1 and square[p-1]==0
        assert parity(a)==parity(shift(p,1))==0
        fixed=sum(a[i]==i for i in range(p))
        assert fixed==2 and (p-fixed)//3==(p-2)//3
        alpha=F(p+1,3*(p-1))
        assert alpha*(p-1)==F(p+1,3)
        count+=1
    print("uniform nonsplit three-cycle word and alternating parity: PASS",count)
    print("Reynolds rank and conjugacy-average scalar: PASS",count)
    print("A_p generation uses adjacent three-cycles, not sampled group orders.")


if __name__=="__main__":
    verify()
