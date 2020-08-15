#!/usr/bin/env python3
L, X, Y, S, D = map(int, input().split())
print(min((D - S) % L / (X + Y), 1e9 * (Y <= X) or (S - D) % L / (Y - X)))
