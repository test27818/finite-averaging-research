"""Exact finite boundary checks for punctured projective averaging layers."""

from explore_nonsplit_projective_layers import investigate,layer_matrix,rank


def verify():
    expected = {5:([2,3],2),11:([5,6],4),17:([1,4,13,16],4),
                23:([1,11,12,22],8),29:([8,12,17,21],8)}
    checked = 0
    for p,(singular,commutator_rank) in expected.items():
        determinants,actual_rank,scalar = investigate(p)
        assert [c for c,d in enumerate(determinants) if not d] == singular
        assert actual_rank == commutator_rank and not scalar
        for c in singular:
            matrix = layer_matrix(p,c)
            assert rank(matrix) < len(matrix)
        checked += 1
    print('punctured nonsplit orbit layers and no all-shift scalar boundary: PASS',checked)


if __name__ == '__main__':
    verify()
