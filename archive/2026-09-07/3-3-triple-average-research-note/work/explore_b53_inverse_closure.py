"""Layered short-flank activation with a frozen, acyclic output certificate."""
import json
import argparse
from pathlib import Path
from time import perf_counter
from compile_bn_integer_templates import compile_returns, primitive_matrix
from explore_b17_integral_return_cover import mul
from verify_twenty_five_arithmetic_group import finite_order


def inverse(m):
    return primitive_matrix((m[3],-m[1],-m[2],m[0]))


def search(dimension=53,expanded=False):
    start = perf_counter()
    rows,_ = compile_returns(dimension,True,True,True)
    if expanded:
        data = json.loads(Path(__file__).with_name(f"b{dimension}_extra_atom_full_returns.json").read_text(encoding="utf-8"))
        rows.update({tuple(item["matrix"]):item["row"] for item in data["hits"]})
    keys = sorted(rows)
    seeds = [(-26,-1,433,17),(-229,-14,3816,234)]
    if dimension == 59:
        from verify_b59_extra_pair import KEYS
        seeds = list(KEYS)
    elif dimension != 53:
        raise ValueError("No independently verified seed pair for this dimension")
    nodes = [dict(matrix=m,seed=True) for m in seeds]
    known = set(seeds)
    tested = set()
    for layer in range(1,len(keys)+1):
        letters = [(i,sign,m if sign == 1 else inverse(m))
                   for i,node in enumerate(nodes) for m in [tuple(node["matrix"])]
                   for sign in (1,-1)]
        flanks = {primitive_matrix((1,0,0,1)): []}
        for i,sign,m in letters:
            flanks.setdefault(m,[(i,sign)])
        for i,sign,m in letters:
            for j,sj,n in letters:
                flanks.setdefault(primitive_matrix(mul(n,m)),[(i,sign),(j,sj)])
        pending = [m for m in keys if m not in known]
        print("layer",layer,"known",len(nodes),"flanks",len(flanks),
              "comparison upper bound",len(pending)*len(flanks),flush=True)
        if len(pending)*len(flanks)>2000000:
            print("Comparison budget reached; no closure claim.",flush=True)
            break
        additions = []
        for m in pending:
            for flank,word in flanks.items():
                pair = (flank,m)
                if pair in tested:
                    continue
                tested.add(pair)
                order = finite_order(mul(flank,m))
                if order:
                    additions.append(dict(matrix=m,flank=word,order=order,layer=layer))
                    break
        if not additions:
            break
        nodes.extend(additions)
        known.update(tuple(node["matrix"]) for node in additions)
    suffix = "_expanded" if expanded else ""
    out = Path(__file__).with_name(f"b{dimension}{suffix}_inverse_closure_certificate.json")
    out.write_text(json.dumps(dict(n=dimension,nodes=nodes,templates=len(keys)),indent=2)+"\n",
                   encoding="utf-8")
    print("certified candidates",len(nodes),"comparisons",len(tested),
          "seconds",round(perf_counter()-start,3),flush=True)
    print("standard macro activated",(-3,0,dimension-4,1) in known)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n",type=int,default=53)
    parser.add_argument("--expanded",action="store_true")
    args = parser.parse_args()
    search(args.n,args.expanded)
