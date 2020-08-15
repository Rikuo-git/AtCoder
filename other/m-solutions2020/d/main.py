#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
c = 1000
for i in range(1, n):
    if a[i] > a[i - 1]:
        c = c // a[i - 1] * a[i] + c % a[i - 1]
print(c)
