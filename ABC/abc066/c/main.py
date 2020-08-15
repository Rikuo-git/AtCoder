#!/usr/bin/env python3
n = int(input())
a = input().split()
ans = a[1 - n % 2::2][::-1] + a[n % 2::2]
print(*ans)
