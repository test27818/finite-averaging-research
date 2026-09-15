"""Exact interfaces for B_n, n=2 mod 4, into duplicated n/2-point states."""

from collections import Counter
from fractions import Fraction as F
from math import gcd

from verify_fifteen_via_subblocks import at_prime, centered_g, is_three_power, actual_average


def bn(n, u, v):
    return Counter([u]*(n-4)+[v]*3+[-(n-4)*u-3*v])


def bridge(n, u, v):
    if n < 14 or n % 4 != 2 or gcd(u, v) != 1:
        raise ValueError("primitive B_n with n=2 mod 4, n>=14 required")
    if not is_three_power(gcd(u-v, n)):
        raise ValueError("illegal B_n pair")
    u, v = F(u), F(v)
    state = bn(n, u, v)
    steps = []

    def take(triple):
        nonlocal state
        steps.append(triple)
        state = actual_average(state, triple)
        return sum(triple, F(0))/3

    if at_prime(u, 2):
        if at_prime(F(n-10, 2)*u+v, 4):
            v = take((-(n-4)*u-3*v, v, v))
        w = -(n-4)*u-3*v
        block = [u]*6+[v,w]
        name = "odd_u"
    elif at_prime(u, 4) == 0:
        w = -(n-4)*u-3*v
        a = take((u, u, v))
        block = [u]*6+[a,w]
        name = "u_0_mod4"
    else:
        w = -(n-4)*u-3*v
        a = take((u, v, v))
        block = [u]*5+[v,a,w]
        name = "u_2_mod4"

    assert len(block) == 8 and centered_g(block) in (0, 1)
    mean = sum(block, F(0))/8
    assert is_three_power(mean.denominator)
    output = state.copy()
    for value, count in Counter(block).items():
        assert output[value] >= count
        output[value] -= count
        if not output[value]:
            del output[value]
    output[mean] += 8
    assert sum(output.values()) == n
    assert sum(value*count for value, count in output.items()) == 0
    assert all(count % 2 == 0 for count in output.values())
    compressed = [value for value, count in output.items() for _ in range(count//2)]
    assert len(compressed) == n//2
    local_g = centered_g(compressed)
    assert local_g == 0 or is_three_power(local_g)
    assert len(steps) <= 1
    return name


def verify():
    cases = Counter()
    for n in (14, 18, 22, 26, 30, 34, 38, 42, 46, 54, 66, 78, 90):
        for u in range(-20, 21):
            for v in range(-20, 21):
                if gcd(u, v) != 1 or not is_three_power(gcd(u-v, n)):
                    continue
                cases[bridge(n, u, v)] += 1
    print("even B_n eight-point halving interfaces: PASS", sum(cases.values()))
    print("halving parity cases", dict(sorted(cases.items())))


if __name__ == "__main__":
    verify()
