#!/usr/bin/env python3
(n, m,), *sub = [i.split() for i in open(0)]

r = {str(i+1): 0 for i in range(int(n))}
pen = 0
ac = 0
for p, s in sub:
    if r[p]>-1:
        if s == "WA":
            r[p]+=1
        else:
            ac += 1
            pen += r[p]
            r[p] = -1
print(ac, pen)
