#!/usr/bin/env python3
n = int(input())
x = input()
c = x.count("1")
m = 0
m2 = 0
for i in range(n):
    if x[i] == "1":
        m += pow(2, (n - i - 1), c + 1)
        m %= c + 1
m2 = 0
if c!=1:
    for i in range(n):
        if x[i] == "1":
            m2 += pow(2, (n - i - 1), c - 1)
            m2 %= c - 1

for i in range(n):
    if x[i] == "1":
        if c != 1:
            t = m2 - pow(2, (n - i - 1), c - 1)
            t %= c - 1
            count = 1
        else:
            t = 0
            count = 0
    else:
        t = m + pow(2, (n - i - 1), c + 1)
        t %= c + 1
        count = 1
    while t > 0:
        t %= bin(t).count("1")
        count += 1
    print(count)
