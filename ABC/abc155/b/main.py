#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
a = [i for i in a if i % 2 == 0 and i % 3 != 0 and i % 5 != 0]
print(["APPROVED", "DENIED"][len(a) > 0])
