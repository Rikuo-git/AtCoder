n, *a = map(int, open(0).read().split())
b = max(a)
a.remove(b)
c = min(a, key=lambda x: abs(x - b/2))
print(b, c)
