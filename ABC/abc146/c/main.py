#!/usr/bin/env python3
a, b, x = map(int, input().split())
n = 0
while a * 10**n + b * n <= x and n < 10:
    n += 1
if n > 0:
    print(min((x - b * n) // a, 10**9))
else:
    print(n)

# これは2分探索の問題らし
a, b, x = map(int, input().split())
l, r = 0, 10**9 + 1
while r - l > 1:
    m = l + r >> 1
    if a * m + b * len(str(m)) > x:
        r = m
    else:
        l = m
print(l)
