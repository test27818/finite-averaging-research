"""Check saved return certificates and shallow independent completeness."""

import json
from pathlib import Path

from analyze_bn_return_macros import explore_one
from search_b12_return_frontier import replay


def verify():
    work = Path(__file__).resolve().parent
    counts = {}
    for depth, expected in ((5, 21), (6, 87), (7, 395)):
        data = json.loads((work/f"b12_return_depth{depth}.json").read_text(encoding="utf-8"))
        assert data["n"] == 12 and data["depth"] == depth
        matrices = set()
        for row in data["returns"]:
            path = tuple(tuple(indices) for indices in row["path"])
            assert len(path) <= depth
            matrix = tuple(row["matrix"])
            assert replay(path) == matrix
            matrices.add(matrix)
        assert len(matrices) == len(data["returns"]) == expected
        counts[depth] = matrices
    reference = set(explore_one((12, 5))["returns"])
    assert reference == counts[5]
    assert counts[5] <= counts[6] <= counts[7]
    print("B12 stored return certificate replay: PASS 503")
    print("B12 independent depth-5 matrix comparison: PASS 21")


def verify_larger_tables():
    work = Path(__file__).resolve().parent
    checked = 0
    for n, depth in ((15, 6), (18, 7)):
        data = json.loads((work/f"b{n}_return_depth{depth}.json").read_text(encoding="utf-8"))
        assert data["n"] == n and data["depth"] == depth
        assert len(data["returns"]) == depth
        for row in data["returns"]:
            path = tuple(tuple(indices) for indices in row["path"])
            assert len(path) <= depth
            assert replay(path, n=n) == tuple(row["matrix"])
            assert row["matrix"][1] == 0
            checked += 1
    print("B15/B18 bounded return table replay: PASS", checked)


if __name__ == "__main__":
    verify()
    verify_larger_tables()
