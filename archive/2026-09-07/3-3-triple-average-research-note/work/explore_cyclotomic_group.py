"""Explore the projective macro group for n=s^2+s+1, s=3^k."""

from collections import deque
from math import gcd


def primitive(matrix):
    divisor = gcd(*matrix)
    result = tuple(value // divisor for value in matrix)
    if next(value for value in result if value) < 0:
        result = tuple(-value for value in result)
    return result


def multiply(left, right):
    a, b, c, d = left
    e, f, g, h = right
    return primitive((a * e + b * g, a * f + b * h,
                      c * e + d * g, c * f + d * h))


def determinant(matrix):
    a, b, c, d = matrix
    return a * d - b * c


def inverse(matrix):
    a, b, c, d = matrix
    return primitive((d, -b, -c, a))


def matrices(s):
    a = (s, 0, -s * s, -1)
    r = (s - 1, 1, s, 0)
    b = (1, s, 0, -s * s)
    return {"A": a, "R": r, "B": b,
            "a": inverse(a), "r": inverse(r), "b": inverse(b)}


def search(s, depth):
    generators = matrices(s)
    identity = (1, 0, 0, 1)
    seen = {identity: ""}
    frontier = [identity]
    det_one = {}
    for level in range(depth):
        following = []
        for matrix in frontier:
            for letter, generator in generators.items():
                result = multiply(generator, matrix)
                if result in seen:
                    continue
                word = seen[matrix] + letter
                seen[result] = word
                following.append(result)
                if abs(determinant(result)) == 1:
                    det_one[result] = word
        frontier = following
        print("s", s, "depth", level + 1, "seen", len(seen),
              "det-one", len(det_one), flush=True)
    print("det-one sample", list(det_one.items())[:30])
    return det_one


def row_classes(n, multiplier_group):
    rows = []
    for x in range(n):
        for y in range(n):
            if gcd(gcd(x, y), n) != 1:
                continue
            orbit = {(m * x % n, m * y % n) for m in multiplier_group}
            if min(orbit) == (x, y):
                rows.append((x, y))
    return rows


def action_labels(s):
    n = s * s + s + 1
    multipliers = set()
    value = 1
    for _ in range(100):
        multipliers.add(value % n)
        value = value * s % n
        if value == 1:
            break
    multipliers |= {-value % n for value in list(multipliers)}
    print("s", s, "n", n, "multipliers", sorted(multipliers),
          "row classes", len(row_classes(n, multipliers)))


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--s", type=int, default=9)
    parser.add_argument("--depth", type=int, default=6)
    args = parser.parse_args()
    action_labels(args.s)
    search(args.s, args.depth)
