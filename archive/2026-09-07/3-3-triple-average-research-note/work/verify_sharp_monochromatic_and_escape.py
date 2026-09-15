"""Sharp residue concentration and three-atom escape of extremal frozen inputs.

No averaging-word search: the paths use two explicit formulas. Finite residue
checks recurse only through zero-free sequences, updating one cyclic bitset.
The unbounded concentration proof cites Balandraud plus an elementary sumset
argument, and is written in the accompanying document.
"""
from collections import Counter
from fractions import Fraction as F
from math import gcd
from pathlib import Path
import json

if not __debug__:
    raise RuntimeError('Assertions required')

ROOT = Path(__file__).resolve().parent


def primes(limit):
    sieve = bytearray(b'\x01')*(limit+1)
    sieve[:2] = b'\x00\x00'
    for q in range(2, int(limit**0.5)+1):
        if sieve[q]:
            sieve[q*q:limit+1:q] = b'\x00'*((limit-q*q)//q+1)
    return [q for q in range(2, limit+1) if sieve[q]]


def rotate(bits, shift, p):
    return ((bits << shift) | (bits >> (p-shift))) & ((1 << p)-1)


def zero_free(seq, p):
    reachable = 1
    for x in seq:
        shifted = rotate(reachable, x % p, p)
        if shifted & 1:
            return False
        reachable |= shifted
    return True


def mixed_zero(counts, p):
    """Exact mixed p-subset test using at most p coefficients per residue."""
    terms = [(x, min(f, p)) for x, f in counts.items() if f]
    def visit(index, remaining, total, support):
        if remaining == 0:
            return total % p == 0 and support >= 2
        if index == len(terms):
            return False
        x, f = terms[index]
        return any(visit(index+1, remaining-k, total+k*x, support+(k > 0))
                   for k in range(min(f, remaining)+1))
    return visit(0, p, 0, 0)


def structural_no_mixed(counts, p):
    assert sum(counts.values()) >= 2*p-1
    heavy = [x for x, f in counts.items() if f >= p]
    if len(heavy) == 2:
        return len(counts) == 2
    if len(heavy) != 1:
        return False
    a = heavy[0]
    rest = [(x-a) % p for x, f in counts.items() if x != a for _ in range(f)]
    return len(rest) <= p-1 and zero_free(rest, p)


def verify_residue_structure():
    checks = 0
    for p in (3, 5, 7):
        for n in (2*p-1, 3*p+1):
            # Normalization by translation ensures zero belongs to the support.
            def compositions(index, left, row):
                if index == p-1:
                    yield row+[left]
                    return
                for f in range(1 if index == 0 else 0, left+1):
                    yield from compositions(index+1, left-f, row+[f])
            for row in compositions(0, n, []):
                counts = {x: f for x, f in enumerate(row) if f}
                predicted = structural_no_mixed(counts, p)
                assert predicted == (not mixed_zero(counts, p))
                checks += 1
    print('exact no-mixed residue classification: PASS', checks)


def verify_zero_free_defect():
    count, maxima = 0, {}
    for p in (3, 5, 7, 11, 13, 17, 19):
        best = 0
        def visit(start, reachable, seq, multiplicities):
            nonlocal count, best
            if seq:
                h = max(multiplicities.values())
                defect = len(seq)-h
                assert defect <= (p-1)//3
                best = max(best, defect)
                count += 1
            for x in range(start, p):
                shifted = rotate(reachable, x, p)
                if shifted & 1:
                    continue
                multiplicities[x] += 1
                visit(x, reachable | shifted, seq+[x], multiplicities)
                multiplicities[x] -= 1
        visit(1, 1, [], Counter())
        assert best == (p-1)//3
        maxima[p] = best
    print('zero-free sharp defect exhaustive checks: PASS', count, maxima)


def extremal_input(p):
    m = (p-1)//3
    n = 3*p+1
    a = 1 if p % 3 == 1 else 2
    last = 3-4*p if a == 1 else 4-7*p
    raw = [a]*(n-2*m)+[a+1]*m+[a+2]*(m-1)+[last]
    assert sum(raw) == 0 and gcd(*raw) == 1
    assert gcd(*(x-raw[0] for x in raw)) == 1
    diffs = [(x-a) % p for x in raw if x != a]
    assert Counter(diffs) == Counter({1: m, 2: m})
    assert zero_free(diffs, p)
    counts = Counter(x % p for x in raw)
    assert structural_no_mixed(counts, p)
    top = sorted(counts.values(), reverse=True)
    assert sum(top[:2]) == n-m
    return raw, m


def labelled_escape(p):
    raw, m = extremal_input(p)
    state = list(map(F, raw))
    n = len(raw)
    background = list(range(n-2*m))
    plus1 = list(range(n-2*m, n-m))
    plus2 = list(range(n-m, n-1))
    special = [n-1]
    if p % 3 == 1:
        assert m >= 3
        g1 = background[:2*m+3]+plus1[:m-3]+special
        g2 = background[2*m+3:4*m+2]+plus1[m-3:]+plus2
        remainder = background[4*m+2:]
        g3 = g1[:m]+g2[:m-1]+remainder[:m+2]
        expected = (F(-8*m-4, p), F(5*m+2, p))
    else:
        assert m >= 3
        g1 = background[:2*m+4]+plus2[:m-3]+special
        g2 = background[2*m+4:4*m+8]+plus1[:m-2]
        rem_bg = background[4*m+8:]
        g3 = g1[:m+1]+g2[:m]+plus2[m-3:]+plus1[m-2:m-1]+rem_bg[:m-2]
        expected = (F(-13*m-14, p), F(7*m+2, p))
    assert not set(g1) & set(g2)
    energies, path = [sum(x*x for x in state)], []
    for j, group in enumerate((g1, g2, g3)):
        assert len(group) == len(set(group)) == p
        assert all(0 <= i < n for i in group)
        mean = sum(state[i] for i in group)/p
        if j < 2:
            assert mean == expected[j] and mean.denominator == p
        else:
            assert mean == 0
        loss = sum((state[i]-mean)**2 for i in group)
        assert loss > 0
        for i in group:
            state[i] = mean
        assert sum(state) == 0
        energy = sum(x*x for x in state)
        assert energies[-1]-energy == loss
        energies.append(energy)
        # All three stages have only one denominator p; this is independently checked.
        assert all(x.denominator in (1, p) for x in state)
        integers = [int(p*x) for x in state]
        common = gcd(*integers)
        primitive = [x//common for x in integers]
        assert gcd(*(x-primitive[0] for x in primitive)) == 1
        path.append([i+1 for i in group])
    assert sum(x == 0 for x in state) >= p
    replay = list(map(F, raw))
    for indices in path:
        group = [i-1 for i in indices]
        mean = sum(replay[i] for i in group)/p
        for i in group:
            replay[i] = mean
    assert replay == state
    return {'p': p, 'n': n, 'm': m, 'input': raw,
            'operations': path, 'energies': list(map(str, energies)),
            'zero_count': sum(x == 0 for x in state)}


def verify_paths():
    records = [labelled_escape(p) for p in primes(500) if p >= 11]
    # Explicit disproof of the old conjecture and a primitive physical realization.
    raw, m = extremal_input(13)
    assert raw == [1]*32+[2]*4+[3]*3+[-49]
    assert not mixed_zero({0: 32, 1: 4, 2: 4}, 13)
    assert 32+4 < 3*13-2
    # Every p-subset of the first fractional state is nonzero. Only four
    # initial types are present, so this tiny count audit is complete.
    record = next(r for r in records if r['p'] == 13)
    p = 13
    state = list(map(F, record['input']))
    group = [i-1 for i in record['operations'][0]]
    mean = sum(state[i] for i in group)/p
    for i in group:
        state[i] = mean
    count = Counter(state)
    types = list(count)
    def subset(index, left, total):
        if index == len(types):
            return left == 0 and total == 0
        x = types[index]
        return any(subset(index+1, left-k, total+k*x) for k in range(min(left, count[x])+1))
    assert not subset(0, p, F(0))
    (ROOT/'sharp_monochromatic_escape_records.json').write_text(
        json.dumps({'scope': 'Three exact averages produce p zeros for the stated extremal family; full completion invokes the existing zero-trigger theorem.',
                    'records': records}, indent=2)+'\n', encoding='utf-8')
    print('sharp concentration counterexample and three-step escapes: PASS', len(records))


if __name__ == '__main__':
    verify_zero_free_defect()
    verify_residue_structure()
    verify_paths()
    print('sharp monochromatic structure and extremal escape: PASS')
