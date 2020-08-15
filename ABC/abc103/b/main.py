#!/usr/bin/env python3
s = input()
t = input()
for i in range(len(s)):
    if s[i + 1:] + s[:i + 1] == t:
        print("Yes")
        exit()
print("No")
