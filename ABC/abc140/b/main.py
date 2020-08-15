#!/usr/bin/env python3
n=int(input())
*a,=map(int,input().split())
*b,=map(int,input().split())
*c,=map(int,input().split())
print(sum(b)+sum(c[a[i]-1]for i in range(n-1) if a[i]+1==a[i+1]))
