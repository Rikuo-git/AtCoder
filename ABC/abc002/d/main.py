#!/usr/bin/env python3
(n,m),*r=[tuple(map(int,i.split())) for i in open(0)]
r = set(r)
c = 1
for b in range(1<<n):
    g = [-~i for i in range(0,n) if b>>i &1]
    l = len(g)
    if all((g[i],g[j]) in r for i in range(l) for j in range(-~i,l)):
        c = max(c,l)
print(c)
