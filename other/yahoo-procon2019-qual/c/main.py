#!/usr/bin/env python3
k, a, b = map(int, input().split())
if k < a + 1 or 2 > b - a:
    print(k + 1)
else:
    print((k - a + 1) // 2 * (b - a) + a + (k - a + 1) % 2)
