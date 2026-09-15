"""Exact finite certificate for B12 and the resulting twelve-point theorem.

Chronological macro words multiply from the left. The certificate proves
H <= the positive macro group, with H conjugate to Gamma_0(8), index 12.
"""

from collections import Counter, deque
from fractions import Fraction as F
from math import gcd

from explore_thirteen_group import IDENTITY, determinant, inverse, multiply
from explore_thirteen_modular import Fold, S as MODULAR_S, U, modular_word
from verify_bn_arithmetic_structure import core, average
from verify_thirteen_arithmetic_group import average_block


GENERATORS = {
    "A": (3, 0, -8, -1),
    "B": (18, 9, -41, -16),
    "C": (3, 0, 10, 9),
    "D": (3, 0, -8, -9),
}
POSITIVE_INVERSES = {"a": "DDADADA", "b": "CBC",
                     "c": "BCB", "d": "ADADAAD"}
CERTIFICATE = (
    ("Bad", (2, 1, -1, 0)),
    ("AADa", (1, 0, -16, 1)),
    ("cACD", (1, 0, 8, 1)),
    ("ADDaaaB", (50, 9, -89, -16)),
    ("ADaBadA", (22, 3, -59, -8)),
)


def word_matrix(word):
    result = IDENTITY
    for letter in word:
        matrix = (GENERATORS[letter] if letter.isupper()
                  else inverse(GENERATORS[letter.upper()]))
        result = multiply(matrix, result)
    return result


def positive_word(word):
    return "".join(letter if letter.isupper() else POSITIVE_INVERSES[letter]
                   for letter in word)


def macro(name):
    u, v = (F(1), F(0)), (F(0), F(1))
    w = (F(-8), F(-3))
    state = core(u, v)
    path = []

    def take(selected):
        path.append(selected)
        return average(state, selected)

    if name == "A":
        first, second = u, take((v, v, w))
    elif name == "B":
        a = take((w, v, v))
        for _ in range(3):
            first = take((a, u, u))
        b = take((u, v, first))
        second = take((u, b, b))
    else:
        a = take((w, u, u))
        b = take((a, a, v))
        c = take((v, u, u))
        for _ in range(3):
            first = take((b, c, u))
        second = take((v if name == "C" else a, first, u))
    assert state == core(first, second)
    return first+second, tuple(path)


def verify_macros():
    expected = {"A": (1, 3), "B": (6, -81), "C": (7, 27), "D": (7, 27)}
    # Each scalar is the primitive projective representative's denominator.
    for name, matrix in GENERATORS.items():
        actual, path = macro(name)
        length, denominator = expected[name]
        assert len(path) == length
        assert actual == tuple(F(x, denominator) for x in matrix)
        assert determinant(matrix) % 2
        a, b, c, d = matrix
        assert (a+b) % 2 == (c+d) % 2 == 1
    for lower, word in POSITIVE_INVERSES.items():
        assert word_matrix(word) == inverse(GENERATORS[lower.upper()])
    assert word_matrix("BCBC") == IDENTITY
    assert word_matrix("ADDADADA") == IDENTITY
    assert word_matrix("DADADAAD") == IDENTITY
    for word, matrix in CERTIFICATE:
        assert word_matrix(word) == matrix
        assert word_matrix(positive_word(word)) == matrix
        assert determinant(matrix) == 1
        a, b, c, d = matrix
        assert (a-b+c-d) % 8 == 0
    print("B12 four real macros and positive inverses: PASS")
    print("B12 five positive modular generators: PASS")


def row_class(row):
    return min(tuple(scale*x % 8 for x in row) for scale in (1, 3, 5, 7))


def label_action(row, matrix):
    a, b, c, d = matrix
    x, y = row
    return row_class((x*a+y*c, x*b+y*d))


def verify_cosets():
    fold = Fold()
    for word, matrix in CERTIFICATE:
        fold.loop(modular_word(matrix))
        table = fold.close()
    nodes = {fold.root(i) for i in range(len(fold.parent))}
    assert len(nodes) == 12
    assert all((node, letter) in table for node in nodes for letter in "su")
    for node in nodes:
        assert table[table[node, "s"], "s"] == node
        assert table[table[table[node, "u"], "u"], "u"] == node
    base = fold.root(0)
    labels, representatives = {base: row_class((1, 1))}, {base: IDENTITY}
    queue = deque([base])
    while queue:
        node = queue.popleft()
        for letter, matrix in (("s", MODULAR_S), ("u", U)):
            following = table[node, letter]
            label = label_action(labels[node], matrix)
            if following not in labels:
                labels[following] = label
                representatives[following] = multiply(representatives[node], matrix)
                queue.append(following)
            else:
                assert labels[following] == label
    expected = {row_class((a, b)) for a in range(8) for b in range(8)
                if a % 2 or b % 2}
    assert len(expected) == 12 and set(labels.values()) == expected
    translation = {node: table[table[node, "s"], "u"] for node in nodes}
    unused, cusps = set(nodes), []
    while unused:
        start = min(unused)
        node, cycle = start, []
        while node not in cycle:
            cycle.append(node)
            unused.remove(node)
            node = translation[node]
        assert node == start
        matrix = representatives[start]
        pair = matrix[0], matrix[2]
        legal = (pair[0]-pair[1]) % 2 == 1
        assert all(bool(labels[item][0] % 2) == legal for item in cycle)
        cusps.append((len(cycle), pair, legal))
    assert sorted(width for width, _, _ in cusps) == [1, 1, 2, 8]
    assert [(width, pair) for width, pair, legal in cusps if legal] == [(8, (1, 0))]
    assert sum(table[node, "s"] == node for node in nodes) == 0
    assert sum(table[node, "u"] == node for node in nodes) == 0
    print("B12 congruence folding: 12 complete cosets PASS")
    print("B12 independent mod-8 labels: PASS 12")
    print("B12 cusps", cusps)
    print("B12 exactly one legal cusp, representative (1,0): PASS")


def bezout(a, b):
    old_r, r, old_s, s, old_t, t = a, b, 1, 0, 0, 1
    while r:
        quotient = old_r//r
        old_r, r = r, old_r-quotient*r
        old_s, s = s, old_s-quotient*s
        old_t, t = t, old_t-quotient*t
    if old_r == -1:
        return -old_s, -old_t
    assert old_r == 1
    return old_s, old_t


def legal_column_matrix(u, v):
    if gcd(u, v) != 1 or (u-v) % 2 == 0:
        raise ValueError("primitive parameters with odd difference required")
    d, minus_b = bezout(u, v)
    b = -minus_b
    shift = ((u+v-b-d)*pow(u+v, -1, 8)) % 8
    b, d = b+shift*u, d+shift*v
    return u, b, v, d


def verify_columns_and_terminal():
    checked = 0
    for u in range(-30, 31):
        for v in range(-30, 31):
            if gcd(u, v) != 1 or (u-v) % 2 == 0:
                continue
            a, b, c, d = legal_column_matrix(u, v)
            assert a*d-b*c == 1
            assert (a-b+c-d) % 8 == 0
            state = [u]*8+[v]*3+[-8*u-3*v]
            assert gcd(*(abs(x) for x in state)) == 1
            assert gcd(*(abs(x-state[0]) for x in state)) == gcd(u-v, 12)
            checked += 1
    state = [F(1)]*8+[F(0)]*3+[F(-8)]
    operations = average_block(state, list(range(8))+[11])
    assert operations == 6 and not any(state)
    print("B12 legal-column congruence construction: PASS", checked)
    print("B12 terminal (1,0): six real operations PASS")


def verify_positive_path_replay():
    words = [word for word, _ in CERTIFICATE]
    paths = {name: macro(name) for name in GENERATORS}
    checked = 0
    for word in words + [words[i]+words[j] for i in range(5) for j in range(5)]:
        matrix = word_matrix(word)
        u, v = F(matrix[0]), F(matrix[2])
        assert (int(u)-int(v)) % 2

        def numeric_core(u, v):
            state = Counter()
            for value, count in ((u, 8), (v, 3), (-8*u-3*v, 1)):
                state[value] += count
            return state

        state = numeric_core(u, v)
        inverse_word = "".join(letter.swapcase() for letter in reversed(word))
        for letter in positive_word(inverse_word):
            coefficients, path = paths[letter]
            for symbolic_triple in path:
                selected = tuple(a*u+b*v for a, b in symbolic_triple)
                assert all(state[value] >= count
                           for value, count in Counter(selected).items())
                for value in selected:
                    state[value] -= 1
                    if not state[value]:
                        del state[value]
                state[sum(selected, F(0))/3] += 3
            a, b, c, d = coefficients
            u, v = a*u+b*v, c*u+d*v
            assert state == numeric_core(u, v)
        assert v == 0 and u != 0
        values = list(state.elements())
        nonzero = [index for index, value in enumerate(values) if value]
        assert len(nonzero) == 9
        assert average_block(values, nonzero) == 6 and not any(values)
        checked += 1
    print("B12 expanded positive word to zero replay: PASS", checked)


if __name__ == "__main__":
    verify_macros()
    verify_cosets()
    verify_columns_and_terminal()
    verify_positive_path_replay()
