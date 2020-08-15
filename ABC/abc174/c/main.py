#!/usr/bin/env python3
k = int(input())
if k % 2 < 1 or k % 5 < 1:
    print(-1)
else:
    c = 1
    mod = 7 % k
    mop = 7 % k
    while mod > 0:
        mop = mop*10%k
        mod += mop
        mod %= k
        c += 1
    print(c)
