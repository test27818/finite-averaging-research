# import above by execute? quick modify
exec(open('work/search_generic_B.py').read().split('for n in [13,17]:')[0])
for n in [13,17,19]:
 st=b_state(n)
 sig=((F(0),F(1)),(F(1),F(0)),(F(1),F(0)))
 for i in range(3):
  st=step(st,sig)
 print(n,st)
 from collections import Counter
 print(Counter(st))
