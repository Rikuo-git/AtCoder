# my solution
n,m,x,*a=map(int,open(0).read().split())
c=len([i for i in a if i>x])
print(min(c,m-c))

# shortest by Chibitan2
_,m,*a=map(int,open(0).read().split())
c=sorted(a).index(a[0])
print(min(c,m-c))