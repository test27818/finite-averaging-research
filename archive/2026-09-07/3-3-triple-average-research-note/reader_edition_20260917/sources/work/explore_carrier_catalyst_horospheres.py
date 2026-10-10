"""Find full rank-two horospherical slices in the catalyst root group."""

from collections import defaultdict
from itertools import product as words
from math import gcd

from verify_carrier_sweep_catalyst import evaluate, outer_factor
from explore_carrier_sweep_relations import unipotent_rank_one


def dot(left, right):
    return sum(x * y for x, y in zip(left, right))


def matvec(matrix, vector):
    return tuple(sum(matrix[i][j] * vector[j] for j in range(3))
                 for i in range(3))


def rowmat(vector, matrix):
    return tuple(sum(vector[i] * matrix[i][j] for i in range(3))
                 for j in range(3))


def inverse_root(matrix):
    return tuple(tuple(2 * int(i == j) - matrix[i][j]
                       for j in range(3)) for i in range(3))


def canonical_pair(u, f):
    divisor = gcd(*(abs(value) for value in u))
    u = tuple(value // divisor for value in u)
    f = tuple(value * divisor for value in f)
    if next(value for value in u if value) < 0:
        u = tuple(-value for value in u)
        f = tuple(-value for value in f)
    assert dot(f, u) == 0
    return u, f


def initial():
    roots = {}
    for sequence in words(range(6), repeat=4):
        matrix = evaluate(sequence)
        if unipotent_rank_one(matrix):
            roots.setdefault(matrix, sequence)
    paired = {}
    for matrix, sequence in roots.items():
        if inverse_root(matrix) in roots:
            paired[canonical_pair(*outer_factor(matrix))] = sequence
    assert len(paired) == 12
    return paired


def independent(a, b):
    return any(a[i] * b[j] != a[j] * b[i]
               for i in range(3) for j in range(i))


def slices(roots):
    directions = defaultdict(list)
    kernels = defaultdict(list)
    for (u, f), certificate in roots.items():
        directions[u].append((f, certificate))
        primitive_f = canonical_pair(f, u)[0]
        kernels[primitive_f].append((u, certificate))
    direction_hits = [
        (u, values[i], values[j])
        for u, values in directions.items()
        for i in range(len(values)) for j in range(i)
        if independent(values[i][0], values[j][0])
    ]
    kernel_hits = [
        (f, values[i], values[j])
        for f, values in kernels.items()
        for i in range(len(values)) for j in range(i)
        if independent(values[i][0], values[j][0])
    ]
    return direction_hits, kernel_hits


def explore(depth=5):
    generators = initial()
    generator_data = []
    for pair, certificate in generators.items():
        u, f = pair
        matrix = tuple(tuple(int(i == j) + u[i] * f[j]
                             for j in range(3)) for i in range(3))
        generator_data.append((matrix, inverse_root(matrix), certificate))
    seen = dict(generators)
    frontier = dict(generators)
    for level in range(depth + 1):
        direction_hits, kernel_hits = slices(seen)
        print("level", level, "frontier", len(frontier), "total", len(seen),
              "direction slices", len(direction_hits),
              "kernel slices", len(kernel_hits), flush=True)
        if direction_hits and kernel_hits:
            print("direction example", direction_hits[0])
            print("kernel example", kernel_hits[0])
            return
        following = {}
        for (u, f), certificate in frontier.items():
            for matrix, matrix_inverse, generator_word in generator_data:
                output = canonical_pair(matvec(matrix, u),
                                        rowmat(f, matrix_inverse))
                if output not in seen and output not in following:
                    following[output] = (generator_word, certificate)
        seen.update(following)
        frontier = following
    print("No full horospherical slice in the bounded conjugate closure.")


if __name__ == "__main__":
    explore()
