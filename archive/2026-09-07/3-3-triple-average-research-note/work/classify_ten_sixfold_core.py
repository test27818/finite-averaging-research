"""Classify local obstructions around a sixfold value in dimension ten."""

from collections import Counter
from itertools import combinations, combinations_with_replacement


def subset_is_residue_nonconstant(values, subset):
    return len({values[index] for index in subset}) > 1 or values[subset[0]] != 0


def locally_safe_subset(values, subset):
    if sum(values[index] for index in subset) % 3:
        return False
    if not subset_is_residue_nonconstant(values, subset):
        return False
    remaining = [values[index] for index in range(4) if index not in subset]
    return (
        any(value % 2 for value in remaining)
        and any(value % 5 for value in remaining)
    )


def safe_subsets(values):
    # Fill a subset of k exceptions with 3-k copies of the sixfold
    # background value.  There are enough background copies for k=1,2,3.
    return tuple(
        subset
        for size in (1, 2, 3)
        for subset in combinations(range(4), size)
        if locally_safe_subset(values, subset)
    )


def direct_b10_legal(values, singleton):
    """Averaging the other three exceptions, with no p-adic cancellation."""
    value = values[singleton]
    return value % 2 != 0 and value % 5 != 0


def classify():
    candidates = []
    all_patterns = 0
    for values in combinations_with_replacement(range(30), 4):
        if not any(value % 2 for value in values):
            continue
        if not any(value % 5 for value in values):
            continue
        all_patterns += 1
        safe = safe_subsets(values)
        if safe:
            continue
        candidates.append(values)

    by_witness = Counter()
    for values in candidates:
        parity = tuple(index for index, value in enumerate(values) if value % 2)
        five = tuple(index for index, value in enumerate(values) if value % 5)
        by_witness[(len(parity), len(five), len(set(parity) & set(five)))] += 1

    print("patterns", all_patterns, "without local safe subset", len(candidates))
    print("witness-count signatures")
    for signature, count in sorted(by_witness.items()):
        print(" ", signature, count)
    print("examples")
    for values in candidates[:100]:
        print(" ", values, "counts", Counter(values),
              "direct", [i for i in range(4) if direct_b10_legal(values, i)])
    return candidates


if __name__ == "__main__":
    classify()
