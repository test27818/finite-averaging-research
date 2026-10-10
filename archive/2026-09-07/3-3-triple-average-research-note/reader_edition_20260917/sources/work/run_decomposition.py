def evolve(a,b,sigma,steps):
  out=[]
  for _ in range(steps):
    if sigma==-1: c=a+b; ns=1
    else: c=abs(a-b); ns=-1
    x,y=3*b,c
    if x<y:x,y=y,x
    out.append((a,b,sigma,x,y,ns))
    a,b,sigma=x,y,ns
  return out
a,b,s=1,1,-1
for j in range(40):
  z=evolve(a,b,s,1)[0];a,b,s=z[3:]
  print(j+1,a,b,s, 'r',round(a/b,3) if b else None)
