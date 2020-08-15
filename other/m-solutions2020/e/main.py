#!/usr/bin/env python3
from itertools import combinations

n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]
x = set(p[i][0] for i in range(n))
y = set(p[i][1] for i in range(n))
X = list(x)
Y = list(y)
a = len(X)
b = len(Y)
m = min(a, b)
for i in range(m):
    cost = 10**9
    for j in combinations(range(a + b), i):
        c = 0
        nx = {0}
        ny = {0}
        for k in j:
            if k < a:
                nx.add(X[k])
            else:
                ny.add(Y[k - a])
        for ps in p:
            if ps[0] not in nx and ps[1] not in ny:
                c += (min(min(abs(ps[0] - i)
                              for i in nx), min(abs(ps[1] - i)
                                                for i in ny)) * ps[2])
        cost = min(cost, c)
    print(cost)

for i in range(n - m + 1):
    print(0)
