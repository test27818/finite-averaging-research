"""Explore symbolic return macros of B_n kernels for several dimensions."""

from collections import Counter, deque
from concurrent.futures import ProcessPoolExecutor, as_completed
from fractions import Fraction as F
from itertools import combinations_with_replacement
from math import gcd
import os


def add(left, right):
    return left[0] + right[0], left[1] + right[1]


def scale(value, factor):
    return value[0] * factor, value[1] * factor


def normalize_state(state):
    denominator = 1
    for value in state:
        for coordinate in value:
            denominator = denominator * coordinate.denominator // gcd(
                denominator, coordinate.denominator
            )
    integer = Counter()
    content = 0
    for value, count in state.items():
        converted = tuple(int(coordinate * denominator) for coordinate in value)
        integer[converted] += count
        content = gcd(content, *(abs(coordinate) for coordinate in converted))
    if content > 1:
        integer = Counter(
            {
                tuple(coordinate // content for coordinate in value): count
                for value, count in integer.items()
            }
        )
    key = tuple(sorted(integer.items()))
    negative = tuple(
        sorted(
            (
                tuple(-coordinate for coordinate in value),
                count,
            )
            for value, count in integer.items()
        )
    )
    return Counter(dict(min(key, negative)))


def state_key(state):
    return tuple(sorted(state.items()))


def start_state(n):
    m = n - 4
    return Counter({(F(1), F(0)): m, (F(0), F(1)): 3, (F(-m), F(-3)): 1})


def signatures(state):
    values = tuple(state)
    for selected in combinations_with_replacement(values, 3):
        required = Counter(selected)
        if len(required) == 1:
            continue
        if all(state[value] >= count for value, count in required.items()):
            yield selected


def step(state, selected):
    following = state.copy()
    total = (F(0), F(0))
    for value in selected:
        total = add(total, value)
        following[value] -= 1
        if following[value] == 0:
            del following[value]
    following[scale(total, F(1, 3))] += 3
    return normalize_state(+following)


def return_matrix(n, state):
    m = n - 4
    if len(state) != 3:
        return None
    first = [value for value, count in state.items() if count == m]
    second = [value for value, count in state.items() if count == 3]
    singleton = [value for value, count in state.items() if count == 1]
    if len(first) != 1 or len(second) != 1 or len(singleton) != 1:
        return None
    u, v, w = first[0], second[0], singleton[0]
    expected = add(scale(u, -m), scale(v, -3))
    if w != expected:
        return None
    return primitive_matrix((u[0], u[1], v[0], v[1]))


def primitive_matrix(matrix):
    denominator = 1
    for value in matrix:
        denominator = denominator * value.denominator // gcd(
            denominator, value.denominator
        )
    integers = tuple(int(value * denominator) for value in matrix)
    content = gcd(*(abs(value) for value in integers))
    if content:
        integers = tuple(value // content for value in integers)
    negative = tuple(-value for value in integers)
    return min(integers, negative)


def determinant(matrix):
    return matrix[0] * matrix[3] - matrix[1] * matrix[2]


def explore_one(task):
    n, depth = task
    start = normalize_state(start_state(n))
    queue = deque([(start, ())])
    seen = {state_key(start)}
    returns = {}
    level_counts = Counter({0: 1})
    while queue:
        state, path = queue.popleft()
        if path:
            matrix = return_matrix(n, state)
            if matrix is not None:
                returns.setdefault(matrix, path)
        if len(path) >= depth:
            continue
        for selected in signatures(state):
            following = step(state, selected)
            identifier = state_key(following)
            if identifier not in seen:
                seen.add(identifier)
                following_path = path + (selected,)
                level_counts[len(following_path)] += 1
                queue.append((following, following_path))
    determinant_counts = Counter()
    parabolic = []
    for matrix, path in returns.items():
        det = determinant(matrix)
        determinant_counts[det] += 1
        trace = matrix[0] + matrix[3]
        if trace * trace == 4 * det:
            parabolic.append((matrix, path))
    return {
        "n": n,
        "depth": depth,
        "states": len(seen),
        "levels": dict(sorted(level_counts.items())),
        "returns": returns,
        "determinants": dict(sorted(determinant_counts.items())),
        "parabolic": parabolic,
    }


def report(result):
    n = result["n"]
    returns = result["returns"]
    print(
        f"n={n} symbolic states {result['states']} depth {result['depth']} "
        f"levels {result['levels']}"
    )
    print(f"n={n} return matrices {len(returns)} determinants {result['determinants']}")
    print(f"n={n} parabolic returns {len(result['parabolic'])}")
    shortest = sorted(
        ((len(path), matrix, path) for matrix, path in returns.items()),
        key=lambda item: (item[0], item[1]),
    )[:12]
    for length, matrix, path in shortest:
        print(f"n={n} return depth {length} matrix {matrix} path {path}")
    for matrix, path in result["parabolic"][:8]:
        print(f"n={n} parabolic matrix {matrix} path {path}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, action="append")
    parser.add_argument("--depth", type=int, default=5)
    parser.add_argument("--jobs", type=int, default=os.cpu_count() or 1)
    arguments = parser.parse_args()
    dimensions = arguments.n or [12, 15, 18, 21]
    tasks = [(n, arguments.depth) for n in dimensions]
    workers = min(max(1, arguments.jobs), len(tasks))
    if workers == 1:
        results = map(explore_one, tasks)
        executor = None
    else:
        executor = ProcessPoolExecutor(max_workers=workers)
        futures = [executor.submit(explore_one, task) for task in tasks]
        results = (future.result() for future in as_completed(futures))
    try:
        for result in results:
            report(result)
    finally:
        if executor is not None:
            executor.shutdown()
