"""Exact checks supporting the written all-M modular obstruction proofs."""
from fractions import Fraction
from itertools import combinations
from math import gcd
from pathlib import Path
import json


def G(x):
    content = gcd(*x)
    assert content
    return gcd(*((a-x[0])//content for a in x))


def atom(x, positions):
    assert len(positions) == len(set(positions))
    y = list(x)
    mean = sum((Fraction(x[i]) for i in positions), Fraction())/len(positions)
    for i in positions:
        y[i] = mean
    return tuple(y)


def families():
    cases = 0
    output_types = 0
    for p in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
        for M in (1, 2, 3, 5, 6, 9, 25, 81, 1000, 3**30):
            a = p*(p+2)*M
            x = (a,)*p+(1, -p*a-1)
            x0 = (0,)*p+(1, -1)
            assert sum(x) == 0 and gcd(*x) == G(x) == G(x0) == 1
            assert all((b-c) % M == 0 for b, c in zip(x, x0))
            for b in (0, 1):
                for c in (0, 1):
                    selected_sum = (p-b-c)*a+b+c*(-p*a-1)
                    if b+c == 0:
                        assert selected_sum == p*a
                    elif b+c == 1:
                        assert selected_sum % p != 0
                    else:
                        assert selected_sum == -2*a
                        assert G((-2,)*p+(p, p)) == p+2
                    output_types += 1
            a = 2*p*M
            y = (a,)*p+(1,)*(p-1)+(-p*a-(p-1),)
            y0 = (0,)*p+(1,)*(p-1)+(-(p-1),)
            assert sum(y) == 0 and gcd(*y) == G(y) == G(y0) == 1
            assert all((b-c) % M == 0 for b, c in zip(y, y0))
            for ones in range(p):
                for exceptional in (0, 1):
                    count = ones+exceptional
                    selected_sum = (p-count)*a+ones+exceptional*y[-1]
                    assert (selected_sum % p == 0) == (count in (0, p))
                    if count == p:
                        assert selected_sum == -p*a
                    output_types += 1
            assert G((1,)*p+(-1,)*p) == 2
            cases += 2
    return {'family_instances': cases, 'all_choice_types': output_types}


def examples():
    x = (-2, -2, -2, 7, -1)
    for selected in ((0, 1, 3), (0, 1, 2), (0, 3, 4)):
        x = atom(x, selected)
    assert not any(x)
    z = (-3, -3, 0, 1, 2, 3)
    assert G(z) == 1
    good = atom(atom(z, (0, 3, 4)), (1, 2, 5))
    assert not any(good)
    bad = atom(z, (3, 4, 5))
    assert bad == (-3, -3, 0, 2, 2, 2)
    bad = tuple(int(a) for a in bad)
    assert G(bad) == 1
    integer_moves = []
    for selected in combinations(range(6), 3):
        if sum(bad[i] for i in selected) % 3 or len({bad[i] for i in selected}) == 1:
            continue
        integer_moves.append(selected)
        result = tuple(int(a) for a in atom(bad, selected))
        assert sorted(result) == [-2, -2, -2, 2, 2, 2]
        assert G(result) == 2
    assert integer_moves == [(0, 1, 2)]
    return {'literal_atoms': 7, 'bad_successor_all_triples_checked': 20}


if __name__ == '__main__':
    if not __debug__:
        raise RuntimeError('Assertions must be enabled.')
    result = {'families': families(), 'examples': examples(),
              'scope': 'Written proofs cover all odd primes and all positive moduli; finite checks only guard formulas.'}
    target = Path(__file__).with_name('five_six_modular_limits_verification.json')
    target.write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps(result, indent=2))
