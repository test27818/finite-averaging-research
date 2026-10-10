"""Exact contents and Smith factors of carrier-exchange sweeps."""

from itertools import permutations
from math import gcd


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def multiply(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(a)))
             for j in range(len(b[0]))] for i in range(len(a))]


def cleared_carrier(rank, index):
    # This is 3*T_i on differences from the active singleton carrier.
    matrix = [[0] * rank for _ in range(rank)]
    for row in range(rank):
        if row == index:
            matrix[row][index] = -1
        else:
            matrix[row][row] = 3
            matrix[row][index] = -3
    return matrix


def content(matrix):
    return gcd(*(entry for row in matrix for entry in row))


def valuation(value, prime=3):
    result = 0
    while value and value % prime == 0:
        value //= prime
        result += 1
    return result


def determinantal_divisor_two(matrix):
    size = len(matrix)
    result = 0
    for i in range(size):
        for j in range(i + 1, size):
            for k in range(size):
                for ell in range(k + 1, size):
                    result = gcd(result,
                                 matrix[i][k] * matrix[j][ell]
                                 - matrix[i][ell] * matrix[j][k])
    return result


def word(rank, indices):
    matrix = identity(rank)
    for index in indices:
        matrix = multiply(cleared_carrier(rank, index), matrix)
    return matrix


if __name__ == "__main__":
    for rank in range(2, 9):
        sweep = tuple(range(rank))
        matrix = word(rank, sweep)
        print("rank", rank, "sweep", sweep,
              "content-v3", valuation(content(matrix)),
              "minor2-v3", valuation(determinantal_divisor_two(matrix)))
        if rank <= 7:
            distribution = {}
            for order in permutations(range(rank)):
                exponent = valuation(content(word(rank, order)))
                distribution[exponent] = distribution.get(exponent, 0) + 1
            print(" permutation contents", distribution)
