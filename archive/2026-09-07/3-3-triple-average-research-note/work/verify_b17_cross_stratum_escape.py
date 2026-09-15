"""Verify an explicit escape from the odd-background guarded B17 trap.

The 13/14 subproblems invoke existing complete theorems; the 9-point
operation is replayed as six real ternary averages.
"""

from collections import Counter
from fractions import Fraction as F
from math import gcd

from verify_fifteen_via_subblocks import centered_g, actual_average, is_three_power
from verify_thirteen_arithmetic_group import average_block
from explore_b17_guarded_returns import generate, primitive, height


def residue(value, modulus):
    value = F(value)
    return value.numerator*pow(value.denominator,-1,modulus) % modulus


def core(u,v):
    return Counter([u]*13+[v]*3+[-13*u-3*v])


def contract(state, values):
    size = len(values)
    assert size in (9,13,14,15)
    if size != 9:
        assert is_three_power(centered_g(values))
    else:
        physical = list(values)
        assert average_block(physical,list(range(9))) == 6
        assert len(set(physical)) == 1
    mean = sum(values,F(0))/size
    assert is_three_power(mean.denominator)
    result = state.copy()
    for value,count in Counter(values).items():
        assert result[value] >= count
        result[value] -= count
        if not result[value]:
            del result[value]
    result[mean] += size
    return result, mean


def escape(u,v):
    u,v = F(u),F(v)
    assert residue(u,2) == 1
    assert residue(u,5) and residue(u,7) and residue(u,13)
    assert residue(v/u,5) == 3 and residue(v/u,7) == 2
    assert pow(residue(v/u,13),6,13) == 12
    assert residue(u-v,17)
    state = core(u,v)
    preparatory = 0
    while residue(v/u,13) != 8:
        state = actual_average(state,(-13*u-3*v,v,v))
        v = -(13*u+v)/3
        preparatory += 1
        assert preparatory <= 5 and state == core(u,v)
    initial_u, initial_v = u,v
    assert residue(2*v-3*u,13) == 0
    state, a = contract(state,[u]*7+[v,-13*u-3*v])
    assert a == -(6*u+2*v)/9
    assert state == Counter([a]*9+[u]*6+[v]*2)
    state, mu = contract(state,[a]*7+[u]*4+[v]*2)
    assert mu == 2*(-3*u+2*v)/117
    b = (2*a+u)/3
    state = actual_average(state,(a,a,u))
    assert state == core(mu,b)
    assert residue(mu,2) == 0 and residue(b,2) == 1
    assert residue(mu+2*b,7) == 0
    assert residue(mu-b,17)

    state, c = contract(state,[mu]*12+[b,-13*mu-3*b])
    d = (c+mu+b)/3
    state = actual_average(state,(c,mu,b))
    assert state == core(c,d)
    assert c == F(2,2457)*(24*initial_u+23*initial_v)
    assert d == -F(1,63)*(3*initial_u+2*initial_v)
    assert residue(c,5) and residue(d,5) and residue(c+d,5) == 0
    assert residue(c-d,17)
    assert centered_g([c]*12+[d]*2+[-13*c-3*d]) in (1,3)
    # The now-enabled 15-point call is legitimate; stopping here does not
    # claim it will by itself decrease the starting height.
    return preparatory, (c,d)


def verify_followup_descent():
    _, actual = escape(1,93)
    denominator = 1
    from math import lcm
    for value in actual:
        denominator = lcm(denominator,value.denominator)
    pair = primitive(*(int(value*denominator) for value in actual))
    assert pair == (-52,87)
    templates = {row["matrix"]: row for row in generate()}
    M15 = (-3,-3,13,-2)
    M14 = (-3,-6,13,12)
    M13 = (-6,-6,26,13)
    word = (M15,"A",M15,"A","A","A",M14,M13,M15,M14)
    for item in word:
        u,v = map(F,pair)
        state = core(u,v)
        if item == "A":
            state = actual_average(state,(-13*u-3*v,v,v))
            x,y = u,-(13*u+v)/3
        else:
            row = templates[item]
            a,b,modulus = row["guard"]
            assert (a*pair[0]+b*pair[1]) % modulus == 0
            block = [u]*row["alpha"]+[v]*row["beta"]+[-13*u-3*v]
            state, _ = contract(state,block)
            triple = tuple(a*u+b*v for a,b in row["triple"])
            state = actual_average(state,triple)
            a,b,c,d = row["actual"]
            x,y = a*u+b*v,c*u+d*v
        assert state == core(x,y)
        denominator = lcm(x.denominator,y.denominator)
        pair = primitive(int(x*denominator),int(y*denominator))
        assert (pair[0]-pair[1]) % 17
    assert pair == (-22,15)
    assert height(pair) == 32524 < height((1,93)) == 55612
    print("B17 formerly trapped representative descent: PASS 55612 -> 32524")


def verify():
    histogram = Counter()
    for j in range(20):
        u,v = 1,93+23205*j
        for _ in range(6):
            preparatory, _ = escape(u,v)
            histogram[preparatory] += 1
            # Preserve an integer representative with positive first coordinate.
            u,v = 3*u,-13*u-v
            assert gcd(u,v) == 1
    assert set(histogram) == set(range(6))
    print("B17 odd-background trap cross-stratum escape: PASS",sum(histogram.values()))
    print("B17 A-prelude counts",dict(sorted(histogram.items())))
    # Different 17-adic classes and parities, with u still odd.
    lifted = 0
    nonsquares = (2,5,6,7,8,11)
    for u in (1,3,9,11,17):
        for t in nonsquares:
            v0 = next(v for v in range(455)
                      if (v-3*u)%5 == 0 and (v-2*u)%7 == 0 and (v-t*u)%13 == 0)
            for shift in range(3):
                v = v0+455*shift
                if gcd(u,v) == 1 and (u-v)%17:
                    escape(u,v)
                    lifted += 1
    print("B17 independent CRT trap lifts: PASS", lifted)
    verify_followup_descent()


if __name__ == "__main__":
    verify()
