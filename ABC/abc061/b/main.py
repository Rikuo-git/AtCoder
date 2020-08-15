#!/usr/bin/env python3
n, m, *r = map(int,open(0).read().split())
for i in range(1, n + 1):
    print(r.count(i))
