"""Exact checks for the ten-point reduction and terminal theorem."""

from collections import Counter
from fractions import Fraction as F
from itertools import product

from verify_ten_descent_cover import verify as verify_terminal_cover


def average(state, selected):
    mean = sum((state[index] for index in selected), F(0)) / 3
    result = list(state)
    for index in selected:
        result[index] = mean
    return tuple(result)


def is_unit_mod_ten(value):
    return value % 2 and value % 5


def verify_pairing_lemma():
    checked = 0
    split_cases = 0
    for differences in product(range(10), repeat=4):
        if sum(differences) % 10:
            continue
        if not any(value % 2 for value in differences):
            continue
        if not any(value % 5 for value in differences):
            continue
        checked += 1
        if any(is_unit_mod_ten(value) for value in differences):
            continue
        split_cases += 1
        assert (is_unit_mod_ten(differences[0] + differences[1])
                or is_unit_mod_ten(differences[0] + differences[2]))
    return checked, split_cases


def verify_four_step_bridge(bound=5):
    checked = 0
    for u, a, b, c in product(range(-bound, bound + 1), repeat=4):
        d = -6 * u - a - b - c
        state = tuple(map(F, [u] * 6 + [a, b, c, d]))

        state = average(state, (0, 8, 9))
        q = F(-5 * u - a - b, 3)
        assert state[0] == state[8] == state[9] == q

        state = average(state, (0, 6, 7))
        r = F(-5 * u + 2 * a + 2 * b, 9)
        assert state[0] == state[6] == state[7] == r

        state = average(state, (1, 8, 0))
        s = F(-11 * u - a - b, 27)
        assert state[1] == state[8] == state[0] == s

        state = average(state, (2, 9, 6))
        assert state[2] == state[9] == state[6] == s
        assert Counter(state) == Counter([s] * 6 + [F(u)] * 3 + [r])
        assert r == -6 * s - 3 * u
        assert s - u == F(-40 * u - (a - u) - (b - u), 27)
        checked += 1
    return checked


def main():
    local_cases, split_cases = verify_pairing_lemma()
    bridge_cases = verify_four_step_bridge()
    verify_terminal_cover()
    print("ten-point complete theorem certificate: PASS")
    print("mod-10 four-difference cases", local_cases,
          "split-witness cases", split_cases)
    print("exact four-step bridge samples", bridge_cases)
    print("terminal local-real cover: PASS")


if __name__ == "__main__":
    main()
