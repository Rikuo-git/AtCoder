# my solution
import math
n = int(input())
a = math.ceil(n/1.08) # = int(--)
b = math.floor(a*1.08) # = int()
print(a*(n == b) or ":(")

# code by eugalt
n = int(input()) * 25
r = (n + 24)//27
print((r, ':(')[r * 27 < n])

