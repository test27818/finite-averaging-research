"""Numerical comparison for p=13 at n=26=2p and n=27=2p+1.

n=26 uses exact integer reachability (the p <= n <= 2p denominator lemma).
n=27 uses an exact meet-in-the-middle zero-subset certificate followed by
the general 2p+1 zero-trigger tail.  Both use the same G=1 raw sampling model.
"""

from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache
from itertools import combinations_with_replacement
import json
from math import gcd
from pathlib import Path
from random import Random
from time import perf_counter
from fractions import Fraction

P = 13


def sign_canonical(values):
    values = tuple(sorted(values))
    return min(values, tuple(sorted(-x for x in values)))


def primitive(values):
    g = gcd(*(abs(x) for x in values))
    if g > 1:
        values = tuple(x // g for x in values)
    return sign_canonical(values)


def difference_gcd(values):
    return gcd(*(values[i] - values[0] for i in range(1, len(values))))


def legal(values):
    # n=27 is a power of 3, so its candidate condition is G=1.
    return bool(any(values)) and difference_gcd(values) == 1


def legal_26(values):
    # At n=26, the candidate condition is G in {1,13}.
    if not any(values):
        return False
    g = difference_gcd(values)
    while g % P == 0:
        g //= P
    return g == 1


def energy(values):
    return sum(x * x for x in values)


def apply(values, move, p=P):
    counts = Counter(values)
    used = Counter(move)
    assert len(move) == p and all(counts[x] >= f for x, f in used.items())
    total = sum(move)
    assert total % p == 0
    rest = list((counts - used).elements())
    rest.extend([total // p] * p)
    # Preserve the physical sign and scale of the state.  Global sign is a
    # symmetry for search, but canonicalizing after one operation would make
    # a stored value-multiset path refer to the wrong signs on the next step.
    result = tuple(sorted(rest))
    assert energy(result) < energy(values)
    return result


@lru_cache(maxsize=None)
def successors_26(values):
    counts = Counter(values)
    distinct = tuple(sorted(counts))
    picked, result, seen = [], [], set()

    def visit(index, left):
        if index == len(distinct):
            if left:
                return
            move = tuple(picked)
            if len(set(move)) == 1 or sum(move) % P:
                return
            after = apply(values, move)
            if after != values and after not in seen:
                seen.add(after)
                result.append((after, move))
            return
        value = distinct[index]
        for amount in range(min(counts[value], left) + 1):
            picked.extend([value] * amount)
            visit(index + 1, left - amount)
            if amount:
                del picked[-amount:]

    visit(0, P)
    result.sort(key=lambda item: (energy(item[0]), item[0]))
    return tuple(result)


@lru_cache(maxsize=None)
def reachable_26(values):
    if not any(values):
        return True
    return any(reachable_26(after) for after, _ in successors_26(values))


@lru_cache(maxsize=None)
def shortest_26(values):
    if not any(values):
        return 0
    distances = [shortest_26(after) for after, _ in successors_26(values)]
    distances = [d for d in distances if d is not None]
    return None if not distances else 1 + min(distances)


def enumerate_26(bound):
    seen = set()
    for values in combinations_with_replacement(range(-bound, bound + 1), 26):
        if sum(values) or not any(values):
            continue
        state = primitive(values)
        if state in seen or not legal_26(state):
            continue
        seen.add(state)
        yield state


def exact_26(bound):
    started = perf_counter()
    states = list(enumerate_26(bound))
    reachable_26.cache_clear(); shortest_26.cache_clear()
    solvable, distances, bad = 0, Counter(), []
    for state in states:
        if reachable_26(state):
            solvable += 1
            d = shortest_26(state)
            assert d is not None
            distances[d] += 1
        else:
            bad.append(state)
    return {
        "p": P, "n": 26, "bound": bound, "states": len(states),
        "solvable": solvable, "unsolvable": len(bad),
        "ratio": len(bad) / len(states) if states else None,
        "distance_distribution": dict(sorted(distances.items())),
        "examples": [list(x) for x in bad[:20]],
        "seconds": perf_counter() - started,
        "sampling_model": "sorted primitive zero-sum states in [-bound,bound], conditioned on G=13^k",
    }


def raw_26(rng, bound):
    values = [rng.randint(-bound, bound) for _ in range(25)]
    values.append(-sum(values))
    return primitive(tuple(values))


def zero_subset_26(values):
    """Exact 13-subset sum-zero witness for a two-step certificate."""
    return subset_sum(values, P, 0)


def verify_two_step_26(values, move):
    assert move is not None and len(move) == P and sum(move) == 0
    remaining = list(values)
    for x in move:
        remaining.remove(x)
    assert len(remaining) == P and sum(remaining) == 0
    state = apply(values, move)
    state = apply(state, tuple(remaining))
    assert not any(state)


def random_26_zero_certificate(bound, samples, seed):
    rng = Random(seed); accepted = rejected = certified = 0
    started = perf_counter()
    while accepted < samples:
        state = raw_26(rng, bound)
        if not legal_26(state):
            rejected += 1; continue
        accepted += 1
        move = zero_subset_26(state)
        if move is not None:
            verify_two_step_26(state, move)
            certified += 1
    return {
        "p": P, "n": 26, "bound": bound, "samples": samples,
        "accepted": accepted, "rejected": rejected, "certified": certified,
        "unknown": samples - certified, "certified_ratio": certified / samples,
        "certificate": "two disjoint zero-sum 13-subsets, hence two physical averages",
        "seconds": perf_counter() - started,
        "sampling_model": "26 independent uniform integers in [-bound,bound], final coordinate closes zero sum, primitive-normalized, conditioned on G=13^k",
    }


def random_26(bound, samples, seed):
    rng = Random(seed); accepted = unsolvable = rejected = 0
    distances = Counter(); examples = []; started = perf_counter()
    while accepted < samples:
        state = raw_26(rng, bound)
        if not legal_26(state):
            rejected += 1; continue
        accepted += 1
        if not reachable_26(state):
            unsolvable += 1
            if len(examples) < 10:
                examples.append(list(state))
        else:
            d = shortest_26(state)
            assert d is not None
            distances[d] += 1
    return {
        "p": P, "n": 26, "bound": bound, "samples": samples,
        "accepted": accepted, "rejected": rejected,
        "solvable": samples - unsolvable, "unsolvable": unsolvable,
        "ratio": unsolvable / samples,
        "distance_distribution": dict(sorted(distances.items())),
        "seconds": perf_counter() - started, "examples": examples,
        "sampling_model": "26 independent uniform integers in [-bound,bound], final coordinate closes zero sum, primitive-normalized, conditioned on G=1",
    }


def subset_sum(values, k, target=0):
    """Exact meet-in-the-middle k-subset sum witness."""
    split = len(values) // 2
    left, right = values[:split], values[split:]
    left_map = {}
    for mask in range(1 << len(left)):
        size = mask.bit_count()
        if size > k:
            continue
        total = sum(left[i] for i in range(len(left)) if mask >> i & 1)
        left_map.setdefault((size, total), mask)
    for mask in range(1 << len(right)):
        size = mask.bit_count()
        if size > k:
            continue
        total = sum(right[i] for i in range(len(right)) if mask >> i & 1)
        needed = (k - size, target - total)
        if needed in left_map:
            lm = left_map[needed]
            return tuple(left[i] for i in range(len(left)) if lm >> i & 1) + tuple(
                right[i] for i in range(len(right)) if mask >> i & 1)
    return None


def subset_mod(values, k, p=P, require_nonconstant=True):
    """Find a nonconstant k-subset whose sum is 0 mod p."""
    split = len(values) // 2
    left, right = values[:split], values[split:]
    left_map = {}
    for mask in range(1 << len(left)):
        size = mask.bit_count()
        if size > k:
            continue
        total = sum(left[i] for i in range(len(left)) if mask >> i & 1) % p
        left_map.setdefault((size, total), mask)
    for mask in range(1 << len(right)):
        size = mask.bit_count()
        if size > k:
            continue
        total = sum(right[i] for i in range(len(right)) if mask >> i & 1) % p
        lm = left_map.get((k - size, (-total) % p))
        if lm is None:
            continue
        move = tuple(left[i] for i in range(len(left)) if lm >> i & 1) + tuple(
            right[i] for i in range(len(right)) if mask >> i & 1)
        if not require_nonconstant or len(set(move)) > 1:
            return move
    return None


def tail_27(values, zero_move=None):
    state = values
    path = []
    if zero_move is not None:
        state = apply(state, zero_move)
        path.append(zero_move)
    assert 0 in state
    if not any(state):
        return path
    zero_index = state.index(0)
    other = [i for i in range(27) if i != zero_index]
    # EGZ guarantees a 13-subset with sum divisible by 13; exact zero is not
    # required.  The complement is also divisible by 13 because the total is 0.
    witness = subset_mod(tuple(state[i] for i in other), P, P, require_nonconstant=False)
    assert witness is not None
    remaining = [state[i] for i in other]
    for x in witness:
        remaining.remove(x)
    move1, move2 = tuple(witness), tuple(remaining)
    if len(set(move1)) > 1:
        state = apply(state, move1); path.append(move1)
    if len(set(move2)) > 1:
        state = apply(state, move2); path.append(move2)
    if not any(state):
        return path
    for count in ((P - 1)//2, (P - 1)//2, 1):
        plus = [x for x in state if x > 0]
        minus = [x for x in state if x < 0]
        zeros = [x for x in state if x == 0]
        move = tuple(plus[:count] + minus[:count] + zeros[:P - 2*count])
        assert len(move) == P and sum(move) == 0
        state = apply(state, move); path.append(move)
    assert not any(state)
    return path


def solve_27(values):
    if 0 in values:
        return tail_27(values), "initial_zero"
    direct = subset_sum(values, P, 0)
    if direct is not None:
        return tail_27(values, direct), "initial_zero_sum_subset"
    move = subset_mod(values, P)
    if move is not None:
        after = apply(values, move)
        zero = subset_sum(after, P, 0)
        if zero is not None:
            return [move] + tail_27(after, zero), "one_integer_preprocessing"
    return None, "unknown"


def verify(values, path):
    state = tuple(Fraction(x) for x in values)
    for move in path:
        available = Counter(state); used = Counter(Fraction(x) for x in move)
        assert len(move) == P and len(set(move)) > 1
        assert all(available[x] >= f for x, f in used.items())
        mean = sum((Fraction(x) for x in move), Fraction(0)) / P
        rest = list((available - used).elements())
        state = tuple(sorted(rest + [mean] * P))
        assert sum(state) == sum(Fraction(x) for x in values)
    assert all(x == state[0] for x in state)


def raw_27(rng, bound):
    values = [rng.randint(-bound, bound) for _ in range(26)]
    values.append(-sum(values))
    return primitive(tuple(values))


def random_27(bound, samples, seed):
    rng = Random(seed); accepted = solved = rejected = 0
    modes, lengths = Counter(), Counter(); started = perf_counter()
    while accepted < samples:
        state = raw_27(rng, bound)
        if not legal(state):
            rejected += 1; continue
        accepted += 1
        path, mode = solve_27(state)
        if path is None:
            continue
        verify(state, path); solved += 1
        modes[mode] += 1; lengths[len(path)] += 1
    return {
        "p": P, "n": 27, "bound": bound, "samples": samples,
        "accepted": accepted, "rejected": rejected, "solved": solved,
        "unknown": samples - solved, "solved_ratio": solved / samples,
        "certificate_modes": dict(sorted(modes.items())),
        "path_lengths": dict(sorted(lengths.items())),
        "seconds": perf_counter() - started,
        "sampling_model": "27 independent uniform integers in [-bound,bound], final coordinate closes zero sum, primitive-normalized, conditioned on G=1",
    }


def main(args):
    result = {"exact_n26": [exact_26(b) for b in args.exact_bounds],
              "random_n26_certificate": [random_26_zero_certificate(b, args.samples, args.seed + i)
                                          for i, b in enumerate(args.random_bounds)],
              "random_n27": [random_27(b, args.samples, args.seed + i)
                             for i, b in enumerate(args.random_bounds)]}
    for row in result["exact_n26"]:
        print("n26", json.dumps(row, ensure_ascii=False), flush=True)
    for row in result["random_n26_certificate"]:
        print("n26-random", json.dumps(row, ensure_ascii=False), flush=True)
    for row in result["random_n27"]:
        print("n27", json.dumps(row, ensure_ascii=False), flush=True)
    Path(args.output).write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("p13 boundary experiment: PASS", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--exact-bounds", nargs="+", type=int, default=[1, 2])
    parser.add_argument("--random-bounds", nargs="+", type=int, default=[5, 10, 20])
    parser.add_argument("--samples", type=int, default=100)
    parser.add_argument("--seed", type=int, default=13132627)
    parser.add_argument("--output", default="work/p13_boundary_experiment.json")
    main(parser.parse_args())
