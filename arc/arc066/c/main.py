n, *a = map(int, open(0).read().split())
print(
    pow(2, n // 2, 10**9 + 7) *
    (sorted(a)[n & 1::2] == [*range(1 + n % 2, n, 2)]) or 0)
