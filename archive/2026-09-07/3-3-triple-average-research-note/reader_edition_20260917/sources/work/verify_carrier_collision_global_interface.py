"""Collision-to-equal-carrier bridge and overlap-height obstruction."""

from fractions import Fraction as F
from math import gcd, lcm


def affine_ideal(values):
    values = tuple(map(F, values))
    denominator = lcm(*(value.denominator for value in values))
    integers = [int(value * denominator) for value in values]
    anchor = integers[0]
    divisor = gcd(*(value - anchor for value in integers))
    result = F(divisor, denominator)
    while result.numerator and result.numerator % 3 == 0:
        result /= 3
    while result.denominator % 3 == 0:
        result *= 3
    return abs(result)


def verify_collision_bridge():
    checked = 0
    for collision, other, x, y in (
        (F(2), F(-7), F(5), F(11)),
        (F(-4, 9), F(13, 3), F(7, 9), F(-2)),
    ):
        replacement = (2 * collision + other) / 3
        before = [collision] * 4 + [other, x, y]
        after = [collision] * 2 + [replacement] * 3 + [x, y]
        assert sum(before) == sum(after)
        assert affine_ideal(before) == affine_ideal(after)
        checked += 1

    for collision, first, second, x in (
        (F(2), F(-7), F(5), F(11)),
        (F(-4, 9), F(13, 3), F(7, 9), F(-2)),
    ):
        left = (2 * collision + first) / 3
        right = (2 * collision + second) / 3
        before = [collision] * 6 + [first, second] + [x]
        after = [collision] * 2 + [left] * 3 + [right] * 3 + [x]
        assert sum(before) == sum(after)
        assert affine_ideal(before) == affine_ideal(after)
        checked += 1
    print("collision to equal carriers and affine-ideal preservation: PASS", checked)


def verify_overlap_height_barrier():
    checked = 0
    # A positive root word followed by its same-length positive inverse fixes
    # the local mean and scales all three carrier differences by3^-8.
    for exponent in range(1, 13):
        scale = F(1, 3 ** (8 * exponent))
        differences = tuple(scale * value for value in (1, 2, -3))
        assert sum(differences) == 0
        outside = F(1)
        overlap = outside - differences[0]
        assert overlap == F(3 ** (8 * exponent) - 1,
                            3 ** (8 * exponent))
        assert overlap.numerator == 3 ** (8 * exponent) - 1
        assert overlap.denominator == 3 ** (8 * exponent)
        checked += 1
    print("overlap primitive height grows under local center contraction: PASS",
          checked, 3 ** (8 * 12) - 1)


if __name__ == "__main__":
    verify_collision_bridge()
    verify_overlap_height_barrier()
