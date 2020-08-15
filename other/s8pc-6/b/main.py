(n, ), *arr = [[*map(int, i.split())] for i in open(0)]
a, b = [list(i) for i in zip(*arr)]
a.sort()
b.sort()
m = n // 2
print(sum(b + a[-m:] + b[-m:]) - sum(a + a[:m] + b[:m]))
