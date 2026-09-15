"""Exact polyhedral-cone certificates for catalyst height descent."""

from itertools import permutations, product as choices
from fractions import Fraction as F
from math import gcd

import numpy as np

from explore_carrier_catalyst_reduction import root_lines
from explore_carrier_sweep_relations import normalized


H = np.asarray(((7, -3, -3), (-3, 7, -3), (-3, -3, 7)),
               dtype=np.int64)


def primitive_ray(vector):
    values = tuple(map(int, vector))
    divisor = gcd(*(abs(value) for value in values))
    if not divisor:
        return None
    values = tuple(value // divisor for value in values)
    return values


def cross3(a, b):
    return (a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0])


def dot3(a, b):
    return sum(x * y for x, y in zip(a, b))


def cone_rays(normals):
    normals = tuple(tuple(map(int, row)) for row in normals)
    rays = set()
    for i in range(len(normals)):
        for j in range(i):
            ray = cross3(normals[i], normals[j])
            if not any(ray):
                continue
            for sign in (1, -1):
                candidate = tuple(sign * value for value in ray)
                if all(dot3(row, candidate) >= 0 for row in normals):
                    rays.add(primitive_ray(candidate))
    return tuple(sorted(rays))


def generic_root_cones():
    roots = root_lines()
    cones = {}
    for signs in choices(range(4), repeat=len(roots)):
        normals = []
        for code, (u, f) in zip(signs, roots):
            sign_a = 1 if code & 1 else -1
            sign_b = 1 if code & 2 else -1
            hu = H @ u
            q = int(u @ hu)
            normals.extend((tuple(sign_a * int(value) for value in f),
                            tuple(sign_b * int(value) for value in hu),
                            tuple(q * sign_a * int(f[i])
                                  - 2 * sign_b * int(hu[i])
                                  for i in range(3))))
        rays = cone_rays(normals)
        if rays:
            cones.setdefault(rays, signs)
    return cones


def independent_normals(normals):
    basis = []
    for normal in normals:
        normal = tuple(map(int, normal))
        if not any(normal):
            continue
        if not basis:
            basis.append(normal)
        elif len(basis) == 1:
            if any(cross3(basis[0], normal)):
                basis.append(normal)
        elif det3(basis[0], basis[1], normal):
            basis.append(normal)
        if len(basis) == 3:
            break
    return tuple(basis)


def det3(a, b, c):
    return (a[0] * (b[1] * c[2] - b[2] * c[1])
            - a[1] * (b[0] * c[2] - b[2] * c[0])
            + a[2] * (b[0] * c[1] - b[1] * c[0]))


def exceptional_root_cones():
    roots = root_lines()
    cones = {}
    for zero_mask in range(1, 1 << len(roots)):
        zero = [index for index in range(len(roots))
                if zero_mask & (1 << index)]
        nonzero = [index for index in range(len(roots)) if index not in zero]
        equalities = independent_normals([roots[index][1] for index in zero])
        if len(equalities) >= 3:
            continue
        for signs in choices(range(4), repeat=len(nonzero)):
            normals = []
            for code, index in zip(signs, nonzero):
                u, f = roots[index]
                sign_a = 1 if code & 1 else -1
                sign_b = 1 if code & 2 else -1
                hu = H @ u
                q = int(u @ hu)
                normals.extend((tuple(sign_a * int(value) for value in f),
                                tuple(sign_b * int(value) for value in hu),
                                tuple(q * sign_a * int(f[i])
                                      - 2 * sign_b * int(hu[i])
                                      for i in range(3))))
            rays = constrained_rays(equalities, normals)
            dimension = 3 - len(equalities)
            if len(rays) >= dimension and span_rank(rays) == dimension:
                cones.setdefault(rays, (zero_mask, signs))
    return cones


def constrained_rays(equalities, inequalities):
    equalities = tuple(tuple(map(int, row)) for row in equalities)
    inequalities = tuple(tuple(map(int, row)) for row in inequalities)
    rays = set()
    if len(equalities) == 1:
        for normal in inequalities:
            ray = cross3(equalities[0], normal)
            for sign in (1, -1):
                candidate = tuple(sign * value for value in ray)
                if any(candidate) and all(dot3(row, candidate) >= 0
                                             for row in inequalities):
                    rays.add(primitive_ray(candidate))
    elif len(equalities) == 2:
        ray = cross3(equalities[0], equalities[1])
        for sign in (1, -1):
            candidate = tuple(sign * value for value in ray)
            if any(candidate) and all(dot3(row, candidate) >= 0
                                         for row in inequalities):
                rays.add(primitive_ray(candidate))
    return tuple(sorted(rays))


def span_rank(rays):
    rays = tuple(rays)
    if not rays:
        return 0
    if len(rays) == 1:
        return 1
    if all(not any(cross3(rays[0], ray)) for ray in rays[1:]):
        return 1
    for a in range(len(rays)):
        for b in range(a):
            for c in range(b):
                if det3(rays[a], rays[b], rays[c]):
                    return 3
    return 2


def normalize_quadratic(matrix):
    values = tuple(int(value) for value in matrix.reshape(-1))
    divisor = gcd(*(abs(value) for value in values))
    return tuple(value // divisor for value in values)


def descent_quadratics():
    roots = root_lines()
    sweeps = tuple(np.asarray(normalized(3, order), dtype=np.int64)
                   for order in permutations(range(3)))
    result = {}
    matrices = tuple(sweeps)
    words = tuple((index,) for index in range(6))
    for depth in (1, 2, 3):
        if depth > 1:
            old_matrices, old_words = matrices, words
            matrices = tuple(left @ right
                             for left in sweeps for right in old_matrices)
            words = tuple((index,) + word
                          for index in range(6) for word in old_words)
        for matrix, word in zip(matrices, words):
            base = matrix.T @ H @ matrix
            direct = base - H
            result.setdefault(normalize_quadratic(direct),
                              ((word, "none", -1), None))
            for index, (u, f) in enumerate(roots):
                hu = H @ u
                q = int(u @ hu)
                b = matrix.T @ hu
                a = matrix.T @ f
                after = 4 * q * (base - H) - 4 * np.outer(b, b) + q * q * np.outer(a, a)
                result.setdefault(normalize_quadratic(after),
                                  ((word, "after", index), tuple(map(int, a))))

                mu = matrix @ u
                hmu = H @ mu
                q = int(mu @ hmu)
                b = matrix.T @ hmu
                before = 4 * q * (base - H) - 4 * np.outer(b, b) + q * q * np.outer(f, f)
                result.setdefault(normalize_quadratic(before),
                                  ((word, "before", index), tuple(map(int, f))))
    return tuple((np.asarray(values, dtype=np.int64).reshape((3, 3)),
                  label, applicability)
                 for values, (label, applicability) in result.items())


def certifies(matrix, applicability, rays):
    rays = np.asarray(rays, dtype=np.int64)
    if applicability is not None:
        values = rays @ np.asarray(applicability, dtype=np.int64)
        if not (np.all(values > 0) or np.all(values < 0)):
            return False
    gram = rays @ matrix @ rays.T
    return quadratic_maximum_simplex(gram) < 0


def certificate_face(matrix, applicability, rays):
    rays_array = np.asarray(rays, dtype=np.int64)
    gram = rays_array @ matrix @ rays_array.T
    if quadratic_maximum_simplex(gram) >= 0:
        return None
    if applicability is None:
        return ()
    values = rays_array @ np.asarray(applicability, dtype=np.int64)
    if np.all(values > 0) or np.all(values < 0):
        return ()
    if np.all(values >= 0) or np.all(values <= 0):
        zero_face = tuple(ray for ray, value in zip(rays, values) if value == 0)
        if len(zero_face) == len(rays):
            return None
        return zero_face
    return None


def solve_linear(matrix, target):
    size = len(target)
    work = [[F(int(entry)) for entry in row] + [F(int(value))]
            for row, value in zip(matrix, target)]
    for column in range(size):
        pivot = next((row for row in range(column, size)
                      if work[row][column]), None)
        if pivot is None:
            return None
        work[column], work[pivot] = work[pivot], work[column]
        value = work[column][column]
        work[column] = [entry / value for entry in work[column]]
        for row in range(size):
            if row == column:
                continue
            value = work[row][column]
            work[row] = [x - value * y
                         for x, y in zip(work[row], work[column])]
    return tuple(row[-1] for row in work)


def quadratic_value(gram, vector):
    return sum(F(int(gram[i][j])) * vector[i] * vector[j]
               for i in range(len(vector)) for j in range(len(vector)))


def quadratic_maximum_simplex(gram):
    size = len(gram)
    candidates = [F(int(gram[i][i])) for i in range(size)]
    if any(value >= 0 for value in candidates):
        return max(candidates)
    for i in range(size):
        for j in range(i):
            # q(t)=q((1-t)e_j+t e_i), 0<=t<=1.
            second = F(int(gram[i][i] - 2 * gram[i][j] + gram[j][j]))
            first = F(int(2 * (gram[i][j] - gram[j][j])))
            if second < 0:
                t = -first / (2 * second)
                if 0 < t < 1:
                    vector = [F(0)] * size
                    vector[i] = t
                    vector[j] = 1 - t
                    candidates.append(quadratic_value(gram, vector))
    if size == 3:
        k11 = int(gram[0][0] - 2 * gram[0][2] + gram[2][2])
        k22 = int(gram[1][1] - 2 * gram[1][2] + gram[2][2])
        k12 = int(gram[0][1] - gram[0][2] - gram[1][2] + gram[2][2])
        determinant = k11 * k22 - k12 * k12
        if k11 < 0 and determinant > 0:
            linear_one = F(2 * int(gram[0][2] - gram[2][2]))
            linear_two = F(2 * int(gram[1][2] - gram[2][2]))
            x = F(k12 * linear_two - k22 * linear_one,
                  2 * determinant)
            y = F(k12 * linear_one - k11 * linear_two,
                  2 * determinant)
            vector = (x, y, 1 - x - y)
            if all(value > 0 for value in vector):
                candidates.append(quadratic_value(gram, vector))
    return max(candidates)


def inspect():
    cones = generic_root_cones()
    quadratics = descent_quadratics()
    dimensions = {dimension: sum(span_rank(rays) == dimension for rays in cones)
                  for dimension in (1, 2, 3)}
    print("generic root cones", len(cones), "dimensions", dimensions,
          "descent quadratics", len(quadratics))
    missing = []
    certificates = []
    for rays, signs in cones.items():
        hit = next((label for matrix, label, applicability in quadratics
                    if certifies(matrix, applicability, rays)), None)
        if hit is None:
            missing.append((rays, signs))
        else:
            certificates.append((rays, hit))
    print("certified", len(certificates), "missing", len(missing))
    for row in missing[:20]:
        print("missing cone", row)
    for row in certificates[:20]:
        print("certificate", row)
    refined = []
    unresolved = []
    for rays, signs in missing:
        leaves = refine(tuple(rays), quadratics, 0, 24)
        if leaves is None:
            unresolved.append((rays, signs))
        else:
            refined.extend(leaves)
    print("refined certificates", len(refined),
          "terminal", sum(row[1][1] == "terminal" for row in refined),
          "max depth", max((row[2] for row in refined), default=0),
          "unresolved cones", len(unresolved))
    for row in refined[:30]:
        print("refined", row)
    for row in unresolved:
        print("unresolved", row)
    exceptional = exceptional_root_cones()
    exceptional_certified = []
    exceptional_unresolved = []
    for rays, signature in exceptional.items():
        leaves = refine(tuple(rays), quadratics, 0, 24)
        if leaves is None:
            exceptional_unresolved.append((rays, signature))
        else:
            exceptional_certified.extend(leaves)
    print("exceptional cones", len(exceptional),
          "certificates", len(exceptional_certified),
          "terminal", sum(row[1][1] == "terminal"
                          for row in exceptional_certified),
          "max depth", max((row[2] for row in exceptional_certified), default=0),
          "unresolved", len(exceptional_unresolved))
    for row in exceptional_unresolved[:30]:
        print("exceptional unresolved", row)


def primitive_sum(rays):
    return primitive_ray(np.asarray(rays, dtype=np.int64).sum(axis=0))


def refine(rays, quadratics, depth, maximum):
    for matrix, label, applicability in quadratics:
        zero_face = certificate_face(matrix, applicability, rays)
        if zero_face is None:
            continue
        if zero_face:
            face_result = refine(zero_face, quadratics, depth + 1, maximum)
            if face_result is None:
                continue
            return [(rays, label, depth, "open-away-from-zero-face")] + face_result
        return [(rays, label, depth, "closed")]
    if len(rays) == 1 and terminal_ray(rays[0]):
        return [(rays, ((), "terminal", -1), depth, "terminal")]
    if depth >= maximum:
        return None
    if len(rays) == 1:
        return None
    center = primitive_sum(rays)
    if len(rays) == 2:
        children = ((center, rays[1]), (rays[0], center))
    else:
        children = (
            (center, rays[1], rays[2]),
            (rays[0], center, rays[2]),
            (rays[0], rays[1], center),
        )
    output = []
    for child in children:
        result = refine(child, quadratics, depth + 1, maximum)
        if result is None:
            return None
        output.extend(result)
    return output


def terminal_ray(ray):
    return (any(value == 0 for value in ray)
            or any(ray[i] == ray[j] for i in range(3) for j in range(i)))


if __name__ == "__main__":
    inspect()
