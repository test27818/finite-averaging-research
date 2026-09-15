"""Replay a fixed acyclic B53 activation certificate without searching words."""
import json
from pathlib import Path
from fractions import Fraction as F
from compile_bn_integer_templates import compile_returns
from verify_bn_integer_templates import replay, physical_matrix, normalized_matrix
from verify_b53_positive_seed import verify as verify_seeds
from verify_diagonal_resource_reduction import product


def inverse(m):
    a,b,c,d = m
    determinant = a*d-b*c
    assert determinant
    return (d/determinant,-b/determinant,-c/determinant,a/determinant)


def verify():
    verify_seeds()
    data = json.loads(Path(__file__).with_name("b53_inverse_closure_certificate.json")
                      .read_text(encoding="utf-8"))
    assert data["n"] == 53
    rows,_ = compile_returns(53,True,True,True)
    assert len(rows) == data["templates"]
    matrices = []
    seen = set()
    seeds = [(-26,-1,433,17),(-229,-14,3816,234)]
    for i,node in enumerate(data["nodes"]):
        key = tuple(node["matrix"])
        assert key not in seen
        seen.add(key)
        row = rows[key]
        calls = replay(53,row)
        assert all(size < 53 for size,*_ in calls)
        matrix = physical_matrix(row)
        assert normalized_matrix(matrix) == key
        if i < 2:
            assert node.get("seed") and key == seeds[i]
        else:
            assert not node.get("seed")
            flank = (F(1),F(0),F(0),F(1))
            for index,sign in node["flank"]:
                assert 0 <= index < i and sign in (-1,1)
                part = matrices[index]
                flank = product(part if sign == 1 else inverse(part),flank)
            cycle = product(flank,matrix)
            order = node["order"]
            assert order in (1,2,3,4,6)
            powered = product(*([cycle]*order))
            assert powered[0] and powered == (powered[0],0,0,powered[0])
            # (F M)^h=lambda I gives M^-1=lambda^-1(F M)^(h-1) F.
            right = product(*([cycle]*(order-1)),flank)
            assert product(right,matrix) == product(matrix,right) == powered
        matrices.append(matrix)
    print("fixed acyclic B53 physical inverse closure: PASS",len(matrices))
    print("No root subgroup or complete B53 criterion has been established.")


if __name__ == "__main__":
    verify()
