"""A fixed family k=2(4^b-1)/3,n=4^b; no search."""
from fractions import Fraction as F
from verify_four_prime_entry_and_band import Ledger

def word(b):
    m=2*b;n=2**m;h=(n-1)//3;k=2*h
    first=list(range(k));outside=list(range(k,n))
    second=first[:h-1]+outside
    old=first[h-1:];singleton=old[-1]
    blocks=[old[:-1],second[:h],second[h:]]
    assert all(len(g)==h for g in blocks)
    ops=[first,second]
    for step in range(m-1):
        i,j=step%3,(step+1)%3
        ops.append(blocks[i]+blocks[j])
    untouched=(m-2+2)%3
    leftover=blocks[untouched]+[singleton]
    chosen=[z for i,g in enumerate(blocks) if i!=untouched for z in g][:h-1]
    ops.append(leftover+chosen)
    assert len(ops)==m+2 and all(len(set(g))==len(g)==k for g in ops)
    return k,n,ops

def main():
    columns=0
    for b in(1,2,3):
        k,n,ops=word(b)
        for col in range(n):
            raw=[F(int(i==col)) for i in range(n)];led=Ledger(raw,k)
            for group in ops:led.average(group)
            assert led.state==[F(1,n)]*n
            led.independent_replay(raw);columns+=1
    for b in range(1,41):
        m=2*b;n=2**m;h=(n-1)//3
        x=F(0);previous=F(1)
        for j in range(1,m):previous,x=x,(x+previous)/2
        assert x==F(h+1,n)
        assert h*previous+1==(h+1)*x
    print('dyadic three-block fixed networks exact basis: PASS',columns)
    print('dyadic three-block general recurrence: PASS 40')
    k,n,ops=word(2)
    assert (k,n,len(ops))==(10,16,6)
    print('ten-average sixteen-position universal six-step network: PASS')

if __name__=='__main__':main()
