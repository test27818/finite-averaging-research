exec(open('work/search_generic_maps.py',encoding='utf8').read().split('for n in [13,17,19,23]:')[0])
out,c=search(13,4)
for (u,v),p in out.items():
 if u==(F(2,3),F(1,3)) and v==(F(1),F(0)):
  print(p)
