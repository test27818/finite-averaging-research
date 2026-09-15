"""Search positive local-root words returning to the equal-carrier stratum."""

import argparse
from itertools import permutations
from math import gcd

from explore_carrier_sweep_relations import normalized, product


I4 = tuple(tuple(int(i == j) for j in range(4)) for i in range(4))
SWAP = ((1, 0, 0, -1), (0, 1, 0, -1),
        (0, 0, 1, -1), (0, 0, 0, -1))
ORDERS = tuple(permutations(range(3)))


def primitive(matrix):
    divisor = gcd(*(abs(value) for row in matrix for value in row))
    matrix = tuple(tuple(value // divisor for value in row) for row in matrix)
    first = next(value for row in matrix for value in row if value)
    if first < 0:
        matrix = tuple(tuple(-value for value in row) for row in matrix)
    return matrix


def evaluate_sweeps(sequence):
    matrix = I4
    for index in sequence:
        matrix = product(normalized(3, ORDERS[index], True), matrix)
    return primitive(matrix)


def conjugate_swap(matrix):
    return primitive(product(SWAP, product(matrix, SWAP)))


def search(depth):
    root = evaluate_sweeps((0, 3, 5, 2))
    root_inverse = evaluate_sweeps((1, 5, 3, 4))
    generators = (root, root_inverse,
                  conjugate_swap(root), conjugate_swap(root_inverse))
    seen = {I4: ""}
    frontier = {I4: ""}
    hits = []
    for level in range(1, depth + 1):
        following = {}
        for matrix, word in frontier.items():
            for index, generator in enumerate(generators):
                output = primitive(product(generator, matrix))
                if output in seen or output in following:
                    continue
                certificate = word + str(index)
                if output[3][:3] == (0, 0, 0):
                    hits.append((level, certificate, output))
                following[output] = certificate
        seen.update(following)
        frontier = following
        print("level", level, "frontier", len(frontier),
              "total", len(seen), "new returns", len(hits), flush=True)
        if hits:
            for row in hits[:20]:
                print("return", row)
            return
    print("No equal-carrier return in the bounded four-generator semigroup.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--depth", type=int, default=10)
    args = parser.parse_args()
    search(args.depth)
