"""Weighted multi-exception factor bridges and odd-dimension closure.

The construction uses r-1 ternary combs and at most two coefficient plans;
it never searches over partitions of the expanded n-coordinate state.
"""

from collections import Counter
from fractions import Fraction as F
from math import gcd
from random import Random

from verify_fifteen_via_subblocks import actual_average
from verify_prime_factor_carry_bridge import away_three, logarithmic_depth, legal_g, mean


def carry_plan(a,b,r,allow_unanchored=False):
    assert a >= 7 and b >= r+1 and r >= 2
    a0 = away_three(a)
    k,power = logarithmic_depth(a0)
    weights = [1] if not k else [3**j for j in range(k-1,0,-1) for _ in range(2)]+[1,1,1]
    choices = []
    for multiplier in range(1,power//a0+1):
        if gcd(multiplier,away_three(b)) != 1:
            continue
        outstanding = multiplier*a0
        selected,remainder = [],[]
        for weight in weights:
            if weight <= outstanding:
                selected.append(weight)
                outstanding -= weight
            else:
                remainder.append(weight)
        assert outstanding == 0
        required = max(len(selected)+1,(r-1)*len(remainder)+(1 if allow_unanchored else 2))
        choices.append((required,len(remainder),multiplier,tuple(selected),tuple(remainder)))
    required,_,multiplier,selected,remainder = min(choices)
    if required > a:
        raise ValueError((a,b,r,'required row capacity',required))
    return k,power,multiplier,selected,remainder


def factor_core(a,b,u,exceptions,allow_unanchored=False):
    n,r = a*b,len(exceptions)
    k,power,multiplier,selected,remainder = carry_plan(a,b,r,allow_unanchored)
    u = F(u)
    exceptions = tuple(map(F,exceptions))
    assert (n-r)*u+sum(exceptions,F(0)) == 0
    state = Counter({u:n-r})
    state.update(exceptions)
    assert legal_g(state)
    initial = state.copy()
    rows = []
    reservoir = Counter({exceptions[-1]:1})
    word = []
    for value in exceptions[:-1]:
        difference = u-value
        current = value
        for _ in range(k):
            triple = current,u,u
            state = actual_average(state,triple)
            current = sum(triple)/3
            word.append(triple)
        row = Counter(u-difference*F(weight,power) for weight in selected)
        row[u] += a-len(selected)
        reservoir.update(u-difference*F(weight,power) for weight in remainder)
        assert row[u] >= 1 and sum(row.values()) == a and legal_g(row)
        assert mean(row) == u-F(multiplier,power*(a//away_three(a)))*difference
        rows.append(row)
    reservoir[u] += a-1-(r-1)*len(remainder)
    reservoir = +reservoir
    assert (reservoir[u] >= 1 or allow_unanchored) and sum(reservoir.values()) == a and legal_g(reservoir)
    rows.append(reservoir)
    expected = Counter({u:(b-r)*a})
    for row in rows:
        expected.update(row)
    assert state == expected and sum(state.values()) == n and legal_g(state)
    quotient = Counter({u:b-r})
    quotient.update(mean(row) for row in rows)
    assert sum(quotient.values()) == b and mean(quotient) == 0 and legal_g(quotient)
    assert len(word) == (r-1)*k
    return initial,state,rows,quotient,tuple(word)


def thirty_five_bridge(u,exceptions):
    assert len(exceptions) == 4 and 31*u+sum(exceptions) == 0
    differences = [u-value for value in exceptions]
    anchor = next(i for i in range(4) if len({d % 7 for j,d in enumerate(differences) if j != i}) >= 2)
    reordered = [value for i,value in enumerate(exceptions) if i != anchor]+[exceptions[anchor]]
    return factor_core(7,5,u,reordered,allow_unanchored=True)


def factorization(n):
    result = []
    p = 2
    while p*p <= n:
        if n % p == 0:
            exponent = 0
            while n % p == 0:
                n //= p
                exponent += 1
            result.append((p,exponent))
        p += 1 if p == 2 else 2
    if n > 1:
        result.append((n,1))
    return result


def odd_factor_plan(n):
    assert n >= 7 and n % 2 and n % 3
    factors = factorization(n)
    if len(factors) == 1 and factors[0][1] == 1:
        return None
    if n in (25,35):
        return None
    q = factors[-1][0]
    a,b = n//q,q
    if a in (5,7) and len(factors) > 1:
        a,b = b,a
    r = len(factors)+2
    plan = carry_plan(a,b,r)
    assert a < n and b < n and b >= r+1
    return a,b,r,plan


def eight_divisible_plan(n):
    assert n % 8 == 0 and n % 3
    factors = factorization(n)
    if len(factors) == 1:
        return None
    b = factors[-1][0]
    a = n//b
    r = len(factors)+2
    assert a % 8 == 0 and b >= r+1
    return a,b,r,carry_plan(a,b,r)


def verify_small_capacity():
    # The only small rows needed for odd composite induction.
    expected = {(7,3):(1,2), (11,4):(2,3), (13,4):(2,1),
                (17,4):(1,2), (19,4):(1,4)}
    for (a,r),(multiplier,remainder_count) in expected.items():
        k,power,h,selected,remainder = carry_plan(a,11,r)
        assert h == multiplier and len(remainder) == remainder_count
    for n in (25,35):
        assert odd_factor_plan(n) is None
    for d in range(4,30):
        # 5^(d-1) dominates the continuous logarithmic upper bound.
        assert 5**(d-1) >= 3*d*d+2*d+1
    print('odd-factor row-capacity boundary certificates: PASS 5')
    for a in (8,16):
        carry_plan(a,5,4)
    for d in range(3,30):
        assert 8*5**(d-2) >= 3*d*d+3*d+2
    print('eight-divisible capacity boundary certificates: PASS 2')


def verify_odd_plans():
    checked = 0
    for n in range(7,20000,2):
        if n % 3 == 0:
            continue
        plan = odd_factor_plan(n)
        if plan:
            checked += 1
    print('odd-composite factor plan finite checks: PASS',checked)
    checked = 0
    for n in range(8,20000,8):
        if n % 3 and eight_divisible_plan(n):
            checked += 1
    print('eight-divisible factor plan finite checks: PASS',checked)


def verify_general_bridges():
    random = Random(20260910)
    checked = 0
    shapes = [(7,7,3),(11,7,4),(13,7,4),(17,5,4),(25,5,3),
              (25,7,4),(35,11,5),(49,13,5),(125,13,6),(343,17,7),
              (8,5,4),(27,11,5)]
    for a,b,r in shapes:
        for _ in range(80):
            u = random.randrange(-8,9)
            values = [random.randrange(-40,41) for _ in range(r-1)]
            values.append(-(a*b-r)*u-sum(values))
            content = gcd(u,*values)
            if not content:
                continue
            u //= content
            values = [x//content for x in values]
            state = Counter({F(u):a*b-r})
            state.update(map(F,values))
            if not legal_g(state):
                continue
            factor_core(a,b,u,values)
            checked += 1
    print('multi-exception exact physical/row/quotient interfaces: PASS',checked)


def verify_thirty_five():
    checked = 0
    for u in range(-3,4):
        for first in range(-3,4):
            for second in range(-3,4):
                for third in range(-3,4):
                    exceptions = [first,second,third,-31*u-first-second-third]
                    if gcd(u,*exceptions) != 1:
                        continue
                    state = Counter({F(u):31})
                    state.update(map(F,exceptions))
                    if not legal_g(state):
                        continue
                    _,_,rows,quotient,word = thirty_five_bridge(u,exceptions)
                    assert len(word) == 6 and len(rows) == 4
                    assert sum(quotient.values()) == 5 and legal_g(quotient)
                    # Three rank-one seven-point rows each collapse in two
                    # atomic operations; only the reservoir needs A(7).
                    for row in rows[:-1]:
                        target = mean(row)
                        if len(row) == 1:
                            continue
                        lower = 3*target-2*u
                        current = row
                        for _ in range(2):
                            current = actual_average(current,(F(lower),F(u),F(u)))
                        assert current == Counter({target:7})
                    checked += 1
    print('n35 safe-core bridge and exact rank-one row tails: PASS',checked)


def verify():
    verify_small_capacity()
    verify_odd_plans()
    verify_general_bridges()
    verify_thirty_five()


if __name__ == '__main__':
    verify()
