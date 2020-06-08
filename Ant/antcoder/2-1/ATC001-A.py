import sys
sys.setrecursionlimit(1000000)

h, w = map(int, input().split())
r = [list(input()) for _ in range(h)]


def dfs(i, j):
    r[i][j] = "#"
    for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx = i + x
        ny = j + y
        if 0 <= nx < h and 0 <= ny < w and r[nx][ny]!="#":
            dfs(nx, ny)


for i in range(h):
    for j in range(w):
        if r[i][j] == "s":
            dfs(i, j)
            print("YNeos"["g" in sum(r, [])::2])

# shortest  by sqrt
import sys

sys.setrecursionlimit(500000)
h, w = map(int, input().split())
l = [list(input()) for _ in range(h)]


def dfs(r, c):
    if not (0 <= c < w and 0 <= r < h) or l[r][c] == "#":
        return
    if l[r][c] == "g":
        print("Yes")
        exit()
    l[r][c] = "#"
    dfs(r + 1, c)
    dfs(r - 1, c)
    dfs(r, c + 1)
    dfs(r, c - 1)


for i, y in enumerate(l):
    if "s" in y:
        dfs(i, y.index("s"))
        break
print("No")
