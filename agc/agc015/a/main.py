n, a, b = map(int, input().split())
c = (n - 2) * (b - a)
print(0 if c < 0 else c + 1)
