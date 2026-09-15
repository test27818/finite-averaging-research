"""Test safe support-reducing power-of-three block averages."""

from collections import Counter
from itertools import combinations_with_replacement, product
from math import gcd


def primitive(state):
    divisor = gcd(*(abs(value) for value in state))
    if divisor:
        state = tuple(value // divisor for value in state)
    return tuple(sorted(state))


def difference_gcd(state):
    base = state[0]
    return gcd(*(abs(value - base) for value in state[1:]))


def power_of_three(value):
    while value and value % 3 == 0:
        value //= 3
    return value == 1


def selected_signatures(state, size):
    counts = Counter(state)
    values = sorted(counts)

    def generate(index, left, selected):
        if index == len(values):
            if left == 0:
                yield tuple(selected)
            return
        value = values[index]
        for amount in range(min(counts[value], left) + 1):
            selected.append(amount)
            yield from generate(index + 1, left - amount, selected)
            selected.pop()

    for amounts in generate(0, size, []):
        yield tuple(zip(values, amounts))


def average_block(state, signature, size):
    remaining = Counter(state)
    total = 0
    for value, amount in signature:
        remaining[value] -= amount
        total += value * amount
    raw = []
    for value, amount in remaining.items():
        raw.extend([size * value] * amount)
    raw.extend([total] * size)
    return primitive(tuple(raw))


def reductions(state):
    original_support = len(set(state))
    size = 3
    while size < len(state):
        for signature in selected_signatures(state, size):
            following = average_block(state, signature, size)
            if (len(set(following)) < original_support
                    and power_of_three(difference_gcd(following))):
                yield size, signature, following
        size *= 3


def enumerate_states(n, bound):
    # Nondecreasing prefixes avoid permutation duplicates.
    for prefix in combinations_with_replacement(range(-bound, bound + 1), n - 1):
        last = -sum(prefix)
        if last < prefix[-1] or last > bound:
            continue
        state = primitive(prefix + (last,))
        if state != prefix + (last,) or not any(state):
            continue
        if power_of_three(difference_gcd(state)):
            yield state


def exhaustive(n, bound):
    total = reducible = 0
    failures = []
    for state in enumerate_states(n, bound):
        total += 1
        result = next(reductions(state), None)
        if result is None:
            failures.append(state)
        else:
            reducible += 1
    print("n", n, "bound", bound, "legal", total, "reducible", reducible,
          "failures", len(failures))
    for state in failures[:20]:
        print(" FAILURE", Counter(state))
    return failures


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, action="append")
    parser.add_argument("--bound", type=int, default=3)
    arguments = parser.parse_args()
    for n in arguments.n or range(7, 16):
        exhaustive(n, arguments.bound)
