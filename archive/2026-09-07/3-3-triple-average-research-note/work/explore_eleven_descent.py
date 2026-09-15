"""Explore exact descent macros for the B_11 family."""

from collections import deque
from fractions import Fraction as F
from math import gcd, lcm
from pathlib import Path
import pickle

from symbolic_two_parameter_macros import b_parameters, b_state, choices, step


def matrix_mul(left, right):
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )


def xy_matrix(parameters):
    # (X,Y)=(u,7u+4v).
    change = ((F(1), F(0)), (F(7), F(4)))
    inverse = ((F(1), F(0)), (F(-7, 4), F(1, 4)))
    rational = matrix_mul(change, matrix_mul(parameters, inverse))
    denominator = lcm(*(entry.denominator for row in rational for entry in row))
    entries = [int(entry * denominator) for row in rational for entry in row]
    divisor = gcd(*entries)
    entries = [entry // divisor for entry in entries]
    first = next((entry for entry in entries if entry), 1)
    if first < 0:
        entries = [-entry for entry in entries]
    return tuple(entries)


def macros(max_depth=5):
    cache_path = Path(__file__).with_name(f"eleven_all_macros_depth_{max_depth}.pickle")
    if cache_path.exists():
        with cache_path.open("rb") as stream:
            return pickle.load(stream)

    start = b_state(11)
    queue = deque([(start, ())])
    seen = {start}
    found = {}
    levels = {0: 1}
    while queue:
        state, path = queue.popleft()
        if path:
            for parameters in b_parameters(11, state):
                matrix = xy_matrix(parameters)
                found.setdefault(matrix, path)
        if len(path) == max_depth:
            continue
        for selected, signature in choices(state):
            nxt = step(state, selected)
            if nxt not in seen:
                seen.add(nxt)
                levels[len(path) + 1] = levels.get(len(path) + 1, 0) + 1
                queue.append((nxt, path + (signature,)))
    result = found, len(seen), levels
    with cache_path.open("wb") as stream:
        pickle.dump(result, stream)
    return result


def primitive_pair(x, y):
    divisor = gcd(abs(x), abs(y))
    if not divisor:
        return 0, 0
    x, y = x // divisor, y // divisor
    if x < 0 or (x == 0 and y < 0):
        x, y = -x, -y
    return x, y


def legal_type(x, y):
    x, y = primitive_pair(x, y)
    if not (x or y) or y % 11 == 0:
        return None
    residue = (y - 7 * x) % 4
    if residue == 0:
        return 1
    if residue == 2:
        return 2
    return 4


def weight(x, y):
    scale = legal_type(x, y)
    assert scale is not None
    return scale * scale * (77 * x * x + 3 * y * y)


def image(matrix, pair):
    a, b, c, d = matrix
    x, y = pair
    return a * x + b * y, c * x + d * y


def descends(matrix, pair):
    nxt = primitive_pair(*image(matrix, pair))
    return legal_type(*nxt) is not None and weight(*nxt) < weight(*pair)


def legal_pairs(bound):
    return [
        (x, y)
        for x in range(-bound, bound + 1)
        for y in range(-bound, bound + 1)
        if primitive_pair(x, y) == (x, y) and legal_type(x, y) is not None
    ]


def greedy_cover(found, pairs):
    full = (1 << len(pairs)) - 1
    covers = {}
    for matrix in found:
        bits = 0
        for index, pair in enumerate(pairs):
            if descends(matrix, pair):
                bits |= 1 << index
        if bits:
            covers[matrix] = bits
    selected = []
    covered = 0
    while covered != full:
        matrix = max(covers, key=lambda item: (covers[item] & ~covered).bit_count())
        gain = covers[matrix] & ~covered
        if not gain:
            break
        selected.append(matrix)
        covered |= gain
    return selected, (full & ~covered).bit_count()


def analyze(bound=250, max_depth=5):
    found, state_count, levels = macros(max_depth)
    pairs = legal_pairs(bound)
    selected, missing = greedy_cover(found, pairs)
    print("levels", levels, "states", state_count, "legal returns", len(found))
    print("pairs", len(pairs), "greedy", len(selected), "missing", missing)
    for matrix in selected:
        print(" matrix", matrix, "det", matrix[0] * matrix[3] - matrix[1] * matrix[2],
              "depth", len(found[matrix]))
    for larger in (500, 1000):
        misses = [pair for pair in legal_pairs(larger)
                  if not any(descends(matrix, pair) for matrix in selected)]
        print("bound", larger, "misses", len(misses), misses[:30])


if __name__ == "__main__":
    analyze()
