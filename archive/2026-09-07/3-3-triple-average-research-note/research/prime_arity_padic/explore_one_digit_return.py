"""Bounded exact search for a *legal integer return*, not a reachability oracle.

Compress equal values, prune by integer divisibility and G, force integer
outputs in the last two moves, and memoize failed states. No primitive
rescaling is used: the single p-adic digit remains a physical budget.
"""
from collections import Counter
from fractions import Fraction
from math import gcd
from time import perf_counter
import argparse
import json
from pathlib import Path
from verify_critical_endpoint_precision_return import choices


class Budget(Exception):
    pass


def good(state, p):
    if not any(state):
        return True
    content = gcd(*state)
    d = gcd(*(x-state[0] for x in state)) // content
    while d % p == 0:
        d //= p
    return d == 1


def solve(p, steps=6, node_limit=100000):
    begin = perf_counter()
    original = (1,)*(p+2)+(2,)*(p-2)+(2-3*p,)
    failed = set()
    nodes = 0
    starts = 0
    initial = Counter(original)

    def successors(state, remaining):
        counts = Counter(state)
        vals = tuple(sorted(counts))
        bounds = tuple(counts[v] for v in vals)
        frac = sum(c for v,c in counts.items() if v % p)
        out = []
        modulus = p*p if remaining <= 2 else p
        for take in choices(bounds, p):
            if sum(c > 0 for c in take) == 1:
                continue
            total = sum(c*v for c,v in zip(take,vals))
            if total % modulus:
                continue
            selected_frac = sum(c for c,v in zip(take,vals) if v % p)
            mean = total // p
            new_frac = frac-selected_frac+(p if mean % p else 0)
            if new_frac > p*(remaining-1):
                continue
            nxt_counts = {v:c-k for v,c,k in zip(vals,bounds,take) if c>k}
            nxt_counts[mean] = nxt_counts.get(mean,0)+p
            nxt = tuple(v for v,c in sorted(nxt_counts.items()) for _ in range(c))
            if not good(nxt,p):
                continue
            energy = sum(c*v*v for v,c in nxt_counts.items())
            selected = tuple(v for v,c in zip(vals,take) for _ in range(c))
            out.append((new_frac, energy, nxt, selected))
        out.sort(key=lambda x:(x[0],x[1]))
        return out

    def visit(state, remaining):
        nonlocal nodes
        if all(x % p == 0 for x in state):
            return []
        if remaining == 0 or (state,remaining) in failed:
            return None
        nodes += 1
        if nodes > node_limit:
            raise Budget
        frac = sum(x % p != 0 for x in state)
        if frac > p*remaining:
            return None
        if remaining == 1:
            if frac > p:
                return None
            noninteger = tuple(x for x in state if x % p)
            ints = Counter(x for x in state if x % p == 0)
            vals = tuple(sorted(ints))
            needed = p-frac
            if not vals:
                tuples = [()] if needed == 0 else []
            else:
                tuples = choices(tuple(ints[v] for v in vals),needed)
            for take in tuples:
                selected = noninteger+tuple(v for v,c in zip(vals,take) for _ in range(c))
                if len(selected) != p or sum(selected) % (p*p):
                    continue
                mean = sum(selected)//p
                rest = Counter(state)
                rest.subtract(Counter(selected))
                rest[mean] += p
                nxt = tuple(v for v,c in sorted(rest.items()) for _ in range(c))
                if good(nxt,p):
                    return [selected]
            failed.add((state,remaining))
            return None
        for _,_,nxt,selected in successors(state,remaining):
            tail = visit(nxt,remaining-1)
            if tail is not None:
                return [selected]+tail
        failed.add((state,remaining))
        return None

    result = None
    try:
        for c in sorted(initial):
            pool = initial.copy()
            pool[c] -= 1
            vals = tuple(sorted(pool))
            for take in choices(tuple(pool[v] for v in vals),p):
                A = sum(v*k for v,k in zip(vals,take))
                B = -c-A
                if A > B or A % p == 0 or B % p == 0:
                    continue
                state = tuple(sorted((A,)*p+(B,)*p+(p*c,)))
                if not good(state,p):
                    continue
                starts += 1
                tail = visit(state,steps-2)
                if tail is not None:
                    first = tuple(p*v for v,k in zip(vals,take) for _ in range(k))
                    second = tuple(p*v for v,k in zip(vals,take) for _ in range(pool[v]-k))
                    result = [first,second]+tail
                    break
            if result is not None:
                break
        status = 'found' if result is not None else 'exhausted_two_initial_disjoint_blocks'
    except Budget:
        status = 'budget_exhausted'
    output = {'p':p,'step_bound':steps,'status':status,'expanded_nodes':nodes,
              'initial_pairs':starts,'seconds':round(perf_counter()-begin,3),
              'scope':'Search fixes the first two operations to disjoint fractional blocks; exhaustion is not general impossibility for longer words.'}
    if result is not None:
        actual = list(map(Fraction,original))
        positions = []
        states = []
        for selected in result:
            used = set()
            for value in selected:
                target = Fraction(value,p)
                i = next(i for i,x in enumerate(actual) if i not in used and x == target)
                used.add(i)
            assert len(used) == p
            mean = sum(actual[i] for i in used)/p
            for i in used:
                actual[i] = mean
            assert all(p % x.denominator == 0 for x in actual)
            assert good(tuple(int(p*x) for x in actual),p)
            positions.append(sorted(used))
            states.append([[str(v),m] for v,m in sorted(Counter(actual).items())])
        assert all(x.denominator == 1 for x in actual)
        assert sum(x*x for x in actual) < sum(x*x for x in original)
        output.update(initial=list(original),positions=positions,
                      selected_scaled_values=result,states=states)
    return output


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--p',type=int,required=True)
    parser.add_argument('--steps',type=int,default=6)
    parser.add_argument('--node-limit',type=int,default=100000)
    parser.add_argument('--output')
    args=parser.parse_args()
    result=solve(args.p,args.steps,args.node_limit)
    if args.output:
        Path(args.output).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
