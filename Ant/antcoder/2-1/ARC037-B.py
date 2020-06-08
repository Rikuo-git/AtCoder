import sys

sys.setrecursionlimit(100000)

(n, m), *v = [list(map(int, i.split())) for i in open(0)]
l = [1] + [0] * n


def dfs(i, p):
    global loop

    l[i] = 1

    for j in v:
        if i in j:
            k = sum(j) - i
            if k != p:
                if l[k]:
                    loop = False
                else:
                    dfs(k, i)


c = 0
while 0 in l:
    loop = True
    dfs(l.index(0), 0)
    c += loop
print(c)

# shortest
N, M = map(int, input().split())
p = [i for i in range(N)]


def f(i):
    if i == p[i]:
        return i
    p[i] = f(p[i])
    return p[i]


x = [1] * N
for _ in range(M):
    a, b = map(int, input().split())
    a = f(a - 1)
    b = f(b - 1)
    if a == b:
        x[a] = 0
    else:
        p[a] = b
        x[b] &= x[a]
z = 0
for i in range(N):
    if i == f(i):
        z += x[i]
print(z)


# 深さ優先探索
from collections import deque

# グラフの作成(無向グラフでは#を消す)
N,M = int(input())
graph = [deque([]) for _ in range(N + 1)]
for _ in range(M):
    v = [int(x) for x in input().split()] # uは頂点番号、kは隣接頂点の個数
    for i,j in v:
        graph[j].append(i)
        graph[i].append(j) # 無向グラフ

arrive = [0] * (N + 1) # 到着時刻

# 深さ優先探索
def dfs(v):
    global loop
    stack = deque([v])
    arrive[v] = 1
    while stack:
        v = stack[-1]
        if graph[v]:
            w = graph[v].popleft()
            graph[w].remove(v)
            if arrive[w]:
                loop = False
            else:
                arrive[w] = 1
                stack.append(w)
        else:
            stack.pop()

a= 0
for i in range(N):
    if not arrive[i + 1]:
        loop = True
        dfs(i + 1)
        a+=loop
print(a)


def dfs(now, prev):
    global flag
    # 今いる頂点から行ける頂点を順に next に入れてループ
    for next in g[now]:
        if next != prev:
            if memo[next]:
                # 過去に訪れていれば閉路
                flag = False
            else:
                memo[next] = True
                dfs(next, now)


n, m = map(int, input().split())
g = [[] * n for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

# 訪れたことがあるか
memo = [False for i in range(n)]

ans = 0
# 頂点をループ
for i in range(n):
    if not memo[i]:
        flag = True
        dfs(i, -1)
        if flag:
            # 閉路がなければ木である
            ans += 1
print(ans)