#!/usr/bin/env python3
a, b, c, k = map(int, open(0).read().split())
while a >= b:
    b *= 2
    k -= 1
while b >= c:
    c *= 2
    k -= 1
print("YNeos"[k < 0::2])
