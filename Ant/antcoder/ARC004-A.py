# my solution
(n,), *c = [list(map(int, i.split())) for i in open(0)]
m = 0
for i in range(n):
    for j in range(i + 1, n):
        m = max(m, sum((k - h) ** 2 for k, h in zip(c[i], c[j])))
print(m ** .5)

# fastest by ikatakos
import itertools
print(max(abs(p-q)for p,q in itertools.combinations((complex(*map(int,input().split()))for _ in range(int(input()))),2)))
#全ての組み合わせを考え、複素数に変換し絶対値を出力。好き

# shortest by c_r_5
_,*a=[list(map(int,t.split()))for t in open(0)];print(max(((x-v)**2+(y-w)**2)**.5for x,y in a for v,w in a))
