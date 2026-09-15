"""Find the first Bruhat--Tits macro loop that completes mod-2 homology."""

from check_cyclotomic_abelianization import determinant_one_generators
from cyclotomic_schreier import rewrite_modular, schreier_basis
from explore_cyclotomic_group import determinant
from explore_cyclotomic_tree import explore
from explore_thirteen_modular import modular_word


def free_mask(word, orders):
    mask = 0
    for letter in word:
        column = abs(letter) - 1
        if orders[column] == 0:
            mask ^= 1 << column
    return mask


def insert(mask, basis):
    while mask:
        pivot = mask.bit_length() - 1
        if pivot not in basis:
            basis[pivot] = mask
            return True
        mask ^= basis[pivot]
    return False


def orthogonal_character(basis, free_columns):
    """Return a nonzero bit vector orthogonal to all current rows."""
    pivot_rows = {}
    for row in basis.values():
        value = row
        while value:
            pivot = value.bit_length() - 1
            if pivot in pivot_rows:
                value ^= pivot_rows[pivot]
            else:
                pivot_rows[pivot] = value
                break
    pivot_columns = set(pivot_rows)
    free = next(column for column in free_columns if column not in pivot_columns)
    solution = 1 << free
    for pivot in sorted(pivot_columns):
        row = pivot_rows[pivot]
        if (row & solution).bit_count() & 1:
            solution |= 1 << pivot
    assert all(not ((row & solution).bit_count() & 1)
                   for row in basis.values())
    return solution


def search(s, base_radius, target_radius):
    data = schreier_basis(s)
    orders = data[4]
    free_columns = [index for index, order in enumerate(orders) if order == 0]
    basis = {}
    old_loops = explore(s, base_radius)
    for matrix in determinant_one_generators(old_loops):
        word = rewrite_modular(modular_word(matrix), data)
        insert(free_mask(word, orders), basis)
    print("base rank", len(basis), "target", len(free_columns), flush=True)
    character = orthogonal_character(basis, free_columns)
    support = [column + 1 for column in free_columns if character >> column & 1]
    print("missing character support", support, flush=True)

    old = set(old_loops)
    for matrix, macro_word in explore(s, target_radius).items():
        if matrix in old or determinant(matrix) != 1:
            continue
        word = rewrite_modular(modular_word(matrix), data)
        mask = free_mask(word, orders)
        if (mask & character).bit_count() & 1:
            print("COMPLETES rank", len(basis) + 1, flush=True)
            print("macro word", macro_word, flush=True)
            print("matrix", matrix, flush=True)
            print("modular length", len(modular_word(matrix)), flush=True)
            print("Schreier length", len(word), flush=True)
            return macro_word, matrix, word
    print("NO COMPLETION through radius", target_radius, flush=True)
    return None


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--s", type=int, default=9)
    parser.add_argument("--base-radius", type=int, default=10)
    parser.add_argument("--target-radius", type=int, default=12)
    arguments = parser.parse_args()
    search(arguments.s, arguments.base_radius, arguments.target_radius)
