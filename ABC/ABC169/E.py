# my solution
import numpy as np
(n,),*l = [[*map(int,i.split())]for i in open(0)]
a,b = np.median(l,axis=0)
if n%2>0:
    print(int(b-a+1))
else:
    print(int(b*2-a*2)+1)
#　奇数の時は中央値の間、偶数の時は中央値の間かける2倍

# shortest fsdshn 数学的にやっていることは同じ
n,*l=map(int,open(0).read().split())
m,M=sorted(l[::2]),sorted(l[1::2])
d=n//2
print(M[d]-m[d]+1+(M[d-1]+-m[d-1])*(n%2^1))