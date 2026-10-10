"""Historical independent-level container for cyclotomic macros.

For n91 this is strictly larger than the macro group's integer part.
verify_cyclotomic_level_entanglement.py retains this model and constructs
the coupled index-two refinement without changing historical labels.
"""

from collections import deque

from analyze_cyclotomic_local_images import canonical, multiply_mod
from cyclotomic_schreier import multiplier_group, row_class
from explore_cyclotomic_group import matrices
from explore_thirteen_modular import S, U


def macro_local_orientation_image(s, modulus=8):
    generators = [canonical(matrix, modulus) for matrix in matrices(s).values()]
    identity = canonical((1, 0, 0, 1), modulus)
    seen = {(identity, 0)}
    queue = deque(seen)
    while queue:
        current, parity = queue.popleft()
        for generator in generators:
            following = multiply_mod(current, generator, modulus), parity ^ 1
            if following not in seen:
                seen.add(following)
                queue.append(following)
    orientation_image = {matrix for matrix, parity in seen if parity == 0}
    # Passing from a macro word to its primitive determinant-one matrix can
    # divide by an odd power of 3.  For s=3^(2j), this contributes the central
    # square-root-of-one class 3I modulo 8.
    exponent = 0
    value = s
    while value % 3 == 0:
        exponent += 1
        value //= 3
    assert value == 1
    if exponent % 2 == 0:
        scalar = canonical((3, 0, 0, 3), modulus)
        orientation_image |= {multiply_mod(scalar, matrix, modulus)
                              for matrix in orientation_image}
    return orientation_image


def full_modular_group(modulus=8):
    identity = canonical((1, 0, 0, 1), modulus)
    generators = [canonical(S, modulus), canonical(U, modulus)]
    seen = {identity}
    queue = deque([identity])
    while queue:
        current = queue.popleft()
        for generator in generators:
            following = multiply_mod(current, generator, modulus)
            if following not in seen:
                seen.add(following)
                queue.append(following)
    return seen


def right_coset(subgroup, representative, modulus=8):
    return min(multiply_mod(element, representative, modulus)
               for element in subgroup)


def local_coset_action(s, modulus=8):
    subgroup = macro_local_orientation_image(s, modulus)
    group = full_modular_group(modulus)
    cosets = sorted({right_coset(subgroup, element, modulus) for element in group})
    indices = {coset: index for index, coset in enumerate(cosets)}
    table = {}
    for index, representative in enumerate(cosets):
        for letter, generator in (("s", S), ("u", U)):
            following = multiply_mod(representative,
                                     canonical(generator, modulus), modulus)
            table[index, letter] = indices[right_coset(subgroup, following, modulus)]
    base = indices[right_coset(subgroup, canonical((1, 0, 0, 1), modulus),
                               modulus)]
    return subgroup, cosets, table, base


def congruence_automaton(s, modulus=8):
    n = s * s + s + 1
    multipliers = multiplier_group(n, 3)
    rows = sorted({row_class(n, multipliers, (x, y))
                   for x in range(n) for y in range(n)
                   if __import__("math").gcd(__import__("math").gcd(x, y), n) == 1})
    row_indices = {row: index for index, row in enumerate(rows)}
    subgroup, cosets, local_table, local_base = local_coset_action(s, modulus)

    def row_act(row, matrix):
        x, y = row
        a, b, c, d = matrix
        return row_class(n, multipliers,
                         ((a * x + c * y) % n, (b * x + d * y) % n))

    labels = [(row, local) for row in rows for local in range(len(cosets))]
    indices = {label: index for index, label in enumerate(labels)}
    table = {}
    for index, (row, local) in enumerate(labels):
        for letter, generator in (("s", S), ("u", U)):
            following = (row_act(row, generator), local_table[local, letter])
            table[index, letter] = indices[following]
    base = indices[(row_class(n, multipliers, (1, -1)), local_base)]
    return labels, table, base, subgroup, cosets


def cycles_of(table, labels, word):
    permutation = {}
    for start in range(len(labels)):
        current = start
        for letter in word:
            current = table[current, letter]
        permutation[start] = current
    unused = set(range(len(labels)))
    cycles = []
    while unused:
        start = min(unused)
        cycle = []
        current = start
        while current not in cycle:
            cycle.append(current)
            unused.remove(current)
            current = permutation[current]
        assert current == start
        cycles.append(cycle)
    return cycles


def analyze(s):
    labels, table, base, subgroup, cosets = congruence_automaton(s)
    reached = {base}
    queue = deque([base])
    while queue:
        current = queue.popleft()
        for letter in "su":
            following = table[current, letter]
            if following not in reached:
                reached.add(following)
                queue.append(following)
    e2 = sum(table[index, "s"] == index for index in range(len(labels)))
    e3 = sum(table[index, "u"] == index for index in range(len(labels)))
    cusps = cycles_of(table, labels, "su")
    free_rank = 1 + len(labels) // 6 - e2 // 2 - 2 * e3 // 3
    print("s", s, "local subgroup", len(subgroup), "local cosets", len(cosets))
    print("global labels", len(labels), "reached", len(reached))
    print("elliptic e2", e2, "e3", e3, "free rank", free_rank)
    widths = sorted(len(cycle) for cycle in cusps)
    from collections import Counter
    from math import gcd
    n = s * s + s + 1
    legal = [cycle for cycle in cusps
             if gcd(labels[cycle[0]][0][0], n) == 1]
    legal_data = Counter((len(cycle), labels[cycle[0]][0][0])
                         for cycle in legal)
    print("cusps", len(cusps), "width distribution", Counter(widths))
    print("legal cusps", len(legal), "legal (width, difference-label)",
          legal_data)
    assert sum(widths) == len(labels)
    return labels, table, base, cusps


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--s", type=int, default=9)
    analyze(parser.parse_args().s)
