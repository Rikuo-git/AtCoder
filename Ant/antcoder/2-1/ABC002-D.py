# my solution
(n, m), *r = [list(map(int, i.split())) for i in open(0)]
c = 1
for b in range(1 << n):
    g = [-~i for i in range(0, n) if b >> i & 1]
    l = len(g)
    if all([g[i], g[j]] in r for i in range(l) for j in range(-~i, l)):
        c = max(c, l)
print(c)

# shortest by しろくま
import itertools as t

c = t.combinations
f = lambda: map(int, input().split())
n, m = f()
d = {tuple(f()) for _ in range(m)}
r = range(1, n + 1)
all(any(d >= set(c(o, 2)) for o in c(r, a + 1)) or print(a) for a in r)


