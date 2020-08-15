#!/usr/bin/env python3


def make_divisors(n):
    i = 1
    c = 0
    while i * i <= n:
        if n % i == 0:
            c += 1
            if i != n // i:
                c += 1
        i += 1
    return c * n


def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    prime = []
    t = 1
    for i in range(2, n + 1):
        if not is_prime[i]:
            temp = i
            cnt = 1
            for j in prime:
                if temp % j == 0:
                    ind = 0
                    while temp % j == 0:
                        ind += 1
                        temp //= j
                    cnt *= ind + 1
            t += i * cnt
            continue
        else:
            prime.append(i)
            t += 2 * i
        if i <= int(n**0.5):
            for j in range(i * 2, n + 1, i):
                is_prime[j] = False
    return t


def factorization(n):
    if n == 1:
        return 1
    arr = 0
    temp = n
    c = 1
    for i in p[int(-(-(n**0.5) // 1)) + 1 > p]:
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr = 1
            c *= cnt + 1

    if temp != 1:
        arr = 1
        c *= 2

    if arr == 0:
        c *= 2

    return c * n


n = int(input())
p = primes(n)
# def factorization(n):
# arr = []
#     temp = n
#     c=1
#     for i in range(2, int(-(-n**0.5//1))+1):
#         if temp%i==0:
#             cnt=0
#             while temp%i==0:
#                 cnt+=1
#                 temp //= i
#             c*=cnt+1
#
#     if temp!=1:
#         arr.append([temp, 1])
#
#     if arr==[]:
#         arr.append([n, 1])
#
#     return arr
#
#
# n = int(input())
print(p)

ans = 0
n = int(input())
for i in range(1,n+1):
    k = n//i
    ans += i*k*(k+1)//2
print(ans)
