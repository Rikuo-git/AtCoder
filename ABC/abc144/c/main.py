#!/usr/bin/env python3
def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


y = make_divisors(int(input()))

if len(y) % 2 > 0:
    print(y[len(y) // 2] * 2 - 2)
else:
    print(y[len(y) // 2 - 1] + y[len(y) // 2] - 2)
