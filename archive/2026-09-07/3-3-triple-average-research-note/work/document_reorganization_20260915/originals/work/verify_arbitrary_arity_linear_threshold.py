"""All-integer-arity closure proof audit; no search over averaging words.

General proofs are in outputs/arbitrary_arity_linear_threshold.md.  Shared old
helpers are used only with explicitly supplied protected primes; the old prime
factor selector and primality-gated solvers are deliberately not called.
"""

from collections import Counter
from fractions import Fraction
from itertools import combinations, combinations_with_replacement
from math import gcd
from pathlib import Path
from random import Random
import json

import verify_prime_arity_large_dimension as base
import verify_prime_arity_linear_threshold as linear
from verify_composite_arity_transfer import factors, gap_gcd, primitive_center


def protected(n, q):
    return tuple(p for p in factors(n) if q % p)


def conditions(n, q):
    return q >= 3 and n >= 4 * q - 1 + len(protected(n, q))


def nonunit_move(a, b, q):
    g = gcd(a - b, q)
    assert a != b and g > 1
    k = q // g
    return (a,) * k + (b,) * (q - k)


def background(counts, n, q, primes):
    h = sorted(base.heavy(counts, q))
    b = max(h, key=counts.get)
    assert counts[b] >= 2 * q - 1
    a = next(x for x in h if x != b)
    delta = a - b
    if gcd(delta, q) > 1:
        return nonunit_move(a, b, q), 'background-nonunit', None
    others = [x for x in counts if x not in (a, b)]
    assert others, 'unit difference excludes a legal two-value zero-sum state'
    for x in others:
        move = base.controller(a, b, x, q)
        if sum(move) != q * b:
            return move, 'background-unit-adjust', None
    coefficients = {}
    for x in others:
        assert (b - x) % delta == 0
        coefficients[x] = (b - x) // delta
        assert 1 <= coefficients[x] < q
    assert gcd(delta, n) == 1
    if counts[a] >= 2 * q - 1:
        return base.controller(a, b, others[0], q), 'second-large-anchor', None
    for x in others:
        if counts[x] >= 2 * q - 1:
            if gcd(x - b, q) > 1:
                return nonunit_move(x, b, q), 'progression-nonunit', None
            return base.controller(x, b, a, q), 'progression-unit', None
    total = sum(coefficients[x] * counts[x] for x in others)
    if total >= q and max(coefficients.values()) >= 2:
        return linear.crossing_move(counts, b, delta, q), 'coefficient-crossing', None
    assert total >= q and max(coefficients.values()) == 1
    assert b == 0 and counts[a] == counts[-a]
    return None, 'background-opposite-terminal', a


def choose(counts, n, q, primes):
    assert conditions(n, q) and base.legal(counts, primes)
    h = sorted(base.heavy(counts, q))
    assert len(h) >= 2
    if len(h) >= 4:
        for a, b in combinations(h, 2):
            if gcd(a - b, q) > 1:
                return nonunit_move(a, b, q), 'four-heavy-nonunit', None
        return base.controller(h[0], h[1], h[2], q), 'four-heavy-unit', None
    if len(h) == 3:
        had_nonunit = False
        for u, v in combinations(h, 2):
            if gcd(u - v, q) == 1:
                continue
            had_nonunit = True
            w = next(x for x in h if x not in (u, v))
            for a, b in ((u, v), (v, u)):
                move = nonunit_move(a, b, q)
                if sum(move) != q * w:
                    return move, 'three-heavy-nonunit', None
        a, b, c = h
        # Either all pair differences are units, or the unique obstruction is
        # an even-arity midpoint with the two adjacent differences still units.
        assert gcd(a - b, q) == gcd(b - c, q) == 1
        if had_nonunit:
            assert q % 2 == 0 and a + c == 2 * b and gcd(c - a, q) == 2
        light = next((x for x in counts if x not in h), None)
        if light is not None:
            aa, bb = (a, b) if light < c else (b, c)
            return base.controller(aa, bb, light, q), 'three-heavy-light', None
        if counts[a] > q:
            return base.controller(b, c, a, q), 'three-heavy-spare-min', None
        if counts[c] > q:
            return base.controller(a, b, c, q), 'three-heavy-spare-max', None
        if had_nonunit:
            assert b == 0 and counts[a] == counts[c] == q
            return None, 'midpoint-opposite-terminal', c
        return background(counts, n, q, primes)
    if max(counts[x] for x in h) >= 2 * q - 1:
        return background(counts, n, q, primes)
    pool = counts.copy()
    for x in h:
        pool[x] -= q
    pool += Counter()
    move = linear.protected_egz(counts, pool, n, q, primes)
    return move, 'two-heavy-protected-EGZ', None


def audit(counts, q, branches):
    n = sum(counts.values())
    assert sum(x * f for x, f in counts.items()) == 0
    primes = protected(n, q)
    if not conditions(n, q) or not base.legal(counts, primes):
        return False
    assert len(base.heavy(counts, q)) >= 2
    move, branch, delta = choose(counts, n, q, primes)
    branches[branch] += 1
    if move is None:
        assert set(counts) == {0, delta, -delta}
        assert counts[delta] == counts[-delta] and counts[0] >= q - 2
    else:
        after = base.change(counts, move, q)
        # These checks use the definition, not the chooser's safety logic.
        assert sum(x * f for x, f in after.items()) == 0
        assert all(len({x % ell for x in after}) > 1 for ell in primes)
        assert sum(f >= q for f in after.values()) >= 2
    return True


def replay_original(initial, word, q):
    values = list(map(Fraction, initial))
    for indices in word:
        assert len(indices) == len(set(indices)) == q
        assert all(type(i) is int and 0 <= i < len(values) for i in indices)
        mean = sum(values[i] for i in indices) / q
        # Unlike the prime-only verifier, all divisors of q are permitted.
        assert q % mean.denominator == 0
        for i in indices:
            values[i] = mean
    assert all(x == 0 for x in values)


def solve(raw, q, branches):
    initial = primitive_center(raw)
    n, primes = len(initial), protected(len(initial), q)
    assert conditions(n, q) and base.legal(Counter(initial), primes)
    replay = base.LabelledReplay(initial, q)
    if not any(initial):
        return [], initial
    for move in base.initialize(replay.counts(), n, q, primes):
        replay.step(move)
        assert base.legal(replay.counts(), primes)
    while any(replay.state):
        move, branch, delta = choose(replay.counts(), n, q, primes)
        branches[branch] += 1
        if move is None:
            for _ in range(replay.counts()[delta]):
                replay.step((delta, -delta) + (0,) * (q - 2))
            break
        after = base.change(replay.counts(), move, q)
        assert base.legal(after, primes) and len(base.heavy(after, q)) >= 2
        replay.step(move)
        assert replay.counts() == after
    assert replay.energy == 0
    assert 2 * len(replay.word) <= q * q * sum(x * x for x in initial)
    replay_original(initial, replay.word, q)
    # Also check the actual unnormalized, noncentered input and its true mean.
    from verify_composite_arity_transfer import independent_replay
    independent_replay(raw, replay.word, q)
    return replay.word, initial


def centered_counts(values, weights):
    n = sum(weights)
    total = sum(x * f for x, f in zip(values, weights))
    zs = [n * x - total for x in values]
    common = gcd(*zs)
    counts = Counter()
    for x, f in zip(zs, weights):
        counts[x // common] += f
    return counts


def check_zero_trigger():
    from compare_pair_triple_solvers import BinarySolver
    from verify_composite_arity_transfer import (
        halfblock_construct, construct, construct_six_odd, independent_replay,
    )
    rng = Random(40960009)
    records = []
    with BinarySolver() as binary:
        for q, ns in ((4, (4, 5, 6, 7, 8, 9, 11, 13, 15, 17)),
                      (6, (6, 7, 8, 9, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23))):
            for n in ns:
                rest = [rng.randrange(-9, 10) for _ in range(n-q-1)]
                raw = [0]*q if n == q else [0]*q + rest + [-sum(rest)]
                if n <= 2*q:
                    active = [i for i, x in enumerate(raw) if x]
                    zeros = [i for i, x in enumerate(raw) if x == 0]
                    word = [active + zeros[:q-len(active)]] if active else []
                    independent_replay(raw, word, q)
                    records.append({'arity': q, 'n': n, 'input': raw, 'steps': len(word),
                                    'operations': [[i+1 for i in atom] for atom in word]})
                    continue
                leave = n % (2 if q == 4 else 3)
                inside = raw[leave:]
                assert inside.count(0) > 0 and gap_gcd(inside) == 1
                if q == 4:
                    ops, _ = halfblock_construct(inside, q, binary)
                elif len(inside) % 6 == 0:
                    ops, _ = construct(inside, q, binary)
                else:
                    ops, _ = construct_six_odd(inside, binary)
                word = [[i+leave for i in atom] for atom in ops]
                independent_replay(raw, word, q)
                records.append({'arity': q, 'n': n, 'input': raw, 'steps': len(word),
                                'operations': [[i+1 for i in atom] for atom in word]})
    print('composite zero-trigger original-position paths: PASS', len(records))
    return records


def main():
    rng = Random(20260912046)
    branches = Counter()
    nonunit = midpoints = local = initializations = capacities = 0
    for q in range(3, 41):
        for delta in range(1, 3 * q + 1):
            g = gcd(delta, q)
            if g == 1:
                continue
            move = nonunit_move(delta, 0, q)
            assert sum(move) == q * (delta // g)
            assert 1 <= move.count(delta) <= q // 2 and move.count(0) <= q - 1
            nonunit += 1
        for b in range(1, q + 1):
            for c in range(b + 1, b + q + 1):
                h = (0, b, c)
                bad = []
                escape = False
                for u, v in combinations(h, 2):
                    if gcd(u - v, q) == 1:
                        continue
                    bad.append((u, v))
                    w = next(x for x in h if x not in (u, v))
                    if any(sum(nonunit_move(a, z, q)) != q * w for a, z in ((u, v), (v, u))):
                        escape = True
                if bad and not escape:
                    assert q % 2 == 0 and c == 2 * b and gcd(c, q) == 2 and gcd(b, q) == 1
                    midpoints += 1
        start = 4 * q + (q - 1).bit_length() + 1
        for n in range(start, start + 80):
            assert conditions(n, q)
            capacities += 1
    print('all-arity nonunit and midpoint classification: PASS', nonunit, midpoints)
    print('all-arity uniform threshold capacities: PASS', capacities)
    # Full residue multisets check composite EGZ implementations, with a
    # separate combinations-based existence check for q=4.
    egz = 0
    for q in (4, 6):
        for values in combinations_with_replacement(range(q), 2 * q - 1):
            move = linear.egz_subset(values, q)
            assert not (Counter(move) - Counter(values)) and sum(move) % q == 0
            if q == 4:
                assert any(sum(values[i] for i in ids) % q == 0
                           for ids in combinations(range(len(values)), q))
            egz += 1
    print('composite EGZ residue multisets: PASS', egz)
    arities = (3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 25, 30, 36)
    for q in arities:
        start = 4 * q + (q - 1).bit_length() + 1
        for _ in range(220):
            m = rng.randrange(3, 10)
            weights = [q, q] + [1] * (m - 2)
            remaining = start + rng.randrange(35) - sum(weights)
            for i in range(m - 1):
                add = rng.randrange(remaining + 1)
                weights[i] += add
                remaining -= add
            weights[-1] += remaining
            values = [rng.randrange(-10**12, 10**12) * weights[-1] for _ in range(m-1)]
            values.append(-sum(x*f for x, f in zip(values, weights)) // weights[-1])
            common = gcd(*values)
            local += audit(Counter({x//common: f for x, f in zip(values, weights)}), q, branches)
        # Three-value order / collision cases and both unit and nonunit backgrounds.
        for values in ((-1, 0, 1), (-2, 0, 1), (-3, 1, 2), (-4, 1, 3)):
            for weights in ((q, start - 2*q, q), (q+1, start-2*q-1, q),
                            (q, q, start-2*q)):
                local += audit(centered_counts(values, weights), q, branches)
        for style in range(3):
            if style == 0:
                raw = list(range(1, start))
            elif style == 1:
                raw = [0] * q + list(range(1, start-q))
            else:
                raw = [0] * (2*q) + list(range(1, start-2*q))
            raw.append(-sum(raw))
            counts = Counter(q*x for x in raw)
            ps = protected(start, q)
            assert base.legal(counts, ps)
            moves = base.initialize(counts, start, q, ps)
            assert len(moves) <= 2
            for move in moves:
                counts = base.change(counts, move, q)
            assert base.legal(counts, ps) and len(base.heavy(counts, q)) >= 2
            initializations += 1
    for q in (5, 25):
        local += audit(Counter({-3: q, -1: q, 1: q, 3: q}), q, branches)
        local += audit(Counter({-(2*q+2): q, 1: q, q: 2*q+1}), q, branches)
    for counts in (Counter({-2: 6, -1: 12, 2: 12}), Counter({-2: 6, -1: 32, 4: 11})):
        move, branch, _ = background(counts, sum(counts.values()), 6, protected(sum(counts.values()), 6))
        after = base.change(counts, move, 6)
        assert base.legal(after, protected(sum(counts.values()), 6)) and len(base.heavy(after, 6)) >= 2
        branches[branch] += 1
        local += 1
    print('all-arity large-integer closure and initialization: PASS', local, initializations)
    records = []
    for q in (4, 6, 8, 9, 10, 12, 15):
        first = next(n for n in range(4*q-1, 5*q+1) if conditions(n, q))
        ns = [n for n in range(first, first+10) if conditions(n, q)][:5]
        for n in ns:
            for _ in range(2):
                while True:
                    raw = [rng.randrange(-4, 5) for _ in range(n)]
                    if base.legal(Counter(primitive_center(raw)), protected(n, q)):
                        break
                word, initial = solve(raw, q, branches)
                records.append({'arity': q, 'n': n, 'input': raw, 'G': gap_gcd(raw),
                                'steps': len(word), 'primitive_centered': initial,
                                'operations': [[i+1 for i in atom] for atom in word]})
    required = {'background-nonunit', 'background-unit-adjust', 'four-heavy-nonunit',
                'three-heavy-nonunit', 'three-heavy-light', 'two-heavy-protected-EGZ',
                'midpoint-opposite-terminal', 'coefficient-crossing', 'four-heavy-unit',
                'three-heavy-spare-max', 'progression-nonunit', 'progression-unit'}
    assert required <= branches.keys(), required - branches.keys()
    target = Path(__file__).with_name('arbitrary_arity_linear_witnesses.json')
    zero_records = check_zero_trigger()
    target.write_text(json.dumps({'index_base': 1, 'seed': 20260912046,
                                 'scope': 'finite original-position witnesses, not shortest paths',
                                 'cases': records, 'zero_trigger_cases': zero_records,
                                 'branches': dict(sorted(branches.items()))},
                                indent=2) + '\n', encoding='utf-8')
    print('all-arity original-position full paths: PASS', len(records), max(x['steps'] for x in records))
    print('branches:', dict(sorted(branches.items())))
    print('arbitrary-arity linear threshold: PASS')


if __name__ == '__main__':
    main()
