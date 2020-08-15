#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n, *a = map(int, open(0).read().split())
dp = [10**9] * n


def cost(i):
    if i == 0:
        return 0
    if i == 1:
        return abs(a[1] - a[0])
    if dp[i] < 10**9:
        return dp[i]
    dp[i] = min(
        cost(i - 1) + abs(a[i] - a[i - 1]),
        cost(i - 2) + abs(a[i] - a[i - 2]))
    return dp[i]


print(cost(n - 1))
