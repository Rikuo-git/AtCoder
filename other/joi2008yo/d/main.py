#!/usr/bin/env python3
n = int(input())
N = [[*map(int, input().split())] for _ in range(n)]
m = int(input())
M = set(tuple([*map(int, input().split())]) for _ in range(m))

seiza = [[i - N[0][0], j - N[0][1]] for i, j in N[1:]]

for x, y in M:
    if all((x + i, y + j) in M for i, j in seiza):
        print(x - N[0][0], y - N[0][1])
        exit()
# 要素の探索はset の方が list より早い O(1)
# 2分探索もsortする必要があるときはO(nlog(n)log(n))になってしまう
