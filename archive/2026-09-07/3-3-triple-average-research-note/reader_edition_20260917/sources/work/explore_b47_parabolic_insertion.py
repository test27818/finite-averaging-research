"""Exact parabolic interpolation between short known reversible words.

The known U(47/3^k) root group converts integrality into linear congruences.
No state reachability is inferred from an unfinished modular fold.
"""

from math import gcd,isqrt,lcm

from compile_bn_integer_templates import primitive_matrix
from explore_b17_integral_return_cover import mul
from explore_thirteen_modular import Fold,modular_word
from explore_integral_cycle_closure import short_modular_word
from verify_b47_extra_involutions import INTEGER


def det(m):return m[0]*m[3]-m[1]*m[2]


def merge(residue,modulus,other,base):
    common = gcd(modulus,base)
    if (other-residue) % common:return None
    step = ((other-residue)//common)*pow(modulus//common,-1,base//common) % (base//common)
    new_modulus = lcm(modulus,base)
    return (residue+modulus*step) % new_modulus,new_modulus


def solve(coefficients,targets,modulus):
    residue,period = 0,1
    for c,t in zip(coefficients,targets):
        common = gcd(c,modulus)
        if t % common:return None
        base = modulus//common
        other = (t//common)*pow(c//common,-1,base) % base
        result = merge(residue,period,other,base)
        if result is None:return None
        residue,period = result
    if residue>period//2:residue-=period
    return residue,period


def search(max_power=5,max_modular_length=500,max_retained=25,dyadic_power=0):
    basic = dict(INTEGER)
    basic.update({name.lower():primitive_matrix((m[3],-m[1],-m[2],m[0])) for name,m in INTEGER.items()})
    states = {(-1,0,0,-1):''}
    states.update({m:name for name,m in basic.items()})
    for a,x in basic.items():
        for b,y in basic.items():states.setdefault(primitive_matrix(mul(x,y)),b+a)
    result = {}
    for g,wg in states.items():
        for h,wh in states.items():
            determinant = det(g)*det(h)
            if determinant<=0:continue
            root = isqrt(determinant)
            if root*root != determinant:continue
            constant = mul(g,h)
            linear = mul(mul(g,(0,0,1,0)),h)
            for scale,k,e in ((3**k*2**e,k,e) for k in range(max_power+1) for e in range(dyadic_power+1)):
                modulus = scale*root
                solution = solve([47*x for x in linear],[-scale*x for x in constant],modulus)
                if solution is None:continue
                j,period = solution
                for j in set((j,j+period,j-period)):
                    raw = tuple((scale*a+47*j*b)//modulus for a,b in zip(constant,linear))
                    assert det(raw) == 1
                    matrix = primitive_matrix(raw)
                    assert (matrix[0]+matrix[1]-matrix[2]-matrix[3]) % 47 == 0
                    result.setdefault(matrix,(wh,j,k,e,wg))
    print('parabolic insertion short states',len(states),'integral candidates',len(result),flush=True)
    candidates=[]
    for m,w in result.items():
        modular = short_modular_word(m,max_modular_length)
        if modular is not None:candidates.append((len(modular),modular,w,m))
    fold=Fold();table=fold.close();retained=[]
    for _,word,w,m in sorted(candidates):
        if fold.contains(word,table):continue
        fold.loop(word);table=fold.close();retained.append((w,m))
        nodes={fold.root(i) for i in range(len(fold.parent))}
        missing=sum((node,letter) not in table for node in nodes for letter in 'su')
        print('fold',len(nodes),missing,'word',w,flush=True)
        if not missing:
            print('COMPLETE',len(nodes),'CERTIFICATE',retained,flush=True)
            return retained
        if len(retained) >= max_retained:
            print('BOUND retained-generator limit',max_retained,flush=True)
            return retained
    print('BOUND no complete subgroup',len(retained),flush=True)
    return retained


if __name__ == '__main__':search()
