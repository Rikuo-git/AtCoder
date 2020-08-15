#!/usr/bin/env python3
n, q = map(int, input().split())
c = [*map(int, input().split())]
sets = [set()]
for i in c:
    sets.append(sets[-1] | {i})
back = [set()]
for i in reversed(c):
    back.append(back[-1] | {i})
for _ in range(q):
    l, r = map(int, input().split())
    print(len(back[-l] & sets[r]))
