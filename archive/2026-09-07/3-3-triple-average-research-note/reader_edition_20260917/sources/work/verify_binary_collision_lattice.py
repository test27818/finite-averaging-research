"""Two-type collision lifts via lattice triangles and integer continuations.

Only one-dimensional modular count menus are enumerated. Original-state
tests select one actual integer p-average and independently replay labels.
No averaging-word search or floating point is used.
"""

from fractions import Fraction as F
from math import gcd
from random import Random
from pathlib import Path
import json

from verify_four_prime_entry_and_band import Ledger, factors
from verify_upper_band_descent_boundary import replay_g

if not __debug__:
    raise RuntimeError('Assertions are required.')

ROOT = Path(__file__).parent


def collision_system(p, alpha, light, residue):
    points, lift = [], None
    for j in range(1, light+1):
        i = -j*residue % p
        if i > alpha or i+j > p:
            continue
        value = F(p-i, j)
        if lift is not None and value != lift:
            return None
        lift = value
        points.append((i, j))
    assert points
    return lift, points


def verify_lattice_lemmas():
    critical, unique, multiple, surplus, matching = 0, 0, 0, 0, 0
    examples = []
    for p in range(5, 128):
        if factors(p) != {p: 1}:
            continue
        for alpha in range(2, p-1):
            for z in range(2, p):
                critical += 1
                result = collision_system(p, alpha, p-alpha, z)
                if result is None:
                    continue
                t, points = result
                assert t.denominator == 1 and t == z
                if len(points) == 1:
                    unique += 1
                    js = [(-i*pow(z, -1, p)) % p for i in range(1, alpha+1)]
                    assert sorted(j for j in js if j > p-alpha) == list(range(p-alpha+1, p))
                else:
                    multiple += 1
                    ordered = sorted(points, key=lambda ij: ij[1])
                    a, b = ordered[0], ordered[1]
                    assert b[1]-a[1] == t.denominator
                    assert abs(a[0]*b[1]-a[1]*b[0]) == p*t.denominator == p
        if p > 43:
            continue
        for e in range(1, p-3):
            for alpha in range(e+1, p-1):
                light = p+e-alpha
                assert 1 <= light < p
                for z in range(2, p):
                    surplus += 1
                    result = collision_system(p, alpha, light, z)
                    if result is None:
                        continue
                    matching += 1
                    t, points = result
                    total = p+alpha+light*t
                    assert t.denominator == total.denominator == 1
                    assert 0 < total < 3*p+e
                    if len(points) == 1:
                        assert e == 1
                        i, j = points[0]
                        assert (alpha, light) == (2*i, 2*j)
                        assert total == 3*p
                    else:
                        assert alpha >= t
                    if len(examples) < 8:
                        examples.append({'p': p, 'e': e, 'alpha': alpha,
                                         'light': light, 't': str(t), 'D': str(total)})
        # The elementary coin-count inequality used in the mass bound.
        assert all((2*p//t)*(t-1) >= p for t in range(3, p))
    print('critical two-type collision integrality: PASS', critical, unique, multiple)
    print('surplus two-type collision mass bound: PASS', surplus, matching)
    return examples


def normalize(values):
    common = gcd(*values)
    return tuple(x//common for x in values)


def one_light_move(p, r, alpha, values):
    a, b, c = values
    light, n = p+r-alpha, 3*p+r
    assert r+1 <= alpha <= p-2 and 1 <= light < p
    assert len(set(values)) == 3 and (p+alpha)*a+p*b+light*c == 0
    assert gcd(*values) == gcd(a-b, c-b) == 1
    delta = a-b
    if delta % p == 0:
        return (1, p-1, 0), 'congruent-heavy', 0
    protected = int(gcd(delta, n) > 1)
    if protected:
        for q in factors(gcd(delta, n)):
            assert light % q == 0 and (c-b) % q
    available = light-protected
    assert alpha+available >= p
    z = (c-b)*pow(delta, -1, p) % p
    for j in range(1, available+1):
        i = -j*z % p
        if i <= alpha and i+j <= p:
            mean_numerator = i*a+(p-i-j)*b+j*c
            assert mean_numerator % p == 0
            if mean_numerator != p*a:
                return (i, p-i-j, j), 'noncolliding-binary', protected
    raise AssertionError(('Binary continuation theorem failed', p, r, alpha, values))


def literal_one_light(p, r, alpha, values):
    light = p+r-alpha
    weights = (p+alpha, p, light)
    raw = [x for x, count in zip(values, weights) for _ in range(count)]
    counts, kind, protected = one_light_move(p, r, alpha, values)
    blocks, start = [], 0
    for count in weights:
        blocks.append(list(range(start, start+count)))
        start += count
    group = [i for block, count in zip(blocks, counts) for i in block[:count]]
    ledger = Ledger(raw, p)
    before = sum(x*x for x in raw)
    ledger.average(group)
    assert all(x.denominator == 1 for x in ledger.state)
    mean = ledger.state[group[0]]
    assert mean != values[0]
    assert sum(x == values[0] for x in ledger.state) >= p
    assert sum(x == mean for x in ledger.state) >= p
    assert sum(x*x for x in ledger.state) < before
    replay_g(raw, ledger)
    return {'p': p, 'r': r, 'alpha': alpha, 'values': list(values),
            'weights': list(weights), 'group_counts': list(counts),
            'operation': [i+1 for i in group], 'new_value': str(mean),
            'kind': kind, 'protected': protected}


def random_values(rng, weights):
    a_count, b_count, c_count = weights
    while True:
        u, v = (rng.randrange(-(1 << 50), 1 << 50) for _ in range(2))
        values = normalize((c_count*u, c_count*v, -a_count*u-b_count*v))
        a, b, c = values
        if len(set(values)) == 3 and gcd(a-b, c-b) == 1:
            return values


def verify_one_light():
    rng, records = Random(2026091263), []
    for p in (5, 7, 11, 13, 17, 19, 23, 29, 31, 43):
        for r in range(1, p-2):
            for alpha in range(r+1, p-1):
                weights = (p+alpha, p, p+r-alpha)
                records.append(literal_one_light(p, r, alpha, random_values(rng, weights)))
    # A critical r=1 case in which the unique light type carries the mod2 witness.
    forced = literal_one_light(7, 1, 2, (1, -3, 2))
    assert forced['protected'] == 1
    records.append(forced)
    assert any(x['kind'] == 'congruent-heavy' for x in records)
    print('one-light-type labelled integer continuations: PASS', len(records),
          sum(x['protected'] for x in records), sum(x['r'] == 1 for x in records))
    return records


def three_heavy_move(p, r, values, extras):
    assert len(set(values)) == 3 and sum(extras) == r
    assert gcd(values[0]-values[1], values[2]-values[1]) == 1
    weights = [p+e for e in extras]
    assert sum(w*x for w, x in zip(weights, values)) == 0
    zero = next((i for i, x in enumerate(values) if x == 0), None)
    if zero is not None:
        counts = [0, 0, 0]
        counts[zero] = p
        return counts, 'zero', None
    for i in range(3):
        for j in range(i+1, 3):
            if (values[i]-values[j]) % p == 0:
                counts = [0, 0, 0]
                counts[i], counts[j] = 1, p-1
                if values[i]+(p-1)*values[j] == p*values[3-i-j]:
                    counts[i], counts[j] = 2, p-2
                return counts, 'congruent-pair', 3-i-j
    order = sorted(range(3), key=lambda i: values[i])
    kept = next((i for i in (order[0], order[2]) if extras[i]), order[1])
    assert extras[kept]
    left, right = [i for i in range(3) if i != kept]
    i = (values[right]-values[kept])*pow(values[left]-values[right], -1, p) % p
    counts = [0, 0, 0]
    counts[left], counts[right], counts[kept] = i, p-1-i, 1
    mean_numerator = sum(k*x for k, x in zip(counts, values))
    assert mean_numerator % p == 0
    assert mean_numerator != p*values[kept]
    return counts, 'extra-extreme' if kept != order[1] else 'primitive-middle', kept


def verify_three_heavy():
    rng, records = Random(2026091264), []
    for p in (5, 7, 11, 13, 17, 23, 31):
        for r in range(1, p):
            for extras in ((r, 0, 0), (0, r, 0), (r//2, 0, r-r//2)):
                weights = [p+e for e in extras]
                values = random_values(rng, weights)
                if 0 in values:
                    continue
                counts, kind, kept = three_heavy_move(p, r, values, extras)
                raw = [x for x, weight in zip(values, weights) for _ in range(weight)]
                positions, offset = [], 0
                for count, weight in zip(counts, weights):
                    positions += list(range(offset, offset+count))
                    offset += weight
                ledger = Ledger(raw, p)
                ledger.average(positions)
                assert all(x.denominator == 1 for x in ledger.state)
                assert sum(x*x for x in ledger.state) < sum(x*x for x in raw)
                mean = ledger.state[positions[0]]
                assert sum(x == values[kept] for x in ledger.state) >= p
                assert sum(x == mean for x in ledger.state) >= p and mean != values[kept]
                replay_g(raw, ledger)
                records.append({'p': p, 'r': r, 'values': list(values), 'extras': list(extras),
                                'group_counts': counts, 'kind': kind})
    assert any(x['kind'] == 'primitive-middle' and x['r'] == 1 for x in records)
    # Nonzero collisions can occur if the indispensable G=1 hypothesis is dropped.
    p, r, a, b, c, i = 7, 1, -41, 14, 25, 1
    assert p*a+(p+r)*b+p*c == 0
    assert gcd(a-b, c-b) == 11
    assert i*a+(p-1-i)*c+b == p*b
    print('three-heavy labelled integer continuations including r1: PASS', len(records),
          sum(x['r'] == 1 for x in records))
    print('middle-collision primitive hypothesis control: PASS')
    return records


def monochromatic_move(p, r, alpha, a, b, light):
    n, delta = 3*p+r, a-b
    assert len(light) == p+r-alpha < p
    assert all(x not in (a, b) for x in light)
    assert len({x % p for x in light}) == 1
    assert gcd(delta, *(x-b for x in light)) == 1
    assert (p+alpha)*a+p*b+sum(light) == 0
    if delta % p == 0:
        return (1, p-1, []), []
    qs = tuple(factors(gcd(delta, n)))
    supports = [{j for j, x in enumerate(light) if (x-b) % q} for q in qs]
    assert all(supports)
    protected, uncovered = set(), set(range(len(qs)))
    while uncovered:
        j = max(range(len(light)), key=lambda j: sum(j in supports[k] for k in uncovered))
        protected.add(j)
        uncovered = {k for k in uncovered if j not in supports[k]}
    for j in sorted(protected):
        if all(support & (protected-{j}) for support in supports):
            protected.remove(j)
    assert all(any(support & protected == {j} for support in supports) for j in protected)
    assert len(protected) <= r
    free = sorted((j for j in range(len(light)) if j not in protected), key=lambda j: light[j])
    assert alpha+len(free) >= p
    sums = [0]
    for j in free:
        sums.append(sums[-1]+light[j])
    z = (light[0]-b)*pow(delta, -1, p) % p
    for count in range(1, len(free)+1):
        i = -count*z % p
        if i > alpha or i+count > p:
            continue
        for selected, total in ((free[:count], sums[count]),
                                (free[-count:], sums[-1]-sums[len(free)-count])):
            numerator = i*a+(p-i-count)*b+total
            assert numerator % p == 0
            if numerator != p*a:
                return (i, p-i-count, selected), sorted(protected)
    raise AssertionError(('Monochromatic continuation failed', p, r, alpha))


def verify_monochromatic(one_light_records):
    rng, samples, records = Random(2026091265), [], []
    for record in one_light_records[::17]:
        p, r, alpha = record['p'], record['r'], record['alpha']
        a, b, c = record['values']
        light = [c]*(p+r-alpha)
        k = rng.randrange(1000, 1 << 24)
        light[0] += p*k
        light[1] -= p*k
        assert all(x not in (a, b) for x in light)
        samples.append((p, r, alpha, a, b, light))
    # Three distinct private witnesses at the exact alpha+free=p boundary.
    p, r, alpha, a, b = 29, 3, 4, -48, -78
    light = [b+60+29*u for u in (15, -15, 10, -10, 6, -6)]+[b+60]*22
    light[-1] += 4350
    samples.append((p, r, alpha, a, b, light))
    for p, r, alpha, a, b, light in samples:
        (i, j, chosen), protected = monochromatic_move(p, r, alpha, a, b, light)
        raw = [a]*(p+alpha)+[b]*p+light
        group = list(range(i))+list(range(p+alpha, p+alpha+j))
        group += [2*p+alpha+k for k in chosen]
        ledger = Ledger(raw, p)
        ledger.average(group)
        mean = ledger.state[group[0]]
        assert mean.denominator == 1 and mean != a
        assert sum(x == a for x in ledger.state) >= p and sum(x == mean for x in ledger.state) >= p
        assert sum(x*x for x in ledger.state) < sum(x*x for x in raw)
        replay_g(raw, ledger)
        records.append({'p': p, 'r': r, 'alpha': alpha, 'a': a, 'b': b,
                        'light': light, 'protected_light_indices': protected,
                        'operation': [k+1 for k in group], 'new_value': str(mean)})
    assert len(records[-1]['protected_light_indices']) == 3
    print('one-residue multi-value integer continuations: PASS', len(records),
          max(len(x['protected_light_indices']) for x in records))
    return records


if __name__ == '__main__':
    systems = verify_lattice_lemmas()
    one_light = verify_one_light()
    three_heavy = verify_three_heavy()
    monochromatic = verify_monochromatic(one_light)
    (ROOT/'binary_collision_lattice_records.json').write_text(
        json.dumps({'scope': 'One-step integer continuation lemmas only; the wider multi-value class is not proved closed.',
                    'collision_examples': systems, 'one_light': one_light,
                    'three_heavy': three_heavy, 'monochromatic': monochromatic}, indent=2)+'\n', encoding='utf-8')
    print('binary lattice collision and critical integer branches: PASS')
