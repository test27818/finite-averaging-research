"""Extract mixed-singleton trace-zero structure from existing return libraries.

This does not expand the template grammar.  It only classifies matrices
already produced by ``compile_bn_integer_templates``.
"""

from fractions import Fraction as F
from math import factorial

from compile_bn_integer_templates import compile_returns
from verify_bn_integer_templates import physical_matrix
from verify_diagonal_resource_reduction import product


def standard(p):
    return (F(1), F(0), F(4 - p, 3), F(-1, 3))


def normalized(matrix):
    first = next(value for value in matrix if value)
    return tuple(value / first for value in matrix)


def mixed_parameters(p, matrix):
    a, b, c, d = matrix
    m = p - 4
    singleton = (-m * a - 3 * c, -m * b - 3 * d)
    scale = a + b
    if not scale or sum(singleton) != scale:
        return None
    t = b / scale
    beta = singleton[1] / scale
    if t != F(9 + beta, 2 * p + 1):
        return None
    return t, beta, scale


def inspect(p):
    rows, stats = compile_returns(
        p, include_six=True, current_library=True, expanded_first=True
    )
    a = standard(p)
    trace_zero = []
    mixed = []
    targets = {
        F(0),
        F(1),
        F(1, 10 * factorial((p - 1) // 2)),
    }
    for key, row in rows.items():
        matrix = physical_matrix(row)
        cycle = product(matrix, a)
        if cycle[0] + cycle[3]:
            continue
        trace_zero.append(key)
        parameters = mixed_parameters(p, matrix)
        if parameters is not None:
            t, beta, scale = parameters
            mixed.append((beta, t, scale, beta in targets, key))
    print(
        "p", p,
        "returns", len(rows),
        "trace_zero", len(trace_zero),
        "mixed", len(mixed),
        "stats", (stats["prefixes"], stats["middle_tests"], stats["final_tests"]),
    )
    for item in sorted(mixed)[:20]:
        print("  mixed", item)


if __name__ == "__main__":
    for prime in (17, 23, 29, 41, 47, 53, 59, 71, 83):
        inspect(prime)
