#!/usr/bin/env python3
n=int(input())
i=9
while i>0:
    if n%i==0:
        print("YNeos"[n//i>9::2])
        exit()
    i-=1
print("No")
