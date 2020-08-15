n = int(input())
a = list(map(int, input().split()))
A = int(input())

dp = [[10**9] * (A + 1) for _ in range(n + 1)]
dp[0][0] = 0
for i in range(n):
    for j in range(A + 1):
        if j < a[i]:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = min(dp[i][j], dp[i][j - a[i]] + 1)
print(dp[n][A] if dp[n][A] < 10**9 else -1)
