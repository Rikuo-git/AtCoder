# my source code
k, n, *a = map(int, open(0).read().split())
a.append(a[0] + k)
print(k - max(a[i + 1] - a[i] for i in range(n)))

# shortest by fsdshn
k, n, *l = map(int, open(0).read().split())
print(min((l[i - 1] - l[i]) % k for i in range(n)))
# Ai - Ai+1 を　K  で割った余りは　K - (Ai - Ai+1)　になる
