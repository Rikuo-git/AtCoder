#!/usr/bin/env python3
n,*p=map(int,open(0).read().split())
c=0
n+=1
for i in p:
    n = min(n, i)
    if i<=n:
        c+=1
print(c)
