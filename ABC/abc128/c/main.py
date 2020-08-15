#!/usr/bin/env python3
n, m = map(int, input().split())
e = [[*map(int, input().split())][1:] for _ in range(m)]
p = [*map(int, input().split())]

c = 0

for i in range(2**n):
    count = [0] * m
    for j in range(n):
        if i >> j & 1:
            for k in range(m):
                if j + 1 in e[k]:
                    count[k] = (count[k] + 1) % 2
    if count == p:
        c += 1
print(c)
