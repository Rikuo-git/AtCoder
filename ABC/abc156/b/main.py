#!/usr/bin/env python3
n, k = map(int, input().split())
c = 0
while n > 0:
    c += 1
    n //= k
print(c)
