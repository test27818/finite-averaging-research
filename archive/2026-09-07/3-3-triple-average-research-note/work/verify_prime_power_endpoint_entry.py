"""Prime-power endpoint entry and literal critical-boundary controls.

Universal arguments are in prime_arity_critical_frontier_handoff.md. These
finite checks verify position accounting and formulas, not endpoint consensus.
The entry lemma also works for odd composite averaging arity.
"""

from collections import Counter
from fractions import Fraction as F
from math import gcd, lcm
from random import Random

if not __debug__:
    raise RuntimeError('Assertions are required.')


def primitive(values):
    common = gcd(*values)
    return tuple(x // common for x in values) if common else tuple(values)


def centered_g(values):
    mean = sum(map(F, values), F(0)) / len(values)
    centered = [F(x) - mean for x in values]
    denominator = lcm(*(x.denominator for x in centered))
    integers = primitive(tuple(int(x * denominator) for x in centered))
    return gcd(*(x - integers[0] for x in integers))


def average(values, indices, p):
    assert len(indices) == len(set(indices)) == p
    assert all(0 <= i < len(values) for i in indices)
    result = list(map(F, values))
    mean = sum((result[i] for i in indices), F(0)) / p
    for i in indices:
        result[i] = mean
    assert sum(result) == sum(values)
    return tuple(result)


def prime_power_entry(values, p, ell, exponent, singleton=0):
    """Choose disjoint p-blocks; a swap changes membership, not the values."""
    n = 2 * p + 1
    assert p >= 3 and p % 2 and n == ell ** exponent
    assert ell >= 3 and all(ell % d for d in range(2, int(ell**0.5) + 1))
    assert len(values) == n and sum(values) == 0 and centered_g(values) == 1
    assert 0 <= singleton < n
    rest = [i for i in range(n) if i != singleton]
    first, second = rest[:p], rest[p:]
    difference = sum(values[i] for i in first) - sum(values[i] for i in second)
    repaired = difference % ell == 0
    if repaired:
        i, j = next((i, j) for i in first for j in second
                    if (values[i] - values[j]) % ell)
        first[first.index(i)], second[second.index(j)] = j, i
    assert not set(first).intersection(second)
    assert singleton not in first + second
    state = average(values, first, p)
    state = average(state, second, p)
    a, b = state[first[0]], state[second[0]]
    assert state[singleton] == -p * (a + b)
    assert all(state[i] == a for i in first)
    assert all(state[i] == b for i in second)
    assert centered_g(state) == 1
    assert all(p % x.denominator == 0 for x in state)
    return state, (tuple(first), tuple(second)), repaired


def selected_by_values(state, requested):
    available = {}
    for i, x in enumerate(state):
        available.setdefault(x, []).append(i)
    indices = []
    for value, count in requested:
        assert len(available.get(value, ())) >= count
        indices.extend(available[value][:count])
        del available[value][:count]
    return tuple(indices)


def run_word(values, p, groups):
    state = tuple(map(F, values))
    for group in groups:
        indices = selected_by_values(state, group)
        state = average(state, indices, p)
    assert not any(state)


def verify_boundary_controls():
    checked = 0
    for p in (3, 5, 7, 13, 23, 47):
        initial = (-p,) + (0,) * (p - 1) + (1,) * p
        assert sum(initial) == 0 and centered_g(initial) == 1
        integer_types = []
        for carrier in (0, 1):
            for ones in range(p + 1):
                zeros = p - carrier - ones
                if not 0 <= zeros <= p - 1:
                    continue
                move = (-p,) * carrier + (1,) * ones + (0,) * zeros
                if len(set(move)) > 1 and sum(move) % p == 0:
                    integer_types.append((carrier, ones, zeros))
        assert integer_types == [(1, 0, p - 1)]
        after = average(initial, tuple(range(p)), p)
        assert Counter(after) == Counter({F(-1): p, F(1): p})
        assert all(x.numerator % 2 == 1 and x.denominator == 1 for x in after)

        h = (p - 1) // 2
        tail = [((-1, h), (1, h), (0, 1)),
                ((-1, h), (1, h), (0, 1)),
                ((-1, 1), (1, 1), (0, p - 2))]
        run_word(initial + (0,), p, [((-p, 1), (0, p - 1))] + tail)

        y = (1,) * p + (2,) * p + (-3 * p,)
        assert centered_g(y) == 1
        # Without the carrier, an integer average is an identity.
        assert all((i + 2 * (p - i)) % p for i in range(1, p))
        possible = [i for i in range(p) if (-3 * p + i + 2 * (p - 1 - i)) % p == 0]
        assert possible == [p - 2]
        first = ((1, p - 2), (2, 1), (-3 * p, 1))
        after = average(y, selected_by_values(y, first), p)
        assert sum(count >= p for count in Counter(after).values()) == 1
        assert centered_g(after) == 1 and all(after)
        run_word(y, p, [first, ((-2, h), (1, 2), (2, h - 1)),
                        ((-2, h), (2, h), (0, 1)),
                        ((-2, 1), (2, 1), (0, p - 2))])
        checked += 1
    print('critical boundary unique integer move and four-step controls: PASS', checked)


def verify_n27_labels():
    checked = repaired = 0
    for zero in range(28):
        for one in range(28 - zero):
            two = 27 - zero - one
            if (one + 2 * two) % 3 or max(zero, one, two) == 27:
                continue
            values = [0] * zero + [1] * one + [2] * two
            values[-1] -= sum(values)
            values = primitive(values)
            assert centered_g(values) == 1
            for singleton in range(27):
                _, _, changed = prime_power_entry(values, 13, 3, 3, singleton)
                repaired += changed
                checked += 1
    assert checked == 133 * 27
    print('n27 mod3 multiplicities and every singleton exact entry: PASS', checked)
    assert repaired > 0


def verify_lifts():
    rng = Random(2026091209)
    cases = ((3, 7, 1), (5, 11, 1), (11, 23, 1), (13, 3, 3),
             (23, 47, 1), (171, 7, 3), (1093, 3, 7))
    checked = 0
    for p, ell, exponent in cases:
        for _ in range(8):
            while True:
                raw = [rng.randrange(-(1 << 96), 1 << 96) for _ in range(2 * p)]
                raw.append(-sum(raw))
                values = primitive(raw)
                if centered_g(values) == 1:
                    break
            prime_power_entry(values, p, ell, exponent, rng.randrange(2 * p + 1))
            checked += 1
    print('prime-power entry large-integer labelled replays: PASS', checked)


if __name__ == '__main__':
    verify_boundary_controls()
    verify_n27_labels()
    verify_lifts()
    print('prime-power endpoint entry and critical-boundary checks: PASS')
