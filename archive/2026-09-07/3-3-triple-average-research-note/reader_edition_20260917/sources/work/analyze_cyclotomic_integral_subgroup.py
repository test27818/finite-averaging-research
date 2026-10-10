"""Infer congruence data of determinant-one words in the cyclotomic macros."""

from collections import Counter, deque
from explore_cyclotomic_group import determinant, matrices, multiply


def parity2(matrix):
    points = ((1, 0), (0, 1), (1, 1))
    a, b, c, d = matrix
    permutation = [points.index(((a * x + b * y) % 2,
                                 (c * x + d * y) % 2)) for x, y in points]
    return sum(permutation[i] > permutation[j]
               for i in range(3) for j in range(i + 1, 3)) % 2


def explore(s, depth):
    generators = matrices(s)
    identity = (1, 0, 0, 1)
    seen = {identity: ""}
    frontier = [identity]
    integral = {}
    for level in range(depth):
        following = []
        for matrix in frontier:
            for letter, generator in generators.items():
                result = multiply(generator, matrix)
                if result in seen:
                    continue
                seen[result] = seen[matrix] + letter
                following.append(result)
                if determinant(result) == 1:
                    integral[result] = seen[result]
        frontier = following
        print("depth", level + 1, "states", len(seen), "SL2", len(integral), flush=True)
    n = s * s + s + 1
    for modulus in (2, 4, 7, 8, 13, n):
        images = {tuple(value % modulus for value in matrix) for matrix in integral}
        print("mod", modulus, "images", len(images), flush=True)
    characters = Counter()
    failures = []
    for matrix, word in integral.items():
        a, b, c, d = matrix
        row = ((a - c) % n, (b - d) % n)
        if (row[0] + row[1]) % n:
            failures.append((word, matrix, row))
        else:
            characters[row[0]] += 1
    print("row-stabilizer failures", len(failures), "examples", failures[:10])
    print("row multipliers", characters)
    print("parities", Counter(parity2(matrix) for matrix in integral))


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--s", type=int, default=9)
    parser.add_argument("--depth", type=int, default=8)
    args = parser.parse_args()
    explore(args.s, args.depth)
