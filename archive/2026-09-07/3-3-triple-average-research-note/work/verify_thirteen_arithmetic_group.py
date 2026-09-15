"""Finite exact certificate for the thirteen-position arithmetic-group proof.

Only Python's standard library is used. Words in A/R/B are chronological;
lowercase denotes a projective inverse. Modular words are matrix products.
"""

from collections import Counter, deque
from fractions import Fraction as F
from math import gcd

from explore_thirteen_group import (A, R, IDENTITY, determinant, inverse,
                                    multiply)
from explore_thirteen_modular import B, Fold, S, U, modular_word


CERTIFICATE = (
    ("ar", (3, 1, -7, -2)),
    ("ABrARb", (26, 3, -9, -1)),
    ("RbaARb", (26, 9, -3, -1)),
    ("rBAb", (3, -2, 2, -1)),
    ("AABrrARb", (52, -3, -17, 1)),
    ("ArrBrBaa", (23, 2, -288, -25)),
    ("bABABAbr", (22, 7, 91, 29)),
    ("AAbabaRaBARb", (333, 22, -106, -7)),
    ("ArBrBBabRa", (179, 13, -2451, -178)),
    ("BRbRbRbaBARb", (649, -78, -208, 25)),
    ("rbABABrBRa", (50, 19, -129, -49)),
    ("AArBAbbRbRBARb", (1989, -62, -802, 25)),
    ("RBRbRbaabRaa", (18, 11, 607, 371)),
    ("brBAbAABrbrARb", (71, 29, -49, -20)),
)


def word_matrix(word):
    generators = {"A": A, "R": R, "B": B,
                  "a": inverse(A), "r": inverse(R), "b": inverse(B)}
    result = IDENTITY
    for letter in word:
        result = multiply(generators[letter], result)
    return result


def chi13(value):
    residue = value % 13
    return 0 if residue == 0 else (1 if pow(residue, 6, 13) == 1 else -1)


def parity2(matrix):
    points = ((1, 0), (0, 1), (1, 1))
    a, b, c, d = matrix
    permutation = [points.index(((a * x + b * y) % 2,
                                 (c * x + d * y) % 2)) for x, y in points]
    return sum(permutation[i] > permutation[j]
               for i in range(3) for j in range(i + 1, 3)) % 2


def verify_macro_words():
    u, v = (F(1), F(0)), (F(0), F(1))
    w = (F(-9), F(-3))

    def core(first, second):
        singleton = tuple(-9 * first[i] - 3 * second[i] for i in range(2))
        return Counter([first] * 9 + [second] * 3 + [singleton])

    def average(state, triple):
        assert all(state[value] >= count for value, count in Counter(triple).items())
        new = tuple(sum(value[i] for value in triple) / 3 for i in range(2))
        for value in triple:
            state[value] -= 1
        state[new] += 3
        return new

    state = core(u, v)
    new_v = average(state, (w, v, v))
    assert +state == core(u, new_v)
    assert new_v == (F(-3), F(-1, 3))
    state = core(u, v)
    for _ in range(3):
        new_u = average(state, (v, u, u))
    assert +state == core(new_u, u)
    assert new_u == (F(2, 3), F(1, 3))
    state = core(u, v)
    intermediate = average(state, (w, u, u))
    for _ in range(3):
        new_u = average(state, (intermediate, u, u))
    assert +state == core(new_u, v)
    assert new_u == (F(-1, 9), F(-1, 3))

    C = multiply(A, R)
    C_inverse = inverse(C)
    assert multiply(C, multiply(C, C)) == IDENTITY
    assert multiply(B, multiply(C_inverse, B)) == C
    assert multiply(C_inverse, multiply(B, C_inverse)) == inverse(B)
    assert multiply(R, multiply(C, C)) == inverse(A)
    assert multiply(multiply(C, C), A) == inverse(R)
    for word, matrix in CERTIFICATE:
        assert word_matrix(word) == matrix, word
        assert determinant(matrix) == 1
        a, b, c, d = matrix
        assert (a + b - c - d) % 13 == 0
        assert chi13(a - c) == 1
        assert parity2(matrix) == 0
    print("symbolic macros, positive inverse identities, and 14 matrix words: PASS")


def row_class(row):
    squares = (1, 3, 4, 9, 10, 12)
    return min(((scale * row[0]) % 13, (scale * row[1]) % 13)
               for scale in squares)


def label_action(label, generator):
    (x, y), parity = label
    a, b, c, d = generator
    return row_class((a * x + c * y, b * x + d * y)), parity ^ parity2(generator)


def verify_cosets():
    fold = Fold()
    for word, matrix in CERTIFICATE:
        fold.loop(modular_word(matrix))
        fold.close()
    table = fold.close()
    nodes = {fold.root(value) for value in range(len(fold.parent))}
    assert len(nodes) == 56
    assert all((node, letter) in table for node in nodes for letter in "su")
    for node in nodes:
        assert table[table[node, "s"], "s"] == node
        assert table[table[table[node, "u"], "u"], "u"] == node

    base = fold.root(0)
    labels = {base: (row_class((1, -1)), 0)}
    representatives = {base: IDENTITY}
    pending = deque([base])
    while pending:
        node = pending.popleft()
        for letter, generator in (("s", S), ("u", U)):
            other = table[node, letter]
            label = label_action(labels[node], generator)
            if other not in labels:
                labels[other] = label
                representatives[other] = multiply(representatives[node], generator)
                pending.append(other)
            else:
                assert labels[other] == label
    assert len(set(labels.values())) == 56
    expected = {(row_class((x, y)), parity)
                for x in range(13) for y in range(13) if x or y
                for parity in (0, 1)}
    assert set(labels.values()) == expected

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
        assert position == start
        matrix = representatives[start]
        first_column = matrix[0], matrix[2]
        cycles.append((cycle, first_column, chi13(first_column[0] - first_column[1])))
    assert sorted(len(cycle) for cycle, _, _ in cycles) == [2, 2, 26, 26]
    assert sorted(character for _, _, character in cycles) == [-1, 0, 0, 1]

    terminal_matrices = (S, (1, 0, -1, 1))
    terminal_cycles = []
    for terminal in terminal_matrices:
        position = base
        for letter in modular_word(terminal):
            if letter == "U":
                position = table[table[position, "u"], "u"]
            else:
                position = table[position, letter]
        cycle_index = next(i for i, (cycle, _, _) in enumerate(cycles)
                           if position in cycle)
        terminal_cycles.append(cycle_index)
    assert len(set(terminal_cycles)) == 2
    assert {cycles[i][2] for i in terminal_cycles} == {-1, 1}
    assert sum(table[node, "s"] == node for node in nodes) == 0
    assert sum(table[node, "u"] == node for node in nodes) == 8
    print("finite modular folding: 56 complete cosets PASS")
    print("independent congruence labels: all 56 distinct PASS")
    print("cusps (width, representative, character):",
          [(len(cycle), vector, character) for cycle, vector, character in cycles])
    print("both legal cusps have explicit terminal representatives: PASS")
    print("elliptic points (order 2, order 3): (0, 8); compact modular genus: 1")


def average_block(state, block):
    size = len(block)
    power = 0
    while 3 ** power < size:
        power += 1
    assert 3 ** power == size
    operations = 0
    for digit in range(power):
        stride = 3 ** digit
        for start in range(size):
            if (start // stride) % 3:
                continue
            indices = [block[start + j * stride] for j in range(3)]
            mean = sum(state[index] for index in indices) / 3
            for index in indices:
                state[index] = mean
            operations += 1
    return operations


def verify_terminals():
    positive = [F(0)] * 9 + [F(1)] * 3 + [F(-3)]
    count_positive = average_block(positive, list(range(4, 13)))
    assert not any(positive)
    negative = [F(1)] * 9 + [F(-1)] * 3 + [F(-6)]
    first_block = list(range(7)) + [9, 12]
    count_negative = average_block(negative, first_block)
    assert all(negative[index] == 0 for index in first_block)
    second_block = [7, 8, 10, 11] + first_block[:5]
    count_negative += average_block(negative, second_block)
    assert not any(negative)
    assert count_positive == 6 and count_negative == 12
    for u in range(-30, 31):
        for v in range(-30, 31):
            if gcd(u, v) != 1:
                continue
            values = [u] * 9 + [v] * 3 + [-9 * u - 3 * v]
            assert gcd(*(value - values[0] for value in values)) == gcd(u - v, 13)
    print("terminal paths: 6 and 12 real operations PASS")
    print("primitive core G formula: PASS")


if __name__ == "__main__":
    verify_macro_words()
    verify_cosets()
    verify_terminals()
