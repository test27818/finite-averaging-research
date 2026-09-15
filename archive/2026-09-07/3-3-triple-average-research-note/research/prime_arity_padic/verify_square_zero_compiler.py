"""Independent finite checks; write only inside this research directory."""
from fractions import Fraction as F
from math import gcd
from pathlib import Path
import hashlib
import json
import re

from square_zero_compiler import (
    IDENTITY,compile_correction,conjugate,determinant,inverse,lower,multiply,
    residue,upper,
)

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]


def target_for(level,seed):
    return multiply(multiply(upper(level*(seed+1)),lower(level*(2-seed))),upper(-level*(seed+2)))


def check_general_compiler():
    specifications=(
        (25,(1,1,5,1)),
        (8,(1,1,2,1)),
        (27,(1,1,0,2)),
        (81,(1,1,0,8)),
        (45,(1,1,0,2)),
        (84,(1,1,2,1)),
        (15,(1,1,-3,-1)), # trace0: full defect, a deliberate non-surjective case
        (72,(F(1,5),F(1,5),F(2,5),F(1,5))),
    )
    checks=0
    for h,T in specifications:
        defect=gcd(residue(T[0]+T[3],h),h)
        for seed in range(4):
            target=target_for(defect*h,seed)
            result=compile_correction(T,h,target)
            assert result['defect']==defect
            assert multiply(result['correction'],result['deep_tail'])==target
            checks+=1
    try:
        compile_correction((1,1,-3,-1),15,upper(15))
    except ValueError as error:
        assert 'tangent image' in str(error)
    else:
        raise AssertionError('Expected exact tangent-image obstruction')
    return checks,1


def reflection(p,s,row):
    i,j,k,x,y,u,v=row
    r=p+s;n=3*p+s
    assert i+j+k==x+y+u+v==p and min(row)>=0
    assert 2*i<=p and 2*j<=p and 2*k<=r
    assert x<=p-2*i and y<=p-2*j and u<=r-2*k and v<=p-s
    alpha=i-j;beta=r*j-p*k
    assert p*(x-y)+alpha*v==beta
    Q=p*r*y-p*p*u+v*beta
    J=(F(beta),F(Q),F(-alpha),F(-beta))
    scalar=beta*beta-alpha*Q
    assert multiply(J,J)==(scalar,0,0,scalar)
    assert scalar%n==pow(p,4,n)
    return J


def check_retained_sources():
    path=ROOT/'work/large_symmetric_carrier_shallow_certificate.json'
    cases=json.loads(path.read_text(encoding='utf-8'))['cases']
    assert len(cases)==162
    checks=0
    for case in cases:
        p,s=case['p'],case['s'];n=3*p+s
        delta=0
        for pair in case['root_pairs']:
            i,j=pair[0][:2];alpha=i-j
            delta=gcd(delta,n*(2*j+alpha)-2*p*p)
        if (p,s)==(11,3):
            delta=2 # after the explicitly retained original auxiliary13 repair
        J0,J1=[reflection(p,s,row) for row in case['direction']]
        change=(0,1,1,p)
        T=tuple(v/F(p**4) for v in conjugate(change,multiply(J0,J1)))
        h=delta*n
        defect=gcd(residue(T[0]+T[3],h),h)
        assert defect==(1 if n%2 else 2)
        for seed in range(3):
            compile_correction(T,h,target_for(defect*h,seed))
            checks+=1
    return len(cases),checks


def count_formula(p,s,alpha,h,e):
    i=alpha*(h+1);j=alpha*h;k=p-2*alpha*h-alpha
    return (i,j,k,alpha*h-e,k-e,(alpha-s)*h+alpha+2*e,s*h)


def check_uniform_formula():
    count=0
    for p in (83,89,97,307,1009):
        for s in range(1,10):
            a0=s//3+1
            for alpha in (a0,a0+1):
                q=p//(3*alpha)
                for h in (q-1,q):
                    rho=p-3*alpha*h
                    e0=max(0,2*alpha-rho,((s-alpha)*h-alpha+1)//2)
                    for e in range(e0,e0+3):
                        reflection(p,s,count_formula(p,s,alpha,h,e));count+=1
    example=count_formula(83,1,1,26,0)
    assert example==(27,26,30,26,30,1,26)
    J=reflection(83,1,example)
    assert J==(-306,194315,-1,306)
    assert multiply(J,J)==(-83*1213,0,0,-83*1213)
    return count


def check_frozen_files():
    records=json.loads((HERE/'existing_documents_snapshot.json').read_text(encoding='utf-8'))
    changed=[]
    for name,digest in records.items():
        path=ROOT/name
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest()!=digest:
            changed.append(name)
    assert not changed,changed
    return len(records)


def check_local_links():
    count=0
    for path in HERE.glob('*.md'):
        text=path.read_text(encoding='utf-8')
        assert '???' not in text and '\ufffd' not in text
        for target in re.findall(r'\[[^\]\n]+\]\(([^\)\n]+)\)',text):
            if target.startswith(('https://','http://')):continue
            target=target.split('#',1)[0]
            assert (path.parent/target).is_file(),(path,target)
            count+=1
    return count


def main():
    if not __debug__:raise RuntimeError('Assertions required')
    general,rejections=check_general_compiler()
    cases,compiled=check_retained_sources()
    formulas=check_uniform_formula()
    frozen=check_frozen_files()
    links=check_local_links()
    report={
        'status':'PASS',
        'general_exact_compilations':general,
        'exact_obstruction_rejections':rejections,
        'existing_certificate_cases_read_only':cases,
        'existing_case_exact_compilations':compiled,
        'uniform_formula_instances':formulas,
        'unchanged_existing_documents_and_indexes':frozen,
        'local_links_checked':links,
        'scope':'Exact finite compiler/formula checks, including composite moduli, dyadic and higher trace defects, rational T denominators, and an excluded tangent image. General statements are proved in the accompanying documents. No new averaging words or deep-kernel extraction algorithm.',
    }
    (HERE/'verification_results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
