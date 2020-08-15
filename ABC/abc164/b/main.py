#!/usr/bin/env python3
a, b, c, d = map(int, input().split())
print("YNeos"[-(-c // b) > -(-a // d)::2])
