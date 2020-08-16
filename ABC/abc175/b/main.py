#!/usr/bin/env python3
from bisect import *
n,*l=map(int, open(0).read().split())
l.sort()
n = len(l)
ans = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if len({l[i],l[j],l[k]}) ==3 and l[i] + l[j] > l[k] and l[i] > l[k]- l[j]:
                ans +=1
print(ans)

