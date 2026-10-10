"""Explore the group hidden in a (r,1,...,1) power-block kernel."""

from fractions import Fraction as F
from math import gcd


def identity(size):
    return [[F(i == j) for j in range(size)] for i in range(size)]


def multiply(left, right):
    return [[sum(left[i][k] * right[k][j] for k in range(len(left)))
             for j in range(len(left))] for i in range(len(left))]


def generator(size, r, selected):
    # Difference coordinates e_i = a_i-u.
    result = identity(size)
    for row in range(size):
        result[row][selected] = F(-1, r)
    return result


def clear(matrix):
    denominator = 1
    for row in matrix:
        for value in row:
            denominator = denominator * value.denominator // gcd(denominator, value.denominator)
    entries = [int(value * denominator) for row in matrix for value in row]
    content = gcd(*(abs(value) for value in entries))
    entries = [value // content for value in entries]
    first = next(value for value in entries if value)
    if first < 0:
        entries = [-value for value in entries]
    return tuple(tuple(entries[i * len(matrix) + j] for j in range(len(matrix)))
                 for i in range(len(matrix)))


def determinant(matrix):
    matrix = [list(row) for row in matrix]
    result = F(1)
    for column in range(len(matrix)):
        pivot = next(row for row in range(column, len(matrix)) if matrix[row][column])
        if pivot != column:
            matrix[pivot], matrix[column] = matrix[column], matrix[pivot]
            result *= -1
        value = matrix[column][column]
        result *= value
        for j in range(column, len(matrix)):
            matrix[column][j] /= value
        for row in range(column + 1, len(matrix)):
            factor = matrix[row][column]
            for j in range(column, len(matrix)):
                matrix[row][j] -= factor * matrix[column][j]
    return result


def characteristic_polynomial(matrix):
    # Faddeev-LeVerrier, coefficients of x^n+c1*x^(n-1)+...+cn.
    size = len(matrix)
    current = identity(size)
    coefficients = []
    for k in range(1, size + 1):
        product_matrix = multiply(matrix, current)
        coefficient = -sum(product_matrix[i][i] for i in range(size)) / k
        coefficients.append(coefficient)
        current = [row[:] for row in product_matrix]
        for i in range(size):
            current[i][i] += coefficient
    return tuple(coefficients)


def analyze(size, r):
    generators = [generator(size, r, selected) for selected in range(size)]
    product_matrix = identity(size)
    for item in generators:
        product_matrix = multiply(item, product_matrix)
    integer = clear(product_matrix)
    print("dimension", size, "r", r, "matrix", integer)
    print("det", determinant(integer), "charpoly tail", characteristic_polynomial(integer))
    power = identity(size)
    finite = None
    for exponent in range(1, 101):
        power = multiply(integer, power)
        if clear(power) == tuple(tuple(int(i == j) for j in range(size)) for i in range(size)):
            finite = exponent
            break
    print("projective order", finite)


if __name__ == "__main__":
    for size in range(2, 9):
        for r in (3, 9):
            analyze(size, r)
