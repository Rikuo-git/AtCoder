#!/usr/bin/env python3
n, a, b = map(int, input().split())
c = 0
for i in range(1, n + 1):
    if a <= sum(int(i) for i in str(i)) <= b:
        c += i
print(c)
