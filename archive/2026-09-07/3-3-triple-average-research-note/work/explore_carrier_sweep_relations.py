"""Small-rank diagnostic for the integral carrier-sweep semigroup."""

from itertools import permutations

from explore_carrier_sweep_smith import content, identity, multiply, word


def cleared_carrier(dimension, index):
    matrix = [[0] * dimension for _ in range(dimension)]
    for row in range(dimension):
        if row == index:
            matrix[row][index] = -1
        else:
            matrix[row][row] = 3
            matrix[row][index] = -3
    return matrix


def sweep(leaves, order, boundary=False):
    dimension = leaves + int(boundary)
    matrix = identity(dimension)
    for index in order:
        matrix = multiply(cleared_carrier(dimension, index), matrix)
    return matrix


def normalized(rank, order, boundary=False):
    matrix = sweep(rank, order, boundary)
    divisor = content(matrix)
    return tuple(tuple(value // divisor for value in row) for row in matrix)


def product(a, b):
    return tuple(tuple(value for value in row) for row in multiply(a, b))


def invariants(matrix):
    rank = len(matrix)
    trace = sum(matrix[i][i] for i in range(rank))
    square = product(matrix, matrix)
    trace_two = sum(square[i][i] for i in range(rank))
    return trace, trace_two


def scalar(matrix):
    first = matrix[0][0]
    return all(matrix[i][j] == (first if i == j else 0)
               for i in range(len(matrix)) for j in range(len(matrix)))


def unipotent_rank_one(matrix):
    rank = len(matrix)
    delta = [[matrix[i][j] - int(i == j) for j in range(rank)]
             for i in range(rank)]
    if not any(any(row) for row in delta):
        return False
    square = multiply(delta, delta)
    if any(any(row) for row in square):
        return False
    pivot = next((row for row in delta if any(row)), None)
    return all(not any(row) or all(pivot[i] * row[j] == pivot[j] * row[i]
                                   for i in range(rank) for j in range(rank))
               for row in delta)


def inspect(rank=3, depth=8, boundary=False):
    generators = tuple(normalized(rank, order, boundary)
                       for order in permutations(range(rank)))
    dimension = rank + int(boundary)
    current = {tuple(tuple(row) for row in identity(dimension)): ""}
    seen = dict(current)
    for level in range(1, depth + 1):
        following = {}
        for matrix, certificate in current.items():
            for index, generator in enumerate(generators):
                candidate = product(generator, matrix)
                if candidate in seen or candidate in following:
                    continue
                word_ = certificate + str(index)
                if scalar(candidate):
                    print("positive scalar", level, word_, candidate[0][0])
                    return
                if unipotent_rank_one(candidate):
                    print("positive rank-one unipotent", level, word_, candidate)
                    return
                following[candidate] = word_
        seen.update(following)
        current = following
        print("level", level, "frontier", len(current), "total", len(seen))
    print("No short positive scalar or rank-one unipotent; finite diagnostic only.")


if __name__ == "__main__":
    inspect()
    inspect(boundary=True)
