M = 10**9 + 7
n, k, *a = map(int, open(y := 0).read().split())
a.sort()
x = s = 1
r = k
while r > 1:
    if (t := a[y] * a[y + 1]) > a[-x] * a[~x]:
        s = s * t % M
        y += 2
        r -= 2
    else:
        s = s * a[-x] % M
        x += 1
        r -= 1
if r:
    s *= a[-x]
if a[-1] < 0 < k % 2:
    s = 1
    for i in a[-k:]:
        s = s * i % M
print(s % M)
