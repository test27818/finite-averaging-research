"""Finite checks for the multi-prime dangerous-class core bound."""

from collections import Counter
from itertools import combinations, combinations_with_replacement
from math import gcd


def prime_divisors(n):
    result = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            if d != 3:
                result.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1 and n != 3:
        result.append(n)
    return result


def power_three(value):
    if not value:
        return False
    while value % 3 == 0:
        value //= 3
    return value == 1


def dangerous(values, primes):
    n = len(values)
    result = []
    for p in primes:
        if max(Counter(value % p for value in values).values()) >= n - 3:
            result.append(p)
    return result


def has_safe(values, primes):
    n = len(values)
    for selected in combinations(range(n), 3):
        if sum(values[index] for index in selected) % 3:
            continue
        if len({values[index] for index in selected}) == 1:
            continue
        rest = [index for index in range(n) if index not in selected]
        if all(
            len({values[index] % p for index in rest}) >= 2
            for p in primes
        ):
            return True
    return False


def verify():
    checked = 0
    terminal = 0
    for n in range(7, 31):
        primes = prime_divisors(n)
        if not primes:
            continue
        for values in combinations_with_replacement(range(-3, 4), n):
            if sum(values) or not any(values):
                continue
            g = gcd(*(abs(value - values[0]) for value in values[1:]))
            if not power_three(g):
                continue
            checked += 1
            if has_safe(values, primes):
                continue
            terminal += 1
            count = len(dangerous(values, primes))
            assert max(Counter(values).values()) >= n - 3 * count - 1
    return checked, terminal


if __name__ == "__main__":
    checked, terminal = verify()
    print("multi-prime core checks: PASS")
    print("legal states", checked, "terminal states", terminal)
