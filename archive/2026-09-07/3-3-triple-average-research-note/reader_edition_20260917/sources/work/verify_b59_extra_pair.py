"""Exact physical verification of a fixed pair in the extra-atom library."""
import json
from pathlib import Path
from verify_bn_integer_templates import replay,physical_matrix,normalized_matrix
from verify_diagonal_resource_reduction import product

KEYS = ((-77,-4,1432,80),(-60,-3,281,10))


def verify():
    data = json.loads(Path(__file__).with_name("b59_extra_atom_full_returns.json")
                      .read_text(encoding="utf-8"))
    assert data["n"] == 59
    rows = {tuple(item["matrix"]):item["row"] for item in data["hits"]}
    actual = []
    sizes = set()
    for key in KEYS:
        row = rows[key]
        calls = replay(59,row)
        sizes.update(size for size,*_ in calls)
        assert all(size < 59 for size,*_ in calls)
        m = physical_matrix(row)
        assert normalized_matrix(m) == key
        actual.append(m)
    a,b = actual
    cycle = product(b,a)
    assert cycle[0]+cycle[3] == 0
    square = product(cycle,cycle)
    lam = square[0]
    assert lam and square == (lam,0,0,lam)
    assert product(b,a,b,a) == product(a,b,a,b) == square
    assert lam.numerator * pow(lam.denominator,-1,59)%59 == 1
    print("B59 extra pair physical inverses: PASS 2")
    print("actual matrices",actual)
    print("physical scalar",lam,"child sizes",sorted(sizes))
    print("The seed-pair certificate alone does not assert B59 completeness.")


if __name__ == "__main__":
    verify()
