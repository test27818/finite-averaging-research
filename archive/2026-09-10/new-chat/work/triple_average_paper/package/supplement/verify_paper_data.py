"""Check the finite certificate data as transcribed in the LaTeX paper."""

from collections import Counter
from fractions import Fraction
from pathlib import Path
import re

from explore_ten_descent import matrix_mul
from verify_seven_descent_cover import A, B, CERTIFICATE_WORDS, verify_certificate
from verify_ten_descent_cover import SELECTED, SELECTED_PATHS, determinant, replay_path, verify

if not __debug__:
    raise RuntimeError('Assertions are required.')


def labelled_block(source, label, ending):
    return source.split('\\label{' + label + '}', 1)[1].split(ending, 1)[0]


def matrices(block):
    pattern = r'\\mat\{(-?\d+)\}\{(-?\d+)\}\{(-?\d+)\}\{(-?\d+)\}'
    return tuple(tuple(map(int, group)) for group in re.findall(pattern, block))


def main():
    source = (Path(__file__).resolve().parents[1] / 'triple_average_paper.tex').read_text(encoding='utf-8')
    labels = re.findall(r'\\label\{([^}]+)\}', source)
    assert len(labels) == len(set(labels)), 'duplicate labels'
    references = re.findall(r'\\(?:eqref|ref)\{([^}]+)\}', source)
    assert set(references) <= set(labels), 'unresolved source references'

    block = labelled_block(source, 'eq:seven-generators', r'\end{equation}')
    assert matrices(block) == (tuple(x for row in A for x in row), tuple(x for row in B for x in row))
    block = labelled_block(source, 'eq:seven-words', r'\end{equation}')
    assert tuple(re.findall(r'\b[01]+\b', block)) == CERTIFICATE_WORDS
    _, signatures, _, _ = verify_certificate()
    written = re.findall(r'\\sigma_(\d)=\{\}&\(([^)]+)\)', source)
    assert [int(i) for i, _ in written] == list(range(1, 6))
    assert [tuple(map(int, values.split(','))) for _, values in written] == list(signatures.values())
    print('paper seven-point matrices, words and signatures: PASS')

    block = labelled_block(source, 'eq:ten-matrices', r'\end{equation}')
    assert matrices(block) == SELECTED
    grouped, _ = verify()
    block = labelled_block(source, 'tab:ten-signatures', r'\end{table}')
    written_groups = Counter()
    for line in block.splitlines():
        cells = line.split('&')
        if len(cells) != 10 or not cells[0].strip().isdigit():
            continue
        scale, count = int(cells[1]), int(cells[2])
        signature = []
        for cell in cells[3:]:
            if '--' in cell:
                signature.append(None)
            else:
                match = re.search(r'\((\d+),(\d+)\)', cell)
                assert match, cell
                signature.append(tuple(map(int, match.groups())))
        written_groups[(scale, tuple(signature))] += count
    expected = Counter()
    for (scale, signature), count in grouped.items():
        expected[(scale, tuple((g, h) if h is not None else None for g, h in signature))] += count
    assert written_groups == expected

    block = labelled_block(source, 'tab:ten-words', r'\end{table}')
    change = ((Fraction(1), Fraction(0)), (Fraction(3), Fraction(2)))
    inverse = ((Fraction(1), Fraction(0)), (Fraction(-3, 2), Fraction(1, 2)))
    rows = 0
    for line in block.splitlines():
        cells = line.split('&')
        if len(cells) != 4 or not cells[0].strip().isdigit():
            continue
        matrix = SELECTED[int(cells[0]) - 1]
        assert int(cells[1].strip().strip('$')) == determinant(matrix)
        scale = Fraction(cells[2].strip().strip('$'))
        actual = matrix_mul(change, matrix_mul(replay_path(SELECTED_PATHS[matrix]), inverse))
        assert tuple(x for row in actual for x in row) == tuple(scale * x for x in matrix)
        rows += 1
    assert rows == 7
    print('paper ten-point matrices, scales and twelve signatures: PASS')
    print('paper finite data and internal references: PASS')


if __name__ == '__main__':
    main()
