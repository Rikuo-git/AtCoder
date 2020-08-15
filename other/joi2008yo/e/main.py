#!/usr/bin/env python3
(R, C), *S = [[*map(int, i.split())] for i in open(0)]
ans = 0
r = [[1 ^ i for i in j] for j in S]
for i in range(2 << R):
    arr = []
    sub = 0
    for j in range(R):
        if i >> j & 1:
            arr.append(r[j])
        else:
            arr.append(S[j])
    for i in zip(*arr):
        s = sum(i)
        sub += max(s, R - s)
    ans = max(sub, ans)
print(ans)

import numpy as np

r, c = map(int, input().split())
arr = np.array([list(map(int, input().split())) for _ in range(r)], dtype=np.int8)

ans = 0
for i in range(2**r):
    tmp_arr = arr.copy()
    choice = []
    for j in range(r):
        if i >> j & 1:
            choice.append(True)
        else:
            choice.append(False)
    tmp_arr[choice] ^= 1
    a = tmp_arr.sum(axis=0)
    ans = max(ans, np.maximum(a, r - a).sum())

print(ans)
