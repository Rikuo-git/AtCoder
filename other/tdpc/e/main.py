#!/usr/bin/env python3
D = int(input())
N = input()
l = len(N)
M = 10**9 + 7
dp = [[[0]*D for _ in range(2)]for _ in range(l+1)]
dp[0][0][0] = 1
for i in range(len(N)):
    x = int(N[i])
    for j in range(10):
        m = j%D
        for d in range(D):
            if j==x:
                dp[i+1][0][d] = dp[i][0][d-m]
            if j < x:
                dp[i+1][1][d] += dp[i][0][d-m]
            dp[i+1][1][d] += dp[i][1][d-m]
            dp[i+1][1][d] %= M
print(dp[l][1][0] + dp[l][0][0] - 1)
