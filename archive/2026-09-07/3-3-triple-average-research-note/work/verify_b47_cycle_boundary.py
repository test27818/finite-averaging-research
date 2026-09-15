"""Exact modular sieve for finite-order words in the current B47 library.

Every rational finite-projective-order2x2 matrix satisfies trace^2=k det
for k=0,1,2,3,4. Modular rejection is therefore rigorous, including at
primes dividing a determinant. Exact integer checks decide all survivors.
"""

from time import perf_counter

import numpy as np

from compile_bn_integer_templates import compile_returns,primitive_matrix
from explore_b17_integral_return_cover import mul
from verify_twenty_five_arithmetic_group import finite_order
from audit_bn_current_cycles import a_power_candidates


def candidates(left,right,prime):
    trace = (left@right[:,[0,2,1,3]].T) % prime
    da = (left[:,0]*left[:,3]-left[:,1]*left[:,2]) % prime
    db = (right[:,0]*right[:,3]-right[:,1]*right[:,2]) % prime
    det = da[:,None]*db[None,:] % prime
    trace2 = trace*trace % prime
    possible = trace == 0
    for k in (1,2,3,4):
        possible |= trace2 == k*det % prime
    return zip(*np.nonzero(possible))


def exact_join_cycles(matrices,batch_size=128):
    prime = 1000003
    # Four residue products, determinant products and trace squares fit int64.
    assert 4*(prime-1)**2 < 2**63
    residues = np.array([[x % prime for x in m] for m in matrices],dtype=np.int64)
    found = []
    survivors = 0
    started = perf_counter()
    last_update = started
    for offset in range(0,len(matrices),batch_size):
        for i,j in candidates(residues[offset:offset+batch_size],residues,prime):
            i,j = offset+int(i),int(j)
            survivors += 1
            order = finite_order(mul(matrices[i],matrices[j]))
            if order:found.append((i,j,order))
        if perf_counter()-last_update >= 15:
            print('exact modular join prefixes',min(offset+batch_size,len(matrices)),
                  'of',len(matrices),'integer survivors',survivors,flush=True)
            last_update = perf_counter()
    return found,survivors


def verify_sieve_controls():
    matrices = [(1,0,0,1),(1,1,0,1),(0,-1,1,0),(0,-1,1,1),
                (1,-1,1,1),(0,-3,1,3),(3,0,0,3),(1,0,0,-1)]
    prime = 101
    residues = np.array([[x % prime for x in m] for m in matrices],dtype=np.int64)
    proposed = {(int(i),int(j)) for i,j in candidates(residues,residues,prime)}
    exact = {(i,j) for i,a in enumerate(matrices) for j,b in enumerate(matrices) if finite_order(mul(a,b))}
    assert exact <= proposed
    assert {finite_order(m) for m in matrices} >= {1,2,3,4,6,None}
    singular_mod_prime = np.array([[prime,0,0,1],[1,0,0,prime]],dtype=np.int64) % prime
    assert (0,1) in {(int(i),int(j)) for i,j in candidates(singular_mod_prime,singular_mod_prime,prime)}
    print('exact cycle sieve finite-order and parabolic controls: PASS',len(exact))


def verify():
    verify_sieve_controls()
    rows,_ = compile_returns(47,True,True,True)
    assert len(rows) == 167
    keys = sorted(rows)
    pairs = sorted({primitive_matrix(mul(a,b)) for a in keys for b in keys})
    assert len(pairs) == 27160
    triples = 0
    for a in keys:
        for b in keys:
            ab = mul(a,b)
            for c in keys:
                assert finite_order(mul(ab,c)) is None
                triples += 1
    assert all(finite_order(m) is None for m in pairs+keys)
    powers = sum(len(a_power_candidates(47,m)) for m in pairs)
    assert powers == 0
    print('B47 exact cycles through length3 and all exponents A^j BC: PASS',triples,len(pairs),flush=True)
    cycles,survivors = exact_join_cycles(pairs)
    assert not cycles
    print('B47 exact four-factor exclusion via integer modular sieve: PASS',len(pairs)**2,survivors)


if __name__ == '__main__':
    verify()
