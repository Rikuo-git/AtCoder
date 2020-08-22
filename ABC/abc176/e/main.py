(h,w,m),*s=[[*map(int,i.split())]for i in open(0)]
r,c=[0]*-~h,[0]*-~w
for x,y in s:
    r[x]+=1
    c[y]+=1
R,C=max(r),max(c)
print(R+C-(r.count(R)*c.count(C)==sum(r[x]+c[y]==R+C for x,y in s)))
