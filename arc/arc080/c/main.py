#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
o = sum(i % 2 > 0 for i in a)
q = sum(i % 4 < 1 for i in a)
if n == o + q and o - 1 == q:
    print("Yes")
else:
    print("YNeos"[o > q::2])
