#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
p = 0
ans = 0
for i in a:
    ans += max(p - i, 0)
    p = max(p, i)
print(ans)
