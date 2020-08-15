#!/usr/bin/env python3
from bisect import bisect_left
from itertools import combinations


def bisect_find(array, n):
    index = bisect_left(array, n)
    if index >= len(array) or array[index] != n:
        return False
    else:
        return True


n = int(input())
p = list([tuple(map(int, input().split())) for _ in range(n)])
p.sort()
ans = 0
for (a, b), (c, d) in combinations(p, 2):
    s = a - c
    t = b - d
    e = s**2 + t**2
    na = (a + t, b - s)
    nb = (c + t, d - s)
    if bisect_find(p, na) and bisect_find(p, nb):
        ans = max(ans, e)
print(ans)

# pypyだとMLEだからpythonでは無理そう
n = int(input())
table = [[0]*5001]*5001
p = []
for _ in range(n):
    x, y = map(int, input().split())
    table[x][y] == 1
    p.append([x, y])

for (a, b), (c, d) in combinations(p, 2):
    s = a - c
    t = b - d
    if table[a+t][b-s] and table[c+t][d-s]
    ans = max(ans, s**2 + t**2)
print(ans)
