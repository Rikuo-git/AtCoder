#!/usr/bin/env python3
# def is_ok(arg):
#     return c[arg] - c[i] >= k
#
#
# def bisect(ng, ok):
#     while abs(ok - ng) > 1:
#         mid = (ok + ng) // 2
#         if is_ok(mid):
#             ok = mid
#         else:
#             ng = mid
#     return ok
#
#
# n, k, *a = map(int, open(0).read().split())
# c = [0]
# ans = 0
# for i in a:
#     c.append(c[-1] + i)
# for i in range(n):
#     ans += n + 1 - bisect(i, n + 1)
# print(ans)
n, k, *a = map(int, open(0).read().split())
ans = r = s = 0
for l in range(n):
    while r < n:
        if s >= k:
            break
        s += a[r]
        r += 1
    if s < k:
        break
    ans += n - r + 1
    s -= a[l]
print(ans)
