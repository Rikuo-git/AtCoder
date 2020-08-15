#!/usr/bin/env python3
n, p = map(int, input().split())
temp = p
ans = 1
for i in range(2, int(-(-(p**0.5) // 1)) + 1):
    if temp % i == 0:
        cnt = 0
        while temp % i == 0:
            cnt += 1
            temp //= i
        ans *= i**(cnt // n)
if temp != 1:
    ans *= temp*(n == 1) or 1
print(ans)
