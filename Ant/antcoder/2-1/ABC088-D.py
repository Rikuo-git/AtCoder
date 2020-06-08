from collections import deque

h, w = map(int, input().split())
map = [list(input()) for _ in range(h)]
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)


def bfs():
    q = deque([])
    q.append((0, 0))
    d = [([-1] * w) for _ in range(h)]

    d[0][0] = ~-sum(1 for i in range(h) for j in range(w) if map[i][j] == ".")

    while q:
        x, y = q.popleft()
        if (x, y) == (h - 1, w - 1):
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and d[nx][ny] == -1 and map[nx][ny] != "#":
                q.append((nx, ny))
                d[nx][ny] = d[x][y] - 1
    return d[h - 1][w - 1]


print(bfs())