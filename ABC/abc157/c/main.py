#!/usr/bin/env python3
(n, _), *m = [[*map(int, i.split())] for i in open(0)]

a = [0]*(n<2) or [1]+[0] * ~-n

for s, c in m:
    if s==1 and a[s-1] in (1,c):
        a[s-1] = c
    elif a[s - 1] in (0, c):
        a[s - 1] = c
    else:
        print(-1)
        exit()

a = int("".join([*map(str, a)]))
if len(str(a))!=n:
    print(-1)
else:
    print(a)

# フラグを立てる
f=lambda:map(int,input().split())
n,m=f()
l=[0]*n
b=[0]*n
if n>1: l[0]=1
for _ in range(m):
  s,c=f()
  s-=1
  if b[s] and l[s]!=c or n>1 and s==c==0:
    print(-1)
    exit()
  l[s]=c
  b[s]=1
print(*l,sep='')
