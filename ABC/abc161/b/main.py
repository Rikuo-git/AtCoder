#!/usr/bin/env python3
n, m, *a = map(int, open(0).read().split())
s = sum(a)
print("YNeos"[sum(i * 4 * m >= s for i in a) < m::2])
