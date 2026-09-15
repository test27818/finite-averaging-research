"""Exact positive five-average experiments near n=11.

Independent uniform samples are filtered only by the conjectured G rule.
Search failure means a resource limit, not nonreachability. Explicit position
certificates are replayed independently using Fraction on the raw input.
"""

import argparse
from collections import Counter
from concurrent.futures import ProcessPoolExecutor, as_completed
from fractions import Fraction
from functools import lru_cache
import heapq
import json
from math import gcd
from pathlib import Path
from random import Random
from time import perf_counter


if not __debug__:
    raise RuntimeError("Assertions must be enabled.")


def canonical(values, sort=True):
    divisor = gcd(*values)
    result = tuple(x // divisor if divisor else x for x in values)
    ordered = tuple(sorted(result))
    reflected = tuple(-x for x in reversed(ordered))
    if reflected < ordered:
        result = tuple(-x for x in result)
        ordered = reflected
    return ordered if sort else result


def centered(raw, sort=True):
    n, total = len(raw), sum(raw)
    return canonical(tuple(n * x - total for x in raw), sort=sort)


def difference_gcd(state):
    return gcd(*(x - state[0] for x in state))


def passes_rule(state, q=5):
    if not any(state):
        return True
    value = difference_gcd(state)
    while value % q == 0:
        value //= q
    return value == 1


@lru_cache(maxsize=4096)
def selections(capacities, q):
    """Count patterns are cached; value-dependent arithmetic stays exact."""
    result = []
    suffix = [0] * (len(capacities) + 1)
    for i in range(len(capacities) - 1, -1, -1):
        suffix[i] = suffix[i + 1] + capacities[i]

    def visit(i, left, pattern):
        if i == len(capacities):
            if left == 0:
                result.append(tuple(pattern))
            return
        for take in range(max(0, left - suffix[i + 1]), min(capacities[i], left) + 1):
            pattern.append(take)
            visit(i + 1, left - take, pattern)
            pattern.pop()

    visit(0, q, [])
    return tuple(result)


def moves_and_states(state, q=5):
    counts = Counter(state)
    values, capacities = tuple(counts), tuple(counts.values())
    for pattern in selections(capacities, q):
        if sum(take > 0 for take in pattern) < 2:
            continue
        move = tuple(x for x, take in zip(values, pattern) for _ in range(take))
        total = sum(move)
        after = [q * x for x, count, take in zip(values, capacities, pattern)
                 for _ in range(count - take)] + [total] * q
        yield move, canonical(tuple(after))


def apply_values(state, move, q=5):
    counts = Counter(state)
    used = Counter(move)
    assert len(move) == q and all(counts[x] >= f for x, f in used.items())
    rest = counts - used
    values = [q * x for x, f in rest.items() for _ in range(f)] + [sum(move)] * q
    return canonical(tuple(values))


def first_zero_move(state, q=5):
    counts = Counter(state)
    values, capacities = tuple(counts), tuple(counts.values())
    for pattern in selections(capacities, q):
        if sum(take > 0 for take in pattern) < 2:
            continue
        if sum(x * take for x, take in zip(values, pattern)) == 0:
            return tuple(x for x, take in zip(values, pattern) for _ in range(take))
    return None


def zero_tail(state, q=5):
    """At n=2q+1 one zero suffices, using only existing positions."""
    assert len(state) == 2 * q + 1 and 0 in state
    current = tuple(state)
    moves = []

    def take(indices):
        nonlocal current
        move = tuple(current[i] for i in indices)
        if len(set(move)) == 1:
            return
        assert len(indices) == len(set(indices)) == q
        moves.append(move)
        values = [q * x for x in current]
        for i in indices:
            values[i] = sum(move)
        current = canonical(tuple(values), sort=False)

    zero_index = current.index(0)
    others = [i for i in range(len(state)) if i != zero_index]
    take(others[:q])
    take(others[q:])
    while any(current):
        nonzero = sorted(set(x for x in current if x))
        assert len(nonzero) == 2 and sum(nonzero) == 0
        a, b = nonzero
        left = [i for i, x in enumerate(current) if x == a]
        right = [i for i, x in enumerate(current) if x == b]
        zeros = [i for i, x in enumerate(current) if not x]
        pairs = min(len(left), len(right), (q - 1) // 2)
        take(left[:pairs] + right[:pairs] + zeros[:q - 2 * pairs])
    assert len(moves) <= 5
    return moves


def short_tail(state, q=5, budget_depth=3):
    """Try only zero-producing moves before the certified five-step tail."""
    if not any(state):
        return []
    assert 0 in state
    best = zero_tail(state, q)
    seen = {}

    def visit(current, path, depth):
        nonlocal best
        if len(path) >= len(best):
            return
        if not any(current):
            best = path.copy()
            return
        if depth == 0 or len(path) + (sum(x != 0 for x in current) + q - 1) // q >= len(best):
            return
        if seen.get(current, -1) >= depth:
            return
        seen[current] = depth
        for move, after in moves_and_states(current, q):
            if sum(move) == 0:
                visit(after, path + [move], depth - 1)

    visit(state, [], budget_depth)
    return best


def lower_bound(state, q=5):
    active = sum(x != 0 for x in state)
    if not active:
        return 0
    basic = (active + q - 1) // q
    if active == len(state) and first_zero_move(state, q) is None:
        basic += 1
    return basic


def replay(raw, moves, q=5):
    """Map value choices to labels, then verify independently from raw data."""
    labelled = centered(raw, sort=False)
    operations = []
    for move in moves:
        unused, indices = set(range(len(raw))), []
        for value in move:
            index = next(i for i in unused if labelled[i] == value)
            unused.remove(index)
            indices.append(index)
        values = [q * x for x in labelled]
        for i in indices:
            values[i] = sum(move)
        labelled = canonical(tuple(values), sort=False)
        operations.append([i + 1 for i in indices])
    assert not any(labelled)
    return verify_operations(raw, operations, q)


def verify_operations(raw, operations, q=5):
    exact = list(map(Fraction, raw))
    target = Fraction(sum(raw), len(raw))
    max_denominator_exponent = 0
    max_numerator_bits = 0
    for step, indices in enumerate(operations):
        assert len(indices) == len(set(indices)) == q
        assert all(isinstance(i, int) and 1 <= i <= len(raw) for i in indices)
        before = sum(exact[i - 1] for i in indices)
        mean = before / q
        denominator, exponent = mean.denominator, 0
        while denominator % q == 0:
            denominator //= q
            exponent += 1
        assert denominator == 1
        max_denominator_exponent = max(max_denominator_exponent, exponent)
        max_numerator_bits = max(max_numerator_bits, abs(mean.numerator).bit_length())
        for i in indices:
            exact[i - 1] = mean
        assert sum(exact[i - 1] for i in indices) == before
    assert all(x == target for x in exact)
    return {"operations": operations, "verified": True, "target": str(target),
            "max_denominator_exponent": max_denominator_exponent,
            "max_mean_numerator_bits": max_numerator_bits}


def path_to(nodes, index):
    path = []
    while nodes[index][1] is not None:
        _, parent, move, _ = nodes[index]
        path.append(move)
        index = parent
    return path[::-1]


def search(raw, q=5, seconds=2, max_nodes=30000, width=128, max_depth=20,
           mode="beam"):
    state = centered(raw)
    assert len(state) == 2 * q + 1 and passes_rule(state, q)
    start = perf_counter()
    initial_lower = lower_bound(state, q)
    nodes = [(state, None, None, 0)]
    seen = {state: 0}
    expanded = generated = 0
    best_path = None
    first_zero_depth = 0 if 0 in state else None
    initial_zero_subset = first_zero_move(state, q) is not None
    complete_depth = -1
    reason = "depth-limit"

    def finish(path, reason):
        elapsed = perf_counter() - start
        result = {"status": "solved" if path is not None else "not-found-within-budget",
                  "reason": reason, "q": q, "n": len(raw), "input": raw,
                  "primitive_centered": list(state), "G": difference_gcd(state),
                  "steps": len(path) if path is not None else None,
                  "solve_seconds": elapsed, "expanded": expanded, "generated": generated,
                  "visited": len(seen), "mode": mode, "width": width,
                  "lower_bound": initial_lower, "optimal": path is not None and len(path) == initial_lower,
                  "initial_zero": 0 in state, "initial_zero_subset": initial_zero_subset,
                  "first_zero_depth": first_zero_depth, "complete_search_depth": complete_depth}
        if path is not None:
            result.update(replay(raw, path, q))
        return result

    if not any(state):
        return finish([], "already-constant")
    if 0 in state:
        return finish(short_tail(state, q), "initial-zero-certified-tail")
    if initial_zero_subset:
        move = first_zero_move(state, q)
        after = apply_values(state, move, q)
        first_zero_depth = 1
        return finish([move] + short_tail(after, q), "one-step-zero-certified-tail")

    frontier = [0]
    for depth in range(max_depth):
        candidates = {}
        for index in frontier:
            if perf_counter() - start >= seconds or expanded >= max_nodes:
                reason = "time-limit" if perf_counter() - start >= seconds else "node-limit"
                return finish(best_path, reason)
            current = nodes[index][0]
            expanded += 1
            for move, after in moves_and_states(current, q):
                generated += 1
                if not passes_rule(after, q):
                    continue
                new_depth = depth + 1
                if 0 in after:
                    path = path_to(nodes, index) + [move]
                    if first_zero_depth is None:
                        first_zero_depth = new_depth
                    tail = short_tail(after, q)
                    path += tail
                    if best_path is None or len(path) < len(best_path):
                        best_path = path
                    return finish(best_path, "searched-zero-certified-tail")
                if seen.get(after, 10**9) <= new_depth:
                    continue
                # Unselected beam states are not entered in the global seen
                # map: they may become useful after another branch is tried.
                if after not in candidates:
                    energy = sum(x * x for x in after)
                    score = (energy, len(set(after)))
                    candidates[after] = (score, index, move)
        if mode == "bfs":
            selected = list(candidates.items())
            complete_depth = depth + 1
        else:
            selected = heapq.nsmallest(width, candidates.items(), key=lambda item: item[1][0])
        if not selected:
            return finish(best_path, "frontier-exhausted")
        frontier = []
        for after, (_, parent, move) in selected:
            seen[after] = depth + 1
            frontier.append(len(nodes))
            nodes.append((after, parent, move, depth + 1))
    return finish(best_path, reason)


def sample_cases(n, count, low, high, seed):
    rng = Random(seed)
    result, attempts = [], 0
    while len(result) < count:
        raw = [rng.randint(low, high) for _ in range(n)]
        attempts += 1
        if passes_rule(centered(raw), 5):
            result.append(raw)
    return result, attempts


def worker(payload):
    index, raw, options = payload
    return index, search(raw, **options)


def run_batch(args):
    cases, attempts = sample_cases(args.n, args.count, -args.bound, args.bound, args.seed)
    options = {"seconds": args.seconds, "max_nodes": args.nodes, "width": args.width,
               "max_depth": args.depth, "mode": args.mode}
    started = perf_counter()
    results = [None] * len(cases)
    if args.jobs == 1:
        for index, raw in enumerate(cases):
            results[index] = search(raw, **options)
            row = results[index]
            print("case", index, row["status"], row["steps"], row["first_zero_depth"],
                  round(row["solve_seconds"], 4), row["expanded"], flush=True)
    else:
        with ProcessPoolExecutor(max_workers=args.jobs) as pool:
            futures = [pool.submit(worker, (i, raw, options)) for i, raw in enumerate(cases)]
            for future in as_completed(futures):
                index, row = future.result()
                results[index] = row
                print("case", index, row["status"], row["steps"], row["first_zero_depth"],
                      round(row["solve_seconds"], 4), row["expanded"], flush=True)
    solved = [row for row in results if row["status"] == "solved"]
    summary = {"samples": len(cases), "solved": len(solved), "attempts": attempts,
               "initial_zero": sum(row["initial_zero"] for row in results),
               "initial_zero_subset": sum(row["initial_zero_subset"] for row in results),
               "solved_neither_initial_zero_nor_subset": sum(not row["initial_zero"] and not row["initial_zero_subset"] for row in solved),
               "mean_steps": sum(row["steps"] for row in solved) / len(solved) if solved else None,
               "min_steps": min((row["steps"] for row in solved), default=None),
               "max_steps": max((row["steps"] for row in solved), default=None),
               "wall_seconds": perf_counter() - started,
               "total_solve_seconds": sum(row["solve_seconds"] for row in results)}
    report = {"settings": vars(args), "sampling": "independent uniform raw integers, then G=5^a rejection only",
              "scope": "finite search, no claim that passing G is sufficient at n11",
              "summary": summary, "cases": results}
    Path(args.output).write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print("SUMMARY", json.dumps(summary), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=11)
    parser.add_argument("--count", type=int, default=20)
    parser.add_argument("--bound", type=int, default=20)
    parser.add_argument("--seed", type=int, default=5122026)
    parser.add_argument("--seconds", type=float, default=2)
    parser.add_argument("--nodes", type=int, default=30000)
    parser.add_argument("--width", type=int, default=128)
    parser.add_argument("--depth", type=int, default=20)
    parser.add_argument("--mode", choices=("beam", "bfs"), default="beam")
    parser.add_argument("--jobs", type=int, default=1)
    parser.add_argument("--output", default="work/five_average_n11_random.json")
    run_batch(parser.parse_args())
