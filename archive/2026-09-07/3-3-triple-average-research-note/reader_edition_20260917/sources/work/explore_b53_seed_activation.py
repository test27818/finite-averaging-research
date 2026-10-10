"""Exact bounded activation by finite-order products of known reversible flanks."""
from compile_bn_integer_templates import compile_returns, primitive_matrix
from explore_b17_integral_return_cover import mul
from verify_twenty_five_arithmetic_group import finite_order


def search(depth=5):
    rows,_ = compile_returns(53,True,True,True)
    a,b = (-26,-1,433,17),(-229,-14,3816,234)
    generators = dict(A=a,B=b,a=(a[3],-a[1],-a[2],a[0]),
                      b=(b[3],-b[1],-b[2],b[0]))
    identity = primitive_matrix((1,0,0,1))
    seen = {identity:""}
    frontier = [identity]
    activated = {}
    for level in range(depth+1):
        for flank in frontier:
            for matrix in rows:
                if matrix in (a,b) or matrix in activated:
                    continue
                order = finite_order(mul(flank,matrix))
                if order:
                    activated[matrix] = (seen[flank],order)
                    print("activated",matrix,activated[matrix],flush=True)
        if level == depth:
            break
        following = []
        for matrix in frontier:
            for letter,g in generators.items():
                result = primitive_matrix(mul(g,matrix))
                if result not in seen:
                    seen[result] = seen[matrix]+letter
                    following.append(result)
        frontier = following
    print("templates",len(rows),"flanks",len(seen),"new inverses",len(activated))
    print("Finite search only; negative output is not an impossibility theorem.")


if __name__ == "__main__":
    search()
