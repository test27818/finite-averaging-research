"""Finite checks for the isolated non-3 prime safe-core reduction."""

from collections import Counter
from fractions import Fraction
from itertools import combinations, combinations_with_replacement
from math import gcd
from random import Random


def difference_gcd(values):
    return gcd(*(abs(value - values[0]) for value in values[1:]))


def is_three_power(value):
    if value == 0:
        return True
    while value % 3 == 0:
        value //= 3
    return value == 1


def isolated_prime(n):
    value = n
    while value % 3 == 0:
        value //= 3
    if value == 1:
        return None
    p = None
    d = 2
    while d * d <= value:
        if value % d == 0:
            if p is not None or d == 3:
                return None
            p = d
            while value % d == 0:
                value //= d
        d += 1
    if value > 1:
        if p is not None and value != p:
            return None
        p = value
    return p


def safe_triples(values, p):
    n = len(values)
    result = []
    for selected in combinations(range(n), 3):
        if sum(values[index] for index in selected) % 3:
            continue
        if len({values[index] for index in selected}) == 1:
            continue
        remainder = [
            values[index] % p
            for index in range(n)
            if index not in selected
        ]
        if len(set(remainder)) >= 2:
            result.append(selected)
    return result


def bridge_candidates(values):
    n = len(values)
    counts = Counter(values)
    repeated = next(
        (value for value, count in counts.items() if count >= n - 4),
        None,
    )
    if repeated is None:
        return []
    keep = list(values)
    for _ in range(n - 4):
        keep.remove(repeated)
    return list(combinations(range(4), 3)), repeated, tuple(keep)


def verify_exhaustive():
    checked = 0
    terminal = 0
    for n in (7, 8, 9, 10, 11, 13):
        p = isolated_prime(n)
        if p is None:
            continue
        for values in combinations_with_replacement(range(-3, 4), n):
            if sum(values) or not any(values):
                continue
            if not is_three_power(difference_gcd(values)):
                continue
            checked += 1
            if not safe_triples(values, p):
                terminal += 1
                assert max(Counter(values).values()) >= n - 4
    return checked, terminal


def verify_random():
    random = Random(20260908)
    checked = 0
    terminal = 0
    for n in (7, 8, 11, 13, 16, 17, 19, 25, 27):
        p = isolated_prime(n)
        if p is None:
            continue
        for _ in range(1000):
            values = [random.randrange(-10**5, 10**5) for _ in range(n - 1)]
            values.append(-sum(values))
            divisor = gcd(*(abs(value) for value in values))
            if divisor:
                values = [value // divisor for value in values]
            if not is_three_power(difference_gcd(values)):
                continue
            checked += 1
            if not safe_triples(values, p):
                terminal += 1
                assert max(Counter(values).values()) >= n - 4
    return checked, terminal


def verify_bridge():
    # Check that a residual triple can avoid the p residue of the repeated value.
    random = Random(931)
    checked = 0
    for n, p in ((7, 7), (11, 11), (13, 13), (16, 2), (25, 5)):
        for _ in range(500):
            u = random.randrange(-100, 101)
            residual = [random.randrange(-100, 101) for _ in range(4)]
            values = [u] * (n - 4) + residual
            if difference_gcd(values) % p == 0:
                continue
            good = []
            for selected in combinations(range(4), 3):
                total = sum(residual[index] for index in selected)
                if total % 3 == 0:
                    # Integrality is optional for the bridge, but check the
                    # stronger p-safe choice whenever it is available.
                    if Fraction(total, 3) % p != u % p:
                        good.append(selected)
            if not good:
                # The theorem only needs a rational average; use the
                # congruence argument directly.
                assert any(
                    sum(residual[index] for index in selected) % p
                    != (3 * u) % p
                    for selected in combinations(range(4), 3)
                )
            checked += 1
    return checked


if __name__ == "__main__":
    exhaustive, terminal = verify_exhaustive()
    random_checked, random_terminal = verify_random()
    bridge = verify_bridge()
    print("isolated-prime safe-core checks: PASS")
    print("exhaustive legal states", exhaustive, "terminal", terminal)
    print("random legal states", random_checked, "terminal", random_terminal)
    print("bridge samples", bridge)
