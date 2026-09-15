"""Exact projective matrix exploration; search results are not proofs."""

from math import gcd


def primitive(matrix):
    divisor = gcd(*matrix)
    result = tuple(value // divisor for value in matrix)
    if next(value for value in result if value) < 0:
        result = tuple(-value for value in result)
    return result


def multiply(left, right):
    a, b, c, d = left
    e, f, g, h = right
    return primitive((a * e + b * g, a * f + b * h,
                      c * e + d * g, c * f + d * h))


def inverse(matrix):
    a, b, c, d = matrix
    return primitive((d, -b, -c, a))


def determinant(matrix):
    a, b, c, d = matrix
    return a * d - b * c


IDENTITY = (1, 0, 0, 1)
A = (3, 0, -9, -1)
R = (2, 1, 3, 0)
C = multiply(A, R)


def search(depth):
    generators = {"A": A, "R": R, "a": inverse(A), "r": inverse(R)}
    seen = {IDENTITY: ""}
    frontier = [IDENTITY]
    integral = []
    parabolic = []
    for length in range(1, depth + 1):
        following = []
        for matrix in frontier:
            for letter, generator in generators.items():
                result = multiply(generator, matrix)
                if result in seen:
                    continue
                word = seen[matrix] + letter
                seen[result] = word
                following.append(result)
                det = determinant(result)
                trace = result[0] + result[3]
                if trace * trace == 4 * det:
                    parabolic.append((word, result))
                if abs(det) == 1:
                    integral.append((word, result))
        frontier = following
        print("depth", length, "seen", len(seen), "integral", len(integral),
              "parabolic", len(parabolic), flush=True)
        if parabolic:
            break
    print("integral sample", integral[:30])
    print("parabolic sample", parabolic[:30])


if __name__ == "__main__":
    print("C", C, "C^3", multiply(multiply(C, C), C))
    for middle in (C, multiply(C, C)):
        print("A C^j A", multiply(A, multiply(middle, A)))
        print("a C^j a", multiply(inverse(A), multiply(middle, inverse(A))))
    search(12)
