#!/usr/bin/env python3
i = [0] * (10**5 + 1)
for x in range(1, 100):
    for y in range(1, 100):
        for z in range(1, 100):
            i[x**2 + y**2 + z**2 + x * y + y * z + z * x] += 1

n = int(input())

print(*i[1:n + 1], sep="\n")
