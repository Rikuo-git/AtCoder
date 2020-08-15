#!/usr/bin/env python3
n, d = map(int, input().split())
c = 0
for i in range(n):
    x, y = map(int, input().split())
    if x**2 + y**2 <= d**2:
        c += 1
print(c)
