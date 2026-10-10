"""Search for projective positive inverses in the star-kernel macro monoid."""

from collections import deque
from fractions import Fraction as F
from itertools import permutations
from math import gcd

from explore_star_kernel_group import generator, identity, multiply


def primitive_matrix(matrix):
    denominator = 1
    for row in matrix:
        for value in row:
            denominator = denominator * value.denominator // gcd(denominator,
                                                                   value.denominator)
    entries = [int(value * denominator) for row in matrix for value in row]
    content = gcd(*(abs(value) for value in entries))
    entries = [value // content for value in entries]
    first = next((value for value in entries if value), 1)
    if first < 0:
        entries = [-value for value in entries]
    size = len(matrix)
    return tuple(tuple(entries[index * size:(index + 1) * size])
                 for index in range(size))


def inverse(matrix):
    size = len(matrix)
    augmented = [list(row) + list(unit) for row, unit in zip(matrix, identity(size))]
    for column in range(size):
        pivot = next(row for row in range(column, size)
                     if augmented[row][column])
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [value / scale for value in augmented[column]]
        for row in range(size):
            if row == column:
                continue
            scale = augmented[row][column]
            augmented[row] = [left - scale * right for left, right
                              in zip(augmented[row], augmented[column])]
    return [row[size:] for row in augmented]


def permutation_matrix(permutation):
    size = len(permutation)
    return [[F(column == permutation[row]) for column in range(size)]
            for row in range(size)]


def search(size, r, depth):
    transformations = [generator(size, r, selected) for selected in range(size)]
    inverse_target = inverse(transformations[0])
    targets = {primitive_matrix(multiply(permutation_matrix(permutation),
                                         inverse_target))
               for permutation in permutations(range(size))}
    start = identity(size)
    seen = {primitive_matrix(start): ""}
    frontier = [(start, "")]
    for level in range(1, depth + 1):
        following = []
        for matrix, word in frontier:
            for selected, transformation in enumerate(transformations):
                result = multiply(transformation, matrix)
                key = primitive_matrix(result)
                if key in targets:
                    print("FOUND size", size, "r", r, "depth", level,
                          "word", word + str(selected), flush=True)
                    return word + str(selected)
                if key not in seen:
                    new_word = word + str(selected)
                    seen[key] = new_word
                    following.append((result, new_word))
        frontier = following
        print("size", size, "r", r, "depth", level, "states", len(seen),
              flush=True)
    print("NOT FOUND size", size, "r", r, "depth", depth, flush=True)
    return None


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--size", type=int, action="append")
    parser.add_argument("--r", type=int, default=3)
    parser.add_argument("--depth", type=int, default=8)
    arguments = parser.parse_args()
    for size in arguments.size or range(2, 8):
        search(size, arguments.r, arguments.depth)
