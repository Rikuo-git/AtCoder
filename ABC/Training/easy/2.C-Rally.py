#my solution
n, *x = map(int, open(0).read().split())
p = round(sum(x)/n)
print(sum((i - p)**2 for i in x))


#shortest solution by c_r_5 全ての座標を総当たり
_,x=open(0)
print(min(sum((i-int(j))**2for j in x.split())for i in range(99)))
