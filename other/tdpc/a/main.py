#!/usr/bin/env python3
n, *p = map(int, open(0).read().split())
dp = [[0] * (sum(p) + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    for j in range(sum(p) + 1):
        if j < p[i]:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - p[i]])
print(sum(dp[n]))

input()
d = 1

for i in input().split():
    d |= d << int(i)
print(bin(d).count("1"))
