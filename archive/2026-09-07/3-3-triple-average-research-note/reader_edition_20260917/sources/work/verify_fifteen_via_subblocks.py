"""Exact interfaces for B15 -> a legal 12-subproblem -> legal 10-subproblem.

The 10/12 equalizations invoke existing theorems, not new atomic operations.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import combinations_with_replacement
from math import gcd, lcm


def at_prime(value, prime):
    value = F(value)
    return value.numerator * pow(value.denominator, -1, prime) % prime


def is_three_power(value):
    if value <= 0:
        return False
    while value % 3 == 0:
        value //= 3
    return value == 1


def centered_g(values):
    mean = sum(values, F(0))/len(values)
    denominator = lcm(*(F(value-mean).denominator for value in values))
    integers = [int((value-mean)*denominator) for value in values]
    content = gcd(*integers)
    if not content:
        return 0
    primitive = [value//content for value in integers]
    return gcd(*(value-primitive[0] for value in primitive))


def local_lattice_formula(integers):
    anchor = integers[0]
    content = gcd(*(value-anchor for value in integers))
    if not content:
        return 0
    total = sum((value-anchor)//content for value in integers)
    return len(integers)//gcd(len(integers), total)


def core(u, v):
    values = [F(u)]*11+[F(v)]*3+[-11*F(u)-3*F(v)]
    return Counter(values)


def actual_average(state, triple):
    for value, count in Counter(triple).items():
        assert state[value] >= count
    following = state.copy()
    for value in triple:
        following[value] -= 1
        if not following[value]:
            del following[value]
    following[sum(triple, F(0))/3] += 3
    return following


def invoke_solved_block(state, values, allowed_size):
    """Check a proved local criterion, then record the contracted state."""
    assert len(values) == allowed_size and allowed_size in (10, 12)
    local = centered_g(values)
    assert local == 0 or is_three_power(local)
    mean = sum(values, F(0))/len(values)
    assert is_three_power(mean.denominator)
    following = state.copy()
    for value, count in Counter(values).items():
        assert following[value] >= count
        following[value] -= count
        if not following[value]:
            del following[value]
    following[mean] += len(values)
    return following, mean


def reduce_pair(u, v):
    u, v = F(u), F(v)
    state = core(u, v)
    steps = 0
    if at_prime(u, 2):
        while at_prime(v/u, 8) != 6:
            state = actual_average(state, (-11*u-3*v, v, v))
            v = -(11*u+v)/3
            steps += 1
            assert steps <= 7 and state == core(u, v)
        old_u, old_v = u, v
        block = [u]*9+[v]*2+[-11*u-3*v]
        state, mu = invoke_solved_block(state, block, 12)
        assert mu == -(2*u+v)/12 and at_prime(mu, 2) == 0
        assert (at_prime(old_u, 5)-at_prime(mu, 5)) % 5
        state = actual_average(state, (mu, u, v))
        u, v = mu, (mu+old_u+old_v)/3
        assert state == core(u, v)
        assert at_prime(u, 2) == 0 and at_prime(v, 2) == 1
    block = [u]*6+[v]*3+[-11*u-3*v]
    state, mean = invoke_solved_block(state, block, 10)
    assert mean == -u/2
    for _ in range(5):
        state = actual_average(state, (mean, mean, u))
    assert state == Counter({F(0): 15})
    return steps


def verify():
    # The eight-cycle proof does not sample large p-adic truncations.
    for start in range(8):
        orbit = []
        t = start
        while t not in orbit:
            orbit.append(t)
            t = (5*t-1) % 8
        assert len(orbit) == 8 and t == start and 6 in orbit
    print("B15 mod-8 transitivity of A: PASS 8")
    checked, cases = 0, Counter()
    for u in range(-35, 36):
        for v in range(-35, 36):
            if gcd(u, v) != 1 or (u-v) % 5 == 0:
                continue
            assert at_prime(u, 2) or at_prime(v, 2)
            steps = reduce_pair(u, v)
            cases[steps] += 1
            checked += 1
    print("B15 twelve/ten subproblem interfaces: PASS", checked)
    print("B15 A-step histogram", dict(sorted(cases.items())))

    lattice_cases = 0
    for size in range(2, 9):
        for values in combinations_with_replacement(range(-2, 3), size):
            assert local_lattice_formula(values) == centered_g(list(map(F, values)))
            lattice_cases += 1
    print("affine-lattice local G formula: PASS", lattice_cases)


if __name__ == "__main__":
    verify()
