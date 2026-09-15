"""Compress the sufficient quadratic cones for catalyst height reduction."""

import argparse
from itertools import permutations

import numpy as np

from explore_carrier_catalyst_reduction import (
    height, primitive, reduce_plane, root_lines, terminal,
)
from explore_carrier_sweep_relations import normalized


def root_minimal_vectors(bound):
    roots = root_lines()
    values = np.arange(-bound, bound + 1, dtype=np.int64)
    output = []
    for first in values:
        second, third = np.meshgrid(values, values, indexing="ij")
        vectors = np.column_stack((
            np.full(second.size, first, dtype=np.int64),
            second.ravel(), third.ravel(),
        ))
        vectors = vectors[primitive(vectors)]
        vectors = vectors[~reduce_plane(vectors, roots)]
        output.append(vectors[~terminal(vectors)])
    return np.vstack(output)


def cone_candidates(vectors, matrices, matrix_words, roots):
    initial = height(vectors)
    candidates = []
    labels = []
    for matrix, matrix_word in zip(matrices, matrix_words):
        output = vectors @ matrix.T
        output_height = height(output)
        output_sum = output.sum(axis=1)
        candidates.append(output_height < initial)
        labels.append((matrix_word, "none", -1))
        for index, (u, f) in enumerate(roots):
            q = 10 * (u @ u) - 3 * u.sum() ** 2
            value = output @ f
            bilinear = 10 * (output @ u) - 3 * output_sum * u.sum()
            candidates.append(
                4 * q * output_height - 4 * bilinear * bilinear
                + value * value * q * q < 4 * q * initial
            )
            labels.append((matrix_word, "after", index))

            output_u = matrix @ u
            q = 10 * (output_u @ output_u) - 3 * output_u.sum() ** 2
            value = vectors @ f
            bilinear = (10 * (output @ output_u)
                        - 3 * output_sum * output_u.sum())
            candidates.append(
                4 * q * output_height - 4 * bilinear * bilinear
                + value * value * q * q < 4 * q * initial
            )
            labels.append((matrix_word, "before", index))
    return np.asarray(candidates, dtype=np.bool_), labels


def greedy_cover(coverage, labels):
    uncovered = np.ones(coverage.shape[1], dtype=np.bool_)
    selected = []
    while True:
        gains = np.count_nonzero(coverage[:, uncovered], axis=1)
        index = int(np.argmax(gains))
        gain = int(gains[index])
        if not gain:
            break
        selected.append((labels[index], gain))
        uncovered &= ~coverage[index]
    return selected, uncovered


def inspect(bound):
    vectors = root_minimal_vectors(bound)
    roots = root_lines()
    sweep_words = tuple((index,) for index in range(6))
    sweeps = tuple(np.asarray(normalized(3, order), dtype=np.int64)
                   for order in permutations(range(3)))
    current = vectors
    print("root-minimal nonterminal", len(current))
    for depth in (1, 2, 3):
        if depth == 1:
            matrices, matrix_words = sweeps, sweep_words
        else:
            previous_matrices, previous_words = matrices, matrix_words
            matrices = tuple(left @ right
                             for left in sweeps for right in previous_matrices)
            matrix_words = tuple((index,) + word
                                 for index in range(6) for word in previous_words)
        coverage, labels = cone_candidates(current, matrices, matrix_words, roots)
        selected, uncovered = greedy_cover(coverage, labels)
        print("depth", depth, "candidates", len(labels),
              "selected", len(selected), "left", int(uncovered.sum()))
        print("selected cones", selected)
        current = current[uncovered]
        if not len(current):
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--bound", type=int, default=50)
    args = parser.parse_args()
    inspect(args.bound)
