#!/usr/bin/env python3
h, w, n, *a = map(int,open(0).read().split())
ans = []
for i, j in enumerate(a):
    ans += [i + 1] * j
for i in range(h):
    print(*ans[i*w:(i+1)*w][::-1+2*(i%2)])
