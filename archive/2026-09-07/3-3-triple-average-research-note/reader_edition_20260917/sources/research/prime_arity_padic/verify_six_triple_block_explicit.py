"""Independent integer-DAG audit of the new static G=3 theorem.

The oracle searches actual triples, without calling the proposed criterion or
its forced continuation algorithm. No depth cutoff is used.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations, combinations_with_replacement
from math import gcd
from pathlib import Path
from random import Random
import json
from verify_subcritical_complement_dynamics import core_distance

TRIPLES = tuple(combinations(range(6), 3))


def primitive(x):
    g = gcd(*x)
    if not g:
        return (0,)*6
    return tuple(sorted(t//g for t in x))


def gap(x):
    return gcd(*(t-x[0] for t in x))


def atom(x, indices):
    s = sum(x[i] for i in indices)
    assert len(indices) == len(set(indices)) == 3 and s % 3 == 0
    y = list(x)
    for i in indices:
        y[i] = s//3
    return tuple(y)


@lru_cache(None)
def oracle(x):
    if not any(x):
        return True
    for indices in TRIPLES:
        values = [x[i] for i in indices]
        if sum(values) % 3 or len(set(values)) == 1:
            continue
        y = primitive(atom(x, indices))
        assert sum(t*t for t in y) < sum(t*t for t in x)
        if oracle(y):
            return True
    return False


def split_block(x, size=3):
    counts = Counter(x)
    a = next(v for v, count in counts.items() if count >= size)
    rest = list(x)
    for _ in range(size):
        rest.remove(a)
    return a, rest


def G3_static(x):
    assert any(x) and gcd(*x) == 1 and gap(x) == 3
    counts = Counter(x)
    assert max(counts.values()) >= 3
    if max(counts.values()) == 3:
        return True
    assert max(counts.values()) == 4
    a, rest = split_block(x, 4)
    t = 2*a+rest[0]
    return t == 0 or (t % 3 == 0 and t % 9 != 0)


def fourfold_static(a, b):
    """Complete fixed formula for (a,a,a,a,b,-4a-b), not just G=3."""
    d = gcd(a, b)
    if not d:
        return True
    a, b = a//d, b//d
    x = (a, a, a, a, b, -4*a-b)
    return a == 0 or 2*a+b == 0 or (gap(x) == 3 and (2*a+b) % 9 != 0)


def G3_original_static(x):
    """Exactly twenty fixed arithmetic checks; no continuation or oracle."""
    assert gcd(*x) == 1 and gap(x) == 3
    for indices in TRIPLES:
        if sum(x[i] for i in indices) == 0:
            return True
        y = primitive(atom(x, indices))
        if gap(y) == 3 and G3_static(y):
            return True
    return False


def forced_core(x):
    x = primitive(x)
    rounds = 0
    while any(x):
        g = gap(x)
        if g % 2 == 0:
            return False, rounds
        if g == 3:
            return G3_static(x), rounds
        assert g == 1
        a, (b, c, d) = split_block(x)
        if a == 0:
            return True, rounds
        if len({b % 3, c % 3, d % 3}) == 1:
            return False, rounds
        assert len({b % 3, c % 3, d % 3}) == 3
        rest = [b, c, d]
        e = next(t for t in rest if (t-a) % 3 == 0)
        rest.remove(e)
        m = (2*a+e)//3
        if m == 0:
            return True, rounds
        exit_state = primitive((-m,)*3+(a, a, e))
        exit_g = gap(exit_state)
        content = gcd(a, m)
        assert exit_g == gcd((a+m)//content, 6)
        if exit_g == 3:
            assert G3_static(exit_state)
            return True, rounds
        assert exit_g in (1, 2, 6)
        if e == a:
            return False, rounds
        next_state = primitive((m,)*3+(a, *rest))
        assert gap(next_state) == 1
        assert sum(t*t for t in next_state) < sum(t*t for t in x)
        x = next_state
        rounds += 1
    return True, rounds


def full_input(x):
    x = primitive(x)
    if not any(x):
        return True
    for indices in TRIPLES:
        if sum(x[i] for i in indices) % 3:
            continue
        if forced_core(atom(x, indices))[0]:
            return True
    return False


def invariant_move(x):
    """Literal chosen move from the written G=3 proof, including parity choice."""
    x = primitive(x)
    assert G3_static(x)
    if max(Counter(x).values()) == 4:
        a, (b, c) = split_block(x, 4)
        t = (2*a+b)//3
        if t == 0:
            return 'terminal', atom((a, a, a, a, b, c), (0, 1, 4))
        assert t % 3
        index = 4 if (t-a) % 3 == 0 else 5
        return 'four', atom((a, a, a, a, b, c), (0, 1, index))
    a, rest = split_block(x)
    r = [(t-a)//3 for t in rest]
    inverse = pow(a, -1, 3)
    residues = [t*inverse % 3 for t in r]
    ordered = tuple(sorted(residues))
    values = (a, a, a, *rest)
    if ordered == (0, 0, 1):
        k = residues.index(1)
        j = next(i for i in range(3) if residues[i] == 0 and (r[i]-r[k]) % 2)
        return '001', atom(values, (0, 1, 3+j))
    if ordered == (0, 2, 2):
        j = residues.index(0)
        return '022', atom(values, (0, 1, 3+j))
    assert ordered == (1, 1, 2)
    k = next(i for i in range(3) if residues[i] == 1 and r[i] % 2)
    selected = (0,)+tuple(3+i for i in range(3) if i != k)
    return '112', atom(values, selected)


def check_move(x):
    branch, raw = invariant_move(x)
    y = primitive(raw)
    if branch == 'terminal':
        assert raw.count(0) >= 3
    else:
        assert G3_static(y)
    assert sum(t*t for t in y) < sum(t*t for t in x)
    return branch


def run():
    rng = Random(2026091607)
    branches = Counter()
    comparisons = Counter()
    max_rounds = 0
    for x in combinations_with_replacement(range(-9, 10), 6):
        if sum(x):
            continue
        x = primitive(x)
        assert full_input(x) == oracle(x), x
        comparisons['initial_multisets'] += 1
        if any(x) and gap(x) == 3:
            assert G3_original_static(x) == oracle(x)
            comparisons['original_G3_static'] += 1
    for _ in range(16000):
        a, b, c = [rng.randrange(-800, 801) for _ in range(3)]
        d = -3*a-b-c
        x = primitive((a, a, a, b, c, d))
        predicted, rounds = forced_core(x)
        max_rounds = max(max_rounds, rounds)
        assert predicted == oracle(x), (x, predicted)
        comparisons['general_core_samples'] += 1
        if any(x) and gap(x) == 3:
            assert G3_static(x) == oracle(x), x
            comparisons['static_G3_samples'] += 1
            if G3_static(x):
                branches[check_move(x)] += 1
    for a in range(-80, 81):
        for b in range(-80, 81):
            repeated = primitive((a,)*3+(b,)*2+(-3*a-2*b,))
            predicted_repeated = not any(repeated) or a == 0 or gap(repeated) == 3
            assert predicted_repeated == oracle(repeated), (a, b, repeated)
            comparisons['triple_pair_static'] += 1
            x = primitive((a,)*4+(b, -4*a-b))
            assert fourfold_static(a, b) == oracle(x), (a, b, x)
            comparisons['all_fourfold_static'] += 1
            if not any(x) or gap(x) != 3:
                continue
            assert G3_static(x) == oracle(x), x
            comparisons['fourfold_samples'] += 1
            if G3_static(x):
                branches[check_move(x)] += 1
    for _ in range(3000):
        first = [3*rng.randrange(-150, 151)+1 for i in range(5)]
        x = primitive(first+[-sum(first)])
        if gap(x) == 3:
            assert G3_original_static(x) == oracle(x), x
            comparisons['original_G3_static'] += 1
    for _ in range(10000):
        a, b, c = [3*rng.randrange(-10**30, 10**30)+1 for _ in range(3)]
        d = -3*a-b-c
        x = primitive((a, a, a, b, c, d))
        if any(x) and gap(x) == 3 and G3_static(x):
            branches[check_move(x)] += 1
            comparisons['large_integer_invariant_moves'] += 1
    # Guard the recorded candidate obstructions using the separate five-core oracle.
    five_energy = ((-5, -5, -5, -4, 19), (-7, -7, -7, 4, 17))
    assert all(sum(t*t for t in x) == 452 and gap(x) == 1 for x in five_energy)
    assert core_distance(3, 1, 24) is None
    assert core_distance(3, 11, 24) == 5

    def valuation3(value):
        if value == 0:
            return None
        order = 0
        while value % 3 == 0:
            value //= 3
            order += 1
        return order

    five_values = ((-80, -80, -80, 41, 199), (-80, -80, -80, 59, 181))
    signatures = []
    for x in five_values:
        signatures.append((tuple(valuation3(t) for t in x),
                           tuple(valuation3(x[i]-x[j]) for i in range(5) for j in range(i)),
                           tuple(valuation3(x[i]+x[j]) for i in range(5) for j in range(i))))
        assert gap(x) == 1 and gcd(*x) == 1 and sum(x) == 0
    assert signatures[0] == signatures[1]
    assert core_distance(3, 121, 279) is None
    assert core_distance(3, 139, 261) == 9
    result = {'comparisons': dict(comparisons), 'invariant_move_branches': dict(branches),
              'max_forced_rounds_in_samples': max_rounds,
              'five_candidate_counterexample_pairs': 2,
              'independent_integer_DAG_states': oracle.cache_info().currsize,
              'scope': 'General proofs are in the note; sample size does not establish universal claims.'}
    target = Path(__file__).with_name('six_triple_block_explicit_verification.json')
    target.write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    if not __debug__:
        raise RuntimeError('Assertions must be enabled.')
    run()
