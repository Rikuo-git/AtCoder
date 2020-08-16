#!/usr/bin/env python3
N =input()
n=int(N)
ans=0

if len(N)>1:
    for i in range(1,10):
        for j in range(i+1,10):
            if j < int(N[0]):
                ans += 10**((len(N)-2)*2)*2
            elif j == int(N[0]) and i <= int(N[-1]):
                if i == int(N[-1]):
                    ans += 10**(len(N)-2)*(1 if len(N)<3 else int(N[1:-1]))*2
                else:
                    ans += 10**((len(N)-2)*2)*2
            else:
                if len(N)>2:
                    ans += 10**((len(N)-3)*2)*2
            break
for i in range(10):


print(ans)

for i in range()
