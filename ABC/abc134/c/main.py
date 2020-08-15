#!/usr/bin/env python3
n,*a=map(int, open(0).read().split())
s = sorted(a)
for i in a:
    if i!=s[-1]:
        print(s[-1])
    else:
        print(s[-2])
