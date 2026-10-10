"""Projective positive inverse search for the three carrier exchanges."""

import argparse
from math import gcd

from explore_carrier_sweep_relations import cleared_carrier


def multiply(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3))
                       for j in range(3)) for i in range(3))


def primitive(matrix):
    divisor = gcd(*(abs(value) for row in matrix for value in row))
    matrix = tuple(tuple(value // divisor for value in row) for row in matrix)
    first = next(value for row in matrix for value in row if value)
    if first < 0:
        matrix = tuple(tuple(-value for value in row) for row in matrix)
    return matrix


def inverse_primitive(matrix):
    a, b, c = matrix
    adjugate = (
        (b[1] * c[2] - b[2] * c[1],
         a[2] * c[1] - a[1] * c[2],
         a[1] * b[2] - a[2] * b[1]),
        (b[2] * c[0] - b[0] * c[2],
         a[0] * c[2] - a[2] * c[0],
         a[2] * b[0] - a[0] * b[2]),
        (b[0] * c[1] - b[1] * c[0],
         a[1] * c[0] - a[0] * c[1],
         a[0] * b[1] - a[1] * b[0]),
    )
    return primitive(adjugate)


def search(depth):
    generators = tuple(primitive(cleared_carrier(3, index))
                       for index in range(3))
    targets = {inverse_primitive(matrix): index
               for index, matrix in enumerate(generators)}
    identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    seen = {identity: ""}
    frontier = {identity: ""}
    found = {}
    for level in range(1, depth + 1):
        following = {}
        for matrix, word in frontier.items():
            for index, generator in enumerate(generators):
                output = primitive(multiply(generator, matrix))
                if output in seen or output in following:
                    continue
                certificate = word + str(index)
                if output in targets:
                    found[targets[output]] = certificate
                following[output] = certificate
        seen.update(following)
        frontier = following
        print("level", level, "frontier", len(frontier),
              "total", len(seen), "inverse targets", found, flush=True)
        if len(found) == 3:
            break
    print("positive projective carrier inverses", found)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--depth", type=int, default=14)
    args = parser.parse_args()
    search(args.depth)
