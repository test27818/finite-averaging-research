"""Low-dyadic composite closure and the70/110/130 variable-comb patches.

The symbolic proof handles unbounded dimensions. Finite plan checks and
weighted-state replay validate the small capacity and local-witness edges.
"""

from collections import Counter
from fractions import Fraction as F
from math import gcd
from random import Random

from verify_multiexception_factor_bridge import carry_plan,factorization,odd_factor_plan,eight_divisible_plan
from verify_fifteen_via_subblocks import actual_average
from verify_prime_factor_carry_bridge import legal_g,mean


def comb_plan(a,depth,multiplier):
    power = 3**depth
    weights = [3**j for j in range(depth-1,0,-1) for _ in range(2)]+[1,1,1]
    outstanding = multiplier*a
    selected,remainder = [],[]
    for weight in weights:
        if weight <= outstanding:
            selected.append(weight)
            outstanding -= weight
        else:
            remainder.append(weight)
    assert outstanding == 0 and sum(selected) == multiplier*a
    return power,selected,remainder


def exceptional_bridge(n,u,exceptions):
    assert n in (70,110,130) and len(exceptions) == 5
    a,b = n//5,5
    u = F(u)
    exceptions = tuple(map(F,exceptions))
    assert (n-5)*u+sum(exceptions,F(0)) == 0
    source = Counter({u:n-5})
    source.update(exceptions)
    assert legal_g(source)
    differences = [u-v for v in exceptions]
    residues = [d.numerator*pow(d.denominator,-1,5) % 5 for d in differences]
    changed = len(set(residues[:4])) == 1
    if changed:
        assert len(set(residues)) == 1 and residues[0]
    plans = [(3,1)]*4
    if changed:
        plans[0] = (5,16) if n == 70 else (4,1)
    state = source.copy()
    rows = []
    reservoir = Counter({exceptions[-1]:1})
    operations = 0
    remainder_count = 1
    for value,(depth,h) in zip(exceptions,plans):
        power,selected,remainder = comb_plan(a,depth,h)
        assert len(selected) < a and remainder
        current = value
        for _ in range(depth):
            state = actual_average(state,(current,u,u))
            current = (current+2*u)/3
            operations += 1
        difference = u-value
        row = Counter(u-difference*F(weight,power) for weight in selected)
        row[u] += a-len(selected)
        assert legal_g(row) and mean(row) == u-F(h,power)*difference
        rows.append(row)
        reservoir.update(u-difference*F(weight,power) for weight in remainder)
        remainder_count += len(remainder)
    assert remainder_count < a
    reservoir[u] += a-remainder_count
    assert legal_g(reservoir)
    rows.append(reservoir)
    expected = Counter()
    for row in rows:
        expected.update(row)
    assert state == expected and legal_g(state)
    quotient = Counter(mean(row) for row in rows)
    assert sum(quotient.values()) == 5 and mean(quotient) == 0 and legal_g(quotient)
    assert a % 2 == 0
    # a copies of the legal five-point quotient are paired into n10 calls.
    return changed,operations,rows,quotient


def reduction_plan(n):
    assert n >= 7 and n % 3
    factors = factorization(n)
    if len(factors) == 1 and factors[0][1] == 1:
        return 'prime',None
    if n in (10,14,25,35,70,110,130):
        return 'finite-base',None
    if n % 2:
        return 'odd-factor',odd_factor_plan(n)
    if len(factors) == 1:
        return 'two-power',None
    if n % 8 == 0:
        return 'eight-factor',eight_divisible_plan(n)
    if len(factors) == 2:
        return 'prime-power-halving',n//2
    r = len(factors)+2
    b = factors[-1][0]
    a = n//b
    if a == 10:
        a,b = b,10
    assert a >= 7 and b >= r+1
    return 'low-dyadic-factor',(a,b,r,carry_plan(a,b,r))


def verify_capacity():
    for a in (20,28):
        carry_plan(a,11,5)
    for a in (14,22,26,34):
        carry_plan(a,13,5)
    for prime in (17,19,23,29,31):
        carry_plan(prime,10,5)
    for d in range(4,25):
        assert 4*5**(d-2) >= 3*d*d+3*d+2
    for d in range(5,25):
        assert 2*5**(d-2) >= 3*d*d+d
    for a,depth,h,expected in ((14,5,16,(8,3)),(22,4,1,(4,5)),(26,4,1,(6,3))):
        _,selected,remainder = comb_plan(a,depth,h)
        assert (len(selected),len(remainder)) == expected
    print('low-dyadic factor capacity and variable-comb certificates: PASS 14')


def verify_plans():
    histogram = Counter()
    for n in range(7,50000):
        if n % 3 == 0:
            continue
        kind,plan = reduction_plan(n)
        if kind.endswith('factor'):
            a,b,r,_ = plan
            assert 7 <= a < n and 3 <= b < n and b >= r+1
        elif kind == 'prime-power-halving':
            assert 7 <= plan < n
        histogram[kind] += 1
    print('all-dimension prime-reduction finite plans: PASS',sum(histogram.values()),dict(sorted(histogram.items())))


def verify_exceptions():
    random = Random(20260910)
    counts = Counter()
    for n in (70,110,130):
        for forced in (False,True):
            for _ in range(120):
                u = random.randrange(-10,11)
                if forced:
                    residue = random.randrange(1,5)
                    values = [u-(residue+5*random.randrange(-10,11)) for _ in range(4)]
                else:
                    values = [random.randrange(-40,41) for _ in range(4)]
                values.append(-(n-5)*u-sum(values))
                divisor = gcd(u,*values)
                if not divisor:
                    continue
                u //= divisor
                values = [v//divisor for v in values]
                state = Counter({F(u):n-5})
                state.update(map(F,values))
                if not legal_g(state):
                    continue
                changed,steps,_,_ = exceptional_bridge(n,u,values)
                assert steps == 12+(2 if n == 70 else 1)*changed
                counts[n,changed] += 1
    assert len(counts) == 6
    print('n70/n110/n130 exact variable-factor interfaces: PASS',sum(counts.values()),dict(sorted(counts.items())))


def verify():
    verify_capacity()
    verify_plans()
    verify_exceptions()


if __name__ == '__main__':
    verify()
