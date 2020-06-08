# my solution
# n, *a = map(int, open(0).read.split())
# print(-~a.index(-~i) for i in range(n))

n, *a = map(int, open(0).read().split())
s = [[j, i] for i, j in zip(range(1, n + 1), a)]
s.sort()
print(*[i[1] for i in s])

# shortest by c_r_5
from numpy import *
_, a = open(0)
print(argsort(int32(a.split())) + 1)
# numpy のargsortはsortしてその値のindexを出力

# fastest sortしない
N, *A = map(int, open(0).read().split())
ans = [0] * (N + 1)
for i, j in enumerate(A, 1):
    ans[j] = i
print(" ".join(map(str, ans[1:])))