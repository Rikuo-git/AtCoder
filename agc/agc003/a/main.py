#!/usr/bin/env python3
s = input()
s = {i for i in s}
if len(s) == 4 or s == {"N", "S"} or s == {"W", "E"}:
    print("Yes")
else:
    print("No")
    

S=input()
n,w,e,s='N' in S, 'W' in S, 'E' in S, 'S' in S
print('Yes' if (n==s and e==w) else 'No')
