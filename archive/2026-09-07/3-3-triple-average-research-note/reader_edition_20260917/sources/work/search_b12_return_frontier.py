"""Integer symbolic search with sound return-shape pruning and exact replay."""

from collections import Counter, deque
from concurrent.futures import ProcessPoolExecutor, as_completed
from fractions import Fraction as F
from itertools import combinations_with_replacement
from math import gcd
import argparse
import json
import os
from pathlib import Path
from time import perf_counter


def canonical(state):
    content = gcd(*(abs(x) for value in state for x in value))
    if not content:
        raise ValueError("the symbolic B12 space cannot be uniformly annihilated")
    positive = tuple(sorted((a//content, b//content, count)
                            for (a, b), count in state.items() if count))
    negative = tuple(sorted((-a, -b, count) for a, b, count in positive))
    return min(positive, negative)


def start_state(n=12):
    return canonical({(1, 0): n-4, (0, 1): 3, (-(n-4), -3): 1})


START = start_state()


def choices(state):
    for ids in combinations_with_replacement(range(len(state)), 3):
        if ids[0] == ids[2]:
            continue
        if all(ids.count(index) <= state[index][2] for index in set(ids)):
            yield ids


def step(state, selected):
    result = {(3*a, 3*b): count for a, b, count in state}
    total_a = total_b = 0
    for index in selected:
        a, b, _ = state[index]
        total_a += a
        total_b += b
        value = 3*a, 3*b
        result[value] -= 1
        if not result[value]:
            del result[value]
    value = total_a, total_b
    result[value] = result.get(value, 0) + 3
    return canonical(result)


def return_matrix(state, n=12):
    m = n-4
    if sorted(count for a, b, count in state) != [1, 3, m]:
        return None
    first = next((a, b) for a, b, count in state if count == m)
    second = next((a, b) for a, b, count in state if count == 3)
    single = next((a, b) for a, b, count in state if count == 1)
    assert single == tuple(-m*first[i]-3*second[i] for i in (0, 1))
    entries = first + second
    content = gcd(*(abs(x) for x in entries))
    entries = tuple(x//content for x in entries)
    return min(entries, tuple(-x for x in entries))


def replay(path, return_actual=False, n=12):
    """Indices refer to canonically ordered forms; preserve actual scaling."""
    symbolic = start_state(n)
    actual = Counter({(F(a), F(b)): count for a, b, count in symbolic})
    operations = []
    for selected in path:
        # Recover the unique common scale relating actual and canonical forms.
        denominator = 1
        for value in actual:
            for coordinate in value:
                denominator = denominator*coordinate.denominator//gcd(
                    denominator, coordinate.denominator)
        actual_key = canonical({
            tuple(int(x*denominator) for x in value): count
            for value, count in actual.items()
        })
        assert actual_key == symbolic
        a, b, _ = symbolic[0]
        coordinate = 0 if a else 1
        candidates = [value[coordinate] / (a if coordinate == 0 else b)
                      for value in actual if value[coordinate]]
        scale = next(
            factor for factor in candidates
            if Counter({(F(x)*factor, F(y)*factor): count
                        for x, y, count in symbolic}) == actual
        )
        values = [(symbolic[index][0]*scale, symbolic[index][1]*scale)
                  for index in selected]
        operations.append(tuple(values))
        for value in values:
            assert actual[value] > 0
            actual[value] -= 1
            if not actual[value]:
                del actual[value]
        mean = tuple(sum(value[i] for value in values)/3 for i in (0, 1))
        actual[mean] += 3
        symbolic = step(symbolic, selected)
    matrix = return_matrix(symbolic, n)
    assert matrix is not None
    if return_actual:
        first = next(value for value, count in actual.items() if count == n-4)
        second = next(value for value, count in actual.items() if count == 3)
        return first+second, tuple(operations)
    return matrix


def explore_branch(task):
    state, prefix, depth, n = task
    queue = deque([(state, prefix)])
    seen = {state}
    returns = {}
    processed = 0
    while queue:
        current, path = queue.popleft()
        processed += 1
        matrix = return_matrix(current, n)
        if path and matrix is not None:
            if matrix not in returns or len(path) < len(returns[matrix]):
                returns[matrix] = path
        remaining = depth-len(path)
        # All three selected singleton values can disappear when their
        # mean already occurs outside the triple.
        if remaining <= 0 or len(current) > 3+3*remaining:
            continue
        # A target value can gain at most three copies per operation.
        if max(count for a, b, count in current) + 3*remaining < n-4:
            continue
        for selected in choices(current):
            following = step(current, selected)
            if remaining == 1:
                matrix = return_matrix(following, n)
                if matrix is not None:
                    returns.setdefault(matrix, path+(selected,))
            elif following not in seen:
                seen.add(following)
                queue.append((following, path+(selected,)))
    return returns, processed


def search(depth, jobs, split_depth=2, n=12):
    started = perf_counter()
    split_depth = min(split_depth, depth)
    start = start_state(n)
    frontier = [(start, ())]
    prefix_returns = {}
    seen = {start}
    for _ in range(split_depth):
        following = []
        for state, path in frontier:
            for selected in choices(state):
                target = step(state, selected)
                word = path+(selected,)
                matrix = return_matrix(target, n)
                if matrix is not None:
                    prefix_returns.setdefault(matrix, word)
                if target not in seen:
                    seen.add(target)
                    following.append((target, word))
        frontier = following
    tasks = [(state, path, depth, n) for state, path in frontier]
    workers = max(1, min(jobs, len(tasks)))
    print(f"START B{n} depth={depth} branches={len(tasks)} workers={workers}", flush=True)
    executor = None
    if workers == 1:
        results = map(explore_branch, tasks)
    else:
        executor = ProcessPoolExecutor(max_workers=workers)
        results = (future.result() for future in as_completed(
            [executor.submit(explore_branch, task) for task in tasks]))
    returns = dict(prefix_returns)
    processed = 0
    try:
        for branch, count in results:
            processed += count
            for matrix, path in branch.items():
                if (matrix not in returns
                        or (len(path), path) < (len(returns[matrix]), returns[matrix])):
                    returns[matrix] = path
    finally:
        if executor:
            executor.shutdown()
    for matrix, path in returns.items():
        assert replay(path, n=n) == matrix
    elapsed = perf_counter()-started
    print(f"B{n} depth={depth} matrices={len(returns)} inspected={processed} "
          f"seconds={elapsed:.3f}", flush=True)
    return {"n": n, "depth": depth, "method": "integer-symbolic-pruned-v3",
            "seconds": elapsed, "inspected": processed,
            "returns": [{"matrix": matrix, "path": path}
                        for matrix, path in sorted(returns.items())]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--depth", type=int, default=5)
    parser.add_argument("--n", type=int, default=12)
    parser.add_argument("--jobs", type=int, default=os.cpu_count() or 1)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.depth < 2 or args.jobs < 1 or args.n < 8:
        parser.error("depth must be at least 2, n at least 8, and jobs positive")
    result = search(args.depth, args.jobs, n=args.n)
    if args.output:
        args.output.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
