from __future__ import annotations

from math import gcd


def primitive(values: tuple[int, ...]) -> tuple[int, ...]:
    d = 0
    for value in values:
        d = gcd(d, abs(value))
    if d:
        values = tuple(value // d for value in values)
    negated = tuple(-value for value in values)
    return min(values, negated)


def clear_denominator_step(state: tuple[int, ...], chosen: tuple[int, ...]):
    selected_sum = sum(state[index] for index in chosen)
    chosen_set = set(chosen)
    next_state = tuple(
        selected_sum if index in chosen_set else 3 * state[index]
        for index in range(len(state))
    )
    return primitive(next_state), selected_sum % 3


def check_six_element_counterexample() -> None:
    state = (-1, -1, 0, 1, 0, 1)
    state, residue = clear_denominator_step(state, (0, 2, 3))
    assert residue == 0
    assert state == (0, -1, 0, 0, 0, 1)
    state, residue = clear_denominator_step(state, (0, 1, 5))
    assert residue == 0
    assert state == (0, 0, 0, 0, 0, 0)


def check_valuation_one_contraction(bound: int = 300) -> None:
    # For u=3q, v=q+3r, q not divisible by 3, verify H2 <= 7H/9.
    for q in range(-bound, bound + 1):
        if q == 0 or q % 3 == 0:
            continue
        for r in range(-bound, bound + 1):
            h = max(3 * abs(q), abs(q + 3 * r))
            h2 = max(abs(q + r), abs(r))
            assert 9 * h2 <= 7 * h


if __name__ == "__main__":
    check_six_element_counterexample()
    check_valuation_one_contraction()
    print("counterexample and valuation-one contraction checks passed")
