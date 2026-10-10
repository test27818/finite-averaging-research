"""Search short bridges from ten-point states to known solvable terminal sets."""

from collections import Counter, deque
from itertools import combinations
from math import gcd


def primitive(state):
    divisor = gcd(*(abs(value) for value in state))
    if divisor:
        state = tuple(value // divisor for value in state)
    state = tuple(sorted(state))
    negated = tuple(sorted(-value for value in state))
    return min(state, negated)


def arithmetic_good(state):
    state = primitive(state)
    if not any(state):
        return True
    divisor = gcd(*(value - state[0] for value in state))
    while divisor % 3 == 0:
        divisor //= 3
    return divisor == 1


def known_terminal(state):
    if 0 in state:
        return "zero coordinate"
    if not arithmetic_good(state):
        return None
    counts = sorted(Counter(state).values(), reverse=True)
    if len(counts) == 3 and counts[:2] == [6, 3]:
        return "B10"
    return None


def edges(state):
    signatures = set()
    for selected in combinations(range(10), 3):
        signature = tuple(sorted(state[index] for index in selected))
        if signature in signatures or len(set(signature)) == 1:
            continue
        signatures.add(signature)
        total = sum(signature)
        selected_set = set(selected)
        nxt = primitive(tuple(
            total if index in selected_set else 3 * value
            for index, value in enumerate(state)
        ))
        yield nxt, signature


def bridge(start, max_depth=8):
    start = primitive(start)
    queue = deque([start])
    parent = {start: None}
    edge = {}
    depth = {start: 0}
    level_counts = Counter({0: 1})
    while queue:
        state = queue.popleft()
        current_depth = depth[state]
        label = known_terminal(state)
        if label:
            path = []
            while parent[state] is not None:
                path.append((edge[state], state))
                state = parent[state]
            path.reverse()
            return label, path, level_counts, len(parent)
        if current_depth == max_depth:
            continue
        for nxt, signature in edges(state):
            if nxt in parent:
                continue
            parent[nxt] = state
            edge[nxt] = signature
            depth[nxt] = current_depth + 1
            level_counts[current_depth + 1] += 1
            queue.append(nxt)
    return None, [], level_counts, len(parent)


def main():
    examples = (
        (-75, 7, 7, 7, 7, 7, 7, 9, 12, 12),
        (-62, 3, 3, 3, 3, 3, 3, 3, 16, 25),
    )
    for example in examples:
        label, path, levels, seen = bridge(example)
        print("start", primitive(example), "target", label, "depth", len(path))
        print("levels", dict(levels), "seen", seen)
        for signature, state in path:
            print(" average", signature, "->", state)


if __name__ == "__main__":
    main()
