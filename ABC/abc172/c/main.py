#!/usr/bin/env python3
n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
A = [0]
B = [0]
for i in range(n):
    A.append(A[i] + a[i])
for i in range(m):
    B.append(B[i] + b[i])
ans = 0
j = m
for i in range(n + 1):
    if A[i] > k:
        break
    while j > 0 and k - A[i] < B[j]:
        j -= 1
    ans = max(ans, i + j)

print(ans)
# 尺取法というらしい
# https://qiita.com/drken/items/ecd1a472d3a0e7db8dce
