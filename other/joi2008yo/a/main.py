#!/usr/bin/env python3
n= int(input())
c=0
coin=[500,100,50,10,5,1]
n = 1000 -n
for i in coin:
    c += n//i
    n %= i
print(c)
