"""Map explicit n=91 terminal directions to the corrected congruence cusps."""

from collections import Counter, deque
from concurrent.futures import ProcessPoolExecutor, as_completed
from fractions import Fraction as F
from math import gcd
import os
from time import perf_counter

from cyclotomic_congruence import congruence_automaton, cycles_of
from cyclotomic_terminal_classes import primitive_pair
from explore_thirteen_group import primitive
from explore_thirteen_modular import modular_word
from search_n91_missing_class import signatures, step, subset_counts_any


def extended_gcd(a, b):
    old_r, r, old_s, s, old_t, t = a, b, 1, 0, 0, 1
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    sign = 1 if old_r > 0 else -1
    return sign * old_r, sign * old_s, sign * old_t


def matrix_with_first_column(u, v):
    divisor, x, y = extended_gcd(u, v)
    assert divisor == 1
    return primitive((u, -y, v, x))


def follow_modular_word(base, table, word):
    current = base
    for letter in word:
        if letter == "U":
            current = table[table[current, "u"], "u"]
        else:
            current = table[current, letter]
    return current


def direct_terminal_pairs():
    result = set()
    for size in (27, 81):
        for singleton in (0, 1):
            for a in range(82):
                b = size - singleton - a
                if not 0 <= b <= 9:
                    continue
                pair = primitive_pair(b - singleton * 9,
                                      singleton * 81 - a)
                if pair is not None and gcd(pair[0] - pair[1], 91) == 1:
                    result.add(pair)
    return result


def cusp_state(u, v):
    state = Counter()
    for value, count in ((u, 81), (v, 9), (-81 * u - 9 * v, 1)):
        state[F(value)] += count
    return state


def terminal_search_state(start, depth, prefix=()):
    """Search with an absolute depth bound, retaining the actual path prefix.

    Keeping this separate from construction of the initial cusp state lets
    the command line driver split the first move into independent processes.
    The returned path always includes ``prefix``.
    """
    if depth < len(prefix):
        raise ValueError("depth must include the prefix length")
    queue = deque([(start, prefix)])
    seen = {tuple(sorted(start.items()))}
    while queue:
        state, path = queue.popleft()
        terminal = subset_counts_any(state, (27, 81))
        if terminal is not None:
            size, witness = terminal
            return path, size, witness
        if len(path) >= depth:
            continue
        for selected in signatures(state):
            following = step(state, selected)
            key = tuple(sorted(following.items()))
            if key not in seen:
                seen.add(key)
                queue.append((following, path + (selected,)))
    return None


def terminal_search(u, v, depth):
    return terminal_search_state(cusp_state(u, v), depth)


def terminal_search_task(task):
    cusp, pair, search_depth = task[:3]
    if len(task) == 3:
        certificate = terminal_search(*pair, search_depth)
    else:
        prefix = task[3]
        start = cusp_state(*pair)
        for selected in prefix:
            start = step(start, selected)
        certificate = terminal_search_state(start, search_depth, prefix)
    return cusp, pair, certificate


def verify_terminal_certificate(pair, certificate):
    path, size, witness = certificate
    state = cusp_state(*pair)
    for selected in path:
        assert len(selected) == 3
        required = Counter(selected)
        assert all(state[value] >= count for value, count in required.items())
        state = step(state, selected)
    assert size in (27, 81)
    assert len(dict(witness)) == len(witness)
    assert all(isinstance(count, int) and count > 0 for _, count in witness)
    assert sum(state.values()) == 91
    assert sum(value * count for value, count in state.items()) == 0
    assert sum(count for _, count in witness) == size
    assert sum(value * count for value, count in witness) == 0
    assert all(count <= state[value] for value, count in witness)


def analyze(bound, search_depth, jobs=1, cusp_filter=None, split_first=False,
            split_depth=None):
    if bound < 1 or search_depth < 0 or jobs < 1:
        raise ValueError("bound and jobs must be positive; depth must be nonnegative")
    started = perf_counter()
    labels, table, base, _, _ = congruence_automaton(9)
    cusps = cycles_of(table, labels, "su")
    cusp_of = {node: index for index, cycle in enumerate(cusps) for node in cycle}
    legal = {index for index, cycle in enumerate(cusps)
             if gcd(labels[cycle[0]][0][0], 91) == 1}
    if cusp_filter is not None and not cusp_filter <= legal:
        raise ValueError(f"not legal cusp ids: {sorted(cusp_filter - legal)}")
    requested = legal if cusp_filter is None else cusp_filter

    def pair_cusp(pair):
        matrix = matrix_with_first_column(*pair)
        node = follow_modular_word(base, table, modular_word(matrix))
        return cusp_of[node]

    direct = {}
    for pair in sorted(direct_terminal_pairs()):
        direct.setdefault(pair_cusp(pair), pair)
    print("legal cusps", len(legal), "directly terminal", len(legal & set(direct)))

    representatives = {}
    for height in range(1, bound + 1):
        for u in range(-height, height + 1):
            for v in (-height, height):
                if gcd(abs(u), abs(v)) != 1 or gcd(u - v, 91) != 1:
                    continue
                representatives.setdefault(pair_cusp((u, v)), (u, v))
        for v in range(-height + 1, height):
            for u in (-height, height):
                if gcd(abs(u), abs(v)) != 1 or gcd(u - v, 91) != 1:
                    continue
                representatives.setdefault(pair_cusp((u, v)), (u, v))
        if legal <= set(representatives):
            print("all legal cusp representatives found by height", height)
            break
    missing_representatives = requested - set(representatives)
    print("missing representatives", len(missing_representatives))
    if missing_representatives:
        raise ValueError("increase --bound to represent every requested cusp")

    certificates = {}
    for cusp, pair in direct.items():
        if cusp in requested:
            size, witness = subset_counts_any(cusp_state(*pair), (27, 81))
            certificate = (), size, witness
            verify_terminal_certificate(pair, certificate)
            certificates[cusp] = certificate, pair
    tasks = [
        (cusp, representatives[cusp], search_depth)
        for cusp in sorted(requested - set(certificates))
    ]
    candidate_cusps = {task[0] for task in tasks}
    # Prefixes are split only after testing depth zero: otherwise a terminal
    # start could be missed by a branch-only search.
    if split_depth is None:
        split_depth = 1 if split_first else 0
    if split_depth < 0 or split_depth > search_depth:
        raise ValueError("split depth must lie between 0 and search depth")
    if split_depth:
        split_tasks = []
        for cusp, pair, depth in tasks:
            start = cusp_state(*pair)
            initial = subset_counts_any(start, (27, 81))
            if initial is not None:
                certificate = ((), initial[0], initial[1])
                verify_terminal_certificate(pair, certificate)
                certificates[cusp] = certificate, pair
                continue
            frontier = [(start, ())]
            prefix_certificate = None
            for _ in range(split_depth):
                following = []
                for branch_state, prefix in frontier:
                    if prefix:
                        terminal = subset_counts_any(branch_state, (27, 81))
                        if terminal is not None:
                            prefix_certificate = (prefix, terminal[0], terminal[1])
                            break
                    following.extend(
                        (step(branch_state, selected), prefix + (selected,))
                        for selected in signatures(branch_state)
                    )
                if prefix_certificate is not None:
                    break
                frontier = following
            if prefix_certificate is not None:
                verify_terminal_certificate(pair, prefix_certificate)
                certificates[cusp] = prefix_certificate, pair
                continue
            split_tasks.extend(
                (cusp, pair, depth, prefix)
                for _, prefix in frontier
            )
        tasks = split_tasks
    jobs = max(1, min(jobs, len(tasks))) if tasks else 1
    print("search workers", jobs, "candidate tasks", len(tasks),
          "split-depth", split_depth, flush=True)
    if jobs == 1:
        results = map(terminal_search_task, tasks)
        executor = None
    else:
        executor = ProcessPoolExecutor(max_workers=jobs)
        futures = [executor.submit(terminal_search_task, task) for task in tasks]
        results = (future.result() for future in as_completed(futures))
    try:
        for cusp, pair, certificate in results:
            if certificate is not None:
                verify_terminal_certificate(pair, certificate)
                assert len(certificate[0]) <= search_depth
                if (cusp not in certificates
                        or len(certificate[0]) < len(certificates[cusp][0][0])):
                    certificates[cusp] = certificate, pair
                    print("FOUND cusp", cusp, "pair", pair, "certificate", certificate,
                          flush=True)
    finally:
        if executor is not None:
            executor.shutdown()
    for cusp in sorted(candidate_cusps - set(certificates)):
        print("OPEN cusp", cusp, "pair", representatives[cusp], flush=True)
    label = "covered legal cusps" if cusp_filter is None else "covered requested cusps"
    print(label, len(certificates), "/", len(requested))
    print("elapsed seconds", round(perf_counter() - started, 3), flush=True)
    return legal, representatives, certificates


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--bound", type=int, default=200)
    parser.add_argument("--depth", type=int, default=2)
    parser.add_argument(
        "--jobs", type=int, default=os.cpu_count() or 1,
        help="parallel cusp searches (default: all logical processors)",
    )
    parser.add_argument(
        "--cusp", type=int, action="append", dest="cusps",
        help="search only this cusp id; repeat the option for several ids",
    )
    parser.add_argument(
        "--split-first", action="store_true",
        help="split each candidate cusp by its first operation before parallel search",
    )
    parser.add_argument(
        "--split-depth", type=int,
        help="split each candidate cusp by this many prefix operations",
    )
    arguments = parser.parse_args()
    analyze(arguments.bound, arguments.depth, arguments.jobs,
            None if arguments.cusps is None else set(arguments.cusps),
            arguments.split_first, arguments.split_depth)
