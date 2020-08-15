#!/usr/bin/env python3
n, x, y = map(int, input().split())
c = [[n]*n for _ in range(n)]
for i in range(n-1):
    c[i][i+1] = 1
c[x][y] == 1
d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
for i in range(n-2):
    for j in range(i+2, n):
        c[i][j] = 1 + min(c[i+dx][j+dy] for dx, dy in d if 0<=i+dx and 



for i in r
