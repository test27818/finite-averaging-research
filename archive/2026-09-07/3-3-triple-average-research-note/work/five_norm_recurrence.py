a,b=1,1
sign=-1
for d in range(35):
    print(d,a,b,sign,a+b,round(a/b,3))
    c=a+b if sign==-1 else a-b
    a,b=max(3*b,c),min(3*b,c)
    sign=-sign
