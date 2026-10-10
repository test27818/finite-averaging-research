"""MILP search for a low-multiplicity obstruction to the B_10 reduction."""

from itertools import combinations_with_replacement

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import lil_matrix


def triple_types():
    for triple in combinations_with_replacement(range(30), 3):
        if sum(triple) % 3 or len(set(triple)) == 1:
            continue
        counts = {value: triple.count(value) for value in set(triple)}
        yield triple, counts


def solve():
    triples = list(triple_types())
    alternatives = []
    for _, selected in triples:
        current = []
        for value, count in selected.items():
            current.append(("unavailable", value, count - 1))
        for parity in range(2):
            removed = sum(count for value, count in selected.items() if value % 2 != parity)
            current.append(("parity", parity, removed))
        for residue in range(5):
            removed = sum(count for value, count in selected.items() if value % 5 != residue)
            current.append(("mod5", residue, removed))
        alternatives.append(current)

    count_variables = 30
    quotient_variable = 30
    first_binary = 31
    binary_offsets = []
    variable_count = first_binary
    for current in alternatives:
        binary_offsets.append(variable_count)
        variable_count += len(current)

    rows = []
    lower = []
    upper = []

    def add(coefficients, lo=-np.inf, hi=np.inf):
        rows.append(coefficients)
        lower.append(lo)
        upper.append(hi)

    add({index: 1 for index in range(30)}, 10, 10)
    add({**{index: index for index in range(30)}, quotient_variable: -30}, 0, 0)
    for parity in range(2):
        add({index: 1 for index in range(30) if index % 2 == parity}, 1, 9)
    for residue in range(5):
        add({index: 1 for index in range(30) if index % 5 == residue}, -np.inf, 9)

    big_m = 10
    for current, offset in zip(alternatives, binary_offsets):
        add({offset + index: 1 for index in range(len(current))}, 1, np.inf)
        for index, alternative in enumerate(current):
            kind, residue, threshold = alternative
            binary = offset + index
            if kind == "unavailable":
                # binary=1 implies c_residue <= selected multiplicity - 1.
                add({residue: 1, binary: big_m}, -np.inf, threshold + big_m)
            elif kind == "parity":
                coefficients = {
                    value: 1 for value in range(30) if value % 2 != residue
                }
                coefficients[binary] = big_m
                add(coefficients, -np.inf, threshold + big_m)
            else:
                coefficients = {
                    value: 1 for value in range(30) if value % 5 != residue
                }
                coefficients[binary] = big_m
                add(coefficients, -np.inf, threshold + big_m)

    matrix = lil_matrix((len(rows), variable_count), dtype=float)
    for row, coefficients in enumerate(rows):
        for column, value in coefficients.items():
            matrix[row, column] = value

    objective = np.zeros(variable_count)
    bounds_lower = np.zeros(variable_count)
    bounds_upper = np.ones(variable_count)
    bounds_upper[:count_variables] = 5
    bounds_upper[quotient_variable] = 9
    integrality = np.ones(variable_count)

    result = milp(
        objective,
        integrality=integrality,
        bounds=Bounds(bounds_lower, bounds_upper),
        constraints=LinearConstraint(matrix.tocsr(), lower, upper),
        options={"time_limit": 300},
    )
    print("status", result.status, result.message)
    if result.x is not None:
        counts = [round(value) for value in result.x[:30]]
        state = tuple(value for value, count in enumerate(counts) for _ in range(count))
        print("residue counts", counts)
        print("state", state, "sum", sum(state))
    print("triples", len(triples), "variables", variable_count, "constraints", len(rows))


if __name__ == "__main__":
    solve()
