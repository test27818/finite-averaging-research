"""Finite checks of the obstruction-module formulas and explicit networks.

All-parameter statements are proved in the companion note. This script does
not re-prove the established n >= 2p+1 reachability theorem by sampling.
"""
from fractions import Fraction as F
from math import gcd, lcm
from pathlib import Path
from random import Random
import json


def primitive(values):
    den = lcm(*(F(x).denominator for x in values))
    raw = [int(F(x)*den) for x in values]
    common = gcd(*raw)
    return tuple(x//common for x in raw) if common else tuple(raw)


def gap(values):
    x = primitive(values)
    return gcd(*(v-x[0] for v in x))


def obstruction_size(values, p):
    if not any(values):
        return 1
    g = gap(values)
    assert g
    while g % p == 0:
        g //= p
    return g


def val_integer(x, ell):
    assert x
    order = 0
    while x % ell == 0:
        x //= ell
        order += 1
    return order


def val(x, ell):
    x = F(x)
    if not x:
        return float('inf')
    return val_integer(x.numerator, ell)-val_integer(x.denominator, ell)


def average(values, positions):
    assert len(set(positions)) == len(positions)
    y = list(values)
    mean = sum((F(values[i]) for i in positions), F(0))/len(positions)
    for i in positions:
        y[i] = mean
    return tuple(y)


def group_formulas():
    rng = Random(2026091617)
    steps = local = images = 0
    for p in (3, 5, 7, 11):
        for _ in range(180):
            n = rng.randrange(p+1, 3*p+5)
            first = [rng.randrange(-40, 41) for _ in range(n-1)]
            x = tuple(F(v, p**rng.randrange(4)) for v in first)
            x = x+(-sum(x),)
            if not any(x):
                continue
            for _ in range(6):
                y = average(x, rng.sample(range(n), p))
                old = obstruction_size(x, p)
                new = obstruction_size(y, p)
                assert new % old == 0, (p, x, y, old, new)
                z = primitive(x)
                G = gap(x)
                assert n % G == 0
                assert gcd(z[0], G) == 1
                # Smith-cokernel map (mass,moment) -> moment - X_1*mass.
                for t in z:
                    assert (t-z[0]) % G == 0
                images += 1
                for ell in (2, 3, 5, 7, 11):
                    if ell == p:
                        continue
                    alpha = min(val(t, ell) for t in x)
                    beta = min(val(t-x[0], ell) for t in x)
                    assert beta-alpha == val_integer(old, ell)
                    local += 1
                steps += 1
                x = y
                if not any(x):
                    break
    return {'actual_average_edges': steps, 'local_depth_identities': local,
            'Smith_cokernel_image_checks': images}


def transport_and_replication():
    rows = [(2, 1, 2, 2, 2)]*4+[(1, 5, 1, 1, 1)]
    P = [[F(t, 9) for t in row] for row in rows]
    x = (-3, 0, 1, 1, 1)
    assert gap(x) == 1
    assert all(sum(row) == 1 and min(row) > 0 for row in P)
    assert all(sum(P[i][j] for i in range(5)) == 1 for j in range(5))
    assert all(sum(a*b for a,b in zip(row,x)) == 0 for row in P)
    assert P[0] != P[-1]  # Rank2: just two distinct rows, same row sum.
    # Allocate each of nine copies of each input into five nine-position blocks.
    inventory = [list(range(9*j, 9*(j+1))) for j in range(5)]
    blocks = []
    for row in rows:
        block = []
        for j, count in enumerate(row):
            block += inventory[j][:count]
            inventory[j] = inventory[j][count:]
        assert len(block) == 9
        blocks.append(block)
    assert all(not stock for stock in inventory)
    assert sorted(i for block in blocks for i in block) == list(range(45))
    word = []
    for block in blocks:
        word += [block[3*i:3*i+3] for i in range(3)]
        word += [[block[3*i+j] for i in range(3)] for j in range(3)]
    literal_steps = 0
    for source in [x]+[tuple(int(i == j) for i in range(5)) for j in range(5)]:
        state = tuple(F(t) for t in source for _ in range(9))
        for positions in word:
            state = average(state, positions)
            literal_steps += 1
        targets = [sum(a*b for a,b in zip(row,source)) for row in P]
        assert all(state[i] == target for block,target in zip(blocks,targets) for i in block)
    # A legal seven-entry state can create a new order7 obstruction.
    x7 = (-7, 1, 1, 1, 1, 1, 2)
    y7 = average(x7, (0,1,6))
    assert obstruction_size(x7,3) == 1 and obstruction_size(y7,3) == 7
    return {'replicated_input_size': 45, 'word_length': len(word),
            'standard_basis_and_input_literal_steps': literal_steps,
            'new_obstruction_example': '1 divides 7'}


def endpoint_family():
    cases = steps = 0
    for p in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
        x = tuple([-p]+[0]*p+[1]*p)
        assert len(x) == 2*p+1 and sum(x) == 0 and gap(x) == 1

        def select(counts):
            chosen = []
            for value, count in counts:
                candidates = [i for i,t in enumerate(x) if t == value]
                assert len(candidates) >= count
                chosen += candidates[:count]
            assert len(chosen) == p
            return chosen

        x = average(x, select([(-p,1),(0,p-1)]))
        h = (p-1)//2
        for _ in range(2):
            x = average(x, select([(-1,h),(1,h),(0,1)]))
        x = average(x, select([(-1,1),(1,1),(0,p-2)]))
        assert not any(x)
        cases += 1
        steps += 4
    return {'odd_prime_cases': cases, 'literal_averages': steps}


if __name__ == '__main__':
    if not __debug__:
        raise RuntimeError('Assertions required.')
    result = {'obstruction_formulas': group_formulas(),
              'positive_transport': transport_and_replication(),
              'endpoint_reserve_position': endpoint_family(),
              'scope': 'Formula and exact-network checks; established threshold theorem is cited, not inferred.'}
    Path(__file__).with_name('G_obstruction_group_verification.json').write_text(
        json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps(result, indent=2))
