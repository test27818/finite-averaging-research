"""Vectorized finite images of the positively invertible sweep roots."""

from itertools import product as words

import numpy as np

from verify_carrier_sweep_catalyst import evaluate
from explore_carrier_sweep_relations import unipotent_rank_one


def generators():
    roots = {}
    for sequence in words(range(6), repeat=4):
        matrix = evaluate(sequence)
        if unipotent_rank_one(matrix):
            roots.setdefault(matrix, sequence)
    result = []
    for matrix in roots:
        inverse = tuple(tuple(2 * int(i == j) - matrix[i][j]
                              for j in range(3)) for i in range(3))
        if inverse in roots:
            result.append(matrix)
    assert len(result) == 12
    return np.asarray(result, dtype=np.int64)


def codes(matrices, modulus):
    flat = matrices.reshape((-1, 9)).astype(np.int64, copy=False)
    powers = (modulus ** np.arange(9, dtype=np.int64))
    return flat @ powers


def decode(values, modulus):
    values = values.astype(np.int64, copy=True)
    output = np.empty((len(values), 9), dtype=np.int64)
    for index in range(9):
        output[:, index] = values % modulus
        values //= modulus
    return output.reshape((-1, 3, 3))


def closure(modulus):
    gens = generators() % modulus
    identity = np.eye(3, dtype=np.int64)[None, :, :]
    identity_code = int(codes(identity, modulus)[0])
    seen = np.zeros(modulus ** 9, dtype=np.bool_)
    seen[identity_code] = True
    frontier = np.asarray([identity_code], dtype=np.int64)
    rounds = 0
    while len(frontier):
        matrices = decode(frontier, modulus)
        candidates = np.matmul(gens[:, None, :, :],
                               matrices[None, :, :, :]) % modulus
        candidate_codes = np.unique(codes(candidates.reshape((-1, 3, 3)),
                                          modulus))
        following = candidate_codes[~seen[candidate_codes]]
        seen[following] = True
        frontier = following
        rounds += 1
    return int(seen.sum()), rounds


if __name__ == "__main__":
    for modulus in (2, 3, 4, 5):
        size, rounds = closure(modulus)
        print("modulus", modulus, "image", size, "rounds", rounds)
