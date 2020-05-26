# my solution
(n, k), *p = [[*map(int, i.split())] for i in open(0)]
a = sum([p[2 * i + 1] for i in range(k)], [])
print(n - len(set(a)))

n, k = map(int, input().split())
a = set()
for i in [0] * k:
    _ = input()
    a = a | {*input().split()}
print(n - len(a))

# solution by c_r_5
n, _, *t = ''.join([*open(0)][::2]).split()
print(int(n) - len({*t}))
# リストの偶数ばんめ　[1::2]
