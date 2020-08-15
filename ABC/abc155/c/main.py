#!/usr/bin/env python3
from collections import Counter

_, *s = open(0).read().split()

c = Counter(s).most_common()

a = []

p = 0
for i, j in c:
    if p > j:
        break
    p = j
    a.append(i)
print(*sorted(a), sep="\n")
