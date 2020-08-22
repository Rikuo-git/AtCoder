#!/usr/bin/env python3
_, *w = map(int, open(0).read().split())
a = []
for i in w:
    b = [j for j in a if j >= i]
    if b:
        a.remove(min(b))
    a.append(i)
print(len(a))
