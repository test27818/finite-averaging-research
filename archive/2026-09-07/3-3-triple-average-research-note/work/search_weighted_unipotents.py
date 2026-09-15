"""Search the (27,9,3,1) return group for short unipotent elements."""

from collections import deque

from explore_weighted_kernel_group import determinant, explore


def multiply(left, right):
    size = len(left)
    return tuple(tuple(sum(left[row][k] * right[k][column]
                           for k in range(size))
                       for column in range(size))
                 for row in range(size))


def inverse3(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return ((e * i - f * h, c * h - b * i, b * f - c * e),
            (f * g - d * i, a * i - c * g, c * d - a * f),
            (d * h - e * g, b * g - a * h, a * e - b * d))


def characteristic(matrix):
    trace = sum(matrix[i][i] for i in range(3))
    second = (matrix[0][0] * matrix[1][1]
              + matrix[0][0] * matrix[2][2]
              + matrix[1][1] * matrix[2][2]
              - matrix[0][1] * matrix[1][0]
              - matrix[0][2] * matrix[2][0]
              - matrix[1][2] * matrix[2][1])
    return trace, second, determinant(matrix)


def rank_difference(matrix):
    rows = [[matrix[i][j] - int(i == j) for j in range(3)] for i in range(3)]
    if not any(any(row) for row in rows):
        return 0
    minors = []
    for i in range(3):
        for j in range(i + 1, 3):
            for k in range(3):
                for l in range(k + 1, 3):
                    minors.append(rows[i][k] * rows[j][l] - rows[i][l] * rows[j][k])
    return 2 if any(minors) else 1


def search(seed_depth, word_depth):
    returns = explore((27, 9, 3, 1), seed_depth)
    positive = [matrix for matrix in returns if determinant(matrix) == 1]
    generators = []
    labels = []
    for index, matrix in enumerate(positive):
        generators.extend((matrix, inverse3(matrix)))
        labels.extend((str(index), str(index).upper()))
    identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    seen = {identity: ""}
    frontier = [identity]
    for level in range(1, word_depth + 1):
        following = []
        for current in frontier:
            word = seen[current]
            for label, generator in zip(labels, generators):
                output = multiply(generator, current)
                if output in seen:
                    continue
                output_word = word + label
                seen[output] = output_word
                following.append(output)
                if characteristic(output) == (3, 3, 1):
                    print("UNIPOTENT depth", level, "rank", rank_difference(output),
                          "word", output_word, "matrix", output, flush=True)
                    return output_word, output
        frontier = following
        print("group depth", level, "states", len(seen), flush=True)
    print("NO UNIPOTENT through", word_depth)
    return None


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--seed-depth", type=int, default=7)
    parser.add_argument("--word-depth", type=int, default=7)
    arguments = parser.parse_args()
    search(arguments.seed_depth, arguments.word_depth)
