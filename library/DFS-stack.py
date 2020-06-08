# 深さ優先探索
from collections import deque

# グラフの作成(無向グラフでは#を消す)
N = int(input())
graph = [deque([]) for _ in range(N + 1)]
for _ in range(N):
    u, k, * v = [int(x) for x in input().split()] # uは頂点番号、kは隣接頂点の個数
    v.sort()
    for i in v:
        graph[u].append(i)
        # graph[i].append(u) # 無向グラフ

arrive = [0] * (N + 1) # 到着時刻

# 深さ優先探索
def dfs(v):
    stack = [v]
    arrive[v] = 1
    while stack:
        v = stack[-1]
        if graph[v]:
            w = graph[v].popleft()
            if arrive_time[w] < 0:
                arrive[w] = 1
                stack.append(w)
        else:
            stack.pop()

# 孤立している頂点対策
for i in range(N):
    if not arrive[i + 1]:
        dfs(i + 1)
