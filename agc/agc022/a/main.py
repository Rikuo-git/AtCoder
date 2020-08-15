#!/usr/bin/env python3
s = input()
stock = [m for i in range(26) if (m := chr(ord("a") + i)) not in s]
if stock:
    print(s + stock[0])
else:
    for i in range(1, 26):
        if s[-i] > s[-1 - i]:
            print(s[:-1 - i] + min(j for j in s[-i:] if j > s[-1 - i]))
            break
        if i == 25:
            print(-1)
