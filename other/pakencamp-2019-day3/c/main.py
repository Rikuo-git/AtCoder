#!/usr/bin/env python3
(n, m, ), *a = [[*map(int, i.split())] for i in open(0)]
s = 0
for i in range(m):
    for j in range(i + 1, m):
        s = max(s, sum(max(k[i], k[j]) for k in a))
print(s)
