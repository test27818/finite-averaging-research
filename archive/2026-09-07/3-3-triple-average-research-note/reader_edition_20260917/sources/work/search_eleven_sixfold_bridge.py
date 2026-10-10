"""Search symbolic bridges from a sixfold state to the B_11 (7,3,1) core."""

from collections import Counter, deque
from fractions import Fraction as F
from itertools import combinations
from math import gcd


Coeff = tuple[F, F, F, F, F]
State = tuple[Coeff, ...]


def add(values):
    return tuple(sum((value[index] for value in values), F(0))
                 for index in range(5))


def mean(values):
    total = add(values)
    return tuple(value / 3 for value in total)


def step(state: State, selected):
    average = mean([state[index] for index in selected])
    result = list(state)
    for index in selected:
        result[index] = average
    return tuple(sorted(result))


def choices(state):
    seen = set()
    for selected in combinations(range(len(state)), 3):
        signature = tuple(sorted(state[index] for index in selected))
        if signature in seen or len(set(signature)) == 1:
            continue
        seen.add(signature)
        yield selected, signature


def initial_state():
    # Six copies of u and five exceptions a,b,c,d,e, with
    # e=-6u-a-b-c-d so that the total sum is zero.
    u = (F(1), F(0), F(0), F(0), F(0))
    a = (F(0), F(1), F(0), F(0), F(0))
    b = (F(0), F(0), F(1), F(0), F(0))
    c = (F(0), F(0), F(0), F(1), F(0))
    d = (F(0), F(0), F(0), F(0), F(1))
    e = (F(-6), F(-1), F(-1), F(-1), F(-1))
    return tuple(sorted([u] * 6 + [a, b, c, d, e]))


def target_parameters(state):
    counts = Counter(state)
    if sorted(counts.values()) != [1, 3, 7]:
        return None
    background = next(value for value, count in counts.items() if count == 7)
    triple = next(value for value, count in counts.items() if count == 3)
    singleton = next(value for value, count in counts.items() if count == 1)
    assert all(singleton[index] == -7 * background[index] - 3 * triple[index]
               for index in range(5)), (background, triple, singleton)
    return background, triple, singleton


def primitive_form(form):
    denominator = 1
    for value in form:
        denominator = denominator * value.denominator // gcd(
            denominator, value.denominator
        )
    integers = [int(value * denominator) for value in form]
    divisor = gcd(*(abs(value) for value in integers))
    integers = tuple(value // divisor for value in integers)
    first = next(value for value in integers if value)
    return tuple(-value for value in integers) if first < 0 else integers


def search(max_depth=7):
    start = initial_state()
    queue = deque([(start, ())])
    seen = {start}
    found = {}
    levels = Counter({0: 1})
    while queue:
        state, path = queue.popleft()
        if path:
            parameters = target_parameters(state)
            if parameters is not None:
                background, triple, singleton = parameters
                difference = tuple(background[index] - triple[index]
                                  for index in range(5))
                key = (background, triple)
                found.setdefault(key, (background, triple, singleton,
                                       primitive_form(difference), path))
        if len(path) == max_depth:
            continue
        for selected, selected_values in choices(state):
            nxt = step(state, selected)
            if nxt in seen:
                continue
            seen.add(nxt)
            levels[len(path) + 1] += 1
            queue.append((nxt, path + (selected_values,)))
    print("levels", dict(levels), "states", len(seen),
          "generic B11 returns", len(found))
    for key, data in sorted(found.items(), key=lambda item: (len(item[1][-1]), item[1][3])):
        background, triple, singleton, difference, path = data
        print("depth", len(path), "difference", difference)
        print(" background", background)
        print(" triple", triple)
        print(" singleton", singleton)
        print(" path", path)
    return found


def beam_search(max_depth=10, width=20000):
    """Heuristic search retaining states with the most concentrated multiplicities."""
    start = initial_state()
    frontier = [(start, ())]
    seen = {start}

    def score(state):
        counts = sorted(Counter(state).values(), reverse=True)
        # A generic target has [7,3,1]; prioritize a large block, then a
        # triple, while mildly penalizing too many distinct values.
        padded = counts + [0] * 3
        return (
            8 * min(padded[0], 7)
            + 4 * min(padded[1], 3)
            + min(padded[2], 1)
            - len(counts),
            padded[0], padded[1], padded[2], -len(counts),
        )

    for depth in range(1, max_depth + 1):
        candidates = []
        for state, path in frontier:
            for selected, selected_values in choices(state):
                nxt = step(state, selected)
                if nxt in seen:
                    continue
                seen.add(nxt)
                new_path = path + (selected_values,)
                if target_parameters(nxt) is not None:
                    print("BEAM FOUND depth", depth, "path", new_path)
                    return nxt, new_path
                candidates.append((score(nxt), nxt, new_path))
        candidates.sort(reverse=True, key=lambda item: item[0])
        frontier = [(state, path) for _, state, path in candidates[:width]]
        print("beam depth", depth, "generated", len(candidates),
              "frontier", len(frontier), "seen", len(seen),
              "best", frontier[0][0] if frontier else None)
        if not frontier:
            break
    return None


def after_mixed_first_step():
    """State after averaging u,a,b; useful when all five exceptions share a residue."""
    u = (F(1), F(0), F(0), F(0), F(0))
    a = (F(0), F(1), F(0), F(0), F(0))
    b = (F(0), F(0), F(1), F(0), F(0))
    c = (F(0), F(0), F(0), F(1), F(0))
    d = (F(0), F(0), F(0), F(0), F(1))
    e = (F(-6), F(-1), F(-1), F(-1), F(-1))
    q = mean((u, a, b))
    return tuple(sorted([u] * 5 + [q] * 3 + [c, d, e]))


def beam_search_mixed(max_depth=8, width=20000):
    start = after_mixed_first_step()
    frontier = [(start, ())]
    seen = {start}

    def score(state):
        counts = sorted(Counter(state).values(), reverse=True)
        padded = counts + [0] * 3
        return (8 * min(padded[0], 7) + 4 * min(padded[1], 3)
                + min(padded[2], 1) - len(counts),
                padded[0], padded[1], padded[2], -len(counts))

    for depth in range(1, max_depth + 1):
        candidates = []
        for state, path in frontier:
            for selected, selected_values in choices(state):
                nxt = step(state, selected)
                if nxt in seen:
                    continue
                seen.add(nxt)
                new_path = path + (selected_values,)
                if target_parameters(nxt) is not None:
                    print("MIXED BEAM FOUND depth", depth,
                          "path", new_path)
                    return nxt, new_path
                candidates.append((score(nxt), nxt, new_path))
        candidates.sort(reverse=True, key=lambda item: item[0])
        frontier = [(state, path) for _, state, path in candidates[:width]]
        print("mixed beam depth", depth, "generated", len(candidates),
              "frontier", len(frontier), "seen", len(seen),
              "best", frontier[0][0] if frontier else None)
        if not frontier:
            break
    return None


if __name__ == "__main__":
    search()
