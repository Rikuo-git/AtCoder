import sys

sys.setrecursionlimit(1000000)
m = [list(input()) for _ in range(10)]


def dfs(i, j):
    m[i][j] = "O"
    for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        x = i + a
        y = j + b
        if 0 <= x < 10 and 0 <= y < 10:
            if m[x][y] == "o":
                dfs(x, y)
            elif m[x][y] == "x":
                m[x][y] = [1, 0][c > 1]
            elif type(m[x][y]) == int and m[x][y] == ~-c:
                m[x][y] = c


c = 0
for i in range(10):
    for j in range(10):
        if m[i][j] == "o":
            c += 1
            dfs(i, j)

print(["NO", "YES"][c in sum(m, [])])

# shortest by orangecolor
from scipy import array, ndimage

r = range(10)
A = array([[c < "p" for c in input()] for _ in r])
a = 1
for i in r:
    for j in r:
        p = i, j
        o = A[p]
        A[p] = 1
        a &= ndimage.label(A + 0)[1] > 1
        A[p] = o
print("YNEOS"[a::2])

# ndimage.label  集団をらべるして、index[1]でその数を出力