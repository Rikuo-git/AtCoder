#!/usr/bin/env python3
A, B = map(int, input().split())
s = {*range(25 * A, 25 * A + 25)} & {*range(20 * B, 20 * B + 20)}
s = {i // 2 for i in s if i % 2 < 1}
print(-1 * (len(s) < 1) or min(s))
