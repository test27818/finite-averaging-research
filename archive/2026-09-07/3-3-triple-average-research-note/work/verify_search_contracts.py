"""Independent small-domain checks of terminal enumeration and runner mode."""

from collections import Counter
from fractions import Fraction as F
from itertools import combinations
import os
from pathlib import Path
from random import Random
import subprocess
import sys

from explore_single_prime_kernels import (
    zero_sum_selections, terminal_partition, integer_state, integer_step,
    integer_choices, kernel_state, pair_classes, search_pair_integer,
    search_pair_fraction, verify,
)
from search_n91_missing_class import signatures, step
from standard_kernel_interface import TerminalPartitionCertificate
from search_b12_return_frontier import canonical, explore_branch


def brute_subsets(values, size):
    return {
        tuple(sorted(Counter(selected).items()))
        for selected in combinations(values, size)
        if sum(selected, F(0)) == 0
    }


def check_subsets():
    random = Random(90912)
    checked = 0
    for _ in range(80):
        values = tuple(F(random.randrange(-4, 5), random.choice((1, 3, 9)))
                       for _ in range(8))
        state = Counter(values)
        for size in range(9):
            expected = brute_subsets(values, size)
            actual = {tuple(sorted(item)) for item in zero_sum_selections(state, size)}
            assert expected == actual, (values, size, expected, actual)
            checked += 1
    # Include coincident values, the all-zero terminal, and multiple blocks.
    for values in ((0,)*12, (-1,)*6+(1,)*6, (-1,)*9+(1,)*9):
        state = Counter(map(F, values))
        partition = terminal_partition(state)
        if partition is not None:
            TerminalPartitionCertificate(tuple(state.items()), partition).verify()
    print("terminal subset oracle vs position enumeration: PASS", checked)


def check_runner():
    runner = Path(__file__).with_name("run_verifications.py")
    environment = os.environ.copy()
    environment.pop("PYTHONOPTIMIZE", None)
    cases = [
        ([sys.executable, "-O", str(runner), "--list"], environment),
        ([sys.executable, str(runner), "--list"], dict(environment, PYTHONOPTIMIZE="1")),
    ]
    for argv, env in cases:
        result = subprocess.run(argv, env=env, capture_output=True, text=True, timeout=15)
        assert result.returncode == 2
        assert "assertions disabled" in result.stderr
        assert "PASS" not in result.stdout
    print("optimized Python runner rejection: PASS 2")


def check_integer_search():
    checked, transitions = 0, 0
    random = Random(90921)
    for n in (12, 15, 18, 21):
        for pair in pair_classes(n, 3):
            task = n, pair, 2
            _, fraction_result, _ = search_pair_fraction(task)
            _, integer_result, _ = search_pair_integer(task)
            assert (fraction_result is None) == (integer_result is None)
            if integer_result is not None:
                assert len(fraction_result[0]) == len(integer_result[0])
                verify(n, pair, integer_result)
            checked += 1
        state = kernel_state(n, (1, 0))
        for _ in range(12):
            integer = integer_state(state)
            old_successors = {integer_state(step(state, selected))
                              for selected in signatures(state)}
            new_successors = {integer_step(integer, indices)[0]
                              for indices in integer_choices(integer)}
            # A no-op on an all-equal triple was omitted by both engines.
            assert old_successors == new_successors
            transitions += len(new_successors)
            options = list(signatures(state))
            if not options:
                break
            state = step(state, random.choice(options))
    print("integer/Fraction BFS shortest witness comparison: PASS", checked)
    print("projective integer successor equivalence: PASS", transitions)


def check_symbolic_collision():
    # Six distinct forms become the three B12 forms in one step: the mean
    # of (2u+v, 3u-v, -2u) is an already-present u.
    state = canonical({(1, 0): 5, (0, 1): 3, (-8, -3): 1,
                       (2, 1): 1, (3, -1): 1, (-2, 0): 1})
    found, _ = explore_branch((state, (), 1, 12))
    assert (-1, 0, 0, -1) in found
    print("symbolic mean-collision pruning regression: PASS")


if __name__ == "__main__":
    check_subsets()
    check_runner()
    check_integer_search()
    check_symbolic_collision()
