"""Generation test in the coarse mod-n x parity container's abelianization.

For s=9 the actual macro group has an additional mod-8 restriction, so this
script cannot certify generation of the true congruence container.
"""

from cyclotomic_schreier import rewrite_modular, schreier_basis
from explore_cyclotomic_group import determinant, inverse, multiply
from explore_cyclotomic_tree import explore
from explore_thirteen_modular import modular_word


def rank_mod(rows, columns, prime):
    basis = {}
    for sparse in rows:
        row = {column: value % prime for column, value in sparse.items()
               if value % prime}
        while row:
            pivot = min(row)
            if pivot not in basis:
                inverse = pow(row[pivot], -1, prime)
                row = {column: value * inverse % prime for column, value in row.items()}
                basis[pivot] = row
                break
            factor = row[pivot]
            existing = basis[pivot]
            for column, value in existing.items():
                new_value = (row.get(column, 0) - factor * value) % prime
                if new_value:
                    row[column] = new_value
                else:
                    row.pop(column, None)
    return len(basis)


def determinant_one_generators(loops):
    """Generate the orientation kernel, including pairs of reversing loops."""
    positive = [matrix for matrix in loops if determinant(matrix) == 1]
    negative = [matrix for matrix in loops if determinant(matrix) == -1]
    if negative:
        anchor_inverse = inverse(negative[0])
        positive.extend(multiply(anchor_inverse, matrix) for matrix in negative[1:])
    return positive


def check(s, radius):
    data = schreier_basis(s)
    orders = data[4]
    loops = explore(s, radius)
    rows = []
    lengths = []
    generators = determinant_one_generators(loops)
    for matrix in generators:
        word = rewrite_modular(modular_word(matrix), data)
        row = {}
        for letter in word:
            column = abs(letter) - 1
            row[column] = row.get(column, 0) + (1 if letter > 0 else -1)
        rows.append(row)
        lengths.append(len(word))
    free = orders.count(0)
    torsion = orders.count(3)
    print("rewritten orientation-kernel generators", len(rows),
          "length max", max(lengths),
          "mean", sum(lengths) // len(lengths), flush=True)
    for prime in (2, 3, 5, 7):
        columns = free + (torsion if prime == 3 else 0)
        restricted = []
        for row in rows:
            restricted.append({column: value for column, value in row.items()
                               if orders[column] == 0 or prime == 3})
        print("mod", prime, "rank", rank_mod(restricted, columns, prime),
              "target", columns, flush=True)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--s", type=int, default=9)
    parser.add_argument("--radius", type=int, default=10)
    arguments = parser.parse_args()
    check(arguments.s, arguments.radius)
