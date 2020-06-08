# my solution

(d, g), *s = [list(map(int, i.split())) for i in open(0)]
s = [[i[0] * -~n * 100 + i[1], i[0]] for n, i in enumerate(s)]
a = 10 ** 3
for b in range(1 << d):
    su = sum(s[i][0] * (b >> i & 1) for i in range(d))
    n = sum(s[i][1] * (b >> i & 1) for i in range(d))
    if su < g:
        m = d - bin(b)[2:].zfill(d).find("0")
        e = (su - g) // (m * 100)
        if -e < s[m - 1][1]:
            a = min(a, n - e)
    if su >= g:
        a = min(a, n)
print(a)

(d, g), *s = [list(map(int, i.split())) for i in open(0)]


def c(i, t, l):
    if i == d:
        if t >= g:
            return sum(l)
        else:
            m = d - l[::-1].index(0)
            e = (t - g) // (m * 100)
            if -e < s[m - 1][0]:
                return sum(l) - e
            else:
                return 10 ** 3
    return min(c(i + 1, t, l + [0]), c(i + 1, t + s[i][0] * -~i * 100 + s[i][1], l + [s[i][0]]))


print(c(0, 0, []))

# shortest by KyleKatran
(d, g), *l = [list(map(int, i.split())) for i in open(0)]
def f(i, g):
    if i == 0: return 1e9
    n, m = l[i - 1]
    c = min(g // (100 * i), n)
    s = 100 * i * c + m * (c == n)
    c += f(i - 1, g - s) * (s < g)
    return min(c, f(i - 1, g))
print(int(f(d, g)))
# 大きいものから順に全部入れるか決めていく。しかし、最大のものを p > n　個しか使わない場合は成り立たない。
