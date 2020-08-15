#!/usr/bin/env python3
n,*s=open(0).read().split()
print('AC x {}'.format(s.count('AC')))
print('WA x {}'.format(s.count('WA')))
print('TLE x {}'.format(s.count('TLE')))
print('RE x {}'.format(s.count('RE')))
