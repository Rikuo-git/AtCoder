#!/usr/bin/env python3
from itertools import groupby
h,w=map(int,input().split())
s = [[i=="." for i in input()]for _ in range(h)]
ans = [[0]*w for _ in range(h)]
for i in s:
    for j in 
