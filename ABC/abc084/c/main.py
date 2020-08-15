#!/usr/bin/env python3
(n, ), *q = [[*map(int, i.split())] for i in open(0)]
ans = [0] * n
for i in range(n-1):
    c, s, f = q[i]
    for j in range(i):
        ans[j] = c + max(s, -(-ans[j] // f) * f)
    ans[i] = c + s
print(*ans, sep="\n")
