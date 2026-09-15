"""Greedy diagnostics for zero-sum triples in B_p count states."""

from argparse import ArgumentParser
from concurrent.futures import ProcessPoolExecutor
from fractions import Fraction as F
from itertools import combinations_with_replacement
import os

from explore_bcore_zero_triple import (
    has_zero_sum_triple,
    initial,
    legal_case,
    step,
    triples,
)


def score(selected, output, mode):
    total = sum(selected)
    spread = sum((left - right) ** 2
                 for index, left in enumerate(selected)
                 for right in selected[index + 1:])
    scale = sum(abs(value) for value in selected) or 1
    if mode == "sum":
        return abs(total), -spread, len(output)
    if mode == "relative":
        return F(abs(total), scale), -spread, len(output)
    if mode == "energy":
        return -spread, abs(total), len(output)
    if mode == "types":
        return len(output), abs(total), -spread
    raise ValueError(mode)


def inspect(case):
    prime, u, v, steps, mode = case
    state = initial(prime, u, v)
    seen = {state}
    for level in range(steps + 1):
        terminal = has_zero_sum_triple(state)
        if terminal is not None:
            return prime, v, mode, True, level, terminal, len(seen), len(state)
        candidates = []
        for selected in triples(state):
            output = step(state, selected)
            if output not in seen:
                candidates.append((score(selected, output, mode), output))
        if not candidates:
            return prime, v, mode, False, level, "cycle", len(seen), len(state)
        _, state = min(candidates)
        seen.add(state)
    return prime, v, mode, False, steps, "limit", len(seen), len(state)


def main():
    parser = ArgumentParser()
    parser.add_argument("--prime", type=int, action="append", default=None)
    parser.add_argument("--v-min", type=int, default=-100)
    parser.add_argument("--v-max", type=int, default=100)
    parser.add_argument("--steps", type=int, default=100)
    parser.add_argument("--jobs", type=int, default=os.cpu_count() or 1)
    args = parser.parse_args()
    primes = tuple(args.prime or (71, 83, 101, 149))
    modes = ("sum", "relative", "energy", "types")
    cases = tuple((prime, 1, value, args.steps, mode)
                  for prime in primes
                  for value in range(args.v_min, args.v_max + 1)
                  if legal_case(prime, 1, value)
                  for mode in modes)
    workers = min(args.jobs, len(cases))
    print("B-core greedy cases", len(cases), "workers", workers,
          "steps", args.steps, flush=True)
    with ProcessPoolExecutor(max_workers=workers) as executor:
        results = list(executor.map(inspect, cases,
                                    chunksize=max(1, len(cases) // (8 * workers))))
    for prime in primes:
        prime_results = [result for result in results if result[0] == prime]
        parameter_count = len(prime_results) // len(modes)
        for mode in modes:
            selected = [result for result in prime_results if result[2] == mode]
            hits = [result for result in selected if result[3]]
            failures = [result[1] for result in selected if not result[3]]
            maximum = max((result[4] for result in hits), default=None)
            print("prime", prime, "mode", mode, "covered", len(hits), "/",
                  parameter_count, "max-step", maximum,
                  "failure-sample", failures[:20], flush=True)


if __name__ == "__main__":
    main()
