from collections import deque
h,w,n = map(int,input().split())
map = [list(input()) for _ in range(h)]
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)
hp = deque([i+1 for i in range(n)])

def bfs(sx,sy,cost):
    d = [([-1]*w)for _ in range(h)]
    q = deque([])

    q.append((sx,sy))
    d[sx][sy] = 0

    if not hp:
        return cost

    g = hp.popleft()

    for i in range(h):
        for j in range(w):
            if str(g) == map[i][j]:
                gx = i
                gy = j
                break

    while q:
        x,y = q.popleft()
        if (x,y)==(gx,gy):
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < h and 0<= ny < w and map[nx][ny] != 'X' and d[nx][ny] == -1:
                q.append((nx,ny))
                d[nx][ny] = d[x][y] +1
    return bfs(gx,gy,cost+d[gx][gy])

for i in range(h):
    for j in range(w):
        if "S" == map[i][j]:
            print(bfs(i,j,0))
            exit()

# fastest code
import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

H, W, N = map(int, readline().split())

grid = np.frombuffer(read(), 'S1').reshape(H, -1)[:, :W].ravel()

ind = [np.where(grid == b'S')[0][0]]
for n in range(1, N + 1):
    ind.append(np.where(grid == str(n).encode())[0][0])


def grid_graph_edges(H, W):
    idx = np.arange(H * W).reshape(H, W)
    fr = []
    to = []
    x1 = idx[:, 1:].ravel()
    x2 = idx[:, :-1].ravel()
    fr += [x1, x2]
    to += [x2, x1]
    x1 = idx[1:, :].ravel()
    x2 = idx[:-1, :].ravel()
    fr += [x1, x2]
    to += [x2, x1]
    fr = np.concatenate(fr)
    to = np.concatenate(to)
    return fr, to


fr, to = grid_graph_edges(H, W)

bl = (grid[fr] != b'X') & (grid[to] != b'X')
fr = fr[bl];
to = to[bl]

graph = csr_matrix((np.ones(len(fr)), (fr, to)), (H * W, H * W))
dist = dijkstra(graph, directed=False, indices=ind[:-1])

answer = sum(int(dist[i, x]) for i, x in enumerate(ind[1:]))
print(answer)


#shortest
H, W, N = map(int, input().split())
grid = 'X' * (W + 2)
for _ in range(H):
    grid += 'X' + input() + 'X'
grid += 'X' * (W + 2)

start = grid.find('S')

ans = 0
move = [1, -1, W + 2, -(W + 2)]
for i in range(N):
    flg = [0] * len(grid)
    q = [[start, 0]]
    g = str(i + 1)
    while q:
        cp, cd = q.pop(0)
        if grid[cp] == g:
            ans += cd
            start = cp
            break
        elif flg[cp] == 1:
            continue
        else:
            flg[cp] = 1

        for d in move:
            if grid[cp + d] != 'X':
                q.append([cp + d, cd + 1])

print(ans)