from math import gcd


def prim(u, v):
    d = gcd(abs(u), abs(v)); u//=d; v//=d
    return (u,v) if (u>0 or (u==0 and v>=0)) else (-u,-v)


def trace(u,v):
    u,v=prim(u,v); out=[]
    while u+v:
        if u%3==0 and u and v%3:
            q=u//3; out.append((u,v,'A',abs(q).bit_length()))
            u,v=prim(v-q,-q)
        elif v%3==0 and v and u%3:
            q=v//3; out.append((u,v,'B',abs(q).bit_length()))
            u,v=prim(u-q,-q)
        else: return out,('stop',(u,v))
    return out,('success',(u,v))


for pair in [(-23,18),(-97,-48),(-883,783),(-10,7),(-1000,997),(-100000,99997)]:
    tr,end=trace(*pair)
    print(pair,end,'depth',len(tr))
    print(' '.join(x[2] for x in tr))
    print([(x[0],x[1]) for x in tr])
