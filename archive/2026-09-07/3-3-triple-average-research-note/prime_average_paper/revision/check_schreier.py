from verify_revision import mm
I=(1,0,0,1); S=(0,-1,1,0); T=(1,1,0,1); Ti=(1,-1,0,1)
reps=[I,mm(S,Ti),S,mm(S,T)]
def inv(A): a,b,c,d=A;return d,-b,-c,a
for r in reps:
    row=[]
    for g in (S,T,Ti):
        candidates=[mm(mm(r,g),inv(t)) for t in reps]
        good=[(j,H) for j,H in enumerate(candidates) if H[2]%3==0]
        assert len(good)==1
        row.append(good[0])
    print(row)
