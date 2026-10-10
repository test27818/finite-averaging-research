"""Five-return supply: three rows for an n-root, two for transverse control.

All-parameter feasibility is proved by rational linear inequalities in the note.
This verifier checks prescribed formulas and replays physical operations; no search.
"""
from pathlib import Path
from fractions import Fraction as F
from math import gcd,ceil
from time import perf_counter
import json,sys
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/"work"))
from verify_four_prime_entry_and_band import Ledger
from verify_equal_determinant_root_repair import count_matrix
from verify_two_root_column_completion import mm,invq,det,scale,red
from verify_split_torus_column import column
from verify_upper_band_unrestricted_completion import zy
from verify_uniform_odd_middle_cores import bezout
from verify_square_zero_compiler import check_frozen_files,check_local_links

I=(1,0,0,1)
U=lambda t:(1,t,0,1)
if not __debug__:raise RuntimeError("Assertions required")


def min_h(s,a):
    assert a>=1 and 1<=s<=2*a
    return max(7,ceil(F(9*a+2-s,s)),ceil(F(4*a+s+2,3*a-s)))


def cutoff(s):
    a=(s+1)//2
    return max(3*a*min_h(s,a),3*(a+1)*pair_h(s,a+1))


def pair_h(s,a):
    assert a>=1 and 1<=s<=2*a
    return max(4,ceil(F(3*a+2-s,s)))


def transverse_pair(p,s,a):
    h,rho=divmod(p,3*a)
    assert h>=pair_h(s,a)
    low=max(0,2*a-rho,ceil(F((s-a)*h-a,2)))
    high=min(a*h-1,a*h+rho-a-1,(s*h+a+s-rho)//2-1)
    assert low<=high
    e=low;j=a*h;i=j+a;k=p-i-j
    base=(i,j,k,j-e,k-e,(a-s)*h+a+2*e,s*h)
    other=(i,j,k,base[3]-1,base[4]-1,base[5]+2,base[6])
    return base,other


def rows(p,s,a):
    h,rho=divmod(p,3*a)
    assert h>=min_h(s,a)
    L=max(0,5*a-2*rho,ceil(F((s-a)*h-a,2)),
          ceil(F((s-a)*h+2*a+s-2*rho,2)))
    Ubound=min(a*h-a-int(rho==0),
               (s*h+a+s-rho-2)//2,
               (s*h+4*a+2*s-3*rho)//2)
    assert L<=Ubound,(p,s,a,h,rho,L,Ubound)
    e=L;i=a*(h+1);j=a*h;k=p-i-j
    base=(i,j,k,j-e,k-e,(a-s)*h+a+2*e,s*h)
    neighbor=(i,j,k,base[3]-1,base[4]-1,base[5]+2,base[6])
    moved=(i,j,k,base[3]+3*i-p,base[4]+3*j-p,
           base[5]+3*k-p-s,base[6]+s)
    return base,neighbor,moved


def check_formula(p,s,a):
    r=p+s;n=3*p+s
    base,neighbor,moved=rows(p,s,a)
    J=count_matrix(p,r,base);G=count_matrix(p,r,neighbor);M=count_matrix(p,r,moved)
    assert J[0]+J[3]==G[0]+G[3]==0
    assert M==mm(U(-n),J) and det(M)==det(J)
    assert mm(M,invq(J))==U(-n)
    f=-F(det(J),p);g=-F(det(G),p)
    assert f.denominator==g.denominator==1
    f,g=int(f),int(g)
    assert g-f==a*n
    if gcd(p,a*n)==1:
        assert gcd(f,g)==gcd(f,n)==gcd(g,n)==1
        assert mm(J,J)==scale(p*f,I)
        assert mm(G,G)==scale(p*g,I)
        beta=J[0]
        assert mm(invq(J),G)==(1,-F(beta*n,f),0,F(g,f))
    return (base,neighbor,moved),J,G,M,f,g


def check_pair_formula(p,s,a):
    pair=transverse_pair(p,s,a)
    A,B=[count_matrix(p,p+s,row) for row in pair]
    assert A[0]+A[3]==B[0]+B[3]==0
    f,g=-F(det(A),p),-F(det(B),p)
    assert f.denominator==g.denominator==1
    f,g=int(f),int(g)
    assert g-f==a*(3*p+s)
    if gcd(p,a*(3*p+s))==1:
        assert gcd(f,g)==gcd(f,3*p+s)==1
    return pair,A,B,f,g


def replay_word(p,s,word):
    r=p+s;n=3*p+s;atoms=0
    for a,z in ((F(1),F(0)),(F(0),F(1)),(F(-2,5),F(3,7))):
        raw=[a]*p+[r*z-a]*p+[-p*z]*r
        ledger=Ledger(raw,p)
        groups=[list(range(p)),list(range(p,2*p)),list(range(2*p,n))]
        total=I
        for row in word:
            i,j,k,x,y,u,v=row
            ga,gb,gc=groups
            first=ga[:i]+gb[:j]+gc[:k]
            second=ga[i:2*i]+gb[j:2*j]+gc[k:2*k]
            ledger.average(first);ledger.average(second)
            ga,gb,gc=ga[2*i:],gb[2*j:],gc[2*k:]
            fresh=first+second
            kept,fresh=fresh[:r],fresh[r:]
            left=ga[:x]+gb[:y]+gc[:u]+fresh[:v]
            right=ga[x:]+gb[y:]+gc[u:]+fresh[v:]
            assert len(left)==len(right)==p and len(kept)==r
            assert sorted(left+right+kept)==list(range(n))
            ledger.average(left);ledger.average(right)
            groups=[left,right,kept]
            total=mm(scale(F(1,p*p),count_matrix(p,r,row)),total)
            aa=total[0]*a+total[1]*z;zz=total[2]*a+total[3]*z
            assert all(ledger.state[q]==val for gr,val in zip(groups,(aa,r*zz-aa,-p*zz)) for q in gr)
            atoms+=4
        ledger.independent_replay(raw)
    return atoms


def prime(p):
    return p>=2 and all(p%d for d in range(2,int(p**.5)+1))


def verify_inequality_rays():
    """Check the twelve sufficient affine comparisons used in the written proof."""
    cases=0
    for s in range(1,121):
        for a in ((s+1)//2,(s+1)//2+1):
            H=min_h(s,a)
            for rho in (0,3*a-1):
                A=(s-a)*H-a
                B=(s-a)*H+2*a+s-2*rho
                C=s*H+a+s-rho-2
                D=s*H+4*a+2*s-3*rho
                U1=a*H-a-int(rho==0)
                comparisons=((0,U1),(0,C),(0,D),
                             (5*a-2*rho,U1),(10*a-4*rho,C),(10*a-4*rho,D),
                             (A,2*U1),(A+1,C),(A+1,D),
                             (B,2*U1),(B+1,C),(B+1,D))
                assert all(L<=U for L,U in comparisons),(s,a,H,rho,comparisons)
                cases+=1
            H=pair_h(s,a)
            for rho in (0,3*a-1):
                A=(s-a)*H-a;C=s*H+a+s-rho-2
                upper=min(a*H-1,a*H+rho-a-1)
                comparisons=((0,upper),(0,C),(2*a-rho,upper),
                             (4*a-2*rho,C),(A,2*upper),(A+1,C))
                assert all(L<=U for L,U in comparisons),(s,a,H,rho,comparisons)
                cases+=1
    return cases


def template_obstruction(p,s):
    """Necessary interval for the conservation parameter at a trace-zero base."""
    assert prime(p) and 0<s<p
    # D's available count is p-s, hence |3p+s-tp|<=p-s.
    possible=[t for t in range(-1,7) if abs(3*p+s-t*p)<=p-s]
    assert set(possible)<=set((3,4))
    if 2*s>p:
        assert possible==[4]
        # t4 forces v=p-s; trace congruence forces s*i=0 mod p.
        assert all((s*i)%p for i in range(1,(p-1)//2+1))
        return True
    return False


def main():
    started=perf_counter()
    formula_cases=prime_cases=atoms=terminal_checks=0
    for s in range(1,81):
        A=(s+1)//2
        for a in (A,A+1):
            H=min_h(s,a)
            for h in (H,H+1,H+9):
                for rho in range(3*a):
                    p=3*a*h+rho
                    check_formula(p,s,a);formula_cases+=1
            for h in (pair_h(s,a),pair_h(s,a)+3):
                for rho in range(3*a):
                    check_pair_formula(3*a*h+rho,s,a);formula_cases+=1
    # Full resource-to-terminal checks on actual primes in a variable-s region.
    for p in (127,131,149,211,307,503):
        for s in range(1,min(p,30)):
            if p<cutoff(s):continue
            a=(s+1)//2
            first=check_formula(p,s,a)
            second=check_pair_formula(p,s,a+1)
            J0,J1=first[1],second[1]
            n=3*p+s;swap=(1,0,n,-1)
            T0=mm(swap,scale(F(1,p*p),zy(J0,p)))
            T1=mm(swap,scale(F(1,p*p),zy(J1,p)))
            # -(a)+(a+1)=1
            V=mm(T1,invq(T0))
            assert red(V,n)==(1,pow(-p*p,-1,n),0,1)
            # Choose weaker delta2 at even n to reuse the established complete endpoint interface.
            delta=1 if n%2 else 2
            for k in (-3,0,5):
                column(p,s,delta,V,1+n*k,p*p+n*(k+1),1)
                terminal_checks+=1
            prime_cases+=1
            if p==127 and s in (1,5,9):
                base,neighbor,moved=first[0]
                atoms+=replay_word(p,s,(base,base))
                atoms+=replay_word(p,s,(neighbor,neighbor))
                atoms+=replay_word(p,s,(base,moved))
                for row in second[0]:atoms+=replay_word(p,s,(row,row))
    obstacles=[(p,s) for p in (11,13,17) for s in range(1,10) if 2*s>p]
    assert len(obstacles)==8 and all(template_obstruction(*x) for x in obstacles)
    assert max(cutoff(s) for s in range(1,10))==105
    inequalities=verify_inequality_rays()
    old_cases=json.loads((ROOT/'work/large_symmetric_carrier_shallow_certificate.json').read_text())['cases']
    covered=[(c['p'],c['s']) for c in old_cases if c['p']>=cutoff(c['s'])]
    remaining=[{'p':c['p'],'s':c['s'],'root_pairs':c['root_pairs']} for c in old_cases if c['p']<cutoff(c['s'])]
    assert len(covered)==48 and len(remaining)==114
    assert {(c['p'],c['s']) for c in remaining}.isdisjoint(covered)
    assert {(c['p'],c['s']) for c in remaining}|set(covered)=={(c['p'],c['s']) for c in old_cases}
    for p,s in covered:
        a=(s+1)//2;one=check_formula(p,s,a);two=check_pair_formula(p,s,a+1)
        n=3*p+s;swap=(1,0,n,-1)
        T0=mm(swap,scale(F(1,p*p),zy(one[1],p)))
        T1=mm(swap,scale(F(1,p*p),zy(two[1],p)))
        V=mm(T1,invq(T0))
        assert red(V,n)==(1,pow(-p*p,-1,n),0,1)
        for k in (-5,0,7):
            column(p,s,1 if n%2 else 2,V,1+n*k,p*p+n*(k+2),1)
            terminal_checks+=1
    report={"status":"PASS","prescribed_formula_instances":formula_cases,
            "actual_prime_parameter_cases":prime_cases,
            "complete_terminal_interface_checks":terminal_checks,
            "capacity_affine_endpoint_checks":inequalities,
            "original_position_atoms":atoms,
            "nine_offset_integer_cutoffs":{s:cutoff(s) for s in range(1,10)},
            "single_template_obstruction_pairs":obstacles,
            "root_level":"n","conservation_source_rows":3,"transverse_source_rows":2,
            "total_rows_for_two_alphas":5,
            "old_case_replacements":covered,"replaced_finite_cases":48,
            "remaining_finite_root_cases":114,
            "unchanged_frozen_files":check_frozen_files(),
            "local_links_checked":check_local_links(),
            "seconds":round(perf_counter()-started,3),
            "scope":"Fixed-formula and physical replay checks; no macro search. General capacity is proved by explicit inequalities. Combine the s-dependent formula with the old p>=83 formula to replace48 of162 old root certificates, retaining114. External deep-kernel and base-unit theorems remain."}
    (HERE/'conservation_remaining_root_cases.json').write_text(json.dumps({'scope':'Only remaining old root records; (11,3) uses the separate conservation repair. Not a standalone proof certificate.','replaced_by_uniform_formula':covered,'cases':remaining},indent=2)+'\n',encoding='utf-8')
    (HERE/"conservation_capacity_verification.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:v for k,v in report.items() if k!='old_case_replacements'},indent=2))


if __name__=="__main__":main()
