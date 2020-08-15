#!/usr/bin/env python3
from collections import defaultdict

n, *a = map(int, open(0).read().split())
ans = [0, 0]
d = defaultdict(int)
for i in a:
    d[i] += 1
    if d[i] > 1 and i > ans[0]:
        ans = sorted(ans + [i])[-2:]
        d[i] -= 2
print(ans[0] * ans[1])
