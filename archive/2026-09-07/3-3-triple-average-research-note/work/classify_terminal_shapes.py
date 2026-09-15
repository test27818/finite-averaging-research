"""Inspect exact no-safe-operation states and classify sparse terminals."""

from collections import Counter
from itertools import combinations_with_replacement
from math import gcd


def power3(value):
    if value == 0:
        return False
    while value % 3 == 0:
        value //= 3
    return value == 1


def difference_gcd(values):
    return gcd(*(abs(value - values[0]) for value in values[1:]))


def prime_divisors(value):
    out = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            if divisor != 3:
                out.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1 and value != 3:
        out.append(value)
    return out


def safe(values):
    n = len(values)
    primes = prime_divisors(n)
    counts = Counter(values)
    for a in counts:
        for b in counts:
            for c in counts:
                selected = (a, b, c)
                if sum(selected) % 3 or len(set(selected)) == 1:
                    continue
                need = Counter(selected)
                if any(counts[x] < k for x, k in need.items()):
                    continue
                remainder = list(values)
                for value in selected:
                    remainder.remove(value)
                if all(len({value % p for value in remainder}) >= 2
                       for p in primes):
                    return True
    return False


def qmax(n):
    q = 1
    while 3 * q <= n:
        q *= 3
    return q


def sparse_finish(values):
    mean = sum(values) // len(values)
    if sum(values) % len(values):
        return False
    support = [value - mean for value in values if value != mean]
    # The general zero-padding theorem applies if the support fits into qmax.
    return len(support) <= qmax(len(values))


def classify(n, bound):
    counts = Counter()
    total = 0
    for values in combinations_with_replacement(range(-bound, bound + 1), n):
        if sum(values) or not any(values):
            continue
        if not power3(difference_gcd(values)):
            continue
        if safe(values):
            continue
        total += 1
        multiplicity = max(Counter(values).values())
        shape = (multiplicity, len(set(values)),
                 tuple(sorted(Counter(values).values(), reverse=True)))
        counts[shape] += 1
        if total <= 3:
            print("n", n, "terminal", values, "sparse-finish", sparse_finish(values))
    print("n", n, "terminals", total, "shapes", counts.most_common(15))


if __name__ == "__main__":
    for n in (12, 14, 15, 16, 18):
        classify(n, 3)
