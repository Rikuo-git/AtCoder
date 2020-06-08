t = int(input())


for _ in range(t):
    n = int(input())
    *a, = map(int, input().split())
    s = input()

    for i in range(n):
        if s[i] == "1":
            o |= a[i]
        else:
            p |= a[i]

    if o ^ s:
        print(1)
    else:
        print(0)

t = int(input())


def xorset(l):
    s = set()
    for b in range(1 << len(l)):
        n = 0
        for i in range(0, len(l)):
            if b >> i & 1:
                n ^= l[i]
        s.add(n)
    return s

for _ in range(t):
    n = int(input())
    *a, = map(int, input().split())
    s = input()
    o = []
    p = []
    for i in range(n):
        if s[i] == "1":
            o.append(a[i])
        else:
            p.append(a[i])
    sp = set(o)
    sp = xorset(p)
    xorsetp(0,0)
    if so & sp == so:
        print(0)
    else:
        print(1)