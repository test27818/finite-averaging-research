"""Exact bounded test of two-carrier local contraction synchronization.

Each letter contracts the three leaf blocks and one selected carrier by
3^(-8), modelling a positive root followed by its positive inverse.  The
test starts on the equal-carrier subspace and asks whether a nonempty word
returns that subspace to itself for every leaf input.
"""

from argparse import ArgumentParser
from fractions import Fraction as F
from itertools import product


def identity(size):
    return tuple(tuple(F(row == column) for column in range(size))
                 for row in range(size))


def multiply(left, right):
    return tuple(tuple(sum(left[row][index] * right[index][column]
                           for index in range(len(right)))
                       for column in range(len(right[0])))
                 for row in range(len(left)))


def contraction(carrier):
    weights = (3, 3, 3, 1, 1)
    scale = F(1, 3 ** 8)
    selected = (0, 1, 2, carrier)
    matrix = [list(row) for row in identity(5)]
    for row in selected:
        for column in range(5):
            matrix[row][column] = (
                scale * int(row == column)
                + (1 - scale) * F(weights[column], 10)
                if column in selected else F(0))
    return tuple(tuple(row) for row in matrix)


def equal_carrier_basis():
    # u_1,u_2,u_3 are free; w=z=-3/2 sum(u_i).
    return ((F(1), F(0), F(0)),
            (F(0), F(1), F(0)),
            (F(0), F(0), F(1)),
            (F(-3, 2), F(-3, 2), F(-3, 2)),
            (F(-3, 2), F(-3, 2), F(-3, 2)))


def apply(matrix, basis):
    return tuple(tuple(sum(matrix[row][index] * basis[index][column]
                          for index in range(5))
                      for column in range(3))
                 for row in range(5))


def inspect(depth):
    basis = equal_carrier_basis()
    letters = (contraction(3), contraction(4))
    frontier = {identity(5): ""}
    for level in range(1, depth + 1):
        following = {}
        for matrix, word in frontier.items():
            for index, letter in enumerate(letters):
                output = multiply(letter, matrix)
                transformed = apply(output, basis)
                if all(transformed[3][column] == transformed[4][column]
                       for column in range(3)):
                    print("equal-carrier contraction return: PASS", level,
                          word + str(index), flush=True)
                    return
                following[output] = word + str(index)
        frontier = following
        print("level", level, "frontier", len(frontier), flush=True)
    print("equal-carrier contraction synchronization: OPEN", depth,
          "no nonempty return", flush=True)


def main():
    parser = ArgumentParser()
    parser.add_argument("--depth", type=int, default=12)
    args = parser.parse_args()
    inspect(args.depth)


if __name__ == "__main__":
    main()
