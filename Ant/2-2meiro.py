# 迷路の最短絡問題
from collections import deque

n,m = map(int,input().split())
maze = [list(input()) for _ in range(n)]

def bfs():
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    d = [([1e9]*m)for _ in range(n)]
    q = deque([])

    for i in range(n):
        for j in range(m):
            if maze[i][j] == "S":
                sx = i
                sy = j
            if maze[i][j] == "G":
                gx = i
                gy = j
    q.append((sx,sy))
    d[sx][sy] = 0

    while q:
        x,y = q.popleft()
        if (x,y)==(gx,gy):
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < m and maze[nx][ny] != '#' and d[nx][ny] == 1e9:
                q.append((nx,ny))
                d[nx][ny] = d[x][y] + 1

    return d[gx][gy]

print(bfs())