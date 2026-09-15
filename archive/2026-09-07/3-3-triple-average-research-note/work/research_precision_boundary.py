"""Exact experiments on integral ternary averaging in dimensions six and seven."""

from collections import deque
from functools import cache
from itertools import combinations, combinations_with_replacement
from math import gcd
from collections import Counter


def canonical(state):
    state = tuple(sorted(state))
    return min(state, tuple(sorted(-x for x in state)))


def primitive(state):
    divisor = gcd(*state)
    return canonical(tuple(x // divisor for x in state)) if divisor else tuple(state)


def arithmetic_good(state):
    state = primitive(state)
    if not any(state):
        return True
    divisor = gcd(*(value - state[0] for value in state))
    while divisor % 3 == 0:
        divisor //= 3
    return divisor == 1


def integer_edges(state):
    for selected in combinations(range(len(state)), 3):
        total = sum(state[i] for i in selected)
        if total % 3:
            continue
        mean = total // 3
        if all(state[i] == mean for i in selected):
            continue
        nxt = list(state)
        for i in selected:
            nxt[i] = mean
        yield canonical(nxt), selected


@cache
def integer_distance(state):
    if not any(state):
        return 0
    # A zero-sum triple and its six-coordinate complement finish in two steps.
    if len(state) == 6 and any(
        sum(state[i] for i in selected) == 0
        for selected in combinations(range(6), 3)
    ):
        return 1 if sum(x != 0 for x in state) <= 3 else 2
    best = None
    for nxt, _ in integer_edges(state):
        assert sum(x*x for x in nxt) < sum(x*x for x in state)
        following = integer_distance(nxt)
        if following is not None:
            candidate = following + 1
            best = candidate if best is None else min(best, candidate)
    return best


def rational_bfs(state, max_depth):
    start = primitive(state)
    queue = deque([(start, 0)])
    seen = {start}
    while queue:
        current, depth = queue.popleft()
        if not any(current):
            return depth
        if depth == max_depth:
            continue
        for selected in combinations(range(len(current)), 3):
            total = sum(current[i] for i in selected)
            nxt = primitive(tuple(
                total if i in selected else 3 * value
                for i, value in enumerate(current)
            ))
            if nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, depth + 1))
    return None


def centered_states(n, bound):
    seen = set()
    for prefix in combinations_with_replacement(range(-bound, bound + 1), n - 1):
        last = -sum(prefix)
        if not prefix[-1] <= last <= bound:
            continue
        state = primitive(prefix + (last,))
        if state not in seen and any(state):
            seen.add(state)
            yield state


def six_profile(bound):
    count = success = 0
    max_depth = -1
    deepest = None
    primitive_failures = []
    for state in centered_states(6, bound):
        count += 1
        depth = integer_distance(state)
        if depth is not None:
            success += 1
            if depth > max_depth:
                max_depth, deepest = depth, state
        elif gcd(*(value - state[0] for value in state)) == 1:
            primitive_failures.append(state)
    print('six-profile', bound, count, success, max_depth, deepest, flush=True)
    print('G=1 failures', primitive_failures[:8], flush=True)


def seven_zero_profile(bound):
    checked = 0
    for six in centered_states(6, bound):
        state = canonical(six + (0,))
        checked += 1
        if integer_distance(state) is None:
            print('seven-needs-fractions', state, 'checked', checked, flush=True)
            return state
    print('seven-zero-all-integral', bound, checked, flush=True)
    return None


def bounded_precision_profile(n, bound):
    total = integral_failures = extra_precision_failures = 0
    safe_terminal = 0
    for state in centered_states(n, bound):
        if not arithmetic_good(state):
            continue
        total += 1
        check_two_parameter_reduction(state)
        safe = [nxt for nxt, _ in integer_edges(state) if arithmetic_good(nxt)]
        if not safe:
            safe_terminal += 1
            assert max(Counter(state).values()) >= n - 3
        if integer_distance(state) is None:
            integral_failures += 1
            # A finite-range observation, not an assumption of the solver.
            assert not safe, ('integer failure with a safe edge', state)
            scaled = canonical(tuple(3 * value for value in state))
            if integer_distance(scaled) is None:
                extra_precision_failures += 1
                print('precision-one-counterexample', state, flush=True)
    print(
        'bounded-precision', n, bound, 'good', total,
        'integral-failures', integral_failures,
        'precision-one-failures', extra_precision_failures,
        'safe-terminals', safe_terminal, flush=True,
    )


def check_two_parameter_reduction(state):
    n = len(state)
    repeated = [value for value, count in Counter(state).items() if count >= n - 3]
    if not repeated:
        return
    c = repeated[0]
    exceptions = list(state)
    for _ in range(n - 3):
        exceptions.remove(c)
    prime = 7 if n == 7 else 2
    d = next(value for value in exceptions if (value - c) % prime)
    exceptions.remove(d)
    a, b = exceptions
    u, v = 3 * c, a + b + c
    assert 3 * d == -(n - 4) * u - 3 * v
    divisor = gcd(u, v)
    u, v = u // divisor, v // divisor
    assert gcd(u - v, n) == 1
    result = (u,) * (n - 4) + (v,) * 3 + (-(n - 4) * u - 3 * v,)
    assert sum(result) == 0
    assert gcd(*result) == 1
    assert arithmetic_good(result)


def stress_safe_lemma():
    from random import Random

    random = Random(7128)
    checked = 0
    for n in (7, 8):
        for _ in range(2000):
            if n == 7:
                size = random.choice((4, 5))
                residue = random.randrange(7)
                values = [7 * random.randrange(-10**10, 10**10) + residue for _ in range(size)]
            else:
                size = 6
                residue = random.randrange(2)
                values = [2 * random.randrange(-10**10, 10**10) + residue for _ in range(size)]
            values += [random.randrange(-10**10, 10**10) for _ in range(n - 1 - size)]
            values.append(-sum(values))
            state = primitive(values)
            if not arithmetic_good(state) or max(Counter(state).values()) >= n - 3:
                continue
            assert any(arithmetic_good(nxt) for nxt, _ in integer_edges(state)), state
            checked += 1
    print('large-coordinate safe-lemma checks', checked, flush=True)


def check_fractional_witness():
    from fractions import Fraction as F

    state = [F(-4), F(-1)] + [F(1)] * 5
    selected_values = [
        (F(-4), F(1), F(1)),
        (F(-1), F(1), F(1)),
        (F(-2, 3), F(1, 3), F(1, 3)),
        (F(1), F(0), F(0)),
        (F(-2, 3), F(1, 3), F(1, 3)),
        (F(-2, 3), F(1, 3), F(1, 3)),
    ]
    assert not list(integer_edges(tuple(int(x) for x in state)))
    print('fractional-witness', tuple(map(str, sorted(state))))
    for selected in selected_values:
        for value in selected:
            state.remove(value)
        state.extend([sum(selected) / 3] * 3)
        assert sum(state) == 0
        assert all(value.denominator in (1, 3) for value in state)
        print('fractional-witness', tuple(map(str, sorted(state))))
    assert not any(state)


if __name__ == '__main__':
    check_fractional_witness()
    for height in (3, 5, 10, 15):
        six_profile(height)
    for height in (3, 5, 10):
        if seven_zero_profile(height) is not None:
            break
    for state in centered_states(6, 2):
        distance = integer_distance(state)
        rational = rational_bfs(state, 3)
        expected = distance if distance is not None and distance <= 3 else None
        assert rational == expected, (state, distance, rational)
    print('independent rational BFS agrees through depth 3 for height 2', flush=True)
    bounded_precision_profile(7, 15)
    bounded_precision_profile(8, 10)
    stress_safe_lemma()
