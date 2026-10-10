"""Equal-determinant output change replaces the auxiliary13 group computation."""
from pathlib import Path
from fractions import Fraction as F
from math import gcd
from random import Random
from time import perf_counter
import json,sys

sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/"work"))
from verify_four_prime_entry_and_band import Ledger
from verify_uniform_odd_middle_cores import mm,invq,bezout
from verify_upper_band_unrestricted_completion import zy
from verify_split_torus_column import column,supported
from verify_two_root_column_completion import red,scale,det
from verify_square_zero_compiler import check_frozen_files,check_local_links

I=(1,0,0,1)
U=lambda x:(1,x,0,1)
L=lambda x:(1,0,x,1)
P=11
S=3
N=36
R=14
JROW=(4,2,5,2,5,1,3)
GROW=(4,2,5,1,4,3,3)
NROW=(4,2,5,3,0,2,6)
KROW=(4,1,6,2,7,1,1)
if not __debug__:raise RuntimeError("Assertions must remain enabled.")


def count_matrix(p,r,row):
    i,j,k,x,y,u,v=row
    assert min(row)>=0 and i+j+k==x+y+u+v==p
    assert 2*i<=p and 2*j<=p and 2*k<=r
    assert x<=p-2*i and y<=p-2*j and u<=r-2*k and v<=2*p-r
    alpha=i-j
    beta=r*j-p*k
    return (p*(x-y)+alpha*v,p*r*y-p*p*u+beta*v,-alpha,-beta)


def apply_row(ledger,groups,row):
    ga,gb,gc=groups
    i,j,k,x,y,u,v=row
    first=ga[:i]+gb[:j]+gc[:k]
    second=ga[i:2*i]+gb[j:2*j]+gc[k:2*k]
    ledger.average(first);ledger.average(second)
    olda,oldb,oldc=ga[2*i:],gb[2*j:],gc[2*k:]
    fresh=first+second
    kept,fresh=fresh[:R],fresh[R:]
    left=olda[:x]+oldb[:y]+oldc[:u]+fresh[:v]
    right=olda[x:]+oldb[y:]+oldc[u:]+fresh[v:]
    assert len(left)==len(right)==P and len(kept)==R
    assert sorted(left+right+kept)==list(range(N))
    ledger.average(left);ledger.average(right)
    return [left,right,kept]


def assert_state(ledger,groups,a,z):
    vals=(a,R*z-a,-P*z)
    assert all(ledger.state[i]==value for group,value in zip(groups,vals) for i in group)


def replay():
    atoms=0;cycles=0;roots=0
    inputs=((F(1),F(0)),(F(0),F(1)),(F(5,7),F(-3,5)))
    J=count_matrix(P,R,JROW);G=count_matrix(P,R,GROW)
    K=count_matrix(P,R,KROW);M=count_matrix(P,R,NROW)
    for a,z in inputs:
        raw=[a]*P+[R*z-a]*P+[-P*z]*R
        for row,mat in ((JROW,J),(GROW,G),(KROW,K),(NROW,M)):
            ledger=Ledger(raw,P)
            groups=[list(range(P)),list(range(P,2*P)),list(range(2*P,N))]
            groups=apply_row(ledger,groups,row);atoms+=4
            aa=(mat[0]*a+mat[1]*z)/(P*P)
            zz=(mat[2]*a+mat[3]*z)/(P*P)
            assert_state(ledger,groups,aa,zz)
            if mat[0]+mat[3]==0:
                groups=apply_row(ledger,groups,row);atoms+=4;cycles+=1
                lam=-F(det(mat),P**4)
                assert_state(ledger,groups,lam*a,lam*z)
            ledger.independent_replay(raw)
        for sign in (-1,1):
            ledger=Ledger(raw,P)
            groups=[list(range(P)),list(range(P,2*P)),list(range(2*P,N))]
            if sign==1:groups=[groups[1],groups[0],groups[2]]
            groups=apply_row(ledger,groups,JROW)
            groups=apply_row(ledger,groups,NROW)
            if sign==1:groups=[groups[1],groups[0],groups[2]]
            lam=-F(37,11**3)
            assert_state(ledger,groups,lam*(a+sign*N*z),lam*z)
            ledger.independent_replay(raw);atoms+=8;roots+=1
    return atoms,cycles,roots


def matrix_and_ring():
    J,G,M,K=[count_matrix(P,R,row) for row in (JROW,GROW,NROW,KROW)]
    assert J==(-27,568,-2,27)
    assert G==(-27,172,-2,27)
    assert M==(45,-404,-2,27)
    assert K==(-52,905,-3,52)
    assert det(J)==det(M)==407
    assert mm(M,invq(J))==U(-36)
    swap=(-1,14,0,1)
    assert mm(mm(swap,U(-36)),swap)==U(36)
    assert mm(M,J)==scale(-407,U(-36))
    f,g=-37,35
    T=mm(invq(J),G)
    assert T==(1,-F(972,37),0,-F(35,37))
    assert mm(mm(T,U(36)),invq(T))==U(F(36*f,g))
    common,a,b=bezout(f,g)
    assert common==1 and a*f+b*g==1
    # The only localization needed before activating 11 is R0=Z[1/(5*7*37)].
    assert gcd(5*7*37,N)==1 and 5*7*37%13!=0
    for mat,c in ((J,-2),(K,-3)):
        B=(1,mat[0],0,c)
        for t in (F(36),F(-72),F(36,35)):
            assert mm(mm(invq(B),U(t)),B)==U(c*t)
            expected=L(-c*t/det(mat))
            assert mm(mm(mm(mm(invq(B),mat),U(t)),invq(mat)),B)==expected
    assert gcd(2**3*N*N,3**3*N*N)==N*N
    assert all(q%13 for q in (2**3*N*N,3**3*N*N,N*N))
    # Four rows themselves are safe over the only dangerous primes 2 and3.
    for mat in (J,G,M,K):assert gcd(int(det(mat)),N)==1
    return J,G,M,K


def terminal_interface(J,K):
    swap=(1,0,N,-1)
    # -2+3=1, with alpha2 and alpha3 reflections both in GL2(R) after 11 activates.
    T2=mm(swap,scale(F(1,P*P),zy(J,P)))
    T3=mm(swap,scale(F(1,P*P),zy(K,P)))
    V=mm(T3,invq(T2))
    assert red(V,N)==(1,pow(-P*P,-1,N),0,1)
    D=5*7*11*37
    assert D%13!=0
    for x in (*V,*invq(V)):
        assert supported(F(x).denominator,D)
    assert supported(F(det(V)).numerator,D)
    rng=Random(11336)
    checks=0
    for _ in range(48):
        eps=rng.choice((1,-1,5,-7,11,F(1,37)))
        h=2*N
        z=eps+N*F(rng.randrange(-h,h),11)
        y=eps*P*P+N*F(rng.randrange(-h,h),11)
        column(P,S,2,V,z,y,eps)
        checks+=1
    return checks


def finite_difference_identities():
    count=0
    # Check the general determinant row-difference formula over varied parameters.
    for p in (5,7,11,17):
        for r in (p+1,p+3):
            for alpha,j in ((1,1),(2,1),(3,0)):
                i=j+alpha;k=p-i-j;beta=r*j-p*k
                for dx,dy,du in ((1,0,1),(1,-5,1),(2,3,-1)):
                    dv=-dx-dy-du
                    rowdiff=(p*(dx-dy)+alpha*dv,p*r*dy-p*p*du+beta*dv)
                    exact=-beta*rowdiff[0]+alpha*rowdiff[1]
                    assert exact==p*(-beta*dx+(beta+alpha*r)*dy-alpha*p*du)
                    count+=1
    return count


def conservation_formula_checks():
    """Apply the one prescribed move to existing records, without candidate-word search."""
    cases=json.loads((ROOT/"work/large_symmetric_carrier_shallow_certificate.json").read_text())["cases"]
    applicable=identities=0
    for case in cases:
        p,s=case["p"],case["s"];r=p+s;n=3*p+s;found=False
        for pair in case["root_pairs"]:
            for row in pair:
                i,j,k,x,y,u,v=row
                moved=(i,j,k,x+3*i-p,y+3*j-p,u+3*k-r,v+s)
                capacities=(p-2*i,p-2*j,r-2*k,p-s)
                if not all(0<=a<=c for a,c in zip(moved[3:],capacities)):continue
                A=count_matrix(p,r,row);B=count_matrix(p,r,moved)
                assert B==mm(U(-n),A)
                assert det(A)==det(B)
                assert mm(B,invq(A))==U(-n)
                identities+=1;found=True
        applicable+=found
    assert applicable==80
    return applicable,identities


def main():
    start=perf_counter()
    J,G,M,K=matrix_and_ring()
    atoms,cycles,roots=replay()
    transport=terminal_interface(J,K)
    formulas=finite_difference_identities()
    applicable,conservation=conservation_formula_checks()
    report={
        "status":"PASS","parameter":{"p":11,"s":3,"n":36},
        "equal_determinant":407,"root_parameter":-36,
        "source_counts":[4,2,5],"old_output":[2,5,1,3],"new_output":[3,0,2,6],
        "output_move":[1,-5,1,3],"signed_root_eight_atom_replays":roots,
        "scalar_cycle_replays":cycles,"original_position_atoms":atoms,
        "general_row_difference_checks":formulas,
        "existing_cases_admitting_prescribed_move":applicable,
        "conservation_move_identities_checked":conservation,
        "deep_levels":[8*N*N,27*N*N],"merged_deep_level":N*N,
        "completed_terminal_interfaces":transport,
        "auxiliary13_group_computation_used":False,
        "special97_unit_used":False,
        "finite_group_enumeration_used":False,
        "unchanged_frozen_files":check_frozen_files(),
        "local_links_checked":check_local_links(),
        "seconds":round(perf_counter()-start,3),
        "scope":"General equal-determinant quotient identity plus one fully replayed count repair. Deep-group inclusion and level gcd use the cited established Morris/Serre toolkit, not finite tests. No claim that the 162 root-pair certificates have been uniformly removed."
    }
    (HERE/"equal_determinant_root_repair_verification.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2))


if __name__=="__main__":main()
