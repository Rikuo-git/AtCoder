# my solution
import math
a, b, h, m = map(int, input().split())
r = abs(h/12 + m/720 - m/60)*math.pi*2
print((a**2 + b**2 - 2*a*b*math.cos(r))**(0.5))

# shortest
a,b,h,m=map(int,input().split())
from math import*
print((a*a+b*b-2*a*b*cos((m*11/360-h/6)*pi))**.5)

# 余弦定理やるだけ