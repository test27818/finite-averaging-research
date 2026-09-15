"""Exact cone certificate for the ten-position local collision theorem."""

from explore_carrier_catalyst_cone_certificate import (
    descent_quadratics, exceptional_root_cones, generic_root_cones, refine,
    span_rank,
)


def verify():
    quadratics = descent_quadratics()
    assert len(quadratics) == 2805

    generic = generic_root_cones()
    dimensions = {dimension: sum(span_rank(rays) == dimension
                                 for rays in generic)
                  for dimension in (1, 2, 3)}
    assert len(generic) == 30
    assert dimensions == {1: 6, 2: 0, 3: 24}
    generic_leaves = []
    generic_unresolved = []
    for rays in generic:
        result = refine(tuple(rays), quadratics, 0, 24)
        if result is None:
            generic_unresolved.append(rays)
        else:
            generic_leaves.extend(result)
    assert not generic_unresolved
    assert len(generic_leaves) == 538
    assert sum(row[1][1] == "terminal" for row in generic_leaves) == 0
    assert max(row[2] for row in generic_leaves) == 15

    exceptional = exceptional_root_cones()
    exceptional_leaves = []
    exceptional_unresolved = []
    for rays in exceptional:
        result = refine(tuple(rays), quadratics, 0, 24)
        if result is None:
            exceptional_unresolved.append(rays)
        else:
            exceptional_leaves.extend(result)
    assert not exceptional_unresolved
    assert len(exceptional) == 50
    assert len(exceptional_leaves) == 274
    assert sum(row[1][1] == "terminal" for row in exceptional_leaves) == 44
    assert max(row[2] for row in exceptional_leaves) == 7

    labels = [row[1] for row in generic_leaves + exceptional_leaves
              if row[1][1] != "terminal"]
    assert max(len(label[0]) for label in labels) <= 3
    print("carrier catalyst generic cone descent: PASS",
          len(generic), len(generic_leaves), 15)
    print("carrier catalyst exceptional strata and terminals: PASS",
          len(exceptional), len(exceptional_leaves), 44, 7)
    print("ten-position rational collision theorem: PASS")


if __name__ == "__main__":
    verify()
