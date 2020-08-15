n,a,b,*x=map(int,open(0).read().split())
print(sum(min(b,a*(x[i]-x[i-1]))for i in range(1,n)))
