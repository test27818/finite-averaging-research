"""Exact elementary controls for polynomial Bezout specialization."""
from math import gcd


def evaluate(coefficients,x):
    value = 0
    for coefficient in reversed(coefficients):
        value = value*x+coefficient
    return value


def verify():
    # (X+1)-(X-1)=2: every specialized gcd divides the fixed Bezout integer2.
    f,g = (-1,1),(1,1)
    for x in range(-500,501):
        assert evaluate(g,x)-evaluate(f,x) == 2
        assert 2%gcd(abs(evaluate(f,x)),abs(evaluate(g,x))) == 0
    # Consecutive templates have Delta=1 and hence no specialization exception.
    f,g = (0,1),(1,1)
    for x in range(-500,501):
        assert evaluate(g,x)-evaluate(f,x) == 1
        assert gcd(abs(evaluate(f,x)),abs(evaluate(g,x))) == 1
    # A common polynomial factor creates unbounded specialization factors.
    f,g = (-1,0,1),(-2,1,1)  # (X-1)(X+1), (X-1)(X+2)
    for x in range(2,100):
        assert gcd(abs(evaluate(f,x)),abs(evaluate(g,x)))%(x-1) == 0
    print("polynomial Bezout specialization and common-factor boundary: PASS 2100")
    print("General finite-exception theorem follows from Q[X] Bezout, not sampling.")


if __name__ == "__main__":
    verify()
