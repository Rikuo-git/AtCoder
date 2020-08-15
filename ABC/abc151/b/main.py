#!/usr/bin/env python3
n,k,m,*a=map(int,open(0).read().split())
p = m*n-sum(a)
if p >k:
    print(-1)
else:
    if p>0:
        print(p)
    else:
        print(0)
