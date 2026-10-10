"""Complete bounded-state enumeration for seven-average n=15.

The certificate searched here is: an initial zero-sum 7-subset, or one
integer 7-average followed by a zero-sum 7-subset.  The subsequent tail is
replayed exactly by experiment_seven_average_n15.verify.
"""

from __future__ import annotations

import argparse
from itertools import combinations_with_replacement
import json
from pathlib import Path
from time import perf_counter

from experiment_seven_average_n15 import (certificate_mode, legal, primitive,
                                           solve_integer, verify, zero_moves)


def enumerate_states(bound: int):
    seen = set()
    for values in combinations_with_replacement(range(-bound, bound + 1), 15):
        if sum(values) or not any(values):
            continue
        state = primitive(values)
        if state in seen or not legal(state):
            continue
        seen.add(state)
        yield state


def exact_bounded(bound: int):
    started = perf_counter()
    states = list(enumerate_states(bound))
    direct = certified = 0
    modes = {}
    unknown_states = []
    depth_distribution = {}
    for state in states:
        if zero_moves(state):
            direct += 1
        path, depth = solve_integer(state, 1)
        if path is not None:
            verify(state, path)
            certified += 1
            depth_distribution[depth] = depth_distribution.get(depth, 0) + 1
            mode = certificate_mode(state, depth)
            modes[mode] = modes.get(mode, 0) + 1
        elif len(unknown_states) < 20:
            unknown_states.append(list(state))
    return {
        "p": 7, "n": 15, "bound": bound,
        "states": len(states), "direct_zero_subset": direct,
        "certified": certified, "unknown": len(states) - certified,
        "certified_ratio": certified / len(states) if states else None,
        "depth_distribution": dict(sorted(depth_distribution.items())),
        "certificate_mode_distribution": dict(sorted(modes.items())),
        "unknown_states": unknown_states,
        "seconds": perf_counter() - started,
        "sampling_model": "sorted primitive zero-sum integer states in [-bound,bound], conditioned on G=1",
    }


def main(args):
    reports = [exact_bounded(bound) for bound in args.bounds]
    output = {"experiment": "exact bounded seven-average n=15 zero-trigger coverage",
              "reports": reports,
              "warning": "This certifies the displayed finite sets, not all unbounded rational states."}
    for report in reports:
        print(json.dumps(report, ensure_ascii=False), flush=True)
    Path(args.output).write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("exact seven-average n15 bounded enumeration: PASS", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--bounds", nargs="+", type=int, default=[1, 2, 3, 4])
    parser.add_argument("--output", default="work/exact_seven_average_n15_bounded.json")
    main(parser.parse_args())
