"""Historical candidate conditional B15 returns; not a theorem certificate.

Superseded by verify_fifteen_via_subblocks.py and the complete B15 proof.
The handwritten candidate list and its local domains are exploratory only.
"""

from fractions import Fraction as F
from math import gcd
from collections import Counter
from itertools import combinations_with_replacement

from explore_single_prime_kernels import kernel_state, terminal_partition


def primitive(pair):
    x, y = pair
    divisor = gcd(x, y)
    if not divisor:
        return 0, 0
    x, y = x//divisor, y//divisor
    return (-x, -y) if x < 0 or (x == 0 and y < 0) else (x, y)


def height(pair):
    u, v = pair
    return 22*u*u+11*u*v+2*v*v


# Name, integer projective matrix, input linear congruence and modulus.
RETURNS = (
    ("A", (3, 0, -11, -1), (0, 0, 1)),
    ("T21u", (-6, -3, 10, 11), (2, 1, 4)),
    ("T21v", (-6, -3, 22, -1), (2, 1, 4)),
    ("T12u", (-3, -6, -1, 22), (1, 2, 4)),
    ("T12v", (-3, -6, 11, 10), (1, 2, 4)),
    ("Eu", (-15, -12, 19, 44), (1, 0, 4)),
    ("Ev", (-15, -12, 55, 8), (1, 0, 4)),
    ("Eq", (-15, -12, 31, 32), (1, 0, 4)),
    ("L13u", (-3, -3, 11, -2), (1, 1, 13)),
    ("L13v", (-3, -3, -2, 11), (1, 1, 13)),
    ("L11a", (-6, -6, 22, 11), (1, 1, 11)),
    ("L11b", (-6, -6, 11, 22), (1, 1, 11)),
    ("L11c", (-3, -1, 11, 0), (3, 1, 11)),
    ("L11d", (-9, -3, 22, 11), (3, 1, 11)),
)


def edges(pair):
    u, v = pair
    for name, matrix, congruence in RETURNS:
        if (congruence[0]*u+congruence[1]*v) % congruence[2]:
            continue
        a, b, c, d = matrix
        following = primitive((a*u+b*v, c*u+d*v))
        if following != (0, 0) and (following[0]-following[1]) % 5 == 0:
            continue
        yield name, following


def descent(pair, depth):
    initial_height = height(pair)
    frontier = [(pair, ())]
    seen = {pair}
    for _ in range(depth):
        following = []
        for state, path in frontier:
            for name, target in edges(state):
                word = path+(name,)
                if height(target) < initial_height:
                    return target, word
                if target not in seen:
                    seen.add(target)
                    following.append((target, word))
        frontier = following
    return None


def examine(bound, depth):
    bad = []
    counts = Counter()
    for u in range(bound+1):
        for v in range(-bound, bound+1):
            if gcd(u, v) != 1 or (u-v) % 5 == 0:
                continue
            pair = primitive((u, v))
            result = descent(pair, depth)
            if result is None:
                bad.append(pair)
            else:
                counts[len(result[1])] += 1
    bad = sorted(set(bad), key=lambda p: (height(p), p))
    print("B15 conditional macro height descent", dict(sorted(counts.items())),
          "missing", len(bad), "first", bad[:20], flush=True)
    terminals = [pair for pair in bad if terminal_partition(kernel_state(15, pair))]
    remaining = [pair for pair in bad if pair not in terminals]
    print("missing direct terminals",len(terminals),"remaining",len(remaining),
          "first",remaining[:20],flush=True)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--bound", type=int, default=60)
    parser.add_argument("--depth", type=int, default=3)
    args = parser.parse_args()
    examine(args.bound, args.depth)
