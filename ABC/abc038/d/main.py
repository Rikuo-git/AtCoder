#!/usr/bin/env python3
import bisect

(n, ), *s = [[*map(int, i.split())] for i in open(0)]
s.sort(key=lambda x: (x[0], -x[1]))
seq = [i[1] for i in s]
LIS = [seq[0]]
for i in seq:
    if i > LIS[-1]:
        LIS.append(i)
    else:
        LIS[bisect.bisect_left(LIS, i)] = i
print(len(LIS))
