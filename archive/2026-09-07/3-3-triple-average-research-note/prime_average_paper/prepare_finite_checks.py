"""Extract the exact finite algebra checks, without discovery or random tests."""
import ast
from pathlib import Path
import json
import pprint

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def extract(path, names, renames):
    module = ast.parse((ROOT / path).read_text(encoding='utf-8-sig'))
    selected = []
    class Rename(ast.NodeTransformer):
        def visit_Name(self, node):
            return ast.copy_location(ast.Name(id=renames.get(node.id, node.id), ctx=node.ctx), node)
        def visit_FunctionDef(self, node):
            node.name = renames.get(node.name, node.name)
            return self.generic_visit(node)
    for node in module.body:
        name = node.name if isinstance(node, ast.FunctionDef) else None
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            name = node.targets[0].id
        if name in names:
            selected.append(Rename().visit(node))
    assert len(selected) == len(names)
    parts = []
    for node in selected:
        ast.fix_missing_locations(node)
        if isinstance(node, ast.Assign):
            parts.append(node.targets[0].id + ' = ' + pprint.pformat(ast.literal_eval(node.value), width=84))
        else:
            parts.append(ast.unparse(node))
    return '\n\n'.join(parts)


imports = '''from collections import Counter, deque
from fractions import Fraction as F
from itertools import combinations_with_replacement, product
from math import gcd
import json
from pathlib import Path
if not __debug__:
    raise RuntimeError("Run without -O: all assertions are required.")
'''
five = extract('work/verify_five_three_p_threshold.py',
               {'CERTIFICATE', 'equations', 'linear_system', 'verify_certificate'},
               {'CERTIFICATE':'FIVE_TABLE','equations':'five_equations',
                'linear_system':'five_eliminate','verify_certificate':'verify_five'})
seven = extract('work/verify_seven_three_p_threshold.py',
                {'CERTIFICATE', 'equations', 'eliminate', 'verify_certificate'},
                {'CERTIFICATE':'SEVEN_TABLE','equations':'seven_equations',
                 'eliminate':'seven_eliminate','verify_certificate':'verify_seven'})

extra = r'''
def mm(A, B, modulus):
    a,b,c,d=A; e,f,g,h=B
    return ((a*e+b*g)%modulus,(a*f+b*h)%modulus,
            (c*e+d*g)%modulus,(c*f+d*h)%modulus)

def power(A,k,m):
    out=(1,0,0,1)
    while k:
        if k&1: out=mm(A,out,m)
        A=mm(A,A,m); k//=2
    return out

def closure(generators, modulus):
    I=(1,0,0,1); seen={I}; queue=deque([I])
    while queue:
        A=queue.popleft()
        for B in generators:
            C=mm(B,A,modulus)
            if C not in seen: seen.add(C); queue.append(C)
    return seen

def verify_twenty_two():
    m=1936
    A=(4,1,-1,0); Fm=(1,2,0,7)
    X=tuple(t*pow(7,-1,m)%m for t in mm(Fm,Fm,m))
    assert power(A,440,m)==power(X,440,m)==(1,0,0,1)
    X9=tuple(t*pow(7,-1,9)%9 for t in mm(Fm,Fm,9))
    group=closure([power(A,440,9),power(X9,440,9)],9)
    assert len(group)==648
    assert all((a*d-b*c)%9==1 for a,b,c,d in group)
    units={1}; queue=deque([1])
    while queue:
        u=queue.popleft()
        for f in (-1,5,7):
            v=u*f%m
            if v not in units: units.add(v); queue.append(v)
    all_units={u for u in range(m) if gcd(u,m)==1}
    assert len(units)==440 and len(all_units)==880
    other={3*u%m for u in units}
    assert units.isdisjoint(other) and units|other==all_units
    chi={u:0 for u in units}; chi.update({u:1 for u in other})
    # Matrices in the (z,y) chart; inverse representatives are adjugates.
    matrices=[(7,-1,22,-3),(7,0,44,1),(-15,2,-110,15)]
    matrices += [(d,-b,-c,a) for a,b,c,d in matrices[:2]]
    seen={(0,0):0}; queue=deque([(0,0)])
    while queue:
        x,e=point=queue.popleft()
        for a,b,c,d in matrices:
            denominator=(c*x+d)%m
            assert denominator in all_units
            out=((a*x+b)*pow(denominator,-1,m)%m,e^chi[denominator])
            if out not in seen:
                seen[out]=seen[point]+1; queue.append(out)
    assert len(seen)==3872 and max(seen.values())==8
    return {'auxiliary_group':len(group),'unit_image':len(units),
            'marked_states':len(seen),'maximum_depth':max(seen.values())}

if __name__ == '__main__':
    report={'five':verify_five(),'seven':verify_seven(),
            'twenty_two':verify_twenty_two()}
    Path(__file__).with_name('finite_checks_result.json').write_text(
        json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(report,indent=2))
'''
text = imports + '\n' + five + '\n\n' + seven + '\n' + extra
compile(text, 'finite_checks.py', 'exec')
(HERE/'finite_checks.py').write_text(text, encoding='utf-8', newline='\n')
print('Standalone exact certificate program generated.')
