#!/usr/bin/env python3
from functools import reduce

mod = 10**9 + 7


def cmb(n, r, m):
    def mul(a, b):
        return a * b % m

    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over * pow(under, m - 2, m)


n, a, b = map(int, input().split())
print((pow(2, n, mod) - 1 - cmb(n, a, mod) - cmb(n, b, mod)) % mod)
