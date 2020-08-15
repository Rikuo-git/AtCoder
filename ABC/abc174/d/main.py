#!/usr/bin/env python3
input()
c = input()
R = c.count("R")
W = c.count("W")
c2 = "R"*R+"W"*W
r = sum(i!=j and i =="W" for i, j in zip(c,c2))
w = sum(i!=j and i =="R" for i, j in zip(c,c2))
print(min(r,w))
