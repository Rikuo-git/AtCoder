from collections import deque

n, m = map(int, input().split())

maze = [list(input()) for _ in range(n)]


def bfs():
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    d = [([-1] * m) for _ in range(n)]
    q = deque([])
    for i in range(n):
        for j in range(m):
            if maze[i][j] == "#":
                d[i][j] = 0
                q.append((i, j))
    a = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != '#' and d[nx][ny] == -1:
                q.append((nx, ny))
                d[nx][ny] = d[x][y] + 1
                a = max(a, d[nx][ny])
    return a


print(bfs())

from collections import deque

n, m = map(int, input().split())
p = [input() for _ in range(n)]
q = deque([])
a = 0
for i in range(n):
    for j in range(m):
        if p[i][j] == "#":
            q.append((i, j))
for i in range(n):
    for j in range(m):
        a = max(min(abs(i - a) + abs(j - b) for a, b in q), a)
print(a)

# shortest
from scipy.ndimage import *

print(morphology.distance_transform_cdt([[t > '#' for t in s[:-1]] for s in open(0)][1:], 'taxicab').max())
