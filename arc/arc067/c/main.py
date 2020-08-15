#!/usr/bin/env python3
n = int(input())
def count(x):
    c = 1
    t = n
    while t:
        c += (t := t//x)
    return c
limit = int(n**0.5)
ans = count(2)
if n < 3:
    print(ans)
    exit()
data = [i + 1 for i in range(2, n, 2)]
while data:
    p = data[0]
    ans *= count(p)
    ans %= 10**9 + 7
    data = [e for e in data if e % p != 0]
print(ans)
