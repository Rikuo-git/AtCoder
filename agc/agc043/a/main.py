#!/usr/bin/env python3
from collections import deque

h, w = map(int, input().split())
maze = [[i == "#" for i in input()] for _ in range(h)]

dx = [1, 0]
dy = [0, 1]

que = deque([])
que.append((0, 0, maze[0][0], 1 if maze[0][0] else 0))
count = [[h + w] * w for _ in range(h)]

while que:
    x, y, b, c = que.pop()
    if c >= count[x][y]:
        continue
    count[x][y] = c
    if x == h - 1 and y == w - 1:
        continue
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < h and 0 <= ny < w):
            continue
        que.append((nx, ny, maze[nx][ny], c + (not b and maze[nx][ny])))
print(count[h - 1][w - 1])

t, *b = "." * 102
q = range(101)
for s in [*open(i := 0)][1:]:
    a = (i, )
    i += 1
    for x, y, z, c in zip(b, t + s, s, q):
        a += (min(c + (t > z < x), a[-1] + (t > z < y)), )
    b, q = s, a[1:]
print(a[-2])
