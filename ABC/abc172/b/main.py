#!/usr/bin/env python3
s, t = open(0).read().split()

print(sum(1 for i, j in zip(s, t) if i != j))
