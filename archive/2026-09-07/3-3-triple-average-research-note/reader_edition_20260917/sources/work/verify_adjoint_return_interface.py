"""Exact reverse-word adjoints, with every child-call domain rechecked.

A transpose identity alone does not certify a positive reverse macro.
This verifier uses fixed physical subsets and independently tests all
reversed averages plus the original-kernel projection.
"""

from collections import Counter
from fractions import Fraction as F

from compile_bn_integer_templates import compile_returns,solved_size
from verify_bn_integer_templates import physical_matrix,normalized_matrix
from explore_b17_universal_subblocks import universal_call
from verify_flat_star_arithmetic import multiply,inverse


def initial(n):
    return [(F(1),F(0))]*(n-4)+[(F(0),F(1))]*3+[(F(4-n),F(-3))]


def equalize(state,indices):
    mean = tuple(sum(state[i][j] for i in indices)/len(indices) for j in (0,1))
    for i in indices:state[i] = mean
    return mean


def ledger(n,row):
    state = initial(n)
    scalar = F(1)
    normalized = row['source']
    calls = []
    def select(counts):
        result = []
        for (a,b,_),count in zip(normalized,counts):
            target = scalar*a,scalar*b
            result += [i for i,x in enumerate(state) if x == target and i not in result][:count]
        assert len(result) == sum(counts)
        return tuple(result)
    stages = (('first','after_first'),('middle','before_final'))
    if 'extra' in row:
        stages = (('first','after_first'),('middle','before_extra'),('extra','before_final'))
    for key,following in stages:
        positions = select(row[key]['counts'])
        if key == 'first' and len(positions) == 6:
            available = list(positions)
            for _ in range(2):
                triple = []
                for value in ((F(1),F(0)),(F(1),F(0)),(F(0),F(1))):
                    i = next(i for i in available if state[i] == value)
                    available.remove(i)
                    triple.append(i)
                calls.append(tuple(triple))
                equalize(state,triple)
        else:
            calls.append(positions)
            equalize(state,positions)
        scalar *= F(*row[key]['scale'])
        normalized = row[following]
    positions = select(row['final']['counts'])
    remaining = [i for i in range(n) if i not in positions]
    x,y,_ = normalized[row['final']['singleton']]
    singleton = next(i for i in remaining if state[i] == (scalar*x,scalar*y))
    calls.append(positions)
    u = equalize(state,positions)
    repair = [i for i in remaining if i != singleton]+list(positions[:len(positions)-(n-4)])
    assert len(repair) == 3
    calls.append(tuple(repair))
    v = equalize(state,repair)
    w = tuple(-(n-4)*u[j]-3*v[j] for j in (0,1))
    assert len({u,v,w}) == 3
    order = tuple(i for value in (u,v,w) for i,x in enumerate(state) if x == value)
    assert sorted(order) == list(range(n))
    assert u+v == physical_matrix(row)
    return tuple(calls),order


def energy_adjoint(n,matrix):
    m = n-4
    gram = [[F(m*(m+1)),F(3*m)],[F(3*m),F(12)]]
    a,b,c,d = matrix
    return multiply(multiply(inverse(gram),[[a,c],[b,d]]),gram)


def reverse(n,row):
    calls,order = ledger(n,row)
    canonical = initial(n)
    state = [None]*n
    for i,j in enumerate(order):state[j] = canonical[i]
    reverse_calls = tuple(reversed(calls))+(tuple(range(n-4)),tuple(range(n-4,n-1)))
    failures = []
    for step,positions in enumerate(reverse_calls):
        mean = tuple(sum(state[i][j] for i in positions)/len(positions) for j in (0,1))
        block = tuple(Counter(state[i] for i in positions).items())
        if not solved_size(len(positions)) or not universal_call(block,mean):
            failures.append((step,len(positions),block,mean))
        equalize(state,positions)
    target = energy_adjoint(n,physical_matrix(row))
    assert list(state[0]) == target[0] and list(state[n-4]) == target[1]
    assert all(state[i] == state[0] for i in range(n-4))
    return tuple(x for row in target for x in row),reverse_calls,order,tuple(failures)


def investigate(n):
    rows,_ = compile_returns(n,True,True,True)
    accepted = {}
    failure_sizes = Counter()
    for matrix,row in rows.items():
        target,_,_,failures = reverse(n,row)
        if failures:
            failure_sizes.update(size for _,size,_,_ in failures)
        else:
            accepted[normalized_matrix(target)] = matrix
    print('n',n,'forward',len(rows),'universal adjoints',len(accepted),
          'new',len(set(accepted)-set(rows)),'failure sizes',dict(failure_sizes),flush=True)
    if n == 47:
        assert len(rows) == 167 and len(accepted) == 15 and not (set(accepted)-set(rows))
        assert failure_sizes == {45:86,3:121,43:152,9:60,27:111,44:16}
        print('B47 reverse-kernel adjoint identity and exact universal-domain audit: PASS 167 15')
    return accepted


def verify_conformal_inverse_controls():
    # Actual two-parameter core macros at n13 and n7 with closed source blocks.
    checked = 0
    for n,matrices in ((13,((F(1),F(0),F(-3),F(-1,3)),
                           (F(2,3),F(1,3),F(1),F(0)))),
                      (7,((F(1),F(0),F(-1),F(-1,3)),))):
        for matrix in matrices:
            adjoint = tuple(x for row in energy_adjoint(n,matrix) for x in row)
            a,b,c,d = matrix
            # The abstract adjoint formula remains valid without conformality.
            from explore_b17_integral_return_cover import mul
            product = mul(adjoint,matrix)
            assert product != (product[0],0,0,product[0])
            checked += 1
    scalar = (F(1,3),F(0),F(0),F(1,3))
    adjoint = tuple(x for row in energy_adjoint(13,scalar) for x in row)
    assert mul(adjoint,scalar) == (F(1,9),0,0,F(1,9))
    print('energy-adjoint versus scalar-inverse boundary controls: PASS',checked+1)


if __name__ == '__main__':
    investigate(47)
    verify_conformal_inverse_controls()
