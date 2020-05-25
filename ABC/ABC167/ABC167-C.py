# my solution
n, m, x = map(int, input().split())
c, a = [0] * n, [0] * n
for i in range(n):
    c[i], *a[i] = map(int, input().split())
l = []
b = [[a[j][i] for j in range(n)] for i in range(m)]
nums = [("0" * n + bin(i)[2:])[-n:] for i in range(1, 2 ** n)]
*s = map(sum,zip(*a[i] for i in ranen(n)))
for i in nums:
    if min(sum(k[j] * int(i[j]) for j in range(len(i))) for k in b) >= x:
        l.append(sum(c[j] * int(i[j]) for j in range(len(i))))
print(min(l) if l else -1)

# shortest solution
(n, m, x), *t = [[*map(int, t.split())] for t in open(0)]
m = M = 9 ** 9
for i in range(1, 2 ** n):
    c, *a = map(sum, zip(*[t[j] for j in range(n) if i >> j & 1]))
    m = min(m, M * (min(a) < x) or -~c)
print(m % M - 1)

# -~ = +1 ~- = -1
# zip 複数のiterable を同時に扱う
# *list 要素を展開
#リストの縦の足し算と横の足し算
s = list(map(sum, zip(*t)))
t = list(map(sum,t))
 #縦横変換
s = list(map(list, zip(*t)))

# a*boolen or b True の値が採用