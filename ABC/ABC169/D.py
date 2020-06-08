def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


f = factorization(24)
c = 0
for _, i in f:
    if _ == 1:
        print(0)
        exit()
    a = 1
    while a * -~a // 2 <= i:
        a += 1
    c += ~-a
print(c)

# shortest by ducky0
n = int(input())
a = p = 1
while p < 1e6:
    c = t = 0
    p += 1
    while n % p < 1:
        n //= p
        x = c == t
        t += x
        c += 1 - t * x
        a += x
        print(c,t,x)
print(a - (n < 2))
