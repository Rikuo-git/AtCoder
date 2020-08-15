#!/usr/bin/env python3
from collections import defaultdict

d = defaultdict(int)
for _ in range(int(input())):
    d[input()] += 1
for _ in range(int(input())):
    d[input()] -= 1
print(max(*d.values(), 0))
