"""Compute congruence-kernel tangent ranks of the 40-position return group."""

from collections import deque

from explore_weighted_kernel_group import (determinant_integer, explore_fast,
                                            inverse_mod, multiply_mod)


def matrix_mod(matrix, modulus):
    return tuple(tuple(value % modulus for value in row) for row in matrix)


def select_generators(matrices, modulus):
    selected = []
    subgroup = {matrix_mod(((1, 0, 0), (0, 1, 0), (0, 0, 1)), modulus)}
    for matrix in matrices:
        reduced = matrix_mod(matrix, modulus)
        if reduced in subgroup:
            continue
        selected.append(matrix)
        generators = [matrix_mod(value, modulus) for value in selected]
        generators += [inverse_mod(value, modulus) for value in generators]
        subgroup = {matrix_mod(((1, 0, 0), (0, 1, 0), (0, 0, 1)), modulus)}
        queue = deque(subgroup)
        while queue:
            current = queue.popleft()
            for generator in generators:
                following = multiply_mod(generator, current, modulus)
                if following not in subgroup:
                    subgroup.add(following)
                    queue.append(following)
        print("selected", len(selected), "image", len(subgroup), flush=True)
    return selected, subgroup


def flatten_tangent(matrix, modulus, prime):
    result = []
    for row in range(3):
        for column in range(3):
            value = (matrix[row][column] - int(row == column)) % (modulus * prime)
            assert value % modulus == 0
            result.append((value // modulus) % prime)
    return result


def rank(rows, prime):
    basis = {}
    for values in rows:
        row = {index: value % prime for index, value in enumerate(values)
               if value % prime}
        while row:
            pivot = min(row)
            if pivot not in basis:
                inverse = pow(row[pivot], -1, prime)
                basis[pivot] = {index: value * inverse % prime
                                for index, value in row.items()}
                break
            scale = row[pivot]
            for index, value in basis[pivot].items():
                output = (row.get(index, 0) - scale * value) % prime
                if output:
                    row[index] = output
                else:
                    row.pop(index, None)
    return len(basis)


def tangent_rank(matrices, modulus, prime):
    selected, subgroup = select_generators(matrices, modulus)
    generators = []
    for matrix in selected:
        lifted = matrix_mod(matrix, modulus * prime)
        generators.append(lifted)
        generators.append(inverse_mod(lifted, modulus * prime))
    identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    representatives = {matrix_mod(identity, modulus): matrix_mod(identity,
                                                                  modulus * prime)}
    queue = deque(representatives)
    tangent = []
    while queue:
        current = queue.popleft()
        lift = representatives[current]
        for generator in generators:
            output_lift = multiply_mod(generator, lift, modulus * prime)
            output = matrix_mod(output_lift, modulus)
            if output not in representatives:
                representatives[output] = output_lift
                queue.append(output)
            else:
                inverse_rep = inverse_mod(representatives[output], modulus * prime)
                loop = multiply_mod(inverse_rep, output_lift, modulus * prime)
                tangent.append(flatten_tangent(loop, modulus, prime))
    assert len(representatives) == len(subgroup)
    tangent_dimension = rank(tangent, prime)
    print("modulus", modulus, "image", len(subgroup), "tangent loops",
          len(tangent), "rank", tangent_dimension, flush=True)
    return len(subgroup), tangent_dimension


if __name__ == "__main__":
    integral = explore_fast((27, 9, 3, 1), 8)
    positive = [matrix for matrix in integral if determinant_integer(matrix) == 1]
    tangent_rank(positive, 5, 5)
    tangent_rank(positive, 8, 2)
