"""Validate bounded B59 activation output; never claims closure completeness."""
import json
from pathlib import Path
from fractions import Fraction as F
from compile_bn_integer_templates import compile_returns
from verify_bn_integer_templates import replay,physical_matrix,normalized_matrix
from verify_b59_extra_pair import KEYS,verify as verify_seeds
from verify_b53_inverse_closure import inverse
from verify_diagonal_resource_reduction import product


def verify():
    verify_seeds()
    folder = Path(__file__).parent
    data = json.loads((folder/"b59_expanded_inverse_closure_certificate.json").read_text(encoding="utf-8"))
    extra = json.loads((folder/"b59_extra_atom_full_returns.json").read_text(encoding="utf-8"))
    rows,_ = compile_returns(59,True,True,True)
    rows.update({tuple(item["matrix"]):item["row"] for item in extra["hits"]})
    assert data["n"] == 59 and len(rows) == data["templates"]
    actual = []
    seen = set()
    for i,node in enumerate(data["nodes"]):
        key = tuple(node["matrix"])
        assert key not in seen
        seen.add(key)
        calls = replay(59,rows[key])
        assert all(size<59 for size,*_ in calls)
        matrix = physical_matrix(rows[key])
        assert normalized_matrix(matrix) == key
        if i<2:
            assert key == KEYS[i] and node.get("seed")
        else:
            assert not node.get("seed")
            flank = (F(1),F(0),F(0),F(1))
            for index,sign in node["flank"]:
                assert 0<=index<i and sign in (-1,1)
                m = actual[index]
                flank = product(m if sign==1 else inverse(m),flank)
            order = node["order"]
            assert order in (1,2,3,4,6)
            cycle = product(flank,matrix)
            power = product(*([cycle]*order))
            assert power[0] and power == (power[0],0,0,power[0])
            invword = product(*([cycle]*(order-1)),flank)
            assert product(invword,matrix) == product(matrix,invword) == power
        actual.append(matrix)
    print("B59 acyclic expanded physical inverse certificates: PASS",len(actual))
    print("The33-node certificate is budget-limited; completeness uses later root steps.")


if __name__ == "__main__":
    verify()
