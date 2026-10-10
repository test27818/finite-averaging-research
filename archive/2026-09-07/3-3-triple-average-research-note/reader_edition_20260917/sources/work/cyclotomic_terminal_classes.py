"""Enumerate zero-sum power-block terminal classes in (s^2,s,1) cores."""

from math import gcd


def powers_below(n):
    result = []
    value = 1
    while value <= n:
        result.append(value)
        value *= 3
    return result


def unit_classes(n):
    multiplier = set()
    value = 1
    while value not in multiplier:
        multiplier.add(value)
        value = value * 3 % n
    multiplier |= {-value % n for value in list(multiplier)}
    classes = {}
    for value in range(1, n):
        if gcd(value, n) != 1:
            continue
        orbit = {value * scale % n for scale in multiplier}
        classes[value] = min(orbit)
    return multiplier, classes


def primitive_pair(a, b):
    divisor = gcd(abs(a), abs(b))
    if divisor == 0:
        return None
    a, b = a // divisor, b // divisor
    if a < 0 or (a == 0 and b < 0):
        a, b = -a, -b
    return a, b


def enumerate_terminals(s):
    r = s * s
    n = r + s + 1
    multiplier, classes = unit_classes(n)
    found = {}
    largest_power = powers_below(n)[-1]
    # After this block is zeroed, all remaining nonzero positions must fit,
    # together with some new zeros, into one further power-of-three block.
    terminal_sizes = [size for size in powers_below(n)
                      if n - size <= largest_power]
    for size in terminal_sizes:
        for singleton in (0, 1):
            for a in range(r + 1):
                b = size - singleton - a
                if not 0 <= b <= s:
                    continue
                # (a-c*r)u+(b-c*s)v=0.
                pair = primitive_pair(b - singleton * s,
                                      singleton * r - a)
                if pair is None:
                    continue
                u, v = pair
                difference = (u - v) % n
                if gcd(difference, n) != 1:
                    continue
                label = classes[difference]
                found.setdefault(label, (size, singleton, a, b, pair))
    all_labels = sorted(set(classes.values()))
    print("s", s, "n", n, "terminal block sizes", terminal_sizes,
          "unit classes", len(all_labels),
          "terminal classes", len(found), flush=True)
    for label in all_labels:
        print(label, found.get(label), flush=True)
    print("missing", sorted(set(all_labels) - set(found)), flush=True)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--s", type=int, action="append")
    arguments = parser.parse_args()
    for s in arguments.s or [3, 9, 27]:
        enumerate_terminals(s)
