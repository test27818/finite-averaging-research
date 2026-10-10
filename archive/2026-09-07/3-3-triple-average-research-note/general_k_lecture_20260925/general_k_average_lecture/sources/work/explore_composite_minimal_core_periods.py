"""Bounded diagnostic for (q,r,1) cores; not a reachability certificate."""

from math import gcd


def norm(x):
    g = gcd(*x)
    x = tuple(v//g for v in x)
    return tuple(-v for v in x) if next(v for v in x if v) < 0 else x


def mul(a, b):
    x,y,z,w = a
    e,f,g,h = b
    return norm((x*e+y*g,x*f+y*h,z*e+w*g,z*f+w*h))


def finite_order(a):
    x,y,z,w = a
    if y == z == 0 and x == w:
        return 1
    determinant = x*w-y*z
    tr = x+w
    if tr == 0:
        return 2
    if determinant > 0:
        for ratio, order in ((1,3),(2,4),(3,6)):
            if tr*tr == ratio*determinant:
                return order
    return None


def main():
    for q,r in ((4,2),(8,4),(9,3),(16,4),(25,5),(27,9),(32,8)):
        k = q//r
        alphabet = {'A':(k,-1,0,-1),'B':(-r-1,r,-q-r-1,q+r),
                    'C':(-r-1,1,-q-r-1,1)}
        seen = {(1,0,0,1)}
        frontier = [((1,0,0,1),'')]
        found = None
        for depth in range(1,9):
            following = []
            for matrix, word in frontier:
                for name, atom in alphabet.items():
                    result = mul(matrix, atom)
                    newword = word+name
                    order = finite_order(result)
                    if 'A' in newword and order:
                        found = (newword,order,result)
                        break
                    if result not in seen:
                        seen.add(result)
                        following.append((result,newword))
                if found:
                    break
            if found:
                break
            frontier = following
        print('q,r,n',q,r,q+r+1,'A-containing finite period',found,'distinct',len(seen),flush=True)


if __name__ == '__main__':
    main()
