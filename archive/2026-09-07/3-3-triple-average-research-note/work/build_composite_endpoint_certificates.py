"""Build finite CRT/Schreier pivot certificates. Not a universal theorem.

The independent verifier reads only the resulting JSON, never this builder or
the diagnostic pivot selector. Physical averaging words are not searched.
"""

from pathlib import Path
import json

from explore_composite_endpoint_transversals import transversal,label,choose_pivot
from verify_prime_power_endpoint_completion import S,T,mul,inv

LEVELS=(15,35,39,51,55,63,75,87,91,95,99,111,115,119,123,135,143,147,155,
        159,171,175,183,187,195,203,207,215,219,231,255,315,399,435,455,1155)


def main():
    cases=[]
    loops=0
    for n in LEVELS:
        p=(n-1)//2
        assert p%2==1
        moduli,reps=transversal(n)
        keys=list(reps)
        indices={key:i for i,key in enumerate(keys)}
        edges=[]
        for key in keys:
            for gi,g in enumerate((S,T,inv(T))):
                z=mul(reps[key],g)
                target=label(z[2],z[3],moduli)
                matrix=mul(z,inv(reps[target]))
                choice=choose_pivot(matrix,n,p)
                assert choice is not None,(n,matrix)
                mode,shear=choice
                edges.append({'source':indices[key],'generator':gi,'target':indices[target],
                              'mode':mode,'shear':str(shear)})
        cases.append({'level':n,'arity':p,'representatives':[list(reps[key]) for key in keys],
                      'edges':edges})
        loops+=len(edges)
    Path(__file__).with_name('composite_endpoint_pivot_certificates.json').write_text(
        json.dumps({'schema':1,'scope':'finite full-coset certificates, not unbounded n',
                    'cases':cases},indent=2)+'\n',encoding='utf-8')
    print('built composite endpoint certificates:',len(cases),loops)


if __name__=='__main__':
    main()
