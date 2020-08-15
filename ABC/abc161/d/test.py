from heapq import *

k = int(input())
test = []
#!/usr/bin/env python3

a = [*range(1, 10)]
heapify(a)
i = 0
c = 0
while True:
    t = str(heappop(a))
    test.append(t)
    i += 1
    if i == k:
        break
    if t[-1] != "0":
        heappush(a, int(t + str(int(t[-1]) - 1)))
    heappush(a, int(t + t[-1]))
    if t[0] != "9":
        heappush(a, int(t + str(int(t[-1]) + 1)))

print(t)

i = c = 0
while True:
    c += 1
    t = str(c)
    if all(abs(int(t[j]) - int(t[j + 1])) < 2 for j in range(len(t) - 1)):
        i += 1
        if t not in test:
            print(t)
    if i == k:
        break
