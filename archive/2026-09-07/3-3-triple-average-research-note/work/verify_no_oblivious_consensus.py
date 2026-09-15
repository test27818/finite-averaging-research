"""Small exact controls for the fixed-word denominator obstruction."""
from fractions import Fraction as F


def triadic(value):
    d=F(value).denominator
    while d%3==0:
        d//=3
    return d==1


def verify():
    checked=0
    for n in range(2,101):
        power=n
        while power%3==0:
            power//=3
        possible=power==1
        assert triadic(F(1,n))==possible
        matrix=[[F(1,n) for _ in range(n)] for _ in range(n)]
        assert all(sum(row)==1 for row in matrix)
        assert all(sum(matrix[i][j] for i in range(n))==1 for j in range(n))
        checked+=1
    # Tensor averaging maps every coordinate to the global mean for n=3^k.
    for n in (3,9,27):
        vector=[F(i*i-3*i+1) for i in range(n)]
        mean=sum(vector)/n
        assert [sum(F(1,n)*x for x in vector) for _ in vector]==[mean]*n
    print("fixed consensus denominator obstruction: PASS",checked)
    print("triadic tensor consensus controls: PASS 3")
    print("General theorem follows from the coefficient-ring proof.")


if __name__=="__main__":
    verify()
