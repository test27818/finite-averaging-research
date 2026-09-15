"""Uniform factor bridges for two-exception cores, with a sharp test family.

This does not construct the missing entry from arbitrary states into these
cores. Weighted counters keep every construction logarithmic in support.
"""

from collections import Counter
from fractions import Fraction as F
from math import gcd, lcm
from random import Random

from verify_fifteen_via_subblocks import actual_average, centered_g, is_three_power


def away_three(value):
    while value % 3 == 0:
        value //= 3
    return value


def logarithmic_depth(value):
    depth,power = 0,1
    while power < value:
        depth,power = depth+1,power*3
    return depth,power


def weighted_g(state):
    size = sum(state.values())
    mean = sum((value*count for value,count in state.items()),F(0))/size
    centered = [F(value)-mean for value in state]
    denominator = lcm(*(value.denominator for value in centered))
    integers = [int(value*denominator) for value in centered]
    content = gcd(*integers)
    if not content:
        return 0
    integers = [value//content for value in integers]
    return gcd(*(value-integers[0] for value in integers))


def mean(state):
    return sum((value*count for value,count in state.items()),F(0))/sum(state.values())


def legal_g(state):
    value = weighted_g(state)
    return value == 0 or is_three_power(value)


def initial(a,b,u=1,exception=0):
    state = Counter({F(u):a*b-2})
    state[F(exception)] += 1
    state[F(-(a*b-2)*u-exception)] += 1
    return state


def bridge(a,b,u=1,exception=0):
    assert a >= 7 and b >= 3
    n = a*b
    assert gcd(u,exception) == 1
    state = initial(a,b,u,exception)
    assert legal_g(state)
    u,exception = F(u),F(exception)
    exceptional_last = -(n-2)*u-exception
    difference = u-exceptional_last
    if away_three(b) == 1 or u == 0:
        row = Counter({u:a-2})
        row[exception] += 1
        row[exceptional_last] += 1
        quotient = Counter({u:b-1})
        quotient[mean(row)] += 1
        assert legal_g(row) and legal_g(quotient)
        return 0,(),(row,),b-1,quotient

    nonthree = away_three(a)
    depth,power = logarithmic_depth(nonthree)
    current = exceptional_last
    word = []
    for _ in range(depth):
        triple = current,u,u
        state = actual_average(state,triple)
        current = sum(triple)/3
        word.append(triple)
    weights = [1] if depth == 0 else [3**k for k in range(depth-1,0,-1) for _ in range(2)]+[1,1,1]
    assert sum(weights) == power and len(weights) == 2*depth+1
    selected,remainder = [],[]
    outstanding = nonthree
    for weight in weights:
        if weight <= outstanding:
            selected.append(weight)
            outstanding -= weight
        else:
            remainder.append(weight)
    assert outstanding == 0 and selected
    row1 = Counter(u-difference*F(weight,power) for weight in selected)
    row1[u] += a-len(selected)
    row2 = Counter(u-difference*F(weight,power) for weight in remainder)
    row2[exception] += 1
    row2[u] += a-1-len(remainder)
    assert row1[u] > 0 and row2[u] > 0
    expected = row1+row2+Counter({u:a*(b-2)})
    assert state == expected
    assert sum(row1.values()) == sum(row2.values()) == a
    denominator = power*(a//nonthree)
    mu1,mu2 = u-difference/denominator,(1-b)*u+difference/denominator
    assert mean(row1) == mu1 and mean(row2) == mu2
    quotient = Counter({u:b-2})
    quotient[mu1] += 1
    quotient[mu2] += 1
    assert legal_g(row1) and legal_g(row2) and legal_g(quotient)
    assert sum((x*c for x,c in quotient.items()),F(0)) == 0
    assert legal_g(state)
    return depth,tuple(word),(row1,row2),b-2,quotient


def push_columns(columns, denominator, triple):
    plus = sum(columns.get(i,(0,0))[0] for i in triple)
    minus = sum(columns.get(i,(0,0))[1] for i in triple)
    following = {i:(3*x,3*y) for i,(x,y) in columns.items() if i not in triple}
    if plus or minus:
        following.update({i:(plus,minus) for i in triple})
    assert sum(x for x,y in following.values()) == 3*denominator
    assert sum(y for x,y in following.values()) == 3*denominator
    return following,3*denominator


def verify_lower_bound_samples():
    random = Random(20260910)
    words_checked,blocks_checked = 0,0
    for a in (7,8,10,11,25,49,121):
        for b in (7,10):
            n = a*b
            target_depth,_ = logarithmic_depth(away_three(a))
            for depth in range(target_depth):
                for trial in range(4):
                    columns = {n-1:(1,0),n-2:(0,1)}
                    denominator = 1
                    for _ in range(depth):
                        active = random.choice(tuple(columns))
                        others = [i+(i >= active) for i in random.sample(range(n-1),2)]
                        columns,denominator = push_columns(columns,denominator,(active,*others))
                    assert denominator < away_three(a)
                    assert len(columns) <= 2+2*depth
                    # Only touched slots affect these two columns; fill the
                    # remaining positions with unchanged background values.
                    signatures = {(0,0,0)}
                    for x,y in columns.values():
                        signatures |= {(k+1,u+x,v+y) for k,u,v in signatures}
                    untouched = n-len(columns)
                    for count,plus,minus in signatures:
                        if not 0 <= a-count <= untouched:
                            continue
                        assert abs(plus-minus) <= denominator
                        mu = F(a*denominator+plus-minus-n*plus,a*denominator)
                        if is_three_power(mu.denominator):
                            assert plus == minus
                            assert mu == 1-F(b*plus,denominator)
                            prime = 7 if b == 7 else 2
                            assert (mu.numerator*pow(mu.denominator,-1,prime)) % prime == 1
                        blocks_checked += 1
                    words_checked += 1
    print('factor-bridge two-column lower-bound identities: PASS',words_checked,blocks_checked)


def verify():
    for sample in (Counter({F(1):5,F(-13,3):1,F(-2,3):1}), initial(7,7)):
        expanded = [x for x,c in sample.items() for _ in range(c)]
        assert weighted_g(sample) == centered_g(expanded)
    checked = 0
    for a in (7,8,9,10,11,12,13,15,16,17,19,23,25,27,49,81,121,343,1000):
        for b in (3,7,8,9,11,13,25):
            depth,_,_,_,_ = bridge(a,b)
            expected = 0 if away_three(b) == 1 else logarithmic_depth(away_three(a))[0]
            assert depth == expected
            checked += 1
    print('optimal ternary carry factorization interfaces: PASS',checked)
    general = 0
    for a in (7,8,9,10,13,25,49):
        for b in (3,5,7,8,11):
            for u in range(-3,4):
                for exception in range(-4,5):
                    if gcd(u,exception) != 1 or not legal_g(initial(a,b,u,exception)):
                        continue
                    bridge(a,b,u,exception)
                    general += 1
    print('general two-exception core factor interfaces: PASS',general)
    depth,word,rows,constant,quotient = bridge(7,7)
    assert depth == 2 and constant == 5
    assert word == ((F(-47),F(1),F(1)),(F(-15),F(1),F(1)))
    assert quotient == Counter({F(-13,3):1,F(-2,3):1,F(1):5})
    assert all(weighted_g(row) == 1 for row in rows) and weighted_g(quotient) == 1
    print('X49 two-step repair, two row interfaces and one seven-point quotient: PASS')
    for copies in range(2,100):
        threes = copies % 2
        twos = (copies-3*threes)//2
        assert twos >= 0 and 2*twos+3*threes == copies
    print('replication semigroup from multiplicities 2 and 3: PASS 98')
    verify_lower_bound_samples()


if __name__ == '__main__':
    verify()
