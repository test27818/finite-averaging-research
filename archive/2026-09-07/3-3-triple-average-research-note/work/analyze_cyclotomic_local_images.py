"""Compare local images of cyclotomic tree loops with the candidate subgroup."""

from collections import deque
from itertools import product

from check_cyclotomic_abelianization import determinant_one_generators
from explore_cyclotomic_tree import explore, parity2


def canonical(matrix, modulus):
    value = tuple(entry % modulus for entry in matrix)
    negative = tuple(-entry % modulus for entry in value)
    return min(value, negative)


def multiply_mod(left, right, modulus):
    a, b, c, d = left
    e, f, g, h = right
    return canonical((a * e + b * g, a * f + b * h,
                      c * e + d * g, c * f + d * h), modulus)


def generated_image(generators, modulus):
    generators = {canonical(matrix, modulus) for matrix in generators}
    identity = canonical((1, 0, 0, 1), modulus)
    seen = {identity}
    queue = deque([identity])
    while queue:
        current = queue.popleft()
        for generator in generators:
            following = multiply_mod(generator, current, modulus)
            if following not in seen:
                seen.add(following)
                queue.append(following)
    return seen


def expected_image(modulus):
    result = set()
    for matrix in product(range(modulus), repeat=4):
        a, b, c, d = matrix
        if (a * d - b * c) % modulus != 1:
            continue
        if modulus % 2 == 0 and parity2(matrix):
            continue
        result.add(canonical(matrix, modulus))
    return result


def analyze(s, radius):
    loops = explore(s, radius)
    generators = determinant_one_generators(loops)
    for modulus in (4, 5, 7, 8, 16):
        actual = generated_image(generators, modulus)
        expected = expected_image(modulus)
        print("mod", modulus, "actual", len(actual), "expected", len(expected),
              "missing", len(expected - actual), flush=True)
        if len(expected - actual) <= 8:
            print("missing matrices", sorted(expected - actual), flush=True)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--s", type=int, default=9)
    parser.add_argument("--radius", type=int, default=10)
    arguments = parser.parse_args()
    analyze(arguments.s, arguments.radius)
