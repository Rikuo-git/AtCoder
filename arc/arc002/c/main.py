#!/usr/bin/env python3
from itertools import product

n = int(input())
C = input()
B = ["A", "B", "X", "Y"]
LR = product(B, repeat=4)
ans = 10**5
for i in LR:
    L = "".join(i[:2])
    R = "".join(i[-2:])
    c = C.replace(L, "").replace(R, "")
    print(c)
    a = (n - len(c)) // 2 + len(c)
    ans = min(ans, a)
print(ans)
