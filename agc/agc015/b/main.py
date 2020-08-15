S = input()
N = len(S)
print(sum(N + n - 1 if s == "U" else 2 * N - n - 2 for n, s in enumerate(S)))
