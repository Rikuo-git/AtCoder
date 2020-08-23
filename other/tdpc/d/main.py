#!/usr/bin/env python3
n, d = map(int, input().split())
def log(m):
    global d
    c = 0
    while d%m<1:
        c+=1
        d//=m
    return c
a=log(5)
b=log(3)
c=log(2)
if d>1:
    print(0)
    exit()
dp = [[[[0]*(c+1) for _ in range(b+1)]for _ in range(a+1)]for _ in range(n+1)]
dp[0][0][0][0]=1
for i in range(n):
    for p in range(a+1):
        for q in range(b+1):
            for r in range(c+1):
                o = dp[i][p][q][r]/6
                dp[i+1][p][q][r] += o
                dp[i+1][p][q][min(c,r+1)] += o
                dp[i+1][p][q][min(c,r+2)] += o
                dp[i+1][p][min(b,q+1)][min(c,r+1)] += o
                dp[i+1][p][min(b,q+1)][r] += o
                dp[i+1][min(a,p+1)][q][r] += o

print(dp[n][a][b][c])
