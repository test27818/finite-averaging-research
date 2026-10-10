"""Use the proved U(47 Z[1/6]) root group to activate exact positive inverses.

For a known reversible flank G and candidate B, tr(U(t) G B) is linear
in t. An allowed exact rational root supplies a positive involution cycle.
"""

from fractions import Fraction as F
import argparse
import json
from pathlib import Path

from compile_bn_integer_templates import compile_returns,primitive_matrix
from explore_b17_integral_return_cover import mul
from verify_b47_extra_involutions import INTEGER


def admissible_parameter(value):
    value = F(value,47)
    d = value.denominator
    for prime in (2,3):
        while d % prime == 0:d //= prime
    return d == 1


def search(depth=2,rounds=2):
    rows,_ = compile_returns(47,True,True,True)
    known = {m:('seed',name) for name,m in INTEGER.items()}
    for iteration in range(rounds):
        basic = {}
        for m in known:
            basic[m] = ((m,1),)
            inv = primitive_matrix((m[3],-m[1],-m[2],m[0]))
            basic[inv] = ((m,-1),)
        states = {(-1,0,0,-1):()}
        frontier = {(-1,0,0,-1):()}
        for _ in range(depth):
            following = {}
            for a,wa in frontier.items():
                for b,wb in basic.items():
                    target = primitive_matrix(mul(b,a))
                    if target not in states:
                        following[target] = wa+wb
            states.update(following)
            frontier = following
        additions = {}
        for candidate in rows:
            if candidate in known:continue
            for flank,word in states.items():
                product = mul(flank,candidate)
                a,b,c,d = product
                if not b:continue
                t = F(-a-d,b)
                if admissible_parameter(t):
                    value = mul((1,0,t,1),product)
                    assert value[0]+value[3] == 0
                    assert value[0]*value[3]-value[1]*value[2]
                    additions[candidate] = (word,t)
                    break
        print('root activation round',iteration+1,'flanks',len(states),'new',len(additions),flush=True)
        for m,proof in list(additions.items())[:6]:print('sample',m,proof,flush=True)
        known.update(additions)
        if not additions:break
    print('reversible total',len(known),flush=True)
    return known


def export_certificate(known, path):
    indices = {matrix:index for index,matrix in enumerate(known)}
    nodes = []
    for matrix,proof in known.items():
        if proof[0] == 'seed':
            nodes.append(dict(matrix=matrix,seed=proof[1]))
        else:
            word,t = proof
            nodes.append(dict(matrix=matrix,
                              flank=[(indices[m],sign) for m,sign in word],
                              parameter=(t.numerator,t.denominator)))
    certificate = dict(schema_version=1,n=47,nodes=nodes)
    path.write_text(json.dumps(certificate,indent=2)+'\n',encoding='utf-8')
    print('exported fixed activation certificate',path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--depth',type=int,default=2)
    parser.add_argument('--rounds',type=int,default=3)
    parser.add_argument('--export',type=Path)
    args = parser.parse_args()
    known = search(args.depth,args.rounds)
    if args.export is not None:export_certificate(known,args.export)
