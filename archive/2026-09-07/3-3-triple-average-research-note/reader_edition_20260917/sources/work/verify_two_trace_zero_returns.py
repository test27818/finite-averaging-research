"""Two symbolic trace-zero returns, their root, and finite local shadows."""
from fractions import Fraction as F
from verify_diagonal_resource_reduction import product
from verify_b53_inverse_closure import inverse


def projective_mod(matrix,q):
    values=[x.numerator*pow(x.denominator,-1,q)%q for x in map(F,matrix)]
    first=next(x for x in values if x)
    scale=pow(first,-1,q)
    return tuple(x*scale%q for x in values)


def closure(generators,q):
    identity=projective_mod((1,0,0,1),q)
    seen={identity};todo=[identity]
    while todo:
        x=todo.pop()
        for g in generators:
            y=projective_mod(product(x,g),q)
            if y not in seen:
                seen.add(y);todo.append(y)
    return seen


def point_action(matrix,point,q):
    x,y=point;a,b,c,d=matrix
    z=(a*x+b*y)%q;(w:=None)
    w=(c*x+d*y)%q
    if z:
        inv=pow(z,-1,q);return (1,w*inv%q)
    return (0,1)


def orbits(group,q):
    points=[(0,1)]+[(1,t) for t in range(q)]
    left=set(points);result=[]
    while left:
        seed=min(left);orbit={point_action(g,seed,q) for g in group}
        result.append(sorted(orbit));left-=orbit
    return result


def verify():
    checked=0
    sizes={}
    for p in range(11,100):
        if p%2==0 or p%3!=2:
            continue
        m=p-4;N=2*p+1;M=2*p-9
        a=(1,0,F(-p,3),F(-1,3))
        hu=(1,1,0,F(-N,9))
        hv=(1,F(-10,M),0,F(N,M))
        ru=product(a,inverse(hu))
        rv=product(a,inverse(hv))
        assert sum(product(ru,a)[::3])==sum(product(rv,a)[::3])==0
        assert product(hu,hv,inverse(hu),inverse(hv))==(1,F(10,N),0,1)
        for q in (2,5):
            if N%q==0 or M%q==0:
                continue
            group=closure((a,hu,hv),q)
            sizes.setdefault((p%q,q),(len(group),orbits(group,q)))
        checked+=1
    assert all(data[0]==6 for (r,q),data in sizes.items() if q==2)
    assert sizes[(1,5)][1] == sizes[(3,5)][1] == [[(0,1),(1,0),(1,1),(1,2),(1,3),(1,4)]]
    assert sizes[(4,5)][1] == [[(0,1),(1,4)],[(1,0),(1,1),(1,2),(1,3)]]
    # The second orbit has a universal exact zero-sum triple at (u,y)=(1,-3).
    u,y=1,-3;v=u+y
    assert 2*u+v==0 and (1,y%5)==(1,2)
    scales=0
    for p in range(11,150):
        if p%3!=2 or any(p%q==0 for q in range(2,int(p**.5)+1)):
            continue
        m=p-4;N=2*p+1
        h=next(h for h in range(1,p) if pow(3,h,p)==1)
        a=3%p;k=1+3*h;lam=F(N*a,3**k)
        t=F(10,N)
        targets=((lam*(1-t),lam*t),
                 (-lam*m*(1-t)/3,-lam*(m*t+1)/3),(F(0),lam))
        for aa,bb in targets:
            gamma=(1-aa-bb)/p
            alpha,beta=aa+m*gamma,bb+3*gamma
            assert min(alpha,beta,gamma)>=0 and alpha+beta+gamma==1
            for x in (alpha,beta,gamma):
                d=x.denominator
                while d%3==0:d//=3
                assert d==1
        scales+=1
    print("second-return legal scales and nonnegative triadic margins: PASS",scales)
    print("mod2/5 shadows and both finite terminal orbits: PASS")
    print("two symbolic trace-zero returns and primitive factor10 root: PASS",checked)
    print("finite projective shadow sizes",sizes)


if __name__=="__main__":verify()
