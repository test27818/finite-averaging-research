"""Even middle-core formulas and the complete finite certificate for (7,18).

Infinite group containment uses Morris and Serre as stated in the proof.
The finite certificate exhausts its proved quotient, not an input-height box.
All arithmetic is exact; no new averaging word or seed is searched for.
"""

from collections import Counter, deque
from fractions import Fraction as F
from math import gcd, lcm
from pathlib import Path
from random import Random
import json

from verify_four_prime_entry_and_band import (
    Ledger, factors, is_legal, residue, triple_return,
)
from verify_carrier_energy_and_pair_reduction import safe_flatten
from verify_upper_band_three_value_reduction import full_support, mix, select_parameter
from verify_uniform_odd_middle_cores import mm, invq, bezout

if not __debug__:
    raise RuntimeError('Assertions are required.')

ROOT = Path(__file__).parent
P, R, N, IDEAL, MODULUS = 7, 4, 18, 72, 5184
I = (1, 0, 0, 1)
# Coordinates (z,y), y=a+7*z. Every generator is its own projective inverse.
GENERATORS = ((1, 0, 18, -1), (7, -1, 36, -7), (7, -1, 54, -7))
TERMINALS = ((1, 0, (3, 3, 1)), (-1, 2, (4, 2, 1)))  # a,z, counts


def modular(value, modulus):
    value = F(value)
    return value.numerator * pow(value.denominator, -1, modulus) % modulus


def primitive_pair(a, z):
    denominator = lcm(F(a).denominator, F(z).denominator)
    aa, zz = int(a * denominator), int(z * denominator)
    common = gcd(aa, zz)
    assert common
    return aa // common, zz // common


def pair_algebra(p, r):
    n = 2 * p + r
    assert p >= 7 and r % 2 == 0 and 4 <= r <= p - 3
    d = (p * r - n * (r - 1)) // 2
    e = d + n
    assert gcd(d, e) == gcd(d, n) == gcd(e, n) == 1
    assert d % 2 and e % 2 and abs(d * e) > 1
    j, q, sigma = (0, d, -1, 0), (0, e, -1, 0), (-1, r, 0, 1)
    diagonal = mm(invq(j), q)
    assert diagonal == (1, 0, 0, F(e, d))
    assert mm(mm(mm(sigma, diagonal), sigma), invq(diagonal)) == (1, F(r*n, e), 0, 1)
    assert mm(mm(j, (1, r*n, 0, 1)), invq(j)) == (1, 0, F(-r*n, d), 1)
    return d, e


def verify_formulas_and_positions():
    systems = literal = 0
    for p in (7, 11, 13, 17, 19, 23, 31, 43):
        for r in range(4, p - 2, 2):
            d, e = pair_algebra(p, r)
            systems += 1
            if p > 19:
                continue
            for a, z in ((1, 0), (0, 1)):
                raw = [F(a)]*p + [r*F(z)-a]*p + [-p*F(z)]*r
                for s, coefficient in ((r-1, d), (r-3, e)):
                    ledger = Ledger(raw, p)
                    groups = [list(range(p)), list(range(p, 2*p)), list(range(2*p, 2*p+r))]
                    groups = triple_return(ledger, groups, p, r, s)
                    aa, zz = F(coefficient*z, p), F(-a, p)
                    assert [ledger.state[g[0]] for g in groups] == [aa, r*zz-aa, -p*zz]
                    groups = triple_return(ledger, groups, p, r, s)
                    scale = F(-coefficient, p*p)
                    assert [ledger.state[g[0]] for g in groups] == [scale*a, scale*(r*z-a), -scale*p*z]
                    ledger.independent_replay(raw)
                    literal += 1
    assert pair_algebra(7, 4) == (-13, 5)
    print('even middle pair and root identities: PASS', systems)
    print('even middle original-position involutions: PASS', literal)
    return systems, literal


def short_mix_entry(raw, p, r):
    n, primes = len(raw), tuple(factors(len(raw)))
    assert n == 2*p+r and 1 <= r < p and p >= 5
    assert r >= len(primes) and gcd(2*p-1, n) == 1
    assert sum(raw) == 0 and gcd(*raw) == 1 and is_legal(raw, primes)
    _, blocks, singles = safe_flatten(raw, p, 2, ledger=True)
    ledger = Ledger(raw, p)
    for block in blocks:
        ledger.average(block)
    anchor = singles[0]
    first, second, singles, phases = full_support(ledger, *blocks, singles, anchor, primes)
    a, b, w = ledger.state[first[0]], ledger.state[second[0]], ledger.state[anchor]
    conditions = [(ell, residue(p*a-(p-1)*b-w, ell),
                   residue(F(2*p-1, p)*(b-a), ell)) for ell in primes]
    k = select_parameter(p, conditions)
    first, second = mix(ledger, first, second, k)
    role = singles.index(anchor)
    second, singles[role] = ledger.swap(second, anchor)
    assert all(residue(ledger.state[first[0]]-ledger.state[second[0]], ell) for ell in primes)
    carrier = first[p-r:]
    final = first[:p-r]+singles
    ledger.average(final)
    groups = [final, second, carrier]
    aa, bb, cc = [ledger.state[g[0]] for g in groups]
    assert p*(aa+bb)+r*cc == 0
    assert sorted(i for group in groups for i in group) == list(range(n))
    assert all(ledger.state[i] == value for group, value in zip(groups, (aa, bb, cc)) for i in group)
    replay = list(map(F, raw))
    for group in ledger.word:
        assert len(group) == len(set(group)) == p
        average = sum(replay[i] for i in group)/p
        for i in group:
            replay[i] = average
        assert sum(replay) == 0 and is_legal(replay, primes)
    assert replay == ledger.state and len(ledger.word) <= 6+3*len(primes)
    return ledger, groups, phases


def verify_entries():
    rng = Random(2026091427)
    records = []
    for p in (5, 7, 11, 13, 17, 19):
        for r in range(1, p):
            n = 2*p+r
            if r < len(factors(n)) or gcd(2*p-1, n) != 1:
                continue
            for _ in range(2):
                while True:
                    raw = [rng.randrange(-10000, 10001) for _ in range(n-1)]
                    raw.append(-sum(raw))
                    common = gcd(*raw)
                    if common:
                        raw = [x//common for x in raw]
                        if is_legal(raw, factors(n)):
                            break
                ledger, groups, phases = short_mix_entry(raw, p, r)
                records.append({'p': p, 'n': n, 'input': raw, 'operations': ledger.word,
                                'groups': groups, 'values': [str(ledger.state[g[0]]) for g in groups],
                                'phase_count': len(phases)})
    print('short-mixing full-input entries: PASS', len(records))
    return records


def action(matrix, x, inverses):
    a, b, c, d = matrix
    denominator = (c*x+d) % MODULUS
    assert denominator in inverses
    return (a*x+b)*inverses[denominator] % MODULUS


def finite_certificate():
    inverses = {value: pow(value, -1, MODULUS) for value in range(MODULUS)
                if gcd(value, MODULUS) == 1}
    # Every recorded residue is represented by a genuine R^* unit, R=Z[1/65].
    unit_parent = {1: None}
    queue = deque([1])
    while queue:
        value = queue.popleft()
        for factor in (-1, 5, 13):
            following = value*factor % MODULUS
            if following not in unit_parent:
                unit_parent[following] = (value, factor)
                queue.append(following)
    assert set(unit_parent) == set(inverses) and len(unit_parent) == 1728

    starts = [(z*inverses[(a+P*z) % MODULUS]) % MODULUS for a, z, _ in TERMINALS]
    forest = {}
    queue = deque()
    for terminal_id, start in enumerate(starts):
        forest[start] = (terminal_id, None, None, 0)
        queue.append(start)
    while queue:
        x = queue.popleft()
        terminal_id, _, _, depth = forest[x]
        for generator_id, matrix in enumerate(GENERATORS):
            following = action(matrix, x, inverses)
            if following not in forest:
                forest[following] = (terminal_id, x, generator_id, depth+1)
                queue.append(following)
    assert set(forest) == set(range(MODULUS))
    counts = Counter(record[0] for record in forest.values())
    assert counts == {0: 2592, 1: 2592}
    for x, (terminal_id, parent, generator_id, depth) in forest.items():
        assert terminal_id == (0 if x % 4 in (0, 3) else 1)
        if parent is None:
            assert depth == 0 and x == starts[terminal_id]
        else:
            assert action(GENERATORS[generator_id], x, inverses) == parent
            assert forest[parent][0] == terminal_id and forest[parent][3] == depth-1
        for matrix in GENERATORS:
            assert forest[action(matrix, x, inverses)][0] == terminal_id
    print('eighteen complete unit image: PASS', len(unit_parent))
    print('eighteen complete congruence quotient: PASS', len(forest), dict(counts),
          max(record[3] for record in forest.values()))
    return unit_parent, forest


def unit_lift(target, parents):
    value = 1
    while target != 1:
        target, factor = parents[target]
        value *= factor
    return value


def determinant_one_completion(a, z):
    common, alpha, beta = bezout(a, z)
    assert common == 1
    return (a, -beta, z, alpha)


def principal_transport(source, target, unit):
    """Construct an exact H in Gamma(5184,R) sending source to unit*target."""
    a, z = source
    aa, zz = target
    b, d = determinant_one_completion(a, z)[1::2]
    target_b, target_d = determinant_one_completion(aa, zz)[1::2]
    c, e = F(target_b, unit), F(target_d, unit)
    ua, uz = unit*aa, unit*zz
    assert (ua-a) % MODULUS == (uz-z) % MODULUS == 0
    if gcd(a, MODULUS) == 1:
        k = modular(b-c, MODULUS)*pow(a, -1, MODULUS) % MODULUS
    else:
        # For a composite modulus, neither coordinate need be a global unit.
        common, alpha, beta = bezout(a, z)
        assert common == 1
        k = modular(alpha*(b-c)+beta*(d-e), MODULUS)
    c, e = c+k*ua, e+k*uz
    assert modular(c-b, MODULUS) == modular(e-d, MODULUS) == 0
    left, right = (ua, c, uz, e), (a, b, z, d)
    h = mm(left, invq(right))
    assert h[0]*h[3]-h[1]*h[2] == 1
    assert all(modular(value-delta, MODULUS) == 0 for value, delta in zip(h, I))
    assert (h[0]*a+h[1]*z, h[2]*a+h[3]*z) == (ua, uz)
    for value in h:
        assert all(q in (5, 13) for q in factors(F(value).denominator))
    return h


def verify_target_lifts(parents, forest):
    checked = 0
    # Every quotient direction gets an integer primitive lift, not a random box.
    for x in range(MODULUS):
        a, z = 1-P*x, x
        current = x
        while forest[current][1] is not None:
            _, parent, generator_id, _ = forest[current]
            if generator_id == 0:
                a, z = R*z-a, z
            else:
                coefficient = -13 if generator_id == 1 else 5
                a, z = coefficient*z, -a
            a, z = primitive_pair(a, z)
            assert gcd(a+P*z, N) == 1
            assert modular(F(z, a+P*z), MODULUS) == parent
            current = parent
        terminal_id = forest[current][0]
        target_a, target_z, _ = TERMINALS[terminal_id]
        ratio = (a+P*z)*pow(target_a+P*target_z, -1, MODULUS) % MODULUS
        unit = unit_lift(ratio, parents)
        assert unit % MODULUS == ratio
        principal_transport((a, z), (target_a, target_z), unit)
        checked += 1
    print('eighteen exact principal target lifts: PASS', checked)
    return checked


def verify_terminals():
    for a, z, counts in TERMINALS:
        raw = [F(a)]*P+[R*F(z)-a]*P+[-P*F(z)]*R
        ledger = Ledger(raw, P)
        i, j, k = counts
        group = list(range(i))+list(range(P, P+j))+list(range(2*P, 2*P+k))
        assert sum(raw[index] for index in group) == 0
        ledger.average(group)
        # At most 11 nonzero entries remain. Fit them in a 15-point zero-sum window.
        nonzero = [index for index, value in enumerate(ledger.state) if value]
        zeros = [index for index, value in enumerate(ledger.state) if not value]
        window = nonzero+zeros[:2*P+1-len(nonzero)]
        anchor = next(index for index in window if not ledger.state[index])
        rest = [index for index in window if index != anchor]
        first, second = rest[:P], rest[P:]
        ledger.average(first)
        ledger.average(second)
        assert ledger.state[first[0]] == -ledger.state[second[0]]
        h = (P-1)//2
        for start in (0, h):
            ledger.average(first[start:start+h]+second[start:start+h]+[anchor])
        zero_indices = [index for index, value in enumerate(ledger.state) if not value]
        ledger.average([first[-1], second[-1]]+zero_indices[:P-2])
        assert not any(ledger.state)
        ledger.independent_replay(raw)
    print('eighteen literal zero-trigger terminals: PASS', len(TERMINALS))


def main():
    systems, literal = verify_formulas_and_positions()
    entries = verify_entries()
    unit_parents, forest = finite_certificate()
    target_lifts = verify_target_lifts(unit_parents, forest)
    verify_terminals()
    data = {'scope': 'Complete finite quotient after the proved principal-congruence containment; '
                     'infinite arithmetic-group input remains an external theorem.',
            'arity': P, 'dimension': N, 'root_ideal': IDEAL, 'modulus': MODULUS,
            'ring': 'Z[1/65]', 'parameter_systems': systems, 'literal_returns': literal,
            'target_lifts': target_lifts, 'terminals': TERMINALS, 'generators_zy': GENERATORS,
            'unit_generators': [-1, 5, 13],
            'unit_parents': [[key, value] for key, value in sorted(unit_parents.items())],
            'forest': [[key, *value] for key, value in sorted(forest.items())],
            'full_input_entries': entries}
    (ROOT/'even_middle_eighteen_congruence_records.json').write_text(
        json.dumps(data, indent=2)+'\n', encoding='utf-8')
    print('even middle congruence and seven-average eighteen: PASS')


if __name__ == '__main__':
    main()
