# (w, ), (
#     n,
#     k,
# ), *a = [[*map(int, i.split())] for i in open(0)]
# dp = [[[0] * 2 for _ in range(w + 1)] for __ in range(n + 1)]
# for h in range(k):
#     for i in range(n):
#         for j in range(w + 1):
#             if j >= a[i][0]:
#                 dp[i + 1][j][(h+1)%2] = max(dp[i][j][(h+1)%2],
#                                           dp[i][j - a[i][0]][h%2] + a[i][1])
#             else:
#                 dp[i + 1][j][(h+1)%2] = dp[i][j][(h+1)%2]
# print(dp[n][w][k%2])
# 
# 
# 
# import numpy as np
# dp = np.zeros((k+1,w+1),np.int64)
# a = sum(a,[])
# print(a)
# for i,b in zip(a[::2],a[1::2]):
#     for c in range(k):
#         dp[c][i:]=np.maximum(dp[c][i:],dp[c+1][:-i]+b)
#     # for j in range(i): dp[c][j] = max(dp[c][i+j], dp[c-1][j]+b)と同じ
# 
# 
# print(dp[0][w])
import numpy as np
std=np.fromstring(open(0).read(),dtype=np.int64,sep=" ")
w,n,k=std[:3]
s=std[3:].reshape((n,2))
dp=np.zeros((k+1,w+1),np.int64)
for a,b in s:
  for i in range(k):
    dp[i][a:]=np.maximum(dp[i][a:],dp[i+1][:-a]+b)
print(dp[0][w])
