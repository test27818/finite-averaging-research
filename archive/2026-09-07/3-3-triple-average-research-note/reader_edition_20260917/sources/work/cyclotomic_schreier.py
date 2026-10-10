"""Coarse mod-n x parity Schreier model for the cyclotomic macro group.

For s=9 this omits a genuine mod-8 condition; see cyclotomic_congruence.py.
"""

from collections import deque
from math import gcd

from explore_cyclotomic_group import determinant, matrices, multiply
from explore_thirteen_modular import S, U, modular_word


def parity2(matrix):
    points = ((1, 0), (0, 1), (1, 1))
    a, b, c, d = matrix
    permutation = [points.index(((a * x + b * y) % 2,
                                 (c * x + d * y) % 2)) for x, y in points]
    return sum(permutation[i] > permutation[j]
               for i in range(3) for j in range(i + 1, 3)) % 2


def multiplier_group(n, step):
    result = set()
    value = 1
    while value not in result:
        result.add(value)
        value = value * step % n
    return result | {-value % n for value in result}


def row_class(n, multipliers, row):
    return min((scale * row[0] % n, scale * row[1] % n)
               for scale in multipliers)


def coset_automaton(s):
    n = s * s + s + 1
    # Primitive normalization can divide by powers of 3, and the integral
    # macro subgroup itself realizes multiplier 3.  Thus the stabilized row
    # is defined modulo <-1, 3>, not merely <-1, s> when s=3^k.
    multipliers = multiplier_group(n, 3)
    rows = sorted({row_class(n, multipliers, (x, y))
                   for x in range(n) for y in range(n)
                   if gcd(gcd(x, y), n) == 1})
    labels = [(row, parity) for row in rows for parity in (0, 1)]
    indices = {label: index for index, label in enumerate(labels)}

    def act(label, matrix):
        (x, y), parity = label
        a, b, c, d = matrix
        row = row_class(n, multipliers,
                        ((a * x + c * y) % n, (b * x + d * y) % n))
        return row, parity ^ parity2(matrix)

    table = {(index, letter): indices[act(label, matrix)]
             for index, label in enumerate(labels)
             for letter, matrix in (("s", S), ("u", U))}
    base = indices[(row_class(n, multipliers, (1, -1)), 0)]
    reached = {base}
    queue = deque([base])
    while queue:
        current = queue.popleft()
        for letter in "su":
            following = table[current, letter]
            if following not in reached:
                reached.add(following)
                queue.append(following)
    assert len(reached) == len(labels)
    return labels, table, base


def schreier_basis(s):
    labels, table, base = coset_automaton(s)
    transversal = {base: ""}
    tree = set()
    queue = deque([base])
    while queue:
        current = queue.popleft()
        for letter in "su":
            following = table[current, letter]
            if following not in transversal:
                transversal[following] = transversal[current] + letter
                tree.add((current, letter))
                queue.append(following)

    mapping = {}
    orders = []

    def new(order=0):
        orders.append(order)
        return len(orders)

    # S-orbits.
    handled = set()
    for current in range(len(labels)):
        if current in handled:
            continue
        following = table[current, "s"]
        handled.update((current, following))
        if current == following:
            symbol = new(2)
            mapping[current, "s"] = (symbol,)
        elif (current, "s") in tree or (following, "s") in tree:
            mapping[current, "s"] = ()
            mapping[following, "s"] = ()
        else:
            symbol = new()
            mapping[current, "s"] = (symbol,)
            mapping[following, "s"] = (-symbol,)

    # U-orbits.
    handled.clear()
    for current in range(len(labels)):
        if current in handled:
            continue
        orbit = [current]
        while table[orbit[-1], "u"] != current:
            orbit.append(table[orbit[-1], "u"])
        handled.update(orbit)
        if len(orbit) == 1:
            symbol = new(3)
            mapping[current, "u"] = (symbol,)
            continue
        assert len(orbit) == 3
        non_tree = [node for node in orbit if (node, "u") not in tree]
        if len(non_tree) <= 1:
            for node in orbit:
                mapping[node, "u"] = ()
        elif len(non_tree) == 2:
            first, second = non_tree
            symbol = new()
            mapping[first, "u"] = (symbol,)
            mapping[second, "u"] = (-symbol,)
            for node in orbit:
                mapping.setdefault((node, "u"), ())
        else:
            first = new()
            second = new()
            mapping[orbit[0], "u"] = (first,)
            mapping[orbit[1], "u"] = (second,)
            mapping[orbit[2], "u"] = (-second, -first)

    # Verify every defining relator rewrites to the empty free-product word.
    for current in range(len(labels)):
        assert reduce_word(mapping[current, "s"] + mapping[table[current, "s"], "s"], orders) == ()
        first = table[current, "u"]
        second = table[first, "u"]
        assert table[second, "u"] == current
        word = mapping[current, "u"] + mapping[first, "u"] + mapping[second, "u"]
        assert reduce_word(word, orders) == ()

    counts = {order: orders.count(order) for order in (0, 2, 3)}
    return labels, table, base, mapping, tuple(orders), counts


def reduce_word(word, orders):
    stack = []
    for letter in word:
        generator = abs(letter)
        order = orders[generator - 1]
        if order == 2:
            letter = generator
        elif order == 3 and letter < 0:
            for _ in range(2):
                stack = list(reduce_word(tuple(stack) + (generator,), orders))
            continue
        if stack and abs(stack[-1]) == generator:
            if order == 0 and stack[-1] == -letter:
                stack.pop()
                continue
            if order == 2:
                stack.pop()
                continue
            if order == 3 and stack[-1] == generator and letter == generator:
                stack[-1] = -generator
                continue
            if order == 3 and stack[-1] == -generator and letter == generator:
                stack.pop()
                continue
        stack.append(letter)
    return tuple(stack)


def rewrite_modular(word, data):
    _, table, base, mapping, orders, _ = data
    current = base
    output = []
    for letter in word:
        repetitions = 2 if letter == "U" else 1
        actual = "u" if letter == "U" else letter
        for _ in range(repetitions):
            output.extend(mapping[current, actual])
            current = table[current, actual]
    assert current == base
    return reduce_word(tuple(output), orders)


def verify_macro_words(s, macro_words):
    data = schreier_basis(s)
    generators = matrices(s)
    result = []
    for word in macro_words:
        matrix = (1, 0, 0, 1)
        for letter in word:
            matrix = multiply(generators[letter], matrix)
        assert determinant(matrix) == 1
        result.append(rewrite_modular(modular_word(matrix), data))
    return data, result


if __name__ == "__main__":
    for value in (3, 9):
        data = schreier_basis(value)
        print("s", value, "cosets", len(data[0]), "basis", data[-1])
