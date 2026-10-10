"""Bruhat--Tits orbit method for the n=s^2+s+1 macro group."""

from collections import deque

from explore_cyclotomic_group import determinant, inverse, matrices, multiply
from explore_thirteen_modular import Fold, modular_word


def extended_gcd(a, b):
    old_r, r, old_s, s, old_t, t = a, b, 1, 0, 0, 1
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    sign = 1 if old_r > 0 else -1
    return sign * old_r, sign * old_s, sign * old_t


def lattice(matrix):
    a, b, c, d = matrix
    lower, coefficient_c, coefficient_d = extended_gcd(c, d)
    upper = abs(determinant(matrix)) // lower
    offset = (a * coefficient_c + b * coefficient_d) % upper
    return upper, offset, lower


def parity2(matrix):
    points = ((1, 0), (0, 1), (1, 1))
    a, b, c, d = matrix
    permutation = [points.index(((a * x + b * y) % 2,
                                 (c * x + d * y) % 2)) for x, y in points]
    return sum(permutation[i] > permutation[j]
               for i in range(3) for j in range(i + 1, 3)) % 2


def explore(s, radius):
    generators = matrices(s)
    identity = (1, 0, 0, 1)
    states = {lattice(identity): (identity, "")}
    pending = deque(states)
    loops = {}
    bound = 3 ** radius
    while pending:
        matrix, word = states[pending.popleft()]
        for letter, generator in generators.items():
            result = multiply(generator, matrix)
            if abs(determinant(result)) > bound:
                continue
            key = lattice(result)
            if key not in states:
                states[key] = (result, word + letter)
                pending.append(key)
            else:
                representative, representative_word = states[key]
                loop = multiply(inverse(representative), result)
                if abs(determinant(loop)) != 1:
                    raise AssertionError((key, representative, result, loop))
                reverse_word = representative_word.swapcase()[::-1]
                loops[loop] = word + letter + reverse_word
    print("s", s, "radius", radius, "tree vertices", len(states),
          "integral loops", len(loops), flush=True)
    return loops


def fold_loops(loops):
    fold = Fold()
    table = fold.close()
    retained = []
    for matrix, word in loops.items():
        if determinant(matrix) < 0:
            continue
        modular = modular_word(matrix)
        if fold.contains(modular, table):
            continue
        fold.loop(modular)
        table = fold.close()
        nodes = {fold.root(value) for value in range(len(fold.parent))}
        missing = sum((node, letter) not in table
                      for node in nodes for letter in "su")
        retained.append((word, matrix, len(nodes), missing))
        print("fold", len(retained), "nodes", len(nodes), "missing", missing,
              "word", word, flush=True)
        if missing == 0:
            break
    return retained


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--s", type=int, default=9)
    parser.add_argument("--radius", type=int, default=8)
    arguments = parser.parse_args()
    fold_loops(explore(arguments.s, arguments.radius))
