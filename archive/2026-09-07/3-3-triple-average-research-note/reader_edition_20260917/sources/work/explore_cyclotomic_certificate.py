"""Test the thirteen-position words in a coarse cyclotomic quotient.

For s>3 the mod-n row and mod-2 parity labels omit further local conditions;
see cyclotomic_congruence.py before interpreting any folding result.
"""

from collections import deque
from math import gcd

from explore_cyclotomic_group import (determinant, inverse, matrices, multiply,
                                      primitive)
from explore_thirteen_modular import Fold, S, U, modular_word


CERTIFICATE_WORDS = (
    "ar", "ABrARb", "RbaARb", "rBAb", "AABrrARb", "ArrBrBaa",
    "bABABAbr", "AAbabaRaBARb", "ArBrBBabRa", "BRbRbRbaBARb",
    "rbABABrBRa", "AArBAbbRbRBARb", "RBRbRbaabRaa", "brBAbAABrbrARb",
)


def word_matrix(word, generator):
    result = (1, 0, 0, 1)
    for letter in word:
        result = multiply(generator[letter], result)
    return result


def multiplier_group(n, s):
    group = {1}
    value = 1
    while True:
        value = value * s % n
        if value in group:
            break
        group.add(value)
    return group | {-value % n for value in group}


def primitive_rows(n, multiplier):
    rows = []
    for x in range(n):
        for y in range(n):
            if gcd(gcd(x, y), n) != 1:
                continue
            orbit = {(m * x % n, m * y % n) for m in multiplier}
            if min(orbit) == (x, y):
                rows.append((x, y))
    return rows


def row_class(n, multiplier, row):
    orbit = {(m * row[0] % n, m * row[1] % n) for m in multiplier}
    return min(orbit)


def permutation_parity(matrix):
    a, b, c, d = matrix
    points = ((1, 0), (0, 1), (1, 1))
    permutation = [points.index(((a * x + b * y) % 2,
                                 (c * x + d * y) % 2)) for x, y in points]
    return sum(permutation[i] > permutation[j]
               for i in range(3) for j in range(i + 1, 3)) % 2


def verify_generator(s):
    n = s * s + s + 1
    generators = matrices(s)
    multiplier = multiplier_group(n, 3)
    print("COARSE quotient: s", s, "n", n, "|multiplier|", len(multiplier),
          "|rows|", len(primitive_rows(n, multiplier)), flush=True)
    certificate = []
    for word in CERTIFICATE_WORDS:
        matrix = word_matrix(word, generators)
        a, b, c, d = matrix
        row = (a - c, b - d)
        scale = next((value for value in multiplier
                      if (value * 1 - row[0]) % n == 0
                      and (value * -1 - row[1]) % n == 0), None)
        print("  ", word, "stabilizes", scale is not None,
              "det", determinant(matrix), flush=True)
        if scale is not None and permutation_parity(matrix) == 0 and abs(determinant(matrix)) == 1:
            certificate.append(matrix)
    return n, multiplier, generators, certificate


def verify_fold(s, max_vertices=100000):
    n, multiplier, generators, certificate = verify_generator(s)
    rows = primitive_rows(n, multiplier)
    expected = len(rows) * 2
    if expected > max_vertices:
        print("skip folding; expected", expected)
        return
    fold = Fold()
    for matrix in certificate:
        fold.loop(modular_word(matrix))
        fold.close()
    table = fold.close()
    nodes = {fold.root(value) for value in range(len(fold.parent))}
    complete = all((node, letter) in table for node in nodes for letter in "su")
    print("fold vertices", len(nodes), "expected", expected, "complete", complete,
          flush=True)
    if not complete or len(nodes) != expected:
        return
    base = fold.root(0)
    labels = {base: (row_class(n, multiplier, (1, -1)), 0)}
    pending = deque([base])
    while pending:
        node = pending.popleft()
        x, parity = labels[node]
        for letter, matrix in (("s", S), ("u", U)):
            other = table[node, letter]
            a, b, c, d = matrix
            label = (row_class(n, multiplier,
                              ((a * x[0] + c * x[1]) % n,
                               (b * x[0] + d * x[1]) % n)),
                     parity ^ permutation_parity(matrix))
            if other not in labels:
                labels[other] = label
                pending.append(other)
            else:
                assert labels[other] == label
    assert len(set(labels.values())) == expected
    # Cusp cycles under T=SU.
    translation = {node: table[table[node, "s"], "u"] for node in nodes}
    unused = set(nodes)
    cycles = []
    while unused:
        start = min(unused)
        cycle = []
        position = start
        while position not in cycle:
            cycle.append(position)
            unused.remove(position)
            position = translation[position]
        cycles.append((len(cycle), labels[start]))
    print("cusps", len(cycles), "widths", sorted(length for length, _ in cycles),
          "characters", sorted(set(0 if (label[0][0] - label[0][1]) % n == 0
                                   else 1 for _, label in cycles)), flush=True)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--s", type=int, action="append")
    arguments = parser.parse_args()
    for value in arguments.s or [3, 9]:
        verify_fold(value)
