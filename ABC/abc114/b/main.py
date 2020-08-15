#!/usr/bin/env python3
s=input()

print(min(abs(int(s[i:i+3])-753) for i in range(len(s)-2)))
