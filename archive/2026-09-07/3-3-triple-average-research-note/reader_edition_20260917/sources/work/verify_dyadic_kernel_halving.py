"""Verify a single algebraic B_n halving template for 8|n, n>=16.

The twelve-point contraction invokes the completed twelve-point theorem.
All multiplicity and arithmetic checks use at most four distinct values.
"""

from collections import Counter
from fractions import Fraction as F
from math import gcd, lcm

from verify_fifteen_via_subblocks import actual_average, is_three_power


def state_g(items):
    """Centered primitive G from weighted values; no expanded vector."""
    values = [(F(value), count) for value, count in items if count]
    denominator = lcm(*(value.denominator for value, count in values))
    integers = [(int(value*denominator), count) for value, count in values]
    anchor = integers[0][0]
    difference = gcd(*(value-anchor for value, count in integers))
    if not difference:
        return 0
    size = sum(count for value, count in integers)
    total = sum(count*((value-anchor)//difference) for value, count in integers)
    return size//gcd(size, total)


def make_state(items):
    result = Counter()
    for value, count in items:
        result[F(value)] += count
    return result


def bridge(n, u, v):
    if n < 16 or n % 8 or gcd(u, v) != 1:
        raise ValueError("primitive parameters and n>=16 divisible by 8 required")
    if not is_three_power(gcd(u-v, n)):
        raise ValueError("illegal B_n parameter")
    u, v = F(u), F(v)
    w = -(n-4)*u-3*v
    state = make_state(((u,n-4), (v,3), (w,1)))
    state = actual_average(state, (w,u,v))
    a = (w+u+v)/3
    assert state == make_state(((u,n-5), (v,2), (a,3)))
    block = ((u,9), (v,2), (a,1))
    assert state_g(block) in (1,3)
    mu = sum(value*count for value,count in block)/12
    assert mu == F(1,9)*((8-n//4)*u+v)
    assert is_three_power(mu.denominator)
    for value,count in block:
        assert state[value] >= count
        state[value] -= count
        if not state[value]:
            del state[value]
    state[mu] += 12
    assert state == make_state(((mu,12), (u,n-14), (a,2)))
    assert sum(state.values()) == n and sum(value*count for value,count in state.items()) == 0
    assert all(count % 2 == 0 for count in state.values())
    reduced = tuple((value,count//2) for value,count in state.items())
    assert is_three_power(state_g(reduced))
    assert sum(count for value,count in reduced) == n//2
    return reduced


def four_divisible_bridge(n, u, v):
    if n < 16 or n % 4 or gcd(u, v) != 1:
        raise ValueError("primitive parameters and n>=16 divisible by four required")
    if not is_three_power(gcd(u-v, n)):
        raise ValueError("illegal B_n parameter")
    u, v = F(u), F(v)
    w = -(n-4)*u-3*v
    state = make_state(((u,n-4), (v,3), (w,1)))
    state = actual_average(state, (w,u,u))
    a = (w+2*u)/3
    assert state == make_state(((u,n-6), (v,3), (a,3)))
    block = ((u,10), (v,1), (a,1))
    assert state_g(block) in (1,3)
    mu = sum(value*count for value,count in block)/12
    assert mu == F(9-n//4,9)*u
    assert is_three_power(mu.denominator)
    for value,count in block:
        assert state[value] >= count
        state[value] -= count
        if not state[value]:
            del state[value]
    state[mu] += 12
    expected = make_state(((mu,12), (u,n-16), (v,2), (a,2)))
    assert +state == +expected
    assert sum(state.values()) == n
    assert sum(value*count for value,count in state.items()) == 0
    assert all(count % 2 == 0 for count in state.values())
    reduced = tuple((value,count//2) for value,count in state.items())
    assert is_three_power(state_g(reduced))
    return reduced


def verify_four_divisible():
    checked = 0
    for n in (16,20,24,28,32,36,40,44,48,60,84,100,140,420,2048):
        for u in range(-15,16):
            for v in range(-15,16):
                if gcd(u,v) != 1 or not is_three_power(gcd(u-v,n)):
                    continue
                four_divisible_bridge(n,u,v)
                checked += 1
    print("4-divisible B_n twelve-point halving: PASS", checked)


def verify():
    checked = 0
    sizes = (16,24,32,40,48,56,64,72,80,96,128,216,512,2048,27648)
    for n in sizes:
        for u in range(-15,16):
            for v in range(-15,16):
                if gcd(u,v) != 1 or not is_three_power(gcd(u-v,n)):
                    continue
                bridge(n,u,v)
                checked += 1
    # An independent check of the aggregated arithmetic helper.
    from verify_fifteen_via_subblocks import centered_g
    cases = 0
    for n in (16,24,40):
        for pair in ((1,0), (0,1), (2,1), (1,2), (-3,2)):
            if is_three_power(gcd(pair[0]-pair[1],n)):
                items = bridge(n,*pair)
                values = [value for value,count in items for _ in range(count)]
                assert state_g(items) == centered_g(values)
                cases += 1
    print("8-divisible B_n single-template halving: PASS", checked)
    print("weighted G vs expanded centered G: PASS", cases)


if __name__ == "__main__":
    verify()
    verify_four_divisible()
