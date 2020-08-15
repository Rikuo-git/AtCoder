#!/usr/bin/env python3
n=int(input())
s=input()
print('YNeos'[n%2>0 or s[:n//2]!=s[-(n//2):]::2])
