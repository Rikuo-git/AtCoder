#!/usr/bin/env python3
s = input()
k = int(input())
ans = ""
n = len(s)
for p, i in enumerate(s):
    if p == n - 1:
        ans += chr((ord(i) - 97 + k) % 26 + 97)
        break
    if (cost := (123 - ord(i)) % 26) <= k:
        ans += "a"
        k -= cost
    else:
        ans += i
print(ans)
