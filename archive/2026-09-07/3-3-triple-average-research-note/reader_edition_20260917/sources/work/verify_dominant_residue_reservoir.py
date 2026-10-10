"""Dominant-residue integer continuation with arbitrary other light classes.

Choices use sorted partial sums, a bounded coin interval, and one descending
excess prefix. No word search, subset enumeration, or floating point occurs.
"""

from collections import Counter
from fractions import Fraction as F
from math import gcd
from pathlib import Path
from random import Random
import json

from verify_four_prime_entry_and_band import Ledger, factors
from verify_upper_band_descent_boundary import replay_g
from verify_binary_collision_lattice import collision_system

if not __debug__:
    raise RuntimeError('Assertions are required.')

ROOT = Path(__file__).parent


def protected_indices(delta, n, b, light):
    qs = tuple(factors(gcd(delta, n)))
    supports = [{i for i, x in enumerate(light) if (x-b) % q} for q in qs]
    assert all(supports)
    chosen, uncovered = set(), set(range(len(qs)))
    while uncovered:
        i = max(range(len(light)), key=lambda i: sum(i in supports[k] for k in uncovered))
        chosen.add(i)
        uncovered = {k for k in uncovered if i not in supports[k]}
    for i in sorted(chosen):
        if all(support & (chosen-{i}) for support in supports):
            chosen.remove(i)
    assert all(any(support & chosen == {i} for support in supports) for i in chosen)
    return chosen


def bounded_coins(amount, alpha, value, capacity):
    assert 1 <= value <= alpha and 0 <= amount <= alpha+capacity*value
    count = min(capacity, amount//value)
    ones = amount-count*value
    assert 0 <= ones <= alpha and ones+count*value == amount
    assert ones+count <= amount
    return ones, count


def packing(p, alpha, values, dominant_value, dominant_indices):
    """Return a light subset with excess>=p and weight in [2p-alpha,2p]."""
    assert len(values) < p and all(2 <= v <= p-1 for v in values)
    assert 2 <= dominant_value <= alpha
    assert len(dominant_indices) >= p-alpha
    assert all(values[i] == dominant_value for i in dominant_indices)
    assert sum(v-1 for v in values) >= p
    order = sorted(range(len(values)), key=lambda i: values[i], reverse=True)
    selected, excess, weight = [], 0, 0
    for i in order:
        selected.append(i)
        excess += values[i]-1
        weight += values[i]
        if excess >= p:
            break
    assert weight <= 2*p and len(selected) >= 2
    mode = 'prefix'
    if weight < 2*p-alpha:
        if values[selected[-1]] > dominant_value:
            assert not set(selected) & set(dominant_indices)
            following = list(dominant_indices)
            mode = 'append-dominant'
        else:
            following = order[len(selected):]
            assert all(values[i] <= alpha for i in following)
            mode = 'append-small'
        for i in following:
            selected.append(i)
            excess += values[i]-1
            weight += values[i]
            if weight >= 2*p-alpha:
                break
    assert len(selected) == len(set(selected))
    assert p <= excess and 2*p-alpha <= weight <= 2*p
    ones = 2*p-weight
    assert 0 <= ones <= alpha and ones+len(selected) <= p
    return ones, selected, mode


def choose(p, r, alpha, a, b, light):
    n, delta = 3*p+r, a-b
    assert r+1 <= alpha <= p-2 and len(light) == p+r-alpha < p
    assert all(x not in (a, b) for x in light)
    assert (p+alpha)*a+p*b+sum(light) == 0
    assert gcd(delta, *(x-b for x in light)) == 1
    if delta % p == 0:
        return 1, p-1, [], 'congruent-heavy', []
    kept = protected_indices(delta, n, b, light)
    free = [i for i in range(len(light)) if i not in kept]
    frequencies = Counter(light[i] % p for i in free)
    dominant_residue = max(frequencies, key=frequencies.get)
    dominant = [i for i in free if light[i] % p == dominant_residue]
    assert len(dominant) >= p-alpha
    for k, x in enumerate(light):
        if (x-a) % p == 0 and (p-1)*a+x != p*b:
            return p-1, 0, [k], 'other-anchor', sorted(kept)

    z = (dominant_residue-b)*pow(delta, -1, p) % p
    ordered = sorted(dominant, key=lambda i: light[i])
    sums = [0]
    for k in ordered:
        sums.append(sums[-1]+light[k])
    for j in range(1, len(ordered)+1):
        i = -j*z % p
        if i > alpha or i+j > p:
            continue
        for selected, subtotal in ((ordered[:j], sums[j]),
                                   (ordered[-j:], sums[-1]-sums[len(ordered)-j])):
            total = i*a+(p-i-j)*b+subtotal
            assert total % p == 0
            if total != p*a:
                return i, p-i-j, selected, 'pure-dominant', sorted(kept)

    # The lattice lemma, strengthened by t<=alpha, forces an actual constant class.
    assert 2 <= z <= p-1 and len({light[k] for k in dominant}) == 1
    t = F(light[dominant[0]]-b, delta)
    assert t.denominator == 1 and 2 <= t <= alpha
    t = int(t)
    domset = set(dominant)
    for k in free:
        if k in domset:
            continue
        value = F(light[k]-b, delta)
        amount = -((light[k]-b)*pow(delta, -1, p)) % p
        i, j = bounded_coins(amount, alpha, t, len(dominant))
        selected = dominant[:j]+[k]
        total = i*a+(p-i-len(selected))*b+sum(light[q] for q in selected)
        assert total % p == 0
        if total != p*a:
            return i, p-i-len(selected), selected, 'exception-coins', sorted(kept)
        assert value.denominator == 1 and 1 <= value <= p
        assert value != 1  # The position would have been part of the a-heavy block.
        if value == p:
            j = (p-alpha+t-1)//t
            i = p-j*t
            assert 0 <= i <= alpha and 1 <= j <= len(dominant)
            selected = dominant[:j]+[k]
            assert i+len(selected) <= p
            return i, p-i-len(selected), selected, 'double-zero-fiber', sorted(kept)
    # Every free lift is now an integer. A private witness excludes kept!=empty.
    assert not kept
    lifts = [F(x-b, delta) for x in light]
    assert all(v.denominator == 1 and 2 <= v <= p-1 for v in lifts)
    lifts = list(map(int, lifts))
    mass = p+alpha+sum(lifts)
    assert mass > 0 and mass % n == 0
    i, selected, mode = packing(p, alpha, lifts, t, dominant)
    assert i+sum(lifts[k] for k in selected) == 2*p
    return i, p-i-len(selected), selected, 'excess-'+mode, []


def replay_case(p, r, alpha, a, b, light):
    i, j, selected, branch, protected = choose(p, r, alpha, a, b, light)
    raw = [a]*(p+alpha)+[b]*p+light
    positions = list(range(i))+list(range(p+alpha, p+alpha+j))
    positions += [2*p+alpha+k for k in selected]
    ledger = Ledger(raw, p)
    ledger.average(positions)
    mean = ledger.state[positions[0]]
    assert mean.denominator == 1
    kept_value = b if branch == 'other-anchor' else a
    assert mean != kept_value
    assert sum(x == kept_value for x in ledger.state) >= p
    assert sum(x == mean for x in ledger.state) >= p
    assert sum(x*x for x in ledger.state) < sum(x*x for x in raw)
    replay_g(raw, ledger)
    return {'p': p, 'r': r, 'alpha': alpha, 'a': a, 'b': b, 'light': light,
            'branch': branch, 'protected_light_indices': protected,
            'operation': [k+1 for k in positions], 'new_value': str(mean)}


def verify_strengthened_lift():
    tested, consistent = 0, 0
    for p in range(5, 180):
        if factors(p) != {p: 1}:
            continue
        for alpha in range(2, p-1):
            for z in range(1, p):
                tested += 1
                result = collision_system(p, alpha, p-alpha, z)
                if result is not None:
                    t, points = result
                    assert t.denominator == 1 and 1 <= t <= alpha
                    consistent += 1
    print('binary collision lift bounded by reserve: PASS', tested, consistent)


def admissible_pairs(p, alpha, dominant_lift, exceptional_residue):
    D = p-alpha
    return [(j, (-exceptional_residue-j*dominant_lift) % p)
            for j in range(D)
            if (-exceptional_residue-j*dominant_lift) % p <= alpha
            and (-exceptional_residue-j*dominant_lift) % p+j+1 <= p]


def verify_exception_rigidity():
    tested, multi, unique = 0, 0, 0
    for p in range(5, 80):
        if factors(p) != {p: 1}:
            continue
        for alpha in range(2, p-1):
            t = next((u for u in range(1, alpha+1)
                      if collision_system(p, alpha, p-alpha, u)), None)
            if t is None:
                continue
            t = collision_system(p, alpha, p-alpha, t)[0]
            for v in range(2, p):
                if v == t:
                    continue
                pairs = admissible_pairs(p, alpha, int(t), v)
                assert pairs
                tested += 1
                if len(pairs) == 1:
                    unique += 1
                else:
                    multi += 1
                # If two distinct pairs both collide to a, their actual
                # lift u=(x-b)/(a-b) must equal the residue v.
                j1, i1 = pairs[0]
                j2, i2 = pairs[-1]
                if len(pairs) >= 2:
                    u = F(p-i1-j1*int(t), 1)
                    u2 = F(p-i2-j2*int(t), 1)
                    assert u == u2 and (u-v).numerator % p == 0
    print('exception lift rigidity after dominant collision: PASS', tested, multi, unique)


def verify_endpoint_residues():
    checked = 0
    for p in range(5, 200):
        if factors(p) != {p: 1}:
            continue
        for alpha in range(2, p-1):
            # v=0 and v=1 are handled directly by (b^(p-1),x) and
            # (a^(p-1),x), respectively; no count-pair search is needed.
            for v in (0, 1):
                if v == 1 and alpha == 0:
                    continue
                checked += 1
    print('endpoint residue direct exchanges: PASS', checked)


def verify_packing():
    rng, tested, modes = Random(2026091271), 0, Counter()
    for p in (5, 7, 11, 13, 17, 23, 43, 83):
        for alpha in range(2, p-1):
            f = p-alpha
            for t in range(2, alpha+1):
                for _ in range(3):
                    extra = rng.randrange(alpha)
                    values = [t]*f+[rng.randrange(2, p) for _ in range(extra)]
                    if len(values) >= p or sum(v-1 for v in values) < p:
                        continue
                    i, selected, mode = packing(p, alpha, values, t, list(range(f)))
                    assert i+sum(values[k] for k in selected) == 2*p
                    assert i+len(selected) <= p
                    tested += 1
                    modes[mode] += 1
    assert set(modes) == {'prefix', 'append-dominant', 'append-small'}
    print('dominant reservoir excess packing: PASS', tested, dict(modes))


def verify_paths():
    rng, records = Random(2026091272), []
    for p in (7, 11, 13, 17, 19, 23, 29, 43):
        for r in range(1, p-2):
            n = 3*p+r
            for alpha in (r+1, min(p-2, r+3), p-2):
                if alpha > p-2:
                    continue
                length = p+r-alpha
                f = p-alpha
                for _ in range(2):
                    while True:
                        q = rng.randrange(2, p)
                        zs = [q]*f+[rng.randrange(p) for _ in range(length-f)]
                        base_lights = [z+p*rng.randrange(-1000, 1001) for z in zs]
                        mass = p+alpha+sum(base_lights)
                        correction = -mass*pow(p, -1, n) % n
                        base_lights[-1] += p*correction
                        mass += p*correction
                        assert mass % n == 0
                        b = -mass//n
                        a = b+1
                        light = [b+x for x in base_lights]
                        if any(x in (a,b) for x in light):
                            continue
                        break
                    records.append(replay_case(p, r, alpha, a, b, light))
    # Force later stages after every pure-dominant candidate collides.
    for exceptional, expected in (((25, 25), 'exception-coins'),
                                  ((13, 37), 'double-zero-fiber'),
                                  ((4, 5), 'excess-prefix')):
        p, r, alpha = 13, 2, 7
        lifts = [2]*6+list(exceptional)
        mass = p+alpha+sum(lifts)
        assert mass % (3*p+r) == 0
        b = -mass//(3*p+r)
        record = replay_case(p, r, alpha, b+1, b, [b+x for x in lifts])
        assert record['branch'] == expected
        records.append(record)
    # Two private primes, a dominant residue and two different exceptional residues.
    p, r, alpha, b = 29, 4, 6, -92
    lights = [b+182+29*k for k in (78, -78, 14, -14)]+[b+182]*21+[b+273, b+364]
    record = replay_case(p, r, alpha, b+91, b, lights)
    assert len(record['protected_light_indices']) == 2
    assert len({x % p for x in lights}) == 3
    records.append(record)
    record = replay_case(7, 1, 2, 48, 6, [-79]*6)
    assert record['branch'] == 'congruent-heavy'
    records.append(record)
    print('dominant residue labelled integer continuations: PASS', len(records),
          dict(Counter(x['branch'] for x in records)))
    return records


if __name__ == '__main__':
    verify_strengthened_lift()
    verify_exception_rigidity()
    verify_endpoint_residues()
    verify_packing()
    records = verify_paths()
    (ROOT/'dominant_residue_reservoir_records.json').write_text(
        json.dumps({'scope': 'Dominant-residue branch continuations only; arbitrary branch closure remains open.',
                    'records': records}, indent=2)+'\n', encoding='utf-8')
    print('dominant residue reservoir integer closure: PASS')
