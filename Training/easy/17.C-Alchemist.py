# my solution
n,*v=map(int,open(0).read().split())
v.sort()
print(sum(v[i]<<i+(i==0)for i in range(n))/2**n)


# shortest by c_r_5
_,v=open(0)
s,*v=sorted(map(int,v.split()))
for i in v:s=(s+i)/2
print(s)