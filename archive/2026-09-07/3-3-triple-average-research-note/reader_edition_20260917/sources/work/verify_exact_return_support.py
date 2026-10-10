"""Exact stochastic relaxation and monotone carrier support checks."""
from fractions import Fraction as F
from itertools import combinations


def verify():
    count = 0
    for m in range(7,60):
        for mass in (F(1),F(3,2),F(2),F(5,2),F(3)):
            t = mass/m
            x = [F(1-t,m)]*m+[t/3]*3+[F(0)]
            y = [F(m*t-1,3*m)]*m+[F(3-m*t,9)]*3+[F(1,3)]
            u = [F(1,m)]*m+[F(0)]*4
            matrix = [x]*m+[y]*3+[u]
            assert all(min(row)>=0 and sum(row)==1 for row in matrix)
            assert all(sum(row[j] for row in matrix)==1 for j in range(m+4))
            coeff = [(sum(row[:m])-m*row[-1],sum(row[m:m+3])-3*row[-1])
                     for row in matrix]
            assert coeff == [(1-t,t)]*m+[(-(m*(1-t)+1)/3,-m*t/3)]*3+[(1,0)]
            assert [i for i,row in enumerate(matrix) if row[-1]>0] == list(range(m,m+3))
            count += 1
    for values in ([F(1)]+[F(0)]*6,[F(1,3)]*3+[F(0)]*4):
        old = {i for i,x in enumerate(values) if x}
        for triple in combinations(range(7),3):
            following = list(values)
            mean = sum(values[i] for i in triple)/3
            for i in triple:
                following[i] = mean
            assert old <= {i for i,x in enumerate(following) if x}
    print("exact-return stochastic lifts and carrier support: PASS",count)
    print("No finite ternary factorization sufficiency is asserted.")


if __name__ == "__main__":
    verify()
