#!/usr/bin/env python3
x, k, d = map(int, input().split())
x = abs(x)
if (n := k - x // d) < 0:
    print(x - k * d)
else:
    print(abs(d - x % d) if n % 2 else x % d)
