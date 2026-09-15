"""Compare finite B_n controller searches for one non-3 prime factor.

The program is exploratory. It searches the exact kernel
    (u^(n-4), v^3, -(n-4)u-3v)
and uses a zero-sum partition with ternary-digit block sizes. No bounded result is
interpreted as an all-directions theorem.
"""

from collections import Counter, deque
from concurrent.futures import ProcessPoolExecutor, as_completed
from fractions import Fraction as F
from itertools import product, combinations_with_replacement
from math import gcd
import os
from time import perf_counter

from search_n91_missing_class import signatures, step
from standard_kernel_interface import TerminalPartitionCertificate


def nonthree_part(n):
    if n < 1:
        raise ValueError("n must be positive")
    while n % 3 == 0:
        n //= 3
    return n


def ternary_terms(n):
    terms = []
    power = 1
    while n:
        terms.extend([power] * (n % 3))
        n //= 3
        power *= 3
    return tuple(sorted(terms))


def pair_classes(n, bound):
    if n < 7 or bound < 1:
        raise ValueError("n must be at least 7 and bound must be positive")
    result = set()
    modulus = nonthree_part(n)
    for u, v in product(range(-bound, bound + 1), repeat=2):
        if max(abs(u), abs(v)) == 0:
            continue
        if gcd(abs(u), abs(v)) != 1 or gcd(u - v, modulus) != 1:
            continue
        result.add(min((u, v), (-u, -v)))
    return sorted(result)


def kernel_state(n, pair):
    u, v = pair
    state = Counter()
    for value, count in ((u, n - 4), (v, 3), (-(n - 4) * u - 3 * v, 1)):
        state[F(value)] += count
    return state


def scaled_values(state):
    denominator = 1
    for value in state:
        denominator = denominator * value.denominator // gcd(
            denominator, value.denominator
        )
    result = [
        (
            value,
            multiplicity,
            value.numerator * (denominator // value.denominator),
        )
        for value, multiplicity in sorted(state.items())
    ]
    content = gcd(*(abs(item[2]) for item in result))
    if content > 1:
        result = [
            (value, multiplicity, scaled // content)
            for value, multiplicity, scaled in result
        ]
    return result


def zero_sum_selections(state, target_size):
    values = scaled_values(state)
    if target_size == 3:
        # Determine the third value from each ordered pair, rather than
        # enumerate every bounded count vector in the support.
        lookup = {scaled: index for index, (_, _, scaled) in enumerate(values)}
        for left in range(len(values)):
            for middle in range(left, len(values)):
                if left == middle and values[left][1] < 2:
                    continue
                right = lookup.get(-values[left][2]-values[middle][2], -1)
                if right < middle:
                    continue
                counts = Counter((left, middle, right))
                if all(count <= values[index][1] for index, count in counts.items()):
                    yield tuple((values[index][0], count)
                                for index, count in sorted(counts.items()))
        return
    suffix_sizes = [0] * (len(values) + 1)
    for index in range(len(values) - 1, -1, -1):
        suffix_sizes[index] = suffix_sizes[index + 1] + values[index][1]

    def generate(index, remaining, total, counts):
        if remaining > suffix_sizes[index]:
            return
        if remaining == 0:
            if total == 0:
                yield counts
            return
        if not (remaining * values[index][2] <= -total
                <= remaining * values[-1][2]):
            return
        # Two remaining counts are determined by cardinality and zero sum.
        if index == len(values) - 2:
            first, multiplicity, scaled = values[index]
            second, last_count, last_scaled = values[index + 1]
            numerator = -total - remaining * last_scaled
            divisor = scaled - last_scaled
            count, remainder = divmod(numerator, divisor)
            other = remaining - count
            if remainder or not 0 <= count <= multiplicity or not 0 <= other <= last_count:
                return
            selection = counts
            if count:
                selection += ((first, count),)
            if other:
                selection += ((second, other),)
            yield selection
            return
        if index == len(values) - 1:
            value, multiplicity, scaled = values[index]
            if remaining <= multiplicity and total + remaining * scaled == 0:
                if remaining:
                    yield counts + ((value, remaining),)
                else:
                    yield counts
            return
        value, multiplicity, scaled = values[index]
        minimum = max(0, remaining - suffix_sizes[index + 1])
        for count in range(minimum, min(multiplicity, remaining) + 1):
            following = counts + ((value, count),) if count else counts
            yield from generate(
                index + 1,
                remaining - count,
                total + count * scaled,
                following,
            )

    if values:
        yield from generate(0, target_size, 0, ())


def terminal_partition(state):
    sizes = ternary_terms(sum(state.values()))
    memo = {}

    def solve(state_key, remaining_sizes):
        cache_key = state_key, remaining_sizes
        if cache_key in memo:
            return memo[cache_key]
        if not remaining_sizes:
            result = () if not state_key else None
            memo[cache_key] = result
            return result
        current = Counter(dict(state_key))
        if len(remaining_sizes) == 1:
            result = ((state_key,) if sum(current.values()) == remaining_sizes[0]
                      and sum(value * count for value, count in state_key) == 0 else None)
            memo[cache_key] = result
            return result
        target = remaining_sizes[0]
        for selection in zero_sum_selections(current, target):
            following = current.copy()
            for value, count in selection:
                following[value] -= count
                if following[value] == 0:
                    del following[value]
            tail = solve(tuple(sorted(following.items())), remaining_sizes[1:])
            if tail is not None:
                result = (selection,) + tail
                memo[cache_key] = result
                return result
        memo[cache_key] = None
        return None

    return solve(tuple(sorted(state.items())), sizes)


def search_pair_fraction(task):
    n, pair, depth = task
    start = kernel_state(n, pair)
    queue = deque([(start, ())])
    seen = {tuple(sorted(start.items()))}
    while queue:
        state, path = queue.popleft()
        partition = terminal_partition(state)
        if partition is not None:
            return pair, (path, tuple(sorted(state.items())), partition), len(seen)
        if len(path) >= depth:
            continue
        for selected in signatures(state):
            following = step(state, selected)
            identifier = tuple(sorted(following.items()))
            if identifier not in seen:
                seen.add(identifier)
                queue.append((following, path + (selected,)))
    return pair, None, len(seen)


def integer_state(state):
    values = scaled_values(state)
    return tuple((scaled, count) for _, count, scaled in values)


def integer_choices(state):
    for indices in combinations_with_replacement(range(len(state)), 3):
        i, j, k = indices
        if i == k:
            continue
        if (i == j and state[i][1] < 2) or (j == k and state[j][1] < 2):
            continue
        yield indices


def integer_step(state, indices):
    following = {3*value: count for value, count in state}
    total = 0
    for index in indices:
        value, _ = state[index]
        total += value
        following[3*value] -= 1
        if following[3*value] == 0:
            del following[3*value]
    following[total] = following.get(total, 0)+3
    content = gcd(*(abs(value) for value in following)) or 1
    return tuple(sorted((value//content, count) for value, count in following.items())), content


def restore_integer_certificate(n, pair, index_path, partition):
    state = integer_state(kernel_state(n, pair))
    # Primitive input pairs give a primitive expanded integer state.
    scale = F(1)
    operations = []
    for indices in index_path:
        operations.append(tuple(state[index][0]*scale for index in indices))
        state, content = integer_step(state, indices)
        scale *= F(content, 3)
    physical = tuple((value*scale, count) for value, count in state)
    blocks = tuple(tuple((value*scale, count) for value, count in block)
                   for block in partition)
    return tuple(operations), physical, blocks


def search_pair_integer(task):
    n, pair, depth = task
    start = integer_state(kernel_state(n, pair))
    queue = deque([(start, ())])
    seen = {start}
    while queue:
        state, path = queue.popleft()
        partition = terminal_partition(Counter(dict(state)))
        if partition is not None:
            return pair, restore_integer_certificate(n, pair, path, partition), len(seen)
        if len(path) >= depth:
            continue
        for indices in integer_choices(state):
            following, _ = integer_step(state, indices)
            if following not in seen:
                seen.add(following)
                queue.append((following, path+(indices,)))
    return pair, None, len(seen)


def search_pair(task):
    if len(task) == 4:
        n, pair, depth, engine = task
        task = n, pair, depth
    else:
        engine = "integer"
    if engine == "fraction":
        return search_pair_fraction(task)
    return search_pair_integer(task)


def verify(n, pair, certificate):
    path, terminal_state, partition = certificate
    state = kernel_state(n, pair)
    for selected in path:
        assert len(selected) == 3
        required = Counter(selected)
        assert all(state[value] >= count for value, count in required.items())
        state = step(state, selected)
    assert tuple(sorted(state.items())) == terminal_state
    assert sum(value * count for value, count in state.items()) == 0
    terminal = TerminalPartitionCertificate(terminal_state, partition)
    assert terminal.verify() == ternary_terms(n)


def explore(n, bound, depth, jobs, requested_pairs=None, hard_limit=5, engine="integer"):
    if depth < 0 or jobs < 1:
        raise ValueError("depth must be nonnegative and jobs positive")
    started = perf_counter()
    pairs = pair_classes(n, bound)
    if requested_pairs:
        illegal = set(requested_pairs) - set(pairs)
        if illegal:
            raise ValueError(f"pairs outside the legal bounded set: {sorted(illegal)}")
        pairs = sorted(set(requested_pairs))
    tasks = [(n, pair, depth, engine) for pair in pairs]
    found = {}
    state_counts = {}
    worker_count = min(max(1, jobs), len(tasks)) if tasks else 1
    print(f"START n={n} pairs={len(tasks)} depth={depth} workers={worker_count} engine={engine}",
          flush=True)
    if worker_count == 1:
        results = map(search_pair, tasks)
        executor = None
    else:
        executor = ProcessPoolExecutor(max_workers=worker_count)
        futures = [executor.submit(search_pair, task) for task in tasks]
        results = (future.result() for future in as_completed(futures))
    try:
        for pair, certificate, states in results:
            state_counts[pair] = states
            if certificate is not None:
                verify(n, pair, certificate)
                found[pair] = certificate
    finally:
        if executor is not None:
            executor.shutdown()
    histogram = Counter(len(certificate[0]) for certificate in found.values())
    # Summary excludes the fixed block-network tail.
    print(
        f"n={n} pair classes {len(pairs)} depth {depth} "
        f"bound {bound} workers {worker_count}"
    )
    print(f"n={n} terminal coverage {len(found)} / {len(pairs)}")
    print(f"n={n} depth histogram {dict(sorted(histogram.items()))}")
    missing = [pair for pair in pairs if pair not in found]
    print(f"n={n} missing {missing}")
    if missing:
        print(f"n={n} missing state counts", [(pair, state_counts[pair]) for pair in missing])
    hard = sorted(
        (
            (len(certificate[0]), pair, certificate)
            for pair, certificate in found.items()
        ),
        reverse=True,
    )[:hard_limit]
    for path_length, pair, certificate in hard:
        print(f"n={n} hard pair {pair} depth {path_length} certificate {certificate}")
    print(f"n={n} elapsed seconds {perf_counter() - started:.3f}", flush=True)
    return pairs, found


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, action="append")
    parser.add_argument("--bound", type=int, default=8)
    parser.add_argument("--depth", type=int, default=4)
    parser.add_argument("--jobs", type=int, default=os.cpu_count() or 1)
    parser.add_argument("--engine", choices=("integer", "fraction"), default="integer",
                        help="integer projective states or the Fraction reference engine")
    parser.add_argument(
        "--pair",
        action="append",
        metavar="U,V",
        help="search only one primitive pair; repeat for several pairs",
    )
    parser.add_argument(
        "--summary",
        action="store_true",
        help="suppress individual hard-pair certificates",
    )
    arguments = parser.parse_args()
    requested_pairs = None
    if arguments.pair:
        requested_pairs = []
        for item in arguments.pair:
            parts = item.split(",")
            if len(parts) != 2:
                parser.error("--pair must have the form U,V")
            requested_pairs.append(tuple(map(int, parts)))
    for n in arguments.n or [12, 15, 18, 21]:
        explore(
            n,
            arguments.bound,
            arguments.depth,
            arguments.jobs,
            requested_pairs,
            0 if arguments.summary else 5,
            arguments.engine,
        )
