"""Classify residue obstructions to a safe integer move for n=10.

We fix the majority parity to be even and the majority mod-5 class to be
zero.  Translation by 15 and by a multiple of 6 justifies these two
normalizations.  The remaining search is over multisets modulo 30.
"""

from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement


RESIDUES = tuple(range(30))
MAIN_FIVE = tuple(value for value in RESIDUES if value % 5 == 0)
OUTSIDE_FIVE = tuple(value for value in RESIDUES if value % 5 != 0)


def weak_compositions(total, parts, prefix=()):
    if parts == 1:
        yield prefix + (total,)
        return
    for first in range(total + 1):
        yield from weak_compositions(total - first, parts - 1, prefix + (first,))


def state_from_counts(main_counts, outsiders):
    state = []
    for residue, count in zip(MAIN_FIVE, main_counts):
        state.extend([residue] * count)
    state.extend(outsiders)
    return tuple(sorted(state))


def residue_triples(state):
    counts = Counter(state)
    values = tuple(counts)
    for triple in combinations_with_replacement(values, 3):
        selected = Counter(triple)
        if any(selected[value] > counts[value] for value in selected):
            continue
        if sum(triple) % 3:
            continue
        yield triple


def complement_is_mixed(state, triple, modulus):
    remaining = Counter(state)
    remaining.subtract(triple)
    residues = {
        value % modulus
        for value, count in remaining.items()
        if count > 0
    }
    return len(residues) > 1


def safe_at_residue_level(state, triple):
    return (
        len(set(triple)) > 1
        and complement_is_mixed(state, triple, 2)
        and complement_is_mixed(state, triple, 5)
    )


def forced_equal_classes(state):
    """Residue classes whose nonconstant internal triples would be safe."""
    counts = Counter(state)
    forced = []
    for value, count in counts.items():
        if count < 3:
            continue
        triple = (value, value, value)
        if (complement_is_mixed(state, triple, 2)
                and complement_is_mixed(state, triple, 5)):
            forced.append((value, count))
    return tuple(sorted(forced))


def canonical_signature(state):
    counts = Counter(state)
    cells = defaultdict(list)
    for value, count in counts.items():
        cells[(value % 2, value % 5)].append((value % 3, count))
    return tuple(
        (cell, tuple(sorted(entries)))
        for cell, entries in sorted(cells.items())
    )


def classify():
    candidates = []
    tested = 0
    # The mod-5 majority has size 7, 8, or 9.  Odd positions are the
    # parity minority and have total multiplicity exactly two.
    for outside_count in (1, 2, 3):
        main_size = 10 - outside_count
        for outsiders in combinations_with_replacement(OUTSIDE_FIVE, outside_count):
            for main_counts in weak_compositions(main_size, len(MAIN_FIVE)):
                state = state_from_counts(main_counts, outsiders)
                if sum(value % 2 for value in state) != 2:
                    continue
                if sum(state) % 30:
                    continue
                tested += 1
                if any(safe_at_residue_level(state, triple)
                       for triple in residue_triples(state)):
                    continue
                candidates.append(state)

    signatures = Counter(canonical_signature(state) for state in candidates)
    membership_signatures = Counter()
    core_sizes = Counter()
    for state in candidates:
        counts = Counter(state)
        # Odd positions form the parity minority after normalization.
        parity_exception = tuple(value for value in state if value % 2)
        five_exception = tuple(value for value in state if value % 5)
        intersection = sum(bool(value % 2 and value % 5) for value in state)
        core = tuple(value for value in state if value % 2 == 0 and value % 5 == 0)
        core_sizes[len(core)] += 1
        membership_signatures[(
            len(parity_exception), len(five_exception), intersection,
            tuple(sorted(Counter(value % 3 for value in core).items())),
            tuple(sorted(Counter(value % 3 for value in parity_exception).items())),
            tuple(sorted(Counter(value % 3 for value in five_exception).items())),
        )] += 1
    forced_six = sum(
        any(count >= 6 for _, count in forced_equal_classes(state))
        for state in candidates
    )
    assert candidates
    assert forced_six == len(candidates)
    print("tested", tested, "candidate residue multisets", len(candidates))
    print("signatures", len(signatures), "forced sixfold", forced_six)
    print("not immediately forced sixfold", len(candidates) - forced_six)
    print("core sizes", dict(sorted(core_sizes.items())))
    print("membership signatures", len(membership_signatures))
    for signature, count in sorted(membership_signatures.items()):
        print(" membership", signature, "count", count)
    for state in candidates[:80]:
        print(" state", state, "counts", sorted(Counter(state).items()),
              "forced", forced_equal_classes(state))
    return candidates, signatures


if __name__ == "__main__":
    classify()
