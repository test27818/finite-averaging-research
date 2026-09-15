"""Conjugate root closure in the natural index-five direction lattice."""

from fractions import Fraction as F
from itertools import product as words

from verify_carrier_sweep_catalyst import I3, det3, evaluate, outer_factor
from explore_carrier_sweep_relations import product, unipotent_rank_one


def inverse_unipotent(matrix):
    return tuple(tuple(2 * int(i == j) - matrix[i][j]
                       for j in range(3)) for i in range(3))


def matrix_inverse(matrix):
    work = [list(map(F, row)) + [F(i == j) for j in range(3)]
            for i, row in enumerate(matrix)]
    for column in range(3):
        pivot = next(row for row in range(column, 3) if work[row][column])
        work[column], work[pivot] = work[pivot], work[column]
        value = work[column][column]
        work[column] = [entry / value for entry in work[column]]
        for row in range(3):
            if row == column:
                continue
            value = work[row][column]
            work[row] = [x - value * y
                         for x, y in zip(work[row], work[column])]
    return tuple(tuple(entry for entry in row[3:]) for row in work)


def matrix_from_columns(columns):
    return tuple(tuple(columns[column][row] for column in range(3))
                 for row in range(3))


def transform(matrix, basis, basis_inverse):
    output = product(basis_inverse, product(matrix, basis))
    assert all(value.denominator == 1 for row in output for value in row)
    return tuple(tuple(int(value) for value in row) for row in output)


def initial_roots():
    roots = {}
    for sequence in words(range(6), repeat=4):
        matrix = evaluate(sequence)
        if unipotent_rank_one(matrix):
            roots.setdefault(matrix, sequence)
    paired = {}
    for matrix, sequence in roots.items():
        if inverse_unipotent(matrix) in roots:
            paired[matrix] = sequence
    assert len(paired) == 12
    return paired


def direction_basis(roots):
    directions = []
    for matrix in roots:
        direction, _ = outer_factor(matrix)
        if next(value for value in direction if value) < 0:
            direction = tuple(-value for value in direction)
        if direction not in directions:
            directions.append(direction)
    for a in range(len(directions)):
        for b in range(a + 1, len(directions)):
            for c in range(b + 1, len(directions)):
                columns = directions[a], directions[b], directions[c]
                basis = matrix_from_columns(columns)
                determinant = det3(tuple(zip(*basis)))
                if abs(determinant) == 5:
                    return basis, matrix_inverse(basis)
    raise AssertionError("direction lattice has no index-five basis")


def elementary_entry(matrix):
    entries = []
    for row in range(3):
        for column in range(3):
            value = matrix[row][column] - int(row == column)
            if value:
                entries.append((row, column, value))
    return entries[0] if len(entries) == 1 else None


def explore(depth=4):
    generators = initial_roots()
    basis, basis_inverse = direction_basis(generators)
    print("direction lattice basis", basis)
    seen = dict(generators)
    frontier = dict(generators)
    for level in range(depth + 1):
        hits = []
        for matrix, certificate in frontier.items():
            transformed = transform(matrix, basis, basis_inverse)
            entry = elementary_entry(transformed)
            if entry is not None:
                hits.append((entry, certificate, transformed))
        print("level", level, "frontier", len(frontier),
              "total", len(seen), "elementary", len(hits))
        for hit in hits[:20]:
            print(" elementary", hit)
        if hits:
            return
        following = {}
        for root, certificate in frontier.items():
            for generator, generator_word in generators.items():
                conjugate = product(generator, product(root,
                                    inverse_unipotent(generator)))
                if conjugate not in seen and conjugate not in following:
                    following[conjugate] = (generator_word, certificate)
        seen.update(following)
        frontier = following
    print("No elementary root in the bounded conjugate closure.")


if __name__ == "__main__":
    explore()
