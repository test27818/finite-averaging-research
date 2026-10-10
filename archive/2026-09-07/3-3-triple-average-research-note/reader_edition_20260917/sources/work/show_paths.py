import pickle
f,n=pickle.load(open('work/ten_macros_depth_5.pickle','rb'))
for target in [(1,1,-5,-1),(7,-1,-15,-3),(4,-1,0,3),(1,-2,0,3),(13,0,-15,0)]:
 print('TARGET',target)
 for m,p in f.items():
  if m==target:
   print(p)
