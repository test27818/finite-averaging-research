"""Explore exact descent macros for the B_10 family."""

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
    # (X,Y)=(u,3u+2v).
    change = ((F(1), F(0)), (F(3), F(2)))
    inverse = ((F(1), F(0)), (F(-3, 2), F(1, 2)))
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
    cache_path = Path(__file__).with_name(f"ten_macros_depth_{max_depth}.pickle")
    if cache_path.exists():
        with cache_path.open("rb") as stream:
            return pickle.load(stream)

    start = b_state(10)
    queue = deque([(start, ())])
    seen = {start}
    found = {}
    while queue:
        state, path = queue.popleft()
        if path:
            for parameters in b_parameters(10, state):
                found.setdefault(xy_matrix(parameters), path)
        if len(path) == max_depth:
            continue
        for selected, signature in choices(state):
            nxt = step(state, selected)
            if nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, path + (signature,)))
    result = found, len(seen)
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
    if not (x or y) or y % 5 == 0:
        return None
    if (x - y) % 2:
        # This is (u,v)=(2X,Y-3X), with u even and v odd.
        return 2
    if x % 2 and y % 2 and (x + y) % 4 == 0:
        # This is (u,v)=(X,(Y-3X)/2), with u odd and v even.
        return 1
    return None


def weight(x, y):
    scale = legal_type(x, y)
    assert scale is not None
    return scale * scale * (5 * x * x + y * y)


def image(matrix, pair):
    a, b, c, d = matrix
    x, y = pair
    return a * x + b * y, c * x + d * y


def terminal(pair):
    x, y = pair
    return x == 0 or y == 3 * x or y == -x


def descends(matrix, pair):
    nxt = primitive_pair(*image(matrix, pair))
    return (
        nxt == (0, 0)
        or (legal_type(*nxt) is not None and weight(*nxt) < weight(*pair))
    )


def legal_pairs(bound):
    return [
        (x, y)
        for x in range(-bound, bound + 1)
        for y in range(-bound, bound + 1)
        if primitive_pair(x, y) == (x, y)
        and legal_type(x, y) is not None
        and not terminal((x, y))
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

    # Remove choices made redundant by later matrices.
    changed = True
    while changed:
        changed = False
        for matrix in selected[:]:
            others = 0
            for candidate in selected:
                if candidate != matrix:
                    others |= covers[candidate]
            if others == full:
                selected.remove(matrix)
                changed = True
                break
    return selected, (full & ~covered).bit_count(), covers


def analyze(bound=250, max_depth=5):
    found, state_count = macros(max_depth)
    covered = 0
    uncovered = []
    usage = {matrix: 0 for matrix in found}
    legal_count = 0
    for x in range(-bound, bound + 1):
        for y in range(-bound, bound + 1):
            pair = primitive_pair(x, y)
            if pair != (x, y) or legal_type(x, y) is None:
                continue
            legal_count += 1
            if terminal(pair):
                covered += 1
                continue
            candidates = []
            for matrix in found:
                nxt = primitive_pair(*image(matrix, pair))
                if nxt == (0, 0):
                    candidates.append((0, matrix, nxt))
                elif legal_type(*nxt) is not None and weight(*nxt) < weight(*pair):
                    candidates.append((weight(*nxt), matrix, nxt))
            if candidates:
                _, chosen, _ = min(candidates)
                usage[chosen] += 1
                covered += 1
            else:
                uncovered.append(pair)

    used = sorted(
        ((count, matrix, found[matrix]) for matrix, count in usage.items() if count),
        reverse=True,
    )
    print("symbolic states", state_count, "return matrices", len(found))
    print("primitive legal pairs", legal_count, "covered", covered, "uncovered", len(uncovered))
    print("first uncovered", uncovered[:40])
    print("used matrices", len(used))
    for count, matrix, path in used[:30]:
        determinant = matrix[0] * matrix[3] - matrix[1] * matrix[2]
        print(" use", count, "matrix", matrix, "det", determinant, "length", len(path))
    pairs = legal_pairs(bound)
    selected, missing, _ = greedy_cover(found, pairs)
    print("greedy cover", len(selected), "missing", missing)
    for matrix in selected:
        determinant = matrix[0] * matrix[3] - matrix[1] * matrix[2]
        print(" select", matrix, "det", determinant, "length", len(found[matrix]))
    for larger_bound in (500, 1000):
        misses = [
            pair for pair in legal_pairs(larger_bound)
            if not any(descends(matrix, pair) for matrix in selected)
        ]
        print("selected cover bound", larger_bound, "misses", len(misses), misses[:20])
    return found, uncovered, used


if __name__ == "__main__":
    analyze()
