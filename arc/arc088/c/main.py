#!/usr/bin/env python3
x, y = map(int, input().split())
print(len(bin(y // x)) - 2)
