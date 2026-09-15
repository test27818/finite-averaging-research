"""Exact verification of the Burau structure on geometric power-block chains."""

from fractions import Fraction as F

from explore_weighted_kernel_group import (exchange_matrix, generators,
                                            identity, multiply, primitive)


def scalar_matrix(size, scalar):
    return tuple(tuple(scalar if row == column else F(0)
                       for column in range(size)) for row in range(size))


def full_generator(strands, s, selected):
    result = [list(row) for row in identity(strands)]
    result[selected] = [F(0) for _ in range(strands)]
    result[selected][selected] = F(s - 1, s)
    result[selected][selected + 1] = F(1, s)
    result[selected + 1] = [F(0) for _ in range(strands)]
    result[selected + 1][selected] = F(1)
    return tuple(tuple(row) for row in result)


def inverse(matrix):
    size = len(matrix)
    augmented = [list(row) + list(unit) for row, unit in zip(matrix,
                                                              identity(size))]
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
    return tuple(tuple(row[size:]) for row in augmented)


def matrix_power(matrix, exponent):
    result = identity(len(matrix))
    for _ in range(exponent):
        result = multiply(matrix, result)
    return result


def average(state, indices):
    value = sum((state[index] for index in indices), F(0)) / 3
    for index in indices:
        state[index] = value


def expand(state, seed, available, target_size):
    block = [seed]
    while len(block) < target_size:
        following = []
        for position in block:
            pair = available[-2:]
            del available[-2:]
            average(state, [position] + pair)
            following.extend((position, pair[0], pair[1]))
        block = following
    return block


def verify_real_macro(strands, s, common):
    weights = [common * s ** (strands - 1 - index)
               for index in range(strands)]
    values = [F(2 * index - 5) for index in range(strands)]
    state = []
    blocks = []
    for weight, value in zip(weights, values):
        block = list(range(len(state), len(state) + weight))
        blocks.append(block)
        state.extend([value] * weight)
    for selected in range(strands - 1):
        large = blocks[selected]
        small = blocks[selected + 1]
        old_large = state[large[0]]
        old_small = state[small[0]]
        retained = large[:len(small)]
        available = large[len(small):]
        outputs = []
        for seed in small:
            outputs.extend(expand(state, seed, available, s))
        assert not available
        target = F(s - 1, s) * old_large + F(1, s) * old_small
        assert all(state[position] == target for position in outputs)
        assert all(state[position] == old_large for position in retained)
        assert len(outputs) == len(large) and len(retained) == len(small)


def verify(strands, s):
    full = [full_generator(strands, s, index)
            for index in range(strands - 1)]
    reduced_weights = tuple(s ** (strands - 1 - index)
                            for index in range(strands))
    reduced = [exchange_matrix(reduced_weights, index, index + 1)
               for index in range(strands - 1)]

    for index in range(strands - 2):
        left = multiply(full[index], multiply(full[index + 1], full[index]))
        right = multiply(full[index + 1], multiply(full[index], full[index + 1]))
        assert left == right
    for left in range(strands - 1):
        for right in range(left + 2, strands - 1):
            assert multiply(full[left], full[right]) == multiply(full[right],
                                                                         full[left])

    coxeter = identity(strands - 1)
    for matrix in reduced:
        coxeter = multiply(matrix, coxeter)
    assert matrix_power(coxeter, strands) == scalar_matrix(strands - 1,
                                                           F(1, s ** strands))

    coxeter_positive_inverse = matrix_power(coxeter, strands - 1)
    for selected in range(strands - 1):
        lower = identity(strands - 1)
        for index in range(selected):
            lower = multiply(reduced[index], lower)
        higher = identity(strands - 1)
        for index in range(selected + 1, strands - 1):
            higher = multiply(reduced[index], higher)
        positive_inverse = multiply(lower,
                                    multiply(coxeter_positive_inverse, higher))
        assert primitive(positive_inverse) == primitive(inverse(reduced[selected]))

    if reduced_weights[0] <= 10000:
        verify_real_macro(strands, s, common=1)
    print("strands", strands, "s", s, "n", sum(reduced_weights),
          "Burau relations, finite Coxeter center, positive inverses: PASS")


if __name__ == "__main__":
    total = 0
    for strands in range(3, 9):
        for s in (3, 9):
            verify(strands, s)
            total += 1
    print("geometric power-chain Burau checks: PASS", total)
