#!/usr/bin/env python3
(w,),(n,k,),*a = [[*map(int, i.split())]for i in open(0)]
dp = [[[0]*(k+1) for _ in range(w+1)] for _ in range(n+1)]
for h in range(1,k+1):
    for i in range(n):
        for j in range(w):
            if j < a[i][]
            dp[i+1][]
