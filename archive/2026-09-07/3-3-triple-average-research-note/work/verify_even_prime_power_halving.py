"""Uniform disjoint-blocker halving for n=2*p^e and n=4*p^e.

Only an explicit one/two-step prelude and a proved twelve-point child are
used. The symbolic odd-prime witness is independent of the prime size.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import gcd,lcm

from verify_fifteen_via_subblocks import actual_average,is_three_power
from verify_prime_factor_carry_bridge import legal_g,mean
from verify_even_kernel_halving import bridge as twice_odd_bn
from verify_dyadic_kernel_halving import four_divisible_bridge


def residue(x,modulus):
    x = F(x)
    return x.numerator*pow(x.denominator,-1,modulus) % modulus


def core(n,u,exceptions):
    state = Counter({F(u):n-4})
    state.update(map(F,exceptions))
    return state


def contract_twelve(state,block):
    assert sum(block.values()) == 12 and legal_g(block)
    mu = mean(block)
    assert is_three_power(mu.denominator)
    following = state.copy()
    for value,count in block.items():
        assert following[value] >= count
        following[value] -= count
    following[mu] += 12
    return +following,mu


def disjoint_halve(n,p,u,b,bp,c,cp):
    assert n >= 18 and (n % 4 == 2 or n % 8 == 4)
    assert n % p == 0 and p >= 5
    u,b,bp,c,cp = map(F,(u,b,bp,c,cp))
    state = core(n,u,(b,bp,c,cp))
    assert mean(state) == 0 and legal_g(state)
    assert residue(b-u,2) == residue(bp-u,2) == 1
    assert residue(c-u,2) == residue(cp-u,2) == 0
    assert residue(b-u,p) == residue(bp-u,p) == 0
    assert residue(c-u,p) and residue(cp-u,p)
    steps = []
    def take(triple):
        nonlocal state
        state = actual_average(state,triple)
        steps.append(triple)
        return sum(triple)/3
    if n % 4 == 2:
        if residue(u,2) == 0:
            t = take((u,u,c))
            block = Counter({u:8,t:1})
            block.update((b,bp,cp))
            branch = 'twice-odd-even-u'
        else:
            t = take((u,b,c))
            block = Counter({u:9,t:1})
            block.update((bp,cp))
            branch = 'twice-odd-odd-u'
        assert residue(t,2) == 0
    else:
        if residue(u+c,4) != 2 and residue(u+cp,4) == 2:
            c,cp = cp,c
        if residue(u+c,4) == 2:
            t = take((u,u,c))
            block = Counter({u:8,t:1})
            block.update((b,bp,cp))
            branch = 'fourfold-direct'
        else:
            assert residue(u+c,4) == residue(u+cp,4) == 0
            assert residue(b-bp,4) == 2
            a = take((u,b,c))
            t = take((a,u,bp))
            block = Counter({u:8,a:2,t:1})
            block.update((cp,))
            branch = 'fourfold-two-step'
        assert residue(u+t,4) == 2
    assert {residue(value,2) for value in block} == {0,1}
    state,mu = contract_twelve(state,block)
    assert mu == -((n-14)*u+2*t)/12
    expected = Counter({u:n-14})
    expected[t] += 2
    expected[mu] += 12
    assert state == expected
    assert residue(t-u,p)
    if n % 8 == 4:
        assert residue(mu-u,2) == 1
    half = Counter({x:count//2 for x,count in state.items()})
    assert all(count % 2 == 0 for count in state.values())
    assert sum(half.values()) == n//2 and mean(half) == 0 and legal_g(half)
    return branch,tuple(steps),half


def high_core_halve(n,p,u,exceptions):
    assert len(exceptions) == 4 and (n-4)*u+sum(exceptions) == 0
    assert legal_g(core(n,u,exceptions))
    simultaneous = [i for i,x in enumerate(exceptions) if residue(x-u,2) and residue(x-u,p)]
    if simultaneous:
        keep = simultaneous[0]
        other = [F(x) for i,x in enumerate(exceptions) if i != keep]
        v = sum(other)/3
        following = actual_average(core(n,u,exceptions),other)
        expected = Counter({F(u):n-4})
        expected[v] += 3
        expected[F(exceptions[keep])] += 1
        assert following == expected and legal_g(following)
        denominator = lcm(F(u).denominator,v.denominator)
        a,b = int(u*denominator),int(v*denominator)
        content = gcd(a,b)
        if n % 4 == 2:
            twice_odd_bn(n,a//content,b//content)
        else:
            four_divisible_bridge(n,a//content,b//content)
        return 'common-witness'
    odd = [x for x in exceptions if residue(x-u,2)]
    prime = [x for x in exceptions if residue(x-u,p)]
    assert len(odd) == len(prime) == 2
    branch,_,_ = disjoint_halve(n,p,u,*odd,*prime)
    return branch


def verify_residue_table():
    # Complete local classification at2, keeping the other prime symbolic.
    branches = Counter()
    for n8 in (2,4,6):
        n = 20 if n8 == 4 else 22 if n8 == 6 else 26
        p = 5 if n8 == 4 else n//2
        modulus = 8*p
        for u8,b8,bp8,c8 in product(range(8),repeat=4):
            if (b8-u8) % 2 == 0 or (bp8-u8) % 2 == 0 or (c8-u8) % 2:
                continue
            def lift(a8,ap):
                return a8+8*((ap-a8)*pow(8,-1,p) % p)
            u,b,bp,c = lift(u8,1),lift(b8,1),lift(bp8,1),lift(c8,2)
            cp = -(n-4)*u-b-bp-c
            branch,_,_ = disjoint_halve(n,p,u,b,bp,c,cp)
            branches[branch] += 1
    assert sum(branches.values()) == 1536 and set(branches) == {
        'twice-odd-even-u','twice-odd-odd-u','fourfold-direct','fourfold-two-step'}
    print('uniform even prime-power dyadic residue interfaces: PASS 1536',dict(sorted(branches.items())))


def verify_cores():
    checked = Counter()
    for p,e in ((5,1),(5,2),(7,1),(7,2),(11,1),(13,1),(17,1),(19,1),(29,1)):
        for power2 in (2,4):
            n = power2*p**e
            if n < 18:
                continue
            for u,a,b,c in product(range(-2,3),repeat=4):
                exceptions = [a,b,c,-(n-4)*u-a-b-c]
                if gcd(u,*exceptions) != 1 or not legal_g(core(n,u,exceptions)):
                    continue
                checked[high_core_halve(n,p,u,exceptions)] += 1
    print('uniform even prime-power high-core halving: PASS',sum(checked.values()))
    print('high-core branch counts',dict(sorted(checked.items())))


def verify():
    verify_residue_table()
    verify_cores()


if __name__ == '__main__':
    verify()
