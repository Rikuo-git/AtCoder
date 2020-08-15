#!/usr/bin/env python3
from collections import deque

n, *a = map(int, open(0).read().split())
a.sort()
a = deque(a)
que = deque([])
que.append(a.pop())
c = 0
while a:
    c += que.popleft()
    nt = a.pop()
    que += [nt] * 2
print(c)
