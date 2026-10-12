"""Literal checks of the complete local return-product normal form.

Finite enumeration below is an independent audit, not a polynomial algorithm.
No computation timeout or missing product is used as a full-consensus NO.
"""
from itertools import product
from math import gcd
from pathlib import Path
import json

from five_eight_local_products import (source, return_atom, describe_word, realize,
                                      reduce_target, valuation, first_exits,
                                      analyze_scalar, decide_local_target)
from five_eight_exit_language import encode_singleton_pair


def good_g(state):
    content = gcd(*state)
    a,b,c,d = (x//content for x in state)
    return gcd(b-a,c-a,d-a) == 1


def literal_step(state, letter):
    a,b,c,d = state
    if letter == 1:
        selected, rest = (a,a,a,a,b), (a,c,d)
    elif letter == 2:
        selected, rest = (a,a,a,a,c), (b,a,d)
    elif letter == 'D':
        selected, rest = (a,a,a,b,c), (a,a,d)
    else:
        raise ValueError(letter)
    assert sum(selected) % 5 == 0 and len(set(selected)) > 1
    new = (sum(selected)//5,) + rest
    assert 5*new[0] + sum(new[1:]) == 0
    assert 5*new[0]**2 + sum(x*x for x in new[1:]) < 5*a*a + b*b + c*c + d*d
    return new


def audit_words():
    cases = atoms = order_checks = 0
    rejections = 0
    for L in range(1,8):
        for a,q in ((1,1),(2,1),(3,1),(4,1),(6,1),(7,3),(-3,7),(2,-3)):
            for word in product((1,2,'D'), repeat=L):
                state = source(a,q,L)
                all_good = True
                for letter in word:
                    state = literal_step(state,letter)
                    all_good &= good_g(state)
                    atoms += 1
                description = describe_word(word)
                direct = realize(a,q,L,description['blocks'],description['tail'])
                assert direct['state'] == state
                assert direct['all_prefixes_G1'] == all_good == good_g(state)
                reduced = reduce_target(a,q,L,state)
                if all_good:
                    assert reduced['status'] != 'no'
                    if description['blocks']:
                        assert reduced['status'] == 'scalar_membership'
                        assert reduced['scalar'] == description['scalar']
                        assert reduced['return_cost'] == description['return_cost']
                        assert reduced['tail'] == description['tail']
                    else:
                        assert reduced['status'] == 'yes' and reduced['word'] == word
                else:
                    assert reduced['status'] == 'no'
                    rejections += 1
                reversed_blocks = realize(a,q,L,tuple(reversed(description['blocks'])),description['tail'])
                assert reversed_blocks['state'] == state
                assert reversed_blocks['all_prefixes_G1'] == all_good
                cases += 1
                order_checks += 1
    return dict(cases=cases, literal_atoms=atoms, return_order_checks=order_checks,
                exact_G_rejections=rejections)


def product_tables(L, budget):
    """Complete finite tables for audits. Their worst-case size is not polynomial."""
    atoms = {cost: {return_atom(w)[0] for w in product((1,2),repeat=cost-1)}
             for cost in range(1,L+1)}
    products = [{1}] + [set() for _ in range(L)]
    for t in range(1,L+1):
        for cost in range(1,t+1):
            for scalar in products[t-cost]:
                for factor in atoms[cost]:
                    value = scalar * factor
                    if valuation(value,2) <= budget:
                        products[t].add(value)
    return products


def audit_all_states():
    rows = []
    for L in range(1,10):
        for a in (2,3):
            initial = source(a,1,L)
            budget = valuation(initial[3],2)
            direct = {initial}
            for _ in range(L):
                direct = {literal_step(x,letter) for x in direct for letter in (1,2,'D')}
            direct = {x for x in direct if good_g(x)}
            products = product_tables(L,budget)
            represented = set()
            for m in range(L+1):
                for tail in product((1,2),repeat=m):
                    h1,h2 = encode_singleton_pair(tail)
                    for scalar in products[L-m]:
                        u,v = scalar*h1,scalar*h2
                        A,rem = divmod(-initial[3]-u-v,7)
                        assert rem == 0
                        represented.add((A,A+u,A+v,initial[3]))
            assert represented == direct, (a,L,len(direct),len(represented))
            for state in direct:
                assert reduce_target(a,1,L,state)['status'] != 'no'
            exits = {tuple(sorted((out[0],)*5+out[1:])) for state in direct for _,out in first_exits(state)}
            rows.append({'a':a,'L':L,'safe_local_states':len(direct),
                         'safe_outside_exits':len(exits), 'return_product_counts':[len(x) for x in products]})
    return rows


def audit_old_counterexample():
    # The 15-step witness previously excluded every pure-singleton E0 exit.
    # Its eight-step prefix now lies in the complete return-product model.
    a,q,L = 2,1,8
    result = realize(a,q,L,((1,1),(),()),(1,1,2))
    assert result['scalar'] == -88 and result['return_cost'] == 5
    assert result['tail_pair'] == (-16,-21)
    assert result['state'] == (111144,112552,112992,-781264)
    assert result['all_prefixes_G1']
    reduced = reduce_target(a,q,L,result['state'])
    assert reduced['status'] == 'scalar_membership' and reduced['scalar'] == -88
    exits = dict(first_exits(result['state']))
    assert exits['E1'] == (-67056,111144,111144,112992)
    return {'source':source(a,q,L), 'blocks':((1,1),(),()), 'tail':(1,1,2),
            'scalar':-88,'return_cost':5,'local_state':result['state'],
            'successful_E1_exit':exits['E1'], 'two_adic_budget':valuation(result['state'][3],2)}


def audit_arbitrary_targets():
    count = positive = unresolved = partial_yes = partial_no = 0
    for L in range(1,6):
        for a,q in ((2,1),(3,1),(2,-3)):
            initial = source(a,q,L)
            layer = {initial}
            reachable = set(layer)
            for _ in range(L):
                layer = {literal_step(x,letter) for x in layer for letter in (1,2,'D')}
                reachable.update(layer)
            reachable = {x for x in reachable if good_g(x)}
            tables = product_tables(L,valuation(initial[3],2))
            for u in range(-60,61):
                for v in range(-60,61):
                    A,rem = divmod(-initial[3]-u-v,7)
                    if rem:
                        continue
                    target = (A,A+u,A+v,initial[3])
                    reduced = reduce_target(a,q,L,target)
                    if reduced['status'] == 'no':
                        actual = False
                    elif reduced['status'] == 'yes':
                        actual = True
                    else:
                        unresolved += 1
                        actual = reduced['scalar'] in tables[reduced['return_cost']]
                    assert actual == (target in reachable), (a,q,L,target,reduced)
                    partial = decide_local_target(a,q,L,target)
                    if partial['status'] == 'yes':
                        literal = initial
                        for letter in partial['word']:
                            literal = literal_step(literal,letter)
                            assert good_g(literal)
                        assert literal == target and actual
                        partial_yes += 1
                    elif partial['status'] == 'no':
                        assert not actual
                        partial_no += 1
                    positive += actual
                    count += 1
    return {'targets':count,'reachable':positive,'scalar_queries':unresolved,
            'partial_algorithm_yes':partial_yes,'partial_algorithm_no':partial_no}


def audit_scalar_analysis():
    expected = {(1,1),(3,0),(0,3)}
    reached = {(1,1)}
    while True:
        larger = reached | {((-u)%4,(5*v-u)%4) for u,v in reached} | {
            ((5*u-v)%4,(-v)%4) for u,v in reached}
        if larger == reached:
            break
        reached = larger
    assert reached == expected
    totals = {'queries':0,'yes':0,'no':0,'unresolved':0}
    for c in range(13):
        table = product_tables(c,c)[c]
        for R in table:
            assert analyze_scalar(R,c)['status'] != 'no'
        for R in range(-2000,2001):
            answer = analyze_scalar(R,c)
            totals['queries'] += 1
            totals[answer['status']] += 1
            if answer['status'] == 'yes':
                assert R in table
                value = 1
                cost = 0
                for block in answer['blocks']:
                    r,t = return_atom(block)
                    value *= r
                    cost += t
                assert (value,cost) == (R,c)
            elif answer['status'] == 'no':
                assert R not in table
    assert analyze_scalar(-2,7)['status'] == 'unresolved'
    assert analyze_scalar(2,10)['status'] == 'unresolved'
    large = []
    for b,k in ((100,0),(100,50),(100,100),(500,250)):
        c = b+3*k
        R = (-1)**c * 2**b
        answer = analyze_scalar(R,c)
        assert answer['status'] == 'yes'
        modulus = 2**b
        a = (-2*pow(5,c,modulus)*pow(7,-1,modulus)) % modulus
        while a%5 == 0:
            a += modulus
        result = realize(a,1,c,answer['blocks'],())
        assert result['scalar'] == R and result['length'] == c and result['all_prefixes_G1']
        literal = source(a,1,c)
        for block in answer['blocks']:
            for letter in tuple(block)+('D',):
                literal = literal_step(literal,letter)
                assert good_g(literal)
        assert literal == result['state']
        large.append({'b':b,'cost':c,'height_bits':max(abs(x) for x in literal).bit_length()})
    return {'mod4_orbit':sorted(reached),'comparison':totals,'large_constructive_instances':large}


def main():
    record = {'scope':'Exact representation of all local S1/S2/D prefixes from equal exceptions; scalar-product membership remains unresolved.',
              'literal_words':audit_words(), 'complete_state_sets':audit_all_states(),
              'arbitrary_targets':audit_arbitrary_targets(),
              'scalar_analysis':audit_scalar_analysis(),
              'restored_counterexample_prefix':audit_old_counterexample()}
    path = Path(__file__).with_name('five_eight_local_products_verification.json')
    path.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'literal_words':record['literal_words'],
                      'arbitrary_targets':record['arbitrary_targets'],
                      'scalar_analysis':record['scalar_analysis'],
                      'last_state_set_checks':record['complete_state_sets'][-4:],
                      'restored_counterexample_prefix':record['restored_counterexample_prefix']},
                     ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
