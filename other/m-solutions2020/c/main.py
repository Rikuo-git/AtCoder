#!/usr/bin/env python3
n, k, *a = map(int, open(0).read().split())
for i in range(n - k):
    print("YNeos"[a[i] >= a[i + k]::2])
