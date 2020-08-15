a, b, k = map(int, input().split())
print(*sorted({*range(a, b + 1)} & ({*range(a, a + k)} | {*range(b - k + 1, b + 1)})),sep="\n")
