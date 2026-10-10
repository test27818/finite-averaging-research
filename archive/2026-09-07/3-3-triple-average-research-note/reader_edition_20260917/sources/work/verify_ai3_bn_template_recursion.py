"""Exact verifier for parameter-independent B_n subproblem templates.

The verifier treats an already solved child problem as a certified mean
operation and explicitly replays every pre/post ternary average outside that
child.  It checks Smith/gcd lattice conditions, 2x2 output matrices and
away-from-3 determinant units.  It does not claim that the resulting return
semigroup terminates for every B_n.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import gcd, lcm


def is_power_three(value):
    value = abs(int(value))
    if value == 0:
        return False
    while value % 3 == 0:
        value //= 3
    return value == 1


def away_three(value):
    value = abs(int(value))
    if value == 0:
        return 0
    while value % 3 == 0:
        value //= 3
    return value


def prime_divisors(value):
    value = away_three(value)
    result = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            result.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        result.append(value)
    return result


def matrix_det(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def matrix_apply(matrix, pair):
    return tuple(sum(matrix[row][column] * pair[column]
                     for column in range(2)) for row in range(2))


def smith_rank_one(pattern, size, denominator):
    """Return (g, total, anchor, modulus, numerator) for a child pattern.

    The pattern stores integer coefficients z_i in values
    ``u + (z_i/denominator) * (v-u)``.  The affine difference ideal is
    ``(g/denominator) R`` with g the gcd of coefficient differences.  The
    child mean belongs to that ideal iff ``size*g`` away from 3 divides
    ``total - size*anchor``.
    """
    anchor = pattern[0]
    g = gcd(*(value - anchor for value in pattern))
    total = sum(pattern)
    numerator = total - size * anchor
    modulus = away_three(size * g)
    return g, total, anchor, modulus, numerator


def smith_rank_one_groups(groups, size, denominator):
    """Same calculation for repeated coefficient groups, without expansion."""
    groups = [(int(value), int(count)) for value, count in groups if count]
    anchor = groups[0][0]
    g = gcd(*(value - anchor for value, _ in groups))
    total = sum(value * count for value, count in groups)
    numerator = total - size * anchor
    modulus = away_three(size * g)
    return g, total, anchor, modulus, numerator


def denominator_is_power_three(value):
    return is_power_three(F(value).denominator)


def state_g(items):
    """Centered primitive G using weighted values, without expansion."""
    values = [(F(value), int(count)) for value, count in items if count]
    denominator = lcm(*(value.denominator for value, _ in values))
    integers = [(int(value * denominator), count)
                for value, count in values]
    anchor = integers[0][0]
    difference = gcd(*(value - anchor for value, _ in integers))
    if difference == 0:
        return 0
    total = sum(count * ((value - anchor) // difference)
                for (value, count) in integers)
    size = sum(count for _, count in integers)
    return size // gcd(size, total)


def average_state(state, indices):
    indices = tuple(indices)
    if len(indices) != 3 or len(set(indices)) != 3:
        raise ValueError("a real ternary operation needs three distinct positions")
    mean = sum((state[index] for index in indices), F(0)) / 3
    for index in indices:
        state[index] = mean
    return mean


def ternary_equalize(state, indices):
    """Real ternary network for a 3^k block, returning operation count."""
    indices = list(indices)
    if len(indices) == 1:
        return 0
    if len(indices) % 3:
        raise ValueError("target size must be a power of three")
    third = len(indices) // 3
    chunks = [indices[offset * third:(offset + 1) * third]
              for offset in range(3)]
    operations = sum(ternary_equalize(state, chunk) for chunk in chunks)
    for offset in range(third):
        average_state(state, [chunk[offset] for chunk in chunks])
    return operations + third


def b_state(n, u, v):
    r = n - 4
    w = -r * u - 3 * v
    return [F(u)] * r + [F(v)] * 3 + [F(w)]


def replace_child_by_mean(state, indices):
    mean = sum((state[index] for index in indices), F(0)) / len(indices)
    for index in indices:
        state[index] = mean
    return mean


def template_one_data(n, m):
    """B_n -> child B_(n-4), with initial (u^(m-1),v) network."""
    r = n - 4
    if m < 3 or not is_power_three(m) or r < m + 1:
        return None
    child = r
    groups = [(1, m - 1), (0, r - m - 1), (m, 2)]
    smith_g, T, anchor, smith_modulus, smith_numerator = smith_rank_one_groups(
        groups, child, m
    )
    lambda_ = F(T, m * child)
    beta = F(1, 3 * m)
    matrix = ((1 - lambda_, lambda_), (1 - beta, beta))
    determinant = matrix_det(matrix)
    # The child pattern, after multiplying differences by m, is
    # (1^(m-1), 0^(r-m-1), m^2), with gcd 1 and total T.
    return {
        "kind": "T1",
        "n": n,
        "m": m,
        "child": child,
        "q": smith_modulus,
        "T": T,
        "smith_g": smith_g,
        "smith_anchor": anchor,
        "smith_numerator": smith_numerator,
        "matrix": matrix,
        "det": determinant,
        "child_lattice_ok": (smith_numerator % smith_modulus == 0),
        "det_away_unit": gcd(away_three(n),
                               away_three(determinant.numerator)) == 1,
    }


def template_two_data(n, m):
    """B_n -> child B_(n-2), with initial (u^(m-2),v^2) network."""
    r = n - 4
    child = n - 2
    if m < 3 or not is_power_three(m) or r < m - 2:
        return None
    groups = [(2, m - 1), (0, r - m + 2), (m, 1)]
    smith_g, T, anchor, smith_modulus, smith_numerator = smith_rank_one_groups(
        groups, child, m
    )
    lambda_ = F(T, m * child)
    beta = F(2 * (r + 3 * m), 3 * m * child)
    matrix = ((1 - lambda_, lambda_), (1 - beta, beta))
    determinant = matrix_det(matrix)
    return {
        "kind": "T2",
        "n": n,
        "m": m,
        "child": child,
        "q": smith_modulus,
        "T": T,
        "smith_g": smith_g,
        "smith_anchor": anchor,
        "smith_numerator": smith_numerator,
        "matrix": matrix,
        "det": determinant,
        "child_lattice_ok": (smith_numerator % smith_modulus == 0),
        "det_away_unit": gcd(away_three(n),
                               away_three(determinant.numerator)) == 1,
    }


def replay_template(n, m, kind, u, v):
    """Replay all actual operations around an abstract certified child call."""
    state = b_state(n, u, v)
    r = n - 4
    original = tuple(state)
    if kind == "T1":
        # Select m-1 u positions and one v position.
        selected = list(range(m - 1)) + [r]
        a = sum((state[index] for index in selected), F(0)) / m
        ternary_equalize(state, selected)
        assert all(state[index] == a for index in selected)
        child_indices = selected[:m - 1]
        child_indices += list(range(m - 1, r - 2))
        child_indices += [r + 1, r + 2]
        assert len(child_indices) == r
        mu = replace_child_by_mean(state, child_indices)
        residual_a = selected[-1]
        residual_u = [index for index in range(len(state))
                      if state[index] == F(u) and index not in child_indices]
        # The two leftover u positions are the first two available u's.
        assert len(residual_u) >= 2
        b = average_state(state, [residual_a, residual_u[0], residual_u[1]])
        expected = tuple([mu] * r + [b] * 3 + [state[-1]])
        # The state may have duplicate values; compare multisets instead.
        assert Counter(state) == Counter(expected)
        data = template_one_data(n, m)
    elif kind == "T2":
        # Select m-2 u positions and two v positions.
        selected = list(range(m - 2)) + [r, r + 1]
        a = sum((state[index] for index in selected), F(0)) / m
        ternary_equalize(state, selected)
        assert all(state[index] == a for index in selected)
        child_indices = selected[:m - 1]
        child_indices += list(range(m - 2, r))
        child_indices += [r + 2]
        assert len(child_indices) == n - 2
        mu = replace_child_by_mean(state, child_indices)
        # Leave one old a, one old w and two mu's.  Average (a,mu,mu).
        mu_positions = [index for index in range(len(state))
                        if state[index] == mu and index in child_indices]
        assert len(mu_positions) >= 2
        c = average_state(state, [selected[m - 1], mu_positions[0],
                                  mu_positions[1]])
        # The remaining singleton is the original w position.
        w = -(r * F(u) + 3 * F(v))
        assert Counter(state) == Counter([mu] * r + [c] * 3 + [w])
        data = template_two_data(n, m)
    else:
        raise ValueError(kind)
    assert data is not None
    pair = matrix_apply(data["matrix"], (F(u), F(v)))
    assert pair[0] == mu
    assert pair[1] == (b if kind == "T1" else c)
    assert sum(state, F(0)) == sum(original, F(0)) == 0
    return data, state


def check_template_formulas():
    checked = 0
    for n in range(11, 130):
        for m in (3, 9, 27):
            for kind in ("T1", "T2"):
                data = (template_one_data if kind == "T1"
                        else template_two_data)(n, m)
                if data is None:
                    continue
                u, v = F(2), F(-1)
                if kind == "T1":
                    if not data["child_lattice_ok"]:
                        continue
                else:
                    if not data["child_lattice_ok"]:
                        continue
                replay_template(n, m, kind, u, v)
                matrix = data["matrix"]
                assert all(denominator_is_power_three(value)
                           for row in matrix for value in row)
                assert data["det"] == matrix_det(matrix)
                checked += 1
    return checked


def check_smith_conditions():
    checked = 0
    for n in range(11, 301):
        for m in (3, 9, 27, 81):
            for data in (template_one_data(n, m), template_two_data(n, m)):
                if data is None:
                    continue
                q = data["q"]
                T = data["T"]
                assert data["child_lattice_ok"] == (
                    data["smith_numerator"] % q == 0
                )
                # Directly reconstruct the rank-one Smith ideal of the
                # normalized coefficient pattern.
                if data["kind"] == "T1":
                    pattern = [1] * (m - 1) + [0] * (n - 4 - m - 1) + [m] * 2
                else:
                    pattern = [2] * (m - 1) + [0] * (n - 4 - m + 2) + [m]
                differences = [x - pattern[0] for x in pattern]
                smith = gcd(*differences)
                assert smith == data["smith_g"]
                assert sum(pattern) == T == data["T"]
                smith_data = smith_rank_one(pattern, data["child"], m)
                assert smith_data[3] == data["q"]
                assert smith_data[4] == data["smith_numerator"]
                # G_child = s / gcd(s,T); its away part is 1 exactly when
                # the rank-one Smith/Fitting condition holds only when the
                # anchor coefficient is zero.  The general formula uses the
                # affine numerator T-s*anchor above.
                child = data["child"]
                assert (data["smith_numerator"] % data["q"] == 0
                        ) == data["child_lattice_ok"]
                checked += 1
    return checked


def check_determinant_criterion():
    checked = 0
    failures = 0
    for n in range(11, 500):
        for m in (3, 9, 27, 81):
            for data in (template_one_data(n, m), template_two_data(n, m)):
                if data is None or not data["child_lattice_ok"]:
                    continue
                det = data["det"]
                # det is a unit at every away-from-3 prime of n exactly when
                # its reduced numerator has no common away factor with n.
                criterion = data["det_away_unit"]
                direct = all(det.denominator % p and
                             (det.numerator * pow(det.denominator, -1, p)) % p
                             for p in prime_divisors(n))
                assert criterion == direct
                checked += 1
                if not criterion:
                    failures += 1
    return checked, failures


def find_family_examples():
    result = []
    for n in range(11, 800):
        for m in (3, 9, 27, 81, 243):
            for data in (template_one_data(n, m), template_two_data(n, m)):
                if data and data["child_lattice_ok"] and data["det_away_unit"]:
                    result.append((data["kind"], n, m, data["child"],
                                   data["det"]))
    return result


def check_infinite_families_and_boundary():
    """Check two infinite arithmetic families symbolically on a long prefix."""
    checked = 0
    for exponent in range(2, 80):
        n = 3 ** exponent + 4
        data = template_one_data(n, 3)
        assert data["child"] == 3 ** exponent
        assert data["child_lattice_ok"]
        expected_unit = exponent % 6 != 1
        assert data["det_away_unit"] == expected_unit
        if expected_unit:
            checked += 1
        n = 3 ** exponent + 2
        data = template_two_data(n, 3)
        assert data["child"] == 3 ** exponent
        assert data["child_lattice_ok"]
        expected_unit = exponent % 5 != 2
        assert data["det_away_unit"] == expected_unit
        if expected_unit:
            checked += 1

    # Child Smith data alone is insufficient: B_11, m=3 has a solved
    # 9-point child, but det=11/81 destroys the mod-11 witness.
    data = template_two_data(11, 3)
    assert data["child_lattice_ok"] and not data["det_away_unit"]
    assert data["det"] == F(11, 81)
    checked += 1
    return checked


if __name__ == "__main__":
    formulas = check_template_formulas()
    smith = check_smith_conditions()
    determinant_checks, determinant_failures = check_determinant_criterion()
    examples = find_family_examples()
    families = check_infinite_families_and_boundary()
    print("template real-network and 2x2 matrix checks: PASS", formulas)
    print("Smith/Fitting child-lattice checks: PASS", smith)
    print("away-from-3 determinant checks: PASS", determinant_checks,
          "nonunit cases", determinant_failures)
    print("first admissible templates", examples[:12])
    print("infinite-family and determinant-boundary checks: PASS", families)
