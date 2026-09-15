"""Numerical evidence for 7-average at n=15.

This is a certificate-producing experiment, not a completeness claim.  It
keeps exact integer states while searching for a zero-sum 7-subset.  Once a
zero 7-subset exists, the explicit 2p+1 tail reduces the state to zero in
four further 7-averages (for p=7), so every reported path is independently
checkable.  Samples not solved within the integer search depth are unknown,
not counterexamples.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
import json
from math import gcd
from pathlib import Path
from random import Random
from time import perf_counter


P = 7
N = 15


def primitive(values: tuple[int, ...]) -> tuple[int, ...]:
    g = gcd(*(abs(x) for x in values))
    if g > 1:
        values = tuple(x // g for x in values)
    values = tuple(sorted(values))
    reflected = tuple(sorted(-x for x in values))
    return min(values, reflected)


def difference_gcd(values: tuple[int, ...]) -> int:
    return gcd(*(values[i] - values[0] for i in range(1, len(values))))


def legal(values: tuple[int, ...]) -> bool:
    """For n=15 and 7-average, G=1 is the candidate condition."""
    return bool(any(values)) and difference_gcd(values) == 1


def energy(values: tuple[int, ...]) -> int:
    return sum(x * x for x in values)


def apply(values: tuple[int, ...], move: tuple[int, ...]) -> tuple[int, ...]:
    assert len(move) == P
    counts = Counter(values)
    used = Counter(move)
    if any(counts[x] < f for x, f in used.items()):
        return None
    total = sum(move)
    if total % P:
        return None
    rest = list((counts - used).elements())
    rest.extend([total // P] * P)
    # Do not divide by a common gcd here: that would be an algebraic
    # normalization, not a physical seven-average operation.  Sorting only
    # forgets position labels; the verifier later replays value multiplicities.
    result = tuple(sorted(rest))
    return result


def value_patterns(values: tuple[int, ...], amount: int, predicate):
    counts = Counter(values)
    distinct = tuple(sorted(counts))
    picked: list[int] = []

    def visit(index: int, left: int):
        if index == len(distinct):
            if not left:
                move = tuple(picked)
                if predicate(move):
                    yield move
            return
        value = distinct[index]
        cap = min(counts[value], left)
        for take in range(cap + 1):
            picked.extend([value] * take)
            yield from visit(index + 1, left - take)
            if take:
                del picked[-take:]

    yield from visit(0, amount)


@lru_cache(maxsize=None)
def zero_moves(values: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(value_patterns(values, P,
                                lambda move: sum(move) == 0 and len(set(move)) > 1))


@lru_cache(maxsize=None)
def integer_moves(values: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(value_patterns(values, P,
                                lambda move: sum(move) % P == 0 and len(set(move)) > 1))


def tail_after_zero(values: tuple[int, ...], zero_move: tuple[int, ...] | None):
    """Return a 5-operation path from a state containing a zero 7-subset."""
    state = values
    path = []
    if zero_move is not None:
        state = apply(state, zero_move)
        path.append(zero_move)
    assert 0 in state
    if not any(state):
        return path

    zeros = [x for x in state if x == 0]
    nonzero = [x for x in state if x]
    assert len(nonzero) <= 2 * P and sum(nonzero) == 0
    # The first two operations average two disjoint 7-blocks while retaining
    # one zero.  This creates (a^7,(-a)^7,0).
    zero_index = state.index(0)
    other = [i for i in range(N) if i != zero_index]
    # EGZ on any 13 of these 14 entries guarantees a seven-subset whose sum
    # is divisible by 7.  Its complement is also divisible by 7.
    move1_indices = next(c for c in combinations(other, P)
                         if sum(state[i] for i in c) % P == 0)
    move1_set = set(move1_indices)
    move2_indices = tuple(i for i in other if i not in move1_set)
    move1 = tuple(state[i] for i in move1_indices)
    move2 = tuple(state[i] for i in move2_indices)
    assert len(move2) == P and sum(move2) % P == 0
    if len(set(move1)) > 1:
        state = apply(state, move1)
        path.append(move1)
    if len(set(move2)) > 1:
        state = apply(state, move2)
        path.append(move2)
    if not any(state):
        return path

    # At this point state is (a^7, -a^7, 0), up to ordering.  Three successive
    # mixed averages consume 3+3+1, then 3+3+1, then 1+1+5 entries.
    for positive_count in (3, 3, 1):
        plus = [x for x in state if x > 0]
        minus = [x for x in state if x < 0]
        zeros = [x for x in state if x == 0]
        move = tuple(plus[:positive_count] + minus[:positive_count]
                     + zeros[:P - 2 * positive_count])
        assert len(move) == P and sum(move) == 0
        state = apply(state, move)
        path.append(move)
    assert not any(state)
    return path


def solve_integer(values: tuple[int, ...], depth: int = 2):
    """Search for a zero 7-subset at depth <= depth, then use the tail."""
    if 0 in values:
        return tail_after_zero(values, None), 0
    direct = zero_moves(values)
    if direct:
        return tail_after_zero(values, direct[0]), 0

    frontier = [(values, ())]
    seen = {values}
    for level in range(1, depth + 1):
        following = []
        for state, prefix in frontier:
            for move in integer_moves(state):
                after = apply(state, move)
                if after == state or after in seen:
                    continue
                word = prefix + (move,)
                if zero_moves(after):
                    tail = tail_after_zero(after, zero_moves(after)[0])
                    return list(word) + tail, level
                seen.add(after)
                following.append((after, word))
        frontier = following
    return None, None


def certificate_mode(values: tuple[int, ...], found_depth: int | None) -> str:
    """Classify the successful entry mechanism for reporting."""
    if found_depth is None:
        return "unknown"
    if 0 in values:
        return "initial_zero_coordinate"
    if zero_moves(values):
        return "initial_zero_sum_7_subset"
    if found_depth >= 1:
        return "integer_preprocessing"
    return "other"


def verify(values: tuple[int, ...], path) -> tuple[bool, tuple[Fraction, ...]]:
    state = tuple(Fraction(x) for x in values)
    for move in path:
        assert len(move) == P
        available = Counter(state)
        used = Counter(Fraction(x) for x in move)
        assert all(available[x] >= f for x, f in used.items())
        assert len(set(move)) > 1
        mean = sum((Fraction(x) for x in move), Fraction(0)) / P
        assert mean.denominator > 0
        rest = list((available - used).elements())
        state = tuple(sorted(rest + [mean] * P))
        assert sum(state) == sum(Fraction(x) for x in values)
    assert all(x == state[0] for x in state)
    return True, state


def raw_instance(rng: Random, bound: int) -> tuple[int, ...]:
    values = [rng.randint(-bound, bound) for _ in range(N - 1)]
    values.append(-sum(values))
    return primitive(tuple(values))


def experiment(bound: int, samples: int, depth: int, seed: int):
    rng = Random(seed)
    accepted = rejected = solved = direct = 0
    depth_counts = Counter()
    mode_counts = Counter()
    lengths = Counter()
    examples = []
    started = perf_counter()
    while accepted < samples:
        values = raw_instance(rng, bound)
        if not legal(values):
            rejected += 1
            continue
        accepted += 1
        path, found_depth = solve_integer(values, depth)
        if path is not None:
            verify(values, path)
            solved += 1
            depth_counts[found_depth] += 1
            mode_counts[certificate_mode(values, found_depth)] += 1
            lengths[len(path)] += 1
            if len(examples) < 5:
                examples.append({"values": list(values), "depth": found_depth,
                                 "steps": len(path), "path": [list(m) for m in path]})
        if accepted % 100 == 0:
            print("n15 p7", bound, accepted, "solved", solved,
                  "unknown", accepted - solved, flush=True)
    return {
        "p": P, "n": N, "bound": bound, "samples": samples,
        "accepted": accepted, "rejected": rejected, "solved": solved,
        "unknown": samples - solved, "solved_ratio": solved / samples,
        "search_depth": depth, "found_depth_distribution": dict(sorted(depth_counts.items())),
        "certificate_mode_distribution": dict(sorted(mode_counts.items())),
        "path_length_distribution": dict(sorted(lengths.items())),
        "seconds": perf_counter() - started, "examples": examples,
        "sampling_model": "independent uniform integers in [-bound,bound], final coordinate closes the zero sum, primitive-normalized, conditioned on G=1",
    }


def main(args):
    reports = [experiment(bound, args.samples, args.depth, args.seed + i)
               for i, bound in enumerate(args.bounds)]
    for report in reports:
        print(json.dumps(report, ensure_ascii=False), flush=True)
    output = {"experiment": "seven-average n=15 zero-trigger integer search",
              "reports": reports,
              "warning": "unknown samples are not counterexamples; paths are exact certificates, failures are search-incomplete.",
              "formula": "For a true independent counterexample rate r, N >= log(0.05)/log(1-r) gives 95% probability of at least one hit."}
    Path(args.output).write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("seven-average n15 experiment: PASS", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--bounds", nargs="+", type=int, default=[3, 10, 50])
    parser.add_argument("--samples", type=int, default=200)
    parser.add_argument("--depth", type=int, default=2)
    parser.add_argument("--seed", type=int, default=7071515)
    parser.add_argument("--output", default="work/seven_average_n15_experiment.json")
    main(parser.parse_args())
