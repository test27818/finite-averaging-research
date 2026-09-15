"""Verify the finite macros and terminal witness for B_8 Euclidean descent."""

from collections import deque
from fractions import Fraction as F
from itertools import combinations
from math import gcd

from symbolic_two_parameter_macros import b_parameters, b_state, choices, step


def c(a, b):
    return F(a), F(b)


REFLECTION_PATH = (
    tuple(sorted((c(0, 1), c(0, 1), c(1, 0)))),
    tuple(sorted((c(0, 1), c(1, 0), c(1, 0)))),
    tuple(sorted((c(-4, -3), c(F(1, 3), F(2, 3)),
                  c(F(2, 3), F(1, 3))))),
    tuple(sorted((c(F(1, 3), F(2, 3)), c(F(2, 3), F(1, 3)), c(1, 0)))),
)

SWAP_PATH = (
    tuple(sorted((c(-4, -3), c(0, 1), c(1, 0)))),
    tuple(sorted((c(-1, F(-2, 3)), c(-1, F(-2, 3)), c(1, 0)))),
    tuple(sorted((c(-1, F(-2, 3)), c(1, 0), c(1, 0)))),
    tuple(sorted((c(F(-1, 3), F(-4, 9)), c(0, 1),
                  c(F(1, 3), F(-2, 9))))),
    tuple(sorted((c(F(-1, 3), F(-4, 9)), c(0, 1),
                  c(F(1, 3), F(-2, 9))))),
    tuple(sorted((c(0, F(1, 9)), c(0, F(1, 9)),
                  c(F(1, 3), F(-2, 9))))),
)

REDUCTION_PATH = (
    tuple(sorted((c(0, 1), c(1, 0), c(1, 0)))),
    tuple(sorted((c(-4, -3), c(F(2, 3), F(1, 3)),
                  c(F(2, 3), F(1, 3))))),
    tuple(sorted((c(0, 1), c(1, 0), c(1, 0)))),
)


def instantiate(state, u, v):
    return tuple(sorted(F(a) * u + F(b) * v for a, b in state))


def average_step(state, selected):
    mean = sum((state[index] for index in selected), F(0)) / 3
    result = list(state)
    for index in selected:
        result[index] = mean
    return tuple(sorted(result))


def terminal_witness():
    start = tuple(sorted([F(0)] * 4 + [F(1)] * 3 + [F(-3)]))
    queue = deque([start])
    parent = {start: None}
    edge = {}
    while queue:
        state = queue.popleft()
        if not any(state):
            path = []
            while parent[state] is not None:
                path.append((edge[state], state))
                state = parent[state]
            path.reverse()
            return start, path
        for selected in combinations(range(8), 3):
            signature = tuple(state[index] for index in selected)
            nxt = average_step(state, selected)
            if nxt not in parent:
                parent[nxt] = state
                edge[nxt] = signature
                queue.append(nxt)
    raise AssertionError("terminal state should be reachable")


def replay_macro(path):
    start = b_state(8)
    state = start
    for signature in path:
        selected = next(selected for selected, candidate in choices(state)
                        if candidate == signature)
        state = step(state, selected)
    parameters = b_parameters(8, state)
    assert len(parameters) == 1
    return parameters[0], state


def mul(left, right):
    return tuple(tuple(sum((left[i][k] * right[k][j] for k in range(2)), F(0))
                       for j in range(2)) for i in range(2))


def uv_to_xy(matrix):
    change = ((F(1), F(0)), (F(1), F(1)))
    inverse = ((F(1), F(0)), (F(-1), F(1)))
    return mul(change, mul(matrix, inverse))


def primitive_pair(x, y):
    divisor = gcd(x, y)
    return x // divisor, y // divisor


def verify_descent_step(bound=100):
    for y in range(-bound, bound + 1):
        if y == 0 or y % 2 == 0 or abs(y) == 1:
            continue
        for x in range(-bound, bound + 1):
            if gcd(x, y) != 1:
                continue
            if x % 2 == 0:
                x = y - x  # swap macro in (x,y) coordinates
            assert x % 2

            # Choose a translate x0=x (mod 2y) for which x0-2y is the
            # least absolute residue. Equality can occur only when |y|=1.
            residues = [x + 2 * k * y for k in range(-bound - 2, bound + 3)]
            remainder = min(residues, key=abs)
            assert abs(remainder) < abs(y)
            x0 = remainder + 2 * y
            raw = (3 * (x0 + y), 2 * (x0 - 2 * y))
            _, new_y = primitive_pair(*raw)
            assert new_y % 2
            assert abs(new_y) < abs(y)


def main():
    # Coefficients here are in the original (u,v) coordinates.
    reflection_target = ((F(2, 3), F(1, 3)), (F(-1), F(-2, 3)))
    swap_target = ((F(0), F(1, 9)), (F(1, 9), F(0)))
    reduction_target = ((F(2, 3), F(1, 3)), (F(-8, 9), F(-7, 9)))

    actual_reflection, _ = replay_macro(REFLECTION_PATH)
    actual_swap, _ = replay_macro(SWAP_PATH)
    actual_reduction, _ = replay_macro(REDUCTION_PATH)
    start, terminal = terminal_witness()

    # Translate the returned (u,v) maps to (x,y)=(u,u+v), clearing their
    # displayed global denominators. These are the three matrices used in
    # the proof.
    assert actual_reflection == reflection_target
    assert actual_swap == swap_target
    assert actual_reduction == reduction_target
    assert uv_to_xy(reflection_target) == (
        (F(1, 3), F(1, 3)), (F(0), F(-1, 3)))
    assert uv_to_xy(swap_target) == (
        (F(-1, 9), F(1, 9)), (F(0), F(1, 9)))
    assert uv_to_xy(reduction_target) == (
        (F(1, 3), F(1, 3)), (F(2, 9), F(-4, 9)))
    reflection_xy = ((1, 1), (0, -1))
    swap_xy = ((-1, 1), (0, 1))
    assert mul(swap_xy, reflection_xy) == ((-1, -2), (0, -1))
    assert mul(reflection_xy, swap_xy) == ((-1, 2), (0, -1))

    assert len(REFLECTION_PATH) == 4
    assert len(SWAP_PATH) == 6
    assert len(REDUCTION_PATH) == 3
    assert len(terminal) == 4
    assert not any(terminal[-1][1])
    verify_descent_step()

    print("B8 Euclidean macro certificate: PASS")
    print("reflection macro length", len(REFLECTION_PATH), "target", reflection_target)
    print("swap macro length", len(SWAP_PATH), "target", swap_target)
    print("reduction macro length", len(REDUCTION_PATH), "target", reduction_target)
    print("terminal B8(0,1) witness")
    print(" ", start)
    for signature, state in terminal:
        print("  average", signature, "->", state)


if __name__ == "__main__":
    main()
