#!/usr/bin/env python3
s = input()
print(sum(s[i - 1] != s[i] for i in range(1, len(s))))
