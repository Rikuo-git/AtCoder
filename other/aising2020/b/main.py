#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
print(sum(a[i] % 2 > 0 for i in range(0, n, 2)))
