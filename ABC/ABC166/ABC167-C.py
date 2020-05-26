# my solution
# TLE ver
(n, m), h, *r = [[*map(int, i.split())] for i in open(0)]
c = 0
for i in range(n):
    if i + 1 not in sum(r, []):
        c += 1
        continue
    l = [j * (i + 1 in j) for j in r]
    if h[i] > max(h[j-1] for j in set(sum(l, []))-{i + 1}):
        c += 1
print(c)

# AC ver.
(n, m), h, *r = [[*map(int, i.split())] for i in open(0)]
g = [] + h
#[1]*nでよかった。

for i in r: # a,b にすればよかった
    g[i[0] - 1] *= h[i[0] - 1] > h[i[1] - 1]
    g[i[1] - 1] *= h[i[1] - 1] > h[i[0] - 1]
print(len([i for i in g if i != 0]))

# revised ver.
(n, m), h, *r = [[*map(int, i.split())] for i in open(0)]
g = [1]*n
for a,b in r:
    g[-a] *= h[a - 1] > h[b - 1]
    g[-b] *= h[b - 1] > h[b - 1]
print(sum(g))


# shortest by c_r_5
n,h,*t=[[*map(int,t.split())]for t in open(0)]
p=[1]*n[0]
for a,b in t:
    x,y=h[a-1],h[b-1]
    p[-a] &= x>y
    p[-b] &= y>x
print(sum(p))
# やってることは同じ.二次元リストは　for で複数引数をとれる。
# & は bit演算子 1　の理論積を取る
