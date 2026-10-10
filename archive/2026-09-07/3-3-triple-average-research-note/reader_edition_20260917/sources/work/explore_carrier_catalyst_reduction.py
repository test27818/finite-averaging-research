"""Vectorized exact height reduction by the six reversible catalyst roots."""

import argparse
from concurrent.futures import ProcessPoolExecutor
from itertools import product as words
from math import gcd
from os import cpu_count

import numpy as np

from verify_carrier_sweep_catalyst import evaluate, outer_factor
from explore_carrier_sweep_relations import normalized, unipotent_rank_one


def root_lines():
    roots = {}
    for sequence in words(range(6), repeat=4):
        matrix = evaluate(sequence)
        if unipotent_rank_one(matrix):
            roots.setdefault(matrix, sequence)
    result = {}
    for matrix in roots:
        inverse = tuple(tuple(2 * int(i == j) - matrix[i][j]
                              for j in range(3)) for i in range(3))
        if inverse not in roots:
            continue
        u, f = outer_factor(matrix)
        if next(value for value in u if value) < 0:
            u = tuple(-value for value in u)
            f = tuple(-value for value in f)
        result.setdefault(u, f)
    assert len(result) == 6
    return tuple((np.asarray(u, dtype=np.int64),
                  np.asarray(f, dtype=np.int64)) for u, f in result.items())


def height(vectors):
    sums = vectors.sum(axis=1)
    return 10 * (vectors * vectors).sum(axis=1) - 3 * sums * sums


def terminal(vectors):
    return ((vectors == 0).any(axis=1)
            | (vectors[:, 0] == vectors[:, 1])
            | (vectors[:, 0] == vectors[:, 2])
            | (vectors[:, 1] == vectors[:, 2]))


def primitive(vectors):
    return np.gcd.reduce(np.abs(vectors), axis=1) == 1


def reduce_plane(vectors, roots):
    initial = height(vectors)
    best = initial.copy()
    for u, f in roots:
        value = vectors @ f
        bilinear = 10 * (vectors @ u) - 3 * vectors.sum(axis=1) * u.sum()
        denominator = value * (10 * (u @ u) - 3 * u.sum() ** 2)
        active = denominator != 0
        quotient = np.zeros(len(vectors), dtype=np.int64)
        quotient[active] = np.floor_divide(-bilinear[active], denominator[active])
        for shift in (0, 1):
            k = quotient + shift
            output = vectors + (k * value)[:, None] * u[None, :]
            best = np.minimum(best, height(output))
    return best < initial


def reduce_with_sweeps(vectors, roots):
    initial = height(vectors)
    best = initial.copy()
    sweeps = tuple(np.asarray(normalized(3, order), dtype=np.int64)
                   for order in __import__("itertools").permutations(range(3)))
    for sweep in sweeps:
        swept = vectors @ sweep.T
        best = np.minimum(best, height(swept))
        # Sweep first, then take the optimal power in each root subgroup.
        best = np.minimum(best, best_after_roots(swept, roots))
        # Root first, then sweep.  The quadratic form is evaluated on Vd+k*a*Vu.
        for u, f in roots:
            value = vectors @ f
            swept_u = sweep @ u
            bilinear = (10 * (swept @ swept_u)
                        - 3 * swept.sum(axis=1) * swept_u.sum())
            denominator = value * (
                10 * (swept_u @ swept_u) - 3 * swept_u.sum() ** 2
            )
            active = denominator != 0
            quotient = np.zeros(len(vectors), dtype=np.int64)
            quotient[active] = np.floor_divide(
                -bilinear[active], denominator[active]
            )
            for shift in (0, 1):
                k = quotient + shift
                output = swept + (k * value)[:, None] * swept_u[None, :]
                best = np.minimum(best, height(output))
    return best < initial


def reduce_with_matrices(vectors, roots, matrices):
    initial = height(vectors)
    best = initial.copy()
    for matrix in matrices:
        output = vectors @ matrix.T
        best = np.minimum(best, height(output))
        best = np.minimum(best, best_after_roots(output, roots))
        for u, f in roots:
            value = vectors @ f
            output_u = matrix @ u
            bilinear = (10 * (output @ output_u)
                        - 3 * output.sum(axis=1) * output_u.sum())
            denominator = value * (
                10 * (output_u @ output_u) - 3 * output_u.sum() ** 2
            )
            active = denominator != 0
            quotient = np.zeros(len(vectors), dtype=np.int64)
            quotient[active] = np.floor_divide(
                -bilinear[active], denominator[active]
            )
            for shift in (0, 1):
                k = quotient + shift
                candidate = output + (k * value)[:, None] * output_u[None, :]
                best = np.minimum(best, height(candidate))
    return best < initial


def best_after_roots(vectors, roots):
    best = height(vectors)
    for u, f in roots:
        value = vectors @ f
        bilinear = 10 * (vectors @ u) - 3 * vectors.sum(axis=1) * u.sum()
        denominator = value * (10 * (u @ u) - 3 * u.sum() ** 2)
        active = denominator != 0
        quotient = np.zeros(len(vectors), dtype=np.int64)
        quotient[active] = np.floor_divide(-bilinear[active], denominator[active])
        for shift in (0, 1):
            k = quotient + shift
            output = vectors + (k * value)[:, None] * u[None, :]
            best = np.minimum(best, height(output))
    return best


def inspect_chunk(task):
    first_values, bound = task
    roots = root_lines()
    values = np.arange(-bound, bound + 1, dtype=np.int64)
    primitive_count = minimal_count = nonterminal_count = 0
    stage_one_left = stage_two_left = 0
    examples = []
    stage_examples = []
    sweeps = tuple(np.asarray(normalized(3, order), dtype=np.int64)
                   for order in __import__("itertools").permutations(range(3)))
    double_sweeps = tuple(left @ right for left in sweeps for right in sweeps)
    for first in first_values:
        second, third = np.meshgrid(values, values, indexing="ij")
        vectors = np.column_stack((
            np.full(second.size, first, dtype=np.int64),
            second.ravel(), third.ravel(),
        ))
        mask = primitive(vectors)
        vectors = vectors[mask]
        primitive_count += len(vectors)
        reducible = reduce_plane(vectors, roots)
        minimal = vectors[~reducible]
        minimal_count += len(minimal)
        nonterminal = minimal[~terminal(minimal)]
        nonterminal_count += len(nonterminal)
        for vector in nonterminal[:max(0, 30 - len(examples))]:
            examples.append(tuple(map(int, vector)))
        stage = nonterminal
        covered = reduce_with_matrices(stage, roots, sweeps)
        stage = stage[~covered]
        stage_one_left += len(stage)
        for vector in stage[:max(0, 30 - len(stage_examples))]:
            stage_examples.append(tuple(map(int, vector)))
        covered = reduce_with_matrices(stage, roots, double_sweeps)
        stage = stage[~covered]
        stage_two_left += len(stage)
    return (primitive_count, minimal_count, nonterminal_count,
            stage_one_left, stage_two_left, examples, stage_examples)


def inspect(bound, jobs):
    values = list(range(-bound, bound + 1))
    jobs = max(1, min(jobs, len(values)))
    chunks = [tuple(values[index::jobs]) for index in range(jobs)]
    with ProcessPoolExecutor(max_workers=jobs) as pool:
        results = list(pool.map(inspect_chunk,
                                ((chunk, bound) for chunk in chunks)))
    primitive_count = sum(row[0] for row in results)
    minimal_count = sum(row[1] for row in results)
    nonterminal_count = sum(row[2] for row in results)
    stage_one_left = sum(row[3] for row in results)
    stage_two_left = sum(row[4] for row in results)
    examples = [value for row in results for value in row[5]][:30]
    stage_examples = [value for row in results for value in row[6]][:30]
    print("box", bound, "primitive", primitive_count,
          "root-minimal", minimal_count,
          "nonterminal-minimal", nonterminal_count)
    print("examples", examples)
    print("staged root/one-sweep left", stage_one_left,
          "after two-sweep", stage_two_left)
    print("stage-one examples", stage_examples)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--bound", type=int, default=100)
    parser.add_argument("--jobs", type=int, default=cpu_count() or 1)
    args = parser.parse_args()
    inspect(args.bound, args.jobs)
