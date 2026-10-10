"""Uniform labelled reduction for prime p >= 5 and 3p < n < 4p.

Only a bounded residue sieve selects a mixing parameter. No averaging-word
search, floating point, or formal inverse is used. All paths are replayed
independently on the original indices, with local legality checked per atom.
"""

from fractions import Fraction as F
from itertools import product
from math import gcd, prod
from pathlib import Path
from random import Random
import json

from verify_four_prime_entry_and_band import Ledger, factors, residue, is_legal

if not __debug__:
    raise RuntimeError('Assertions are required.')

ROOT = Path(__file__).parent


def selector_bound(primes):
    d = len(primes)
    if d <= 4:
        return 2**d
    modulus, phi = prod(primes), prod(q-1 for q in primes)
    return (2**d-1)*modulus//phi+1


def select_parameter(p, conditions):
    """Choose k with alpha + k*beta nonzero at every specified prime.

    A byte sieve marks at most one residue class per prime. Conditions with
    zero slope are constant nonzero and consume no sieve or capacity.
    """
    banned = []
    for q, alpha, beta in conditions:
        alpha, beta = alpha % q, beta % q
        assert alpha or beta
        if beta:
            banned.append((q, -alpha*pow(beta, -1, q) % q))
    limit = selector_bound([q for q, _ in banned])
    assert limit <= p-1
    sieve = bytearray(limit+1)
    for q, bad in banned:
        start = bad or q
        if start <= limit:
            sieve[start:limit+1:q] = b'\x01'*((limit-start)//q+1)
    k = next(k for k in range(1, limit+1) if not sieve[k])
    assert all((alpha+k*beta) % q for q, alpha, beta in conditions)
    return k


def mix(ledger, first, second, k):
    p = ledger.p
    assert len(first) == len(second) == p and 1 <= k <= p-1
    a, b = ledger.state[first[0]], ledger.state[second[0]]
    left = first[:p-k]+second[:k]
    right = first[p-k:]+second[k:]
    ledger.average(left)
    ledger.average(right)
    assert ledger.state[left[0]] == ((p-k)*a+k*b)/p
    assert ledger.state[right[0]] == (k*a+(p-k)*b)/p
    return left, right


def select_mix(ledger, first, second, target_value, primes):
    a, b = ledger.state[first[0]], ledger.state[second[0]]
    conditions = [(q, residue(a-target_value, q),
                   residue((b-a)/ledger.p, q)) for q in primes]
    return select_parameter(ledger.p, conditions)


def full_support(ledger, first, second, singles, anchor, primes):
    """Keep anchor fixed and make first - anchor a unit at all primes."""
    phases = []
    target = ledger.state[anchor]
    while True:
        support = {q for q in primes if residue(ledger.state[first[0]]-target, q)}
        if len(support) == len(primes):
            return first, second, singles, phases
        q = next(q for q in primes if q not in support)
        swapped = False
        if not residue(ledger.state[second[0]]-target, q):
            chosen = next(i for i in singles if residue(ledger.state[i]-target, q))
            assert chosen != anchor
            role = singles.index(chosen)
            second, singles[role] = ledger.swap(second, chosen)
            swapped = True
        union = [q for q in primes if residue(ledger.state[first[0]]-target, q)
                 or residue(ledger.state[second[0]]-target, q)]
        k = select_mix(ledger, first, second, target, union)
        first, second = mix(ledger, first, second, k)
        following = {q for q in primes if residue(ledger.state[first[0]]-target, q)}
        assert support < following and following == set(union)
        assert ledger.state[anchor] == target
        assert is_legal(ledger.state, primes)
        phases.append({'before': sorted(support), 'after': sorted(following),
                       'swap': swapped, 'k': k})
        assert len(phases) <= len(primes)


def prepare_main_blocks(ledger, blocks, singles, anchor, primes):
    first, second, third = blocks
    a = ledger.state[first[0]]
    assert all(residue(ledger.state[anchor]-a, q) for q in primes)
    good = [q for q in primes if residue(ledger.state[second[0]]-a, q)
            or residue(ledger.state[third[0]]-a, q)]
    if len(good) == len(primes):
        return blocks, singles, None
    # Select the new third block to differ from a at every already good place.
    k = select_mix(ledger, third, second, a, good)
    third, second = mix(ledger, third, second, k)
    role = singles.index(anchor)
    second, singles[role] = ledger.swap(second, anchor)
    assert all(len({residue(ledger.state[g[0]], q) for g in (first, second, third)}) > 1
               for q in primes)
    return [first, second, third], singles, k


def coalesce(ledger, blocks, singles, primes):
    p, r = ledger.p, len(singles)
    first, second, third = blocks
    assert 1 <= r < p
    old = ledger.state[first[0]]
    group, carrier = first[:p-r]+singles, first[p-r:]
    ledger.average(group)
    assert all(ledger.state[i] == old for i in carrier)
    assert is_legal(ledger.state, primes)
    return [group, second, third], carrier


def fold(ledger, blocks, carrier, primes):
    p, r = ledger.p, len(carrier)
    first, second, third = blocks
    d = ledger.state[carrier[0]]
    a, b, c = (ledger.state[g[0]] for g in blocks)
    assert p*(a+b+c)+r*d == 0
    assert all(residue(a-d, q) or residue(b-d, q) for q in primes)
    k = select_mix(ledger, first, second, d, primes)
    first, second = mix(ledger, first, second, k)
    a, b, c = (ledger.state[g[0]] for g in (first, second, third))
    epsilon = 1 if p % 3 == 1 else -1
    m = (p-epsilon)//3
    counts = (m+epsilon, m, m)
    assert sum(counts) == p and all(0 <= 2*s <= p for s in counts)
    groups = [[], [], []]
    for block, count in zip((first, second, third), counts):
        groups[0] += block[:count]
        groups[1] += block[count:2*count]
        groups[2] += block[2*count:]
    for group in groups:
        ledger.average(group)
    A = (m*(a+b+c)+epsilon*a)/p
    B = a+b+c-2*A
    assert ledger.state[groups[0][0]] == ledger.state[groups[1][0]] == A
    assert ledger.state[groups[2][0]] == B
    assert 2*p*A+p*B+r*d == 0
    for q in primes:
        assert residue(A-d, q) == residue(F(epsilon, p)*(a-d), q) != 0
        assert residue(B-d, q) == residue(-2*(A-d), q)
    return [groups[0]+groups[1], groups[2], carrier], k


def replay_and_record(raw, ledger, groups, extra):
    """Independent per-atom residue, mass, denominator and label validation."""
    p, n = ledger.p, len(raw)
    primes = tuple(factors(n))
    state = list(map(F, raw))
    total = sum(state)
    for group in ledger.word:
        assert len(group) == len(set(group)) == p
        assert all(0 <= i < n for i in group)
        average = sum(state[i] for i in group)/p
        for i in group:
            state[i] = average
        assert sum(state) == total == 0
        assert is_legal(state, primes)
        for x in state:
            denominator = x.denominator
            while denominator % p == 0:
                denominator //= p
            assert denominator == 1
    assert state == ledger.state
    assert sorted(i for g in groups for i in g) == list(range(n))
    assert list(map(len, groups)) == [2*p, p, n-3*p]
    values = [state[g[0]] for g in groups]
    assert all(state[i] == x for g, x in zip(groups, values) for i in g)
    return {'p': p, 'n': n, 'prime_factors': list(primes),
            'input': [str(x) for x in raw],
            'operations': [[i+1 for i in group] for group in ledger.word],
            'final_groups': [[i+1 for i in group] for group in groups],
            'final_values': list(map(str, values)), **extra}


def upper_reduce(raw, p):
    n, primes = len(raw), tuple(factors(len(raw)))
    assert p >= 5 and factors(p) == {p: 1} and 3*p < n < 4*p
    assert sum(raw) == 0 and gcd(*raw) == 1 and is_legal(raw, primes)
    assert selector_bound(primes) <= p-1
    protected = {0}
    for q in primes:
        protected.add(next(i for i in range(1, n) if (raw[i]-raw[0]) % q))
    free = [i for i in range(n) if i not in protected]
    assert len(free) >= 2*p
    first, second = free[:p], free[p:2*p]
    ledger = Ledger(raw, p)
    ledger.average(first)
    ledger.average(second)
    used = set(first+second)
    singles = [i for i in range(n) if i not in used]
    first, second, singles, phases = full_support(ledger, first, second, singles, 0, primes)
    third = [i for i in singles if i != 0][:p]
    ledger.average(third)
    used = set(third)
    singles = [i for i in singles if i not in used]
    blocks, singles, repair = prepare_main_blocks(ledger, [first, second, third], singles, 0, primes)
    blocks, carrier = coalesce(ledger, blocks, singles, primes)
    groups, fold_k = fold(ledger, blocks, carrier, primes)
    assert len(ledger.word) <= 12+3*len(primes)
    return replay_and_record(raw, ledger, groups,
                             {'phases': phases, 'repair_k': repair, 'fold_k': fold_k})


def verify_sieve():
    checked = 0
    for primes in ((2,), (7,), (2, 3), (3, 5), (2, 3, 5), (3, 5, 7),
                   (2, 3, 5, 7), (3, 5, 7, 11)):
        for classes in product(*(range(q) for q in primes)):
            k = select_parameter(17, [(q, -bad, 1) for q, bad in zip(primes, classes)])
            assert all(k % q != bad for q, bad in zip(primes, classes))
            checked += 1
    # d >= 5 uses the elementary inclusion-exclusion bound, not Kanold's theorem.
    rng = Random(2026091251)
    for primes in ((2, 3, 5, 7, 11), (3, 5, 7, 11, 13), (2, 3, 5, 7, 11, 13)):
        for _ in range(80):
            conditions = [(q, -rng.randrange(q), 1) for q in primes]
            select_parameter(prod(primes), conditions)
            checked += 1
    capacities = 0
    for p in range(5, 1200):
        if factors(p) != {p: 1}:
            continue
        for n in range(3*p+1, 4*p):
            qs = tuple(factors(n))
            assert selector_bound(qs) <= p-1
            assert n-len(qs)-1 >= 2*p
            capacities += 1
    print('upper-band elementary residue selector: PASS', checked, capacities)


def forced_two_block(p, n):
    """Two blocks, anchor and all nonspecial singles start at 1 mod rad(n)."""
    primes = tuple(factors(n))
    modulus = prod(primes)
    raw = [1]*n
    start = 2*p+1
    assert start+2*len(primes) < n
    for j, q in enumerate(primes):
        unit = modulus//q*pow(modulus//q, -1, q) % modulus
        raw[start+2*j] += unit
        raw[start+2*j+1] -= unit
    raw[-1] -= n
    return raw


def verify_paths():
    rng, records, exceptional = Random(2026091252), [], 0
    for p in (5, 7, 11, 13, 17, 19, 23, 29, 31, 43):
        for r in range(1, p):
            n = 3*p+r
            for _ in range(2):
                while True:
                    raw = [rng.randrange(-(1 << 72), 1 << 72) for _ in range(n-1)]
                    raw.append(-sum(raw))
                    common = gcd(*raw)
                    raw = [x//common for x in raw]
                    if is_legal(raw, tuple(factors(n))):
                        break
                records.append(upper_reduce(raw, p))
                exceptional += int(r < len(factors(n)))
    print('upper-band all-remainder labelled entries: PASS', len(records), exceptional,
          max(len(x['operations']) for x in records))

    forced = []
    for p, n in ((7, 22), (11, 42), (53, 210), (211, 840), (587, 2310)):
        raw = forced_two_block(p, n)
        primes = tuple(factors(n))
        ledger = Ledger(raw, p)
        first, second = list(range(p)), list(range(p, 2*p))
        singles, anchor = list(range(2*p, n)), 2*p
        first, second, singles, phases = full_support(ledger, first, second, singles, anchor, primes)
        assert len(phases) == len(primes)
        third = [i for i in singles if i != anchor][:p]
        ledger.average(third)
        singles = [i for i in singles if i not in set(third)]
        blocks, singles, repair = prepare_main_blocks(ledger, [first, second, third], singles, anchor, primes)
        blocks, carrier = coalesce(ledger, blocks, singles, primes)
        groups, k = fold(ledger, blocks, carrier, primes)
        forced.append(replay_and_record(raw, ledger, groups,
                      {'phases': phases, 'repair_k': repair, 'fold_k': k}))
    print('upper-band forced multi-prime support growth: PASS', len(forced),
          max(len(x['phases']) for x in forced))

    # Force the separate three-block repair with all main blocks initially 1.
    repairs = []
    for p, r in ((5, 2), (7, 3), (11, 7), (53, 51)):
        n = 3*p+r
        raw = [1]*(3*p)+[2]+[1]*(r-1)
        raw[-1] -= n+1
        primes = tuple(factors(n))
        ledger = Ledger(raw, p)
        blocks = [list(range(j*p, (j+1)*p)) for j in range(3)]
        singles = list(range(3*p, n))
        blocks, singles, repair = prepare_main_blocks(ledger, blocks, singles, 3*p, primes)
        assert repair is not None
        blocks, carrier = coalesce(ledger, blocks, singles, primes)
        groups, k = fold(ledger, blocks, carrier, primes)
        repairs.append(replay_and_record(raw, ledger, groups, {'repair_k': repair, 'fold_k': k}))
    print('upper-band simultaneous main-block repair and fold: PASS', len(repairs))

    output = {'scope': 'Uniform reduction only; these are exact labelled sample paths, not terminal solutions.',
              'records': records+forced+repairs}
    (ROOT/'upper_band_three_value_records.json').write_text(
        json.dumps(output, indent=2)+'\n', encoding='utf-8')


def core_state(p, r, y, z):
    return [F(y-p*z)]*(2*p)+[F(-2*y+(2*p+r)*z)]*p+[F(-p*z)]*r


def involution(ledger, groups, s):
    first, second, carrier = groups
    p, r = ledger.p, len(carrier)
    j = (p-r-s)//3
    i = 2*j+r
    assert p-r-s == 3*j and 0 <= 2*s <= r
    assert 0 <= 2*i <= 2*p and 0 <= 2*j <= p-r
    kept = second[-r:]
    left = first[:i]+second[:j]+carrier[:s]
    right = first[i:2*i]+second[j:2*j]+carrier[s:2*s]
    other = first[2*i:]+second[2*j:p-r]+carrier[2*s:]
    for group in (left, right, other):
        ledger.average(group)
    return [left+right, other, kept]


def verify_core_formulas():
    identities, inverse_paths, growth = 0, 0, 0
    for p in (5, 7, 11, 13, 17, 19, 23, 29, 31, 43):
        epsilon = 1 if p % 3 == 1 else -1
        k = (p-epsilon)//3
        for r in range(1, p):
            n = 3*p+r
            for y, z in ((1, 0), (1, 1), (-1, 2)):
                raw = core_state(p, r, y, z)
                w = 3*y-n*z
                energy = sum(x*x for x in raw)
                assert energy == F(p, 3)*(2*w*w+r*n*z*z)
                # The universal safe duplicate-row contraction.
                ledger = Ledger(raw, p)
                a, b, c = list(range(2*p)), list(range(2*p, 3*p)), list(range(3*p, n))
                groups = [a[:p-k]+b[:k], a[p-k:2*(p-k)]+b[k:2*k], a[2*(p-k):]+b[2*k:]]
                for group in groups:
                    ledger.average(group)
                expected_y = F(epsilon*y+k*n*z, p)
                assert ledger.state[groups[0][0]] == expected_y-p*z
                replay_and_record(raw, ledger, [groups[0]+groups[1], groups[2], c], {})
                if w % p:
                    assert gcd(epsilon*y+k*n*z, p*z) == 1
                    after_primitive = sum((p*x)**2 for x in ledger.state)
                    assert after_primitive-energy == F(p*r*n*(p*p-1)*z*z, 3)
                    growth += 1
                identities += 1

            allowed = [s for s in range(r//2+1) if p-r-s >= 0 and (p-r-s) % 3 == 0]
            assert allowed or r < 4
            for s in allowed:
                j = (p-r-s)//3
                mu = (2*p+r)**2+2*n*(j-p)
                assert 3*mu == r*(2*p+r)-2*n*s and mu != 0
                for y, z in ((1, 0), (1, 1)):
                    raw = core_state(p, r, y, z)
                    ledger = Ledger(raw, p)
                    groups = [list(range(2*p)), list(range(2*p, 3*p)), list(range(3*p, n))]
                    groups = involution(ledger, groups, s)
                    yy = F((2*p+r)*y+n*(j-p)*z, p)
                    zz = F(2*y-(2*p+r)*z, p)
                    assert [ledger.state[g[0]] for g in groups] == [yy-p*zz, -2*yy+(2*p+r)*zz, -p*zz]
                    assert all(residue(yy, q) == residue(-y, q) for q in factors(n))
                    groups = involution(ledger, groups, s)
                    scale = F(mu, p*p)
                    expected = [scale*(y-p*z), scale*(-2*y+(2*p+r)*z), scale*(-p*z)]
                    assert [ledger.state[g[0]] for g in groups] == expected
                    replay_and_record(raw, ledger, groups, {})
                    inverse_paths += 1
    print('upper-band quadratic core and primitive-height boundary: PASS', identities, growth)
    print('upper-band physical trace-zero core returns: PASS', inverse_paths)


if __name__ == '__main__':
    verify_sieve()
    verify_paths()
    verify_core_formulas()
    print('upper-band uniform three-value reduction: PASS')
