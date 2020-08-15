#!/usr/bin/env python3
s = input()
c = 0
a = 0
for i in s:
    if i in ["A", "C", "T", "G"]:
        c += 1
        a = max(a, c)
    else:
        c = 0
print(a)


import re
sp = re.split(r'[^ACTG]',s)
print(max(len(i)for i in sp))
