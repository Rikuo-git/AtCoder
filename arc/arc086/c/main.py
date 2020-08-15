#!/usr/bin/env python3
from collections import Counter

n, k, *a = map(int, open(0).read().split())
c = Counter(a)
print(sum(sorted(c.values())[:len(c) - k]))
