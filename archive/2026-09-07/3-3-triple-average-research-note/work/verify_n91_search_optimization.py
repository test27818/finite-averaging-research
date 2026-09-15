"""Regression checks for the exact n=91 subset-DP optimizations."""

from collections import Counter, deque
from fractions import Fraction as F
from math import gcd

from search_n91_missing_class import signatures, step, subset_counts_any


def reference_subset_counts(state, target_sizes):
    """The pre-optimization Fraction-keyed DP, kept as an oracle."""
    total_size = sum(state.values())
    requests = []
    for target_size in target_sizes:
        complement = target_size > total_size - target_size
        effective = total_size - target_size if complement else target_size
        requests.append((target_size, effective, complement))
    denominator = 1
    for value in state:
        denominator = denominator * value.denominator // gcd(
            denominator, value.denominator
        )
    values = [
        (value, multiplicity,
         value.numerator * (denominator // value.denominator))
        for value, multiplicity in state.items()
    ]
    maximum = max(effective for _, effective, _ in requests)
    table = {(0, 0): ()}
    for value, multiplicity, scaled in values:
        following = dict(table)
        for (used, total), witness in table.items():
            for count in range(1, min(multiplicity, maximum - used) + 1):
                following.setdefault(
                    (used + count, total + count * scaled),
                    witness + ((value, count),),
                )
        table = following
    for target_size, effective, complement in requests:
        witness = table.get((effective, 0))
        if witness is not None:
            return target_size, witness
    return None


def generated_states(limit=184):
    start = Counter({F(1): 81, F(-3): 9, F(-54): 1})
    queue = deque([start])
    seen = {tuple(sorted(start.items()))}
    while queue and len(seen) < limit:
        state = queue.popleft()
        yield state
        for selected in signatures(state):
            following = step(state, selected)
            identifier = tuple(sorted(following.items()))
            if identifier not in seen:
                seen.add(identifier)
                queue.append(following)


def verify():
    checked = 0
    for state in generated_states():
        reference = reference_subset_counts(state, (27, 81))
        optimized = subset_counts_any(state, (27, 81))
        assert (reference is None) == (optimized is None)
        if optimized is not None:
            size, witness = optimized
            assert size in (27, 81)
            assert sum(count for _, count in witness) == size
            assert sum(value * count for value, count in witness) == 0
            assert all(count <= state[value] for value, count in witness)
        checked += 1
    return checked


if __name__ == "__main__":
    print("n91 integer subset-DP equivalence: PASS", verify())
