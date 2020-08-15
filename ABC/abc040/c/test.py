n, w = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (w + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(w + 1):
        if j < s[i][1]:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - s[i][1]] + s[i][0])
print(dp[n][w])

dp = [[0] * (w + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(m + 1):
        if j < a[i]:
            dp[i + 1][j] = dp[i][j]
        else:
            dp

n = int(input())
a = list(map(int, input().split()))
A = 12

dp = [[0] * (A + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    for j in range(A + 1):
        if j < a[i]:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = dp[i][j] + dp[i][j - a[i]]
print(dp[n][A])
