#!/usr/bin/env python3
from bisect import bisect_right

d, n, m = int(input()), int(input()), int(input())
s = [0] + sorted([int(input()) for _ in range(n - 1)]) + [d]
c = [int(input()) for _ in range(m)]
ans = 0
for i in c:
    p = bisect_right(s, i)
    ans += min(i - s[p - 1], s[p] - i)
print(ans)
