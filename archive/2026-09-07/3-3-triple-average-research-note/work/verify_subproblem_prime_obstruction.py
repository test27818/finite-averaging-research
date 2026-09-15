"""Exact finite checks of the prime obstruction to bounded subproblem words.

The obstruction is proved for arbitrary length in the document. Here
coefficient vectors keep the B_n parameters symbolic, including at an
inadmissible test point (u,v)=(1,1), as a test of a matrix identity.
"""

from fractions import Fraction as F
from random import Random


def basis_state(n):
    return [(F(1), F(0))]*(n-4)+[(F(0), F(1))]*3+[(F(-(n-4)), F(-3))]


def average_block(state, indices):
    size = len(indices)
    if size == 0 or len(set(indices)) != size:
        raise ValueError("distinct nonempty block required")
    mean = tuple(sum(state[index][coordinate] for index in indices)/size
                 for coordinate in (0,1))
    result = list(state)
    for index in indices:
        result[index] = mean
    return result


def residue(value, prime):
    if value.denominator % prime == 0:
        raise ValueError("not p-integral")
    return value.numerator*pow(value.denominator, -1, prime) % prime


def check_preserved_line(n, prime, state):
    assert n % prime == 0
    assert all(residue(a+b, prime) == 1 for a,b in state)
    assert any(a or b for a,b in state)
    assert sum(a for a,b in state) == sum(b for a,b in state) == 0


def verify():
    random = Random(100917)
    checked = 0
    for n, prime in ((14,7),(15,5),(16,2),(17,17),(18,2),(34,17)):
        allowed = [size for size in range(2,n) if size % prime]
        state = basis_state(n)
        for _ in range(120):
            size = random.choice(allowed)
            state = average_block(state, random.sample(range(n),size))
            check_preserved_line(n,prime,state)
            checked += 1

    # The restriction fails exactly where the hypotheses allow it to fail:
    # averaging 15 positions may introduce 5-adic denominators.
    blocked = basis_state(15)
    annihilated = average_block(blocked, tuple(range(15)))
    assert not any(a or b for a,b in annihilated)

    # Purely combinatorial lower bound used for the one-parameter family.
    for prime in (7,13,17,19):
        for height in (8,32,128):
            directions = [(1,v) for v in range(1,height+1) if (v-1) % prime]
            assert len(directions) == height-1-(height-1)//prime
    print("prime-integral subproblem words preserve diagonal: PASS",checked)
    print("excluded prime and bounded-word counting boundary: PASS")


if __name__ == "__main__":
    verify()
