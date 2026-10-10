"""Finite diagnostic of the full adjacent-output template, not a proof of coverage.

Output variables are eliminated exactly to <=2 integer intervals per source.
No averaging words, arbitrary inputs, or finite group orbits are searched.
"""
from pathlib import Path
from math import gcd
from fractions import Fraction as F
from time import perf_counter
import json,sys
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/'work'))
from verify_common_shape_and_relation_lattice import primes_below,matrix
from verify_uniform_odd_middle_cores import mm,invq
from verify_square_zero_compiler import check_frozen_files,check_local_links


def cd(a,b):return -(-a//b)


def resources(p,r):
    n=2*p+r;gA=gH=num=0
    r4_sources=[]
    for q in (1,2):
        if q*p<r:continue
        for i in range(p//q+1):
            for j in range(i):
                k=p-i-j;alpha=i-j
                if k<0 or q*k>r or alpha==p:continue
                beta=r*j-p*k
                caps=(p-q*i,p-q*j,r-q*k,q*p-r)
                v0=beta*pow(alpha,-1,p)%p
                for v in range(v0,caps[3]+1,p):
                    t=(beta-alpha*v)//p
                    lo=max(0,-t,cd(p-v-t-caps[2],2))
                    hi=min(caps[1],caps[0]-t,(p-v-t)//2)
                    if hi-lo<1:continue
                    # Larger y first, so the second row adds (-1,-1,2,0).
                    y=lo+1
                    row=(y+t,y,p-v-t-2*y,v)
                    J=matrix(p,r,(i,j,k),row)
                    K=matrix(p,r,(i,j,k),(row[0]-1,row[1]-1,row[2]+2,v))
                    f=(J[0]**2+J[1]*J[2])//p
                    g=(K[0]**2+K[1]*K[2])//p
                    assert g-f==alpha*n and gcd(f,n)==1
                    H=n*(i+j)-2*p*p
                    if r==4:
                        assert q==1 and k==1 and alpha%2==0 and H==2*(p-2)
                        r4_sources.append((q,i,j,k))
                    if gcd(f,g)!=1:continue
                    num+=1;gA=gcd(gA,alpha);gH=gcd(gH,H)
    if r in (1,2):assert num==0
    return {'pairs':num,'alpha_gcd':gA,'root_coefficient_gcd':gH,
            'sufficient_resource_test_passes':gA==1 and gH==gcd(n,2)}


def lattice_checks():
    count=0
    for p in primes_below(83):
        for r in range(1,p):
            if r%2:
                B=(0,r,2,-r);index=2*r
            else:
                t=r//2;B=(0,t,1,-t);index=t
            assert abs(B[0]*B[3]-B[1]*B[2])==index
            for k in (1,2,index,max(1,index-1),2*index):
                T=mm(mm(invq(B),(1,k,0,1)),B)
                integral=all(F(x).denominator==1 for x in T)
                assert integral==(k%index==0),(p,r,k,T)
                count+=1
            for ell in (3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79):
                assert not(index%ell==0 and (2*p+r)%ell==0)
    return count


def main():
    if not __debug__:raise RuntimeError('Assertions required')
    start=perf_counter();failed=[];cases=0
    upper_failed=[];passed=0
    for p in primes_below(83):
        for r in range(1,2*p):
            if r==p:continue
            result=resources(p,r);cases+=1
            if not result['sufficient_resource_test_passes']:
                item={'p':p,'r':r,**result};failed.append(item)
                if r>p:upper_failed.append(item)
            else:passed+=1
    assert all(x['r'] in (1,2,4) for x in failed if x['p']>=13)
    report={'status':'PASS','finite_parameter_cases':cases,'sufficient_resource_passes':passed,
            'sufficient_resource_failures':len(failed),'upper_band_failures':upper_failed,
            'all_failures':failed,'lattice_shear_checks':lattice_checks(),
            'frozen_files':check_frozen_files(),'local_links':check_local_links(),
            'seconds':round(perf_counter()-start,3),
            'scope':'Complete finite diagnostic for 5<=p<83 and nonzero-alpha one/two-source adjacent trace-zero rows with coprime scalar pair. Does not certify a new uniform all-parameter theorem or replace original finite certificates.'}
    (HERE/'small_parameter_resource_scope.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k not in ('all_failures','upper_band_failures')},indent=2))
    print('Upper-band diagnostic failures:',[(x['p'],x['r']) for x in upper_failed])


if __name__=='__main__':main()
