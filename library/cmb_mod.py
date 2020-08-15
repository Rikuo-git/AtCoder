from functools import reduce

mod = 10**9 + 7


def cmb(n, r, m):
    mul = lambda a,b: a*b%m
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return (over * pow(under, m - 2, m))%m

