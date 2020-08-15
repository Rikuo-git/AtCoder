#!/usr/bin/env python3
L, R, d = map(int, input().split())
print(R // d - (L - 1) // d)
