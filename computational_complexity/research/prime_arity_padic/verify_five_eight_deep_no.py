"""One exact deep NO certificate; neither an infinite family nor NP-hardness.

Enumerates physical retained multisets, independently of the compressed core
solver. Uses only the established integrality and G necessary conditions.
"""
from collections import Counter
from functools import lru_cache
from math import gcd
from pathlib import Path
import json
from verify_subcritical_uniform_np_hard import retained_multisets
from five_eight_first_escape import FirstEscape


def main():
    stats = Counter()
    def normalize(x):
        g = gcd(*x)
        return tuple(sorted(v//g for v in x)) if g else tuple(x)

    @lru_cache(None)
    def audit(x):
        stats['states'] += 1
        if not any(x):
            return True,0
        children = set()
        for kept in retained_multisets(x,3):
            total = -sum(kept)
            if total % 5:
                stats['noninteger_types'] += 1
                continue
            raw = tuple(sorted((total//5,)*5+kept))
            if raw == x:
                continue
            assert sum(raw) == 0 and sum(t*t for t in raw) < sum(t*t for t in x)
            y = normalize(raw)
            if any(y) and gcd(*(v-y[0] for v in y)) != 1:
                stats['G_obstructions'] += 1
                continue
            children.add(y)
        answers = [audit(y) for y in children]
        stats['edges'] += len(children)
        return any(yes for yes,_ in answers),1+max((h for _,h in answers),default=-1)

    L,q = 14,1350498525211
    U = 5**L*q
    values = (1,)*5+(1+U,1+U,-7-2*U)
    assert sum(values) == 0 and gcd(*values) == 1
    answer,height = audit(tuple(sorted(values)))
    assert not answer
    core = (values[0],)+values[5:]
    escape = FirstEscape().decide(core)
    assert escape['possible'] and len(escape['word']) == L+1
    current = core
    for letter in escape['word']:
        a,b,c,d = current
        if letter == 'S1':
            selected,rest = (a,a,a,a,b),(a,c,d)
        elif letter == 'S2':
            selected,rest = (a,a,a,a,c),(b,a,d)
        elif letter == 'D':
            selected,rest = (a,a,a,b,c),(a,a,d)
        elif letter == 'E0':
            selected,rest = (a,a,a,a,d),(a,b,c)
        else:
            raise AssertionError('unexpected letter in the deep-construction certificate')
        assert sum(selected)%5 == 0 and len(set(selected)) > 1
        current = (sum(selected)//5,)+rest
        raw = normalize((current[0],)*5+current[1:])
        assert gcd(*(v-raw[0] for v in raw)) == 1
    record = {'scope':'One exact deep unsolvable input; no infinite family or NP-hard conclusion.',
              'L':L,'q':q,'source':values,'reachability':answer,
              'longest_G1_integer_path':height,'stats':dict(stats),
              'first_escape_word':escape['word'],'unscaled_first_exit':current}
    output = Path(__file__).with_name('five_eight_deep_no_verification.json')
    output.write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in record.items() if k!='unscaled_first_exit'},indent=2))


if __name__ == '__main__':
    main()
