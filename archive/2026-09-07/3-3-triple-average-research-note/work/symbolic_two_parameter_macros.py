"""Search generic linear averaging macros for the B_7 and B_8 families."""

from collections import Counter, deque
from fractions import Fraction as F
from itertools import combinations


Coeff = tuple[F, F]
State = tuple[Coeff, ...]


def add(values):
    return tuple(sum((value[j] for value in values), F(0)) for j in (0, 1))


def mean(values):
    total = add(values)
    return total[0] / 3, total[1] / 3


def step(state: State, selected):
    average = mean([state[i] for i in selected])
    result = list(state)
    for i in selected:
        result[i] = average
    return tuple(sorted(result))


def choices(state):
    seen = set()
    for selected in combinations(range(len(state)), 3):
        signature = tuple(sorted(state[i] for i in selected))
        if signature in seen:
            continue
        seen.add(signature)
        if len(set(signature)) == 1:
            continue
        yield selected, signature


def b_state(n):
    u = (F(1), F(0))
    v = (F(0), F(1))
    w = (F(-(n - 4)), F(-3))
    return tuple(sorted([u] * (n - 4) + [v] * 3 + [w]))


def b_parameters(n, state):
    counts = Counter(state)
    u_values = [value for value, count in counts.items() if count == n - 4]
    v_values = [value for value, count in counts.items() if count == 3]
    if n == 7:
        triple_values = [value for value, count in counts.items() if count == 3]
        if len(triple_values) != 2 or len(counts) != 3:
            return []
        return [(triple_values[0], triple_values[1]), (triple_values[1], triple_values[0])]
    if len(u_values) == 1 and len(v_values) == 1 and len(counts) == 3:
        return [(u_values[0], v_values[0])]
    return []


def search(n, max_depth):
    start = b_state(n)
    queue = deque([(start, ())])
    seen = {start}
    found = []
    while queue:
        state, path = queue.popleft()
        if path:
            for parameters in b_parameters(n, state):
                found.append((len(path), parameters, path))
        if len(path) == max_depth:
            continue
        for selected, signature in choices(state):
            nxt = step(state, selected)
            if nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, path + (signature,)))
    print('n', n, 'states', len(seen), 'returns', len(found))
    for depth, parameters, path in found[:40]:
        print('depth', depth, 'parameters', parameters, 'path', path)


if __name__ == '__main__':
    search(7, 5)
    search(8, 5)
