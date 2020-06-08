# my solution
import itertools
(n,),p,q=[tuple(map(int, i.split())) for i in open(0)]
j=list(itertools.permutations(range(1, -~n)))
print(abs(j.index(p) - j.index(q)))

# shortest by c_r_5
from itertools import*
n,a,b=eval('eval(input().replace(" ",",")),'*3)
i=list(permutations(range(1,n+1))).index
print(abs(i(a)-i(b)))


# fast code 僕がやりたかったやつ
import math
n=int(input())
def c():
    l=list(map(int, input().split()))
    s=0
    t=list(range(1,n+1))
    for i in range(n):
        s+=t.index(l[i])*math.factorial(n-i-1)
        t.remove(l[i])
    return s
print(abs(c()-c()))