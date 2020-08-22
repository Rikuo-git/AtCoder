from collections import deque

h, w = map(int, input().split())
cx, cy = map(lambda x: int(x) - 1, input().split())
dx, dy = map(lambda x: int(x) - 1, input().split())
s = [[i for i in input()] for _ in range(h)]
c = [[10**6] * w for _ in range(h)]

d = ((1, 0), (-1, 0), (0, 1), (0, -1))
q = deque([(cx, cy)])

c[cx][cy] = 0

while q:
    x, y = q.pop()
    cp = c[x][y]
    if (x, y) == (dx, dy):
        c[x][y] = cp
        break
    for i, j in d:
        nx = x + i
        ny = y + j
        if 0 <= nx < h and 0 <= ny < w and s[nx][ny] != "#" and c[nx][ny] > cp:
            q.append((nx, ny))
            c[nx][ny] = cp
    cp += 1
    for i in range(-2, 3):
        for j in range(-2, 3):
            nx = x + i
            ny = y + j
            if 0 <= nx < h and 0 <= ny < w and s[nx][ny] != "#" and c[nx][
                    ny] > cp:
                c[nx][ny] = cp
                q.appendleft((nx, ny))
print(-1 * (c[dx][dy] == 10**6) or c[dx][dy])
