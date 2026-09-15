"""Exact BFS from B_91(1,-3), looking for zero-sum 27/81 blocks."""

from collections import Counter, deque
from fractions import Fraction as F
from itertools import combinations_with_replacement
from math import gcd


def signatures(state):
    values = tuple(state)
    for selected in combinations_with_replacement(values, 3):
        need = Counter(selected)
        if len(need) == 1 or any(state[value] < count for value, count in need.items()):
            continue
        yield selected


def step(state, selected):
    result = state.copy()
    for value in selected:
        result[value] -= 1
        if result[value] == 0:
            del result[value]
    result[sum(selected, F(0)) / 3] += 3
    return +result


def key(state):
    return tuple(sorted(state.items()))


def _complement_witness(state, witness):
    selected = Counter(dict(witness))
    return tuple(
        (value, multiplicity - selected[value])
        for value, multiplicity in state.items()
        if multiplicity > selected[value]
    )


def _witness_for_scaled(values, target_size):
    """Recover one witness after the cheaper existence pass succeeds."""
    table = {(0, 0): ()}
    for value, multiplicity, scaled_value in values:
        following = dict(table)
        for (used, total), witness in table.items():
            maximum_count = min(multiplicity, target_size - used)
            for count in range(1, maximum_count + 1):
                following.setdefault(
                    (used + count, total + count * scaled_value),
                    witness + ((value, count),),
                )
        table = following
    return table.get((target_size, 0))


def subset_counts_any(state, target_sizes):
    """Find the first requested zero-sum subset using one integer DP.

    All values have rational denominators, so multiplying by their common
    denominator preserves zero sums.  Targets larger than half the state are
    searched through their zero-sum complements; the whole state has sum 0.
    """
    total_size = sum(state.values())
    assert sum(value * count for value, count in state.items()) == 0
    requests = []
    for target_size in target_sizes:
        if not 0 <= target_size <= total_size:
            continue
        complement = target_size > total_size - target_size
        effective_size = total_size - target_size if complement else target_size
        requests.append((target_size, effective_size, complement))
    if not requests:
        return None

    common_denominator = 1
    for value in state:
        common_denominator = (
            common_denominator * value.denominator
            // gcd(common_denominator, value.denominator)
        )
    values = [
        (value,
         multiplicity,
         value.numerator * (common_denominator // value.denominator))
        for value, multiplicity in state.items()
    ]
    # Remove a common content before hashing sums.  This is an exact change
    # of scale and is often substantial after several averaging steps.
    content = gcd(*(abs(scaled_value) for _, _, scaled_value in values))
    if content > 1:
        values = [
            (value, multiplicity, scaled_value // content)
            for value, multiplicity, scaled_value in values
        ]
    maximum_size = max(effective_size for _, effective_size, _ in requests)

    # First run an existence-only DP.  Most BFS states are nonterminal, so
    # retaining a witness tuple for every partial sum is wasted allocation.
    # Cardinality layers also avoid the older two-component tuple key.
    layers = [set() for _ in range(maximum_size + 1)]
    layers[0].add(0)
    for value, multiplicity, scaled_value in values:
        for used in range(maximum_size, -1, -1):
            if not layers[used]:
                continue
            maximum_count = min(multiplicity, maximum_size - used)
            for count in range(1, maximum_count + 1):
                target = layers[used + count]
                delta = count * scaled_value
                target.update(total + delta for total in layers[used])
    for target_size, effective_size, complement in requests:
        if 0 in layers[effective_size]:
            found = _witness_for_scaled(values, effective_size)
            assert found is not None
            if complement:
                found = _complement_witness(state, found)
            return target_size, found
    return None


def subset_counts(state, target_size):
    found = subset_counts_any(state, (target_size,))
    return None if found is None else found[1]


def search(depth):
    start = Counter({F(1): 81, F(-3): 9, F(-54): 1})
    assert sum(value * count for value, count in start.items()) == 0
    queue = deque([(start, ())])
    seen = {key(start)}
    inspected = 0
    while queue:
        state, path = queue.popleft()
        inspected += 1
        if path:
            terminal = subset_counts_any(state, (81, 27))
            if terminal is not None:
                size, witness = terminal
                print("FOUND depth", len(path), "block", size)
                print("path", path)
                print("witness", witness)
                print("state", state)
                return path, witness
        if len(path) >= depth:
            continue
        for selected in signatures(state):
            following = step(state, selected)
            identifier = key(following)
            if identifier not in seen:
                seen.add(identifier)
                queue.append((following, path + (selected,)))
        if inspected % 10000 == 0:
            print("inspected", inspected, "seen", len(seen), "queue", len(queue), flush=True)
    print("NOT FOUND depth", depth, "states", len(seen))
    return None


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--depth", type=int, default=5)
    search(parser.parse_args().depth)
