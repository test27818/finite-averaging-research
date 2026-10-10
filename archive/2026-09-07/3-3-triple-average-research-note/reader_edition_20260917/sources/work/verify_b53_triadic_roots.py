"""Fixed B53 root and cusp words; no discovery search in verification."""
import json
from fractions import Fraction as F
from pathlib import Path
from verify_b53_inverse_closure import verify as verify_closure, inverse
from verify_diagonal_resource_reduction import product, lower, upper, diagonal


def verify():
    verify_closure()
    data = json.loads(Path(__file__).with_name("b53_inverse_closure_certificate.json")
                      .read_text(encoding="utf-8"))
    matrices = [tuple(map(F,node["matrix"])) for node in data["nodes"]]
    first = product(matrices[0],inverse(matrices[4]))
    second = product(matrices[33],inverse(matrices[52]))
    root = product(first,inverse(second))
    root = tuple(x/root[0] for x in root)
    assert root == lower(F(-53,3))
    a = (F(1),F(0),F(-49,3),F(-1,3))
    ret = (F(26,27),F(1,27),F(-1301,81),F(-49,81))
    from verify_bn_integer_templates import normalized_matrix
    assert normalized_matrix(a) in matrices and normalized_matrix(ret) in matrices
    assert product(a,root,inverse(a)) == lower(F(53,9))
    # Lower(371/27) is root raised to -7, conjugated by A twice.
    shift = product(a,a,lower(F(371,3)),inverse(a),inverse(a))
    assert shift == lower(F(371,27))
    cusp = product(shift,a,a,a,inverse(ret),a)
    assert cusp == (0,1,-1,2)
    c = (F(1),F(0),F(1),F(1))
    moved = product(inverse(c),cusp,c)
    assert moved == upper(1)
    d = product(inverse(c),lower(F(53,3)),a,c)
    assert d == (1,0,0,F(-1,3))
    assert product(inverse(d),upper(1),d) == upper(F(-1,3))
    print("B53 fixed lower root, width-one cusp and triadic dilations: PASS")
    print("Both full triadic root groups follow by powers and conjugation.")
    print("No full localized orbit or B53 completeness is asserted.")


if __name__ == "__main__":
    verify()
