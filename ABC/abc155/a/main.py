#!/usr/bin/env python3
print("YNeos"[2 != len(set(map(int, input().split())))::2])
