# my solution
n, k, *x = map(int, open(0).read().split())
print(sum(k - i if k / 2 < i else i for i in x) * 2)
# min(k-i,i)の方が良かったね
# shortest by c_r_5
_, k, t = open(0)
print(sum(min(x, int(k) - x) * 2 for x in map(int, t.split())))
