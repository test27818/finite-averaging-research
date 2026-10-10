"""Exact ternary IDA* over all legal rational states, plus constructive bounds.

The invariant constructor supplies upper bounds only. Search permits arbitrary
triadic denominators and states without repeated values. Budget exhaustion
never proves impossibility or optimality.
"""

from collections import Counter, deque
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, combinations_with_replacement
from math import gcd
from time import perf_counter

from analyze_double_triple_sequence_length import maximal_drop
from verify_all_dimensions_double_triple_invariant import initialize
from verify_prime_double_triple_invariant import replay_step, terminal

if not __debug__:
    raise RuntimeError("Exact search requires assertions.")


def primitive(values, sort=True):
    divisor = gcd(*values)
    result = tuple(x // divisor if divisor else x for x in values)
    return tuple(sorted(result)) if sort else result


def centered(values):
    n, total = len(values), sum(values)
    return primitive(tuple(n * x - total for x in values))


def possible(state, q=3):
    if not any(state):
        return True
    difference = gcd(*(x - state[0] for x in state))
    while difference and difference % q == 0:
        difference //= q
    return difference == 1


def apply_values(state, move, q=3):
    counts = Counter(state)
    used = Counter(move)
    assert all(counts[x] >= f for x, f in used.items())
    remaining = counts - used
    values = [q * x for x, f in remaining.items() for _ in range(f)]
    values += [sum(move)] * q
    return primitive(tuple(values))


@lru_cache(maxsize=30000)
def lower_bound(state):
    nonzero = tuple(x for x in state if x)
    c = (len(nonzero) + 2) // 3
    if not c:
        return 0
    # Counting all zero-sum pairs/triples overestimates disjoint packing,
    # which is the safe direction for this admissible lower bound.
    available = 0
    for size in (2, 3):
        for subset in combinations(nonzero, size):
            if sum(subset) == 0:
                available += 1
                if available >= c:
                    return c
    return c + (max(0, c - available) + 2) // 3


@lru_cache(maxsize=10000)
def successors(state):
    counts = Counter(state)
    result, seen = [], set()
    for move in combinations_with_replacement(sorted(counts), 3):
        if move[0] == move[-1]:
            continue
        if any(counts[x] < f for x, f in Counter(move).items()):
            continue
        after = apply_values(state, move)
        if after in seen or not possible(after):
            continue
        seen.add(after)
        result.append((after, move))
    result.sort(key=lambda item: (lower_bound(item[0]), sum(x != 0 for x in item[0]),
                                  sum(x * x for x in item[0])))
    return tuple(result)


def zero_move(state):
    counts = Counter(state)
    candidates = []
    for move in combinations_with_replacement(sorted(counts), 3):
        if not any(move) or sum(move):
            continue
        if all(counts[x] >= f for x, f in Counter(move).items()):
            candidates.append(move)
    return max(candidates, key=lambda move: (sum(x != 0 for x in move),
                                            sum(x * x for x in move)), default=None)


def power_tail(state):
    active = [i for i, x in enumerate(state) if x]
    if not active:
        return []
    size = 1
    while size < len(active):
        size *= 3
    if size > len(state):
        return None
    active += [i for i, x in enumerate(state) if not x][:size - len(active)]
    current, moves = tuple(state), []
    stride = 1
    while stride < size:
        for start in range(0, size, 3 * stride):
            for offset in range(stride):
                indices = [active[start + offset + t * stride] for t in range(3)]
                move = tuple(current[i] for i in indices)
                if move[0] == move[1] == move[2]:
                    continue
                moves.append(move)
                values = [3 * x for x in current]
                for i in indices:
                    values[i] = sum(move)
                current = primitive(tuple(values), sort=False)
        stride *= 3
    assert not any(current)
    return moves


def four_active_tail(state):
    counts = Counter(x for x in state if x)
    if sum(counts.values()) != 4 or len(state) < 7:
        return None
    current, moves = state, []
    if 3 not in counts.values():
        move = tuple(x for x in state if x)[:3]
        moves.append(move)
        current = apply_values(current, move)
        counts = Counter(x for x in current if x)
    repeated = next(x for x, f in counts.items() if f == 3)
    assert counts[-3 * repeated] == 1
    move = (-3 * repeated, 0, 0)
    moves.append(move)
    current = apply_values(current, move)
    while any(current):
        move = zero_move(current)
        assert move is not None
        moves.append(move)
        current = apply_values(current, move)
    return moves


def invariant_bound(state):
    if len(state) < 11:
        return None
    current, moves = [3 * x for x in state], []

    def take(move):
        nonlocal current
        divisor = gcd(*current)
        moves.append(tuple(x // divisor for x in move))
        current, _ = replay_step(current, move)

    for move in initialize(Counter(current), len(state)):
        take(move)
    while not terminal(Counter(current), len(state)):
        move, _ = maximal_drop(Counter(current), len(state))
        take(move)
    a = next(x for x in current if x)
    for _ in range(3):
        take((a, -a, 0))
    assert not any(current)
    return moves


def upper_bound(state, shortcuts=True):
    if not any(state):
        return []
    current, prefix = state, []
    if shortcuts:
        while any(current):
            move = zero_move(current)
            if move is None:
                break
            prefix.append(move)
            current = apply_values(current, move)
        if not any(current):
            return prefix
    candidates = [tail for tail in (power_tail(current), four_active_tail(current))
                  if tail is not None]
    if candidates:
        return prefix + min(candidates, key=len)
    tail = invariant_bound(current)
    return None if tail is None else prefix + tail


def ida(state, best, seconds=1.0, node_limit=200000, max_depth=64):
    initial_lower = lower_bound(state)
    proved_lower = initial_lower
    expanded = 0
    deadline = perf_counter() + seconds
    interrupted = False
    solution = None
    path = []

    def dfs(current, remaining, seen):
        nonlocal expanded, interrupted, solution
        expanded += 1
        if expanded > node_limit or perf_counter() >= deadline:
            interrupted = True
            return False
        if not any(current):
            solution = path.copy()
            return True
        if lower_bound(current) > remaining:
            return False
        if seen.get(current, -1) >= remaining:
            return False
        seen[current] = remaining
        for after, move in successors(current):
            path.append(move)
            if dfs(after, remaining - 1, seen):
                return True
            path.pop()
            if interrupted:
                return False
        return False

    upper = len(best) if best is not None else max_depth + 1
    for bound in range(initial_lower, min(upper - 1, max_depth) + 1):
        if dfs(state, bound, {}):
            return {"moves": solution, "optimal": True, "lower": len(solution),
                    "expanded": expanded, "completed_depth": bound - 1}
        if interrupted:
            return {"moves": best, "optimal": False, "lower": proved_lower,
                    "expanded": expanded, "completed_depth": proved_lower - 1}
        proved_lower = bound + 1
    return {"moves": best, "optimal": best is not None and proved_lower >= upper,
            "lower": min(proved_lower, upper), "expanded": expanded,
            "completed_depth": proved_lower - 1}


def replay_original(raw, moves, q=3):
    total, n = sum(raw), len(raw)
    labelled = primitive(tuple(n * x - total for x in raw), sort=False)
    exact = list(map(Fraction, raw))
    operations = []
    for move in moves:
        unused, indices = set(range(n)), []
        for value in move:
            index = next(i for i in unused if labelled[i] == value)
            unused.remove(index)
            indices.append(index)
        mean = sum(exact[i] for i in indices) / q
        for i in indices:
            exact[i] = mean
        values = [q * x for x in labelled]
        for i in indices:
            values[i] = sum(move)
        labelled = primitive(tuple(values), sort=False)
        operations.append([i + 1 for i in indices])
    assert all(x == Fraction(total, n) for x in exact)
    return operations


def solve(raw, seconds=0.25, shortcuts=True):
    state = centered(raw)
    assert len(state) >= 7
    if not possible(state):
        return {"status": "impossible", "steps": None}
    successors.cache_clear()
    lower_bound.cache_clear()
    start = perf_counter()
    best = upper_bound(state, shortcuts=shortcuts)
    # Shortcuts are optional candidates: a locally attractive zero-sum block
    # can lead to a longer tail. Keep the original invariant bound as well.
    if shortcuts and any(state) and len(state) >= 11 and (best is None or len(best) > lower_bound(state)):
        alternative = invariant_bound(state)
        if alternative is not None and (best is None or len(alternative) < len(best)):
            best = alternative
    construct_seconds = perf_counter() - start
    initial_steps = len(best) if best is not None else None
    result = ida(state, best, seconds=seconds) if seconds else {
        "moves": best, "optimal": best is not None and len(best) == lower_bound(state),
        "lower": lower_bound(state), "expanded": 0,
        "completed_depth": lower_bound(state) - 1}
    elapsed = perf_counter() - start
    if result["moves"] is None:
        return {"status": "limit", "steps": None, "lowerBound": result["lower"]}
    operations = replay_original(raw, result["moves"])
    return {"status": "solved", "steps": len(operations), "initialSteps": initial_steps,
            "lowerBound": result["lower"], "optimal": result["optimal"],
            "expanded": result["expanded"], "completedDepth": result["completed_depth"],
            "operations": operations, "verified": True,
            "constructSeconds": construct_seconds, "solveSeconds": elapsed}


def breadth_first_distance(raw, q=3, max_depth=4):
    """Independent rational multiset BFS; no gcd normalization or lower bound."""
    target = Fraction(sum(raw), len(raw))
    root = tuple(sorted(map(Fraction, raw)))
    queue = deque([(root, 0)])
    seen = {root}
    while queue:
        state, depth = queue.popleft()
        if all(x == target for x in state):
            return depth
        if depth == max_depth:
            continue
        counts = Counter(state)
        for move in combinations_with_replacement(sorted(counts), q):
            if move[0] == move[-1] or any(counts[x] < f for x, f in Counter(move).items()):
                continue
            remaining = counts - Counter(move)
            after = tuple(sorted(list(remaining.elements()) + [sum(move) / q] * q))
            if after not in seen:
                seen.add(after)
                queue.append((after, depth + 1))
    return None
