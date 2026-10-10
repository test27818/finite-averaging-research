"""Find integral stabilizers by exploring the 3-adic lattice tree."""

from collections import deque
from explore_thirteen_group import (A, R, IDENTITY, determinant, inverse,
                                    multiply)
from explore_thirteen_modular import B, Fold, modular_word


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
    lower, s, t = extended_gcd(c, d)
    upper = abs(determinant(matrix)) // lower
    offset = (a * s + b * t) % upper
    return upper, offset, lower


def main(radius):
    basic = {"A": A, "R": R, "B": B,
             "a": inverse(A), "r": inverse(R), "b": inverse(B)}
    states = {lattice(IDENTITY): (IDENTITY, "")}
    pending = deque(states)
    loops = []
    while pending:
        matrix, word = states[pending.popleft()]
        for letter, generator in basic.items():
            result = multiply(generator, matrix)
            if abs(determinant(result)) > 3 ** radius:
                continue
            key = lattice(result)
            if key not in states:
                states[key] = (result, word + letter)
                pending.append(key)
            else:
                representative, representative_word = states[key]
                loop = multiply(inverse(representative), result)
                assert abs(determinant(loop)) == 1
                reverse_word = representative_word.swapcase()[::-1]
                loops.append((loop, word + letter + reverse_word))
    print("radius", radius, "tree vertices", len(states), "integral loops", len(loops), flush=True)
    fold = Fold()
    table = fold.close()
    negative = None
    retained = []
    matrices = []
    for matrix, word in loops:
        if determinant(matrix) < 0:
            if negative is None:
                negative = matrix, word
            matrix = multiply(negative[0], matrix)
            word += negative[1]
        matrices.append((matrix, word))
    if negative:
        matrices += [(multiply(negative[0], multiply(matrix, inverse(negative[0]))),
                      negative[1].swapcase()[::-1] + word + negative[1])
                     for matrix, word in list(matrices)]
    for matrix, word in matrices:
        word_modular = modular_word(matrix)
        if fold.contains(word_modular, table):
            continue
        fold.loop(word_modular)
        table = fold.close()
        nodes = {fold.root(value) for value in range(len(fold.parent))}
        missing = sum((node, letter) not in table
                      for node in nodes for letter in "su")
        retained.append((word, matrix, len(nodes), missing))
        if missing == 0:
            print("COMPLETE index", len(nodes), flush=True)
            break
    print("retained", retained, flush=True)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--radius", type=int, default=3)
    main(parser.parse_args().radius)
