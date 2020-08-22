#!/usr/bin/env python3
n = input()
print("YNeos"[sum(int(i) for i in n) % 9 > 0::2])
