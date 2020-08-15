#!/usr/bin/env python3
n, m = map(int, input().split())
a = max(n, m)
b = min(n, m)
if b == 1:
    print((a - 2) if a > 1 else 1)
elif b == 2:
    print(0)
else:
    print((a - 2) * (b - 2))
