#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
p = round(sum(a) / n)
print(sum((i - p)**2 for i in a))
