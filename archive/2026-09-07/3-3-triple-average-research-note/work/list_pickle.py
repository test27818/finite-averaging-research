import pickle
f,n=pickle.load(open('work/ten_macros_depth_5.pickle','rb'));print('states',n,'matrices',len(f));
for m,path in list(f.items())[:40]:print(m,'det',m[0]*m[3]-m[1]*m[2],'len',len(path))
