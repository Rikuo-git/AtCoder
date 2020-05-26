# my solution
(n, _, c), b, *a = [list(map(int, t.split())) for t in open(0)]
n = [1] * n
for h, i in enumerate(a):
    n[h] *= sum(j * k for j, k in zip(b, i)) + c > 0
print(sum(n))

# shortest by c_r_5
I = lambda: map(int, input().split())
n, m, c = I()
*b, = I()
print(eval('+(-c<sum(x*y for x,y in zip(I(),b)))' * n))

# revised ver.
(n, _, c), b, *a = [list(map(int, t.split())) for t in open(0)]
print(sum(-c<sum(j * k for j, k in zip(b, i)) for i in a))
