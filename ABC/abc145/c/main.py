#!/usr/bin/env python3
import math

(n, ), *p = [[*map(int, i.split())] for i in open(0)]
m = 0.0
f = math.factorial(n - 1)*2
for i in range(n):
    for j in range(i + 1, n):
        m += ((p[i][0] - p[j][0])**2 + (p[i][1] - p[j][1])**2)**0.5*f
print(m / math.factorial(n))
