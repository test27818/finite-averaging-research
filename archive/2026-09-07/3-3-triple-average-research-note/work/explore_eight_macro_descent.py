"""Explore exact projective descent certificates for the B_8 family."""

from collections import Counter, deque
from fractions import Fraction as F
from itertools import combinations
from math import gcd, lcm, sqrt
from pathlib import Path
import pickle

from symbolic_two_parameter_macros import b_parameters, b_state, choices, step
from verify_seven_descent_cover import (
    display_root,
    exact_uncovered_set,
    image,
    mul,
    polynomial_value,
    transpose,
    valuation,
)


K8 = ((5, 3), (3, 3))  # Q8(u,v)=5u^2+6uv+3v^2


def primitive_matrix(parameters):
    denominator = lcm(*(entry.denominator for row in parameters for entry in row))
    entries = [int(entry * denominator) for row in parameters for entry in row]
    divisor = gcd(*entries)
    entries = [entry // divisor for entry in entries]
    first = next(entry for entry in entries if entry)
    if first < 0:
        entries = [-entry for entry in entries]
    return (tuple(entries[:2]), tuple(entries[2:]))


def determinant(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def safe_for_parity(matrix, parity):
    # If the output sum is odd, its coordinates have no common factor 2 and
    # the primitive output still satisfies u-v odd.
    output = image(matrix, parity)
    return (output[0] + output[1]) % 2 == 1


def parity_preserving(matrix):
    return all(safe_for_parity(matrix, parity) for parity in ((1, 0), (0, 1)))


def macros(max_depth=5):
    start = b_state(8)
    queue = deque([(start, ())])
    seen = {start}
    found = {}
    while queue:
        state, path = queue.popleft()
        if path:
            for parameters in b_parameters(8, state):
                transform = primitive_matrix(parameters)
                if determinant(transform) and transform not in found:
                    found[transform] = path
        if len(path) == max_depth:
            continue
        for selected, signature in choices(state):
            nxt = step(state, selected)
            if nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, path + (signature,)))
    return found, len(seen)


def cached_macros(max_depth):
    cache_path = Path(__file__).with_name(f"eight_macros_depth_{max_depth}.pickle")
    if cache_path.exists():
        with cache_path.open("rb") as stream:
            return pickle.load(stream)
    result = macros(max_depth)
    with cache_path.open("wb") as stream:
        pickle.dump(result, stream)
    return result


def descent_polynomial(transform, guaranteed_divisor):
    image_form = mul(transpose(transform), mul(K8, transform))
    difference = tuple(
        tuple(guaranteed_divisor ** 2 * K8[i][j] - image_form[i][j]
              for j in range(2))
        for i in range(2)
    )
    return difference[0][0], 2 * difference[0][1], difference[1][1]


def signature(residue, transforms, cap):
    return tuple(min(valuation(coordinate, cap)
                     for coordinate in image(transform, residue))
                 for transform in transforms)


def projective_classes(depth):
    modulus = 3 ** depth
    return ([(1, t) for t in range(modulus)]
            + [(3 * t, 1) for t in range(3 ** (depth - 1))])


def valuation_two(value, cap):
    if value == 0:
        return cap
    exponent = 0
    while exponent < cap and value % 2 == 0:
        exponent += 1
        value //= 2
    return exponent


def two_signature(residue, transforms, cap):
    result = []
    for transform in transforms:
        output = image(transform, residue)
        exponent = min(valuation_two(coordinate, cap) for coordinate in output)
        if exponent == cap:
            result.append(None)
            continue
        reduced = tuple(coordinate // 2 ** exponent for coordinate in output)
        result.append(exponent if (reduced[0] + reduced[1]) % 2 else None)
    return tuple(result)


def valid_two_projective_classes(depth):
    modulus = 2 ** depth
    return ([(1, 2 * t) for t in range(2 ** (depth - 1))]
            + [(2 * t, 1) for t in range(2 ** (depth - 1))])


def approximate_roots(polynomial):
    a, b, c = polynomial
    if c == 0:
        return [] if b == 0 else [-a / b]
    discriminant = b * b - 4 * c * a
    if discriminant <= 0:
        return []
    radius = sqrt(discriminant)
    return sorted(((-b - radius) / (2 * c), (-b + radius) / (2 * c)))


def greedy_seed(polynomials):
    endpoints = sorted(root for polynomial in polynomials
                       for root in approximate_roots(polynomial))
    samples = []
    if endpoints:
        samples.append(F(str(endpoints[0] - max(1.0, abs(endpoints[0])))))
        for left, right in zip(endpoints, endpoints[1:]):
            if right - left > 1e-12 * max(1.0, abs(left), abs(right)):
                samples.append(F(str((left + right) / 2)))
        samples.append(F(str(endpoints[-1] + max(1.0, abs(endpoints[-1])))))
    else:
        samples.append(F(0))

    target = (1 << (len(samples) + 1)) - 1
    covers = []
    for polynomial in polynomials:
        bits = 0
        for index, sample in enumerate(samples):
            if polynomial_value(polynomial, sample) > 0:
                bits |= 1 << index
        if polynomial[2] > 0:
            bits |= 1 << len(samples)
        covers.append(bits)

    selected = []
    covered = 0
    while covered != target:
        best = max(range(len(polynomials)),
                   key=lambda index: (covers[index] & ~covered).bit_count())
        gain = covers[best] & ~covered
        if not gain:
            return []
        selected.append(best)
        covered |= covers[best]
    return selected


def small_exact_certificate(polynomials):
    polynomials = tuple(dict.fromkeys(polynomials))
    selected = greedy_seed(polynomials)
    for _ in range(len(polynomials) + 1):
        chosen = [polynomials[index] for index in selected]
        intervals, points, infinity_covered = exact_uncovered_set(chosen)
        legal_points = [point for point in points
                        if point.rational and point.lo not in (F(-1), F(1))]
        if not intervals and not legal_points and infinity_covered:
            return chosen, intervals, legal_points, infinity_covered

        witness = intervals[0] if intervals else None
        if witness is not None:
            candidate = next((index for index, polynomial in enumerate(polynomials)
                              if index not in selected
                              and polynomial_value(polynomial, witness) > 0), None)
        elif legal_points:
            root = legal_points[0].lo
            candidate = next((index for index, polynomial in enumerate(polynomials)
                              if index not in selected
                              and polynomial_value(polynomial, root) > 0), None)
        elif not infinity_covered:
            candidate = next((index for index, polynomial in enumerate(polynomials)
                              if index not in selected and polynomial[2] > 0), None)
        else:
            raise AssertionError("unreachable certificate state")
        if candidate is None:
            return chosen, intervals, legal_points, infinity_covered
        selected.append(candidate)
    raise AssertionError("certificate refinement did not terminate")


def analyze(max_macro_depth=5, residue_depth=7, two_depth=7):
    found, state_count = cached_macros(max_macro_depth)
    universal = sum(parity_preserving(matrix) for matrix in found)
    print("symbolic states", state_count, "nonsingular maps", len(found),
          "universally parity-preserving", universal, flush=True)

    transforms = tuple(found)
    three_grouped = Counter(signature(residue, transforms, residue_depth)
                            for residue in projective_classes(residue_depth))
    two_grouped = Counter(two_signature(residue, transforms, two_depth)
                          for residue in valid_two_projective_classes(two_depth))
    print("3-adic signatures", len(three_grouped),
          "safe 2-adic signatures", len(two_grouped), flush=True)
    print("all determinants", Counter(abs(determinant(matrix)) for matrix in found),
          flush=True)

    failures = []
    checked = 0
    for three_exponents, three_count in three_grouped.items():
        for two_exponents, two_count in two_grouped.items():
            polynomials = []
            for transform, exponent_three, exponent_two in zip(
                    transforms, three_exponents, two_exponents):
                if exponent_two is None:
                    continue
                divisor = 3 ** exponent_three * 2 ** exponent_two
                polynomials.append(descent_polynomial(transform, divisor))
            chosen, intervals, points, infinity_covered = small_exact_certificate(polynomials)
            checked += 1
            if intervals or points or not infinity_covered:
                failures.append((three_exponents, two_exponents,
                                 three_count * two_count, intervals, points,
                                 infinity_covered))
            elif len(chosen) > 20:
                print("large certificate", len(chosen), flush=True)
    print("combined signatures", checked, "failing signatures", len(failures),
          "failing CRT classes", sum(failure[2] for failure in failures), flush=True)
    for failure in failures[:20]:
        print("failure count", failure[2], "open", len(failure[3]),
              [float(sample) for sample in failure[3]],
              "points", [display_root(root) for root in failure[4]],
              "infinity", failure[5])
    return found, three_grouped, two_grouped, failures


if __name__ == "__main__":
    analyze()
