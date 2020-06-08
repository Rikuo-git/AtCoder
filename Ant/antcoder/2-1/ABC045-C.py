# my solution
s = list(input())
n = len(s)
def c(i, t):
    if i == n:
        return eval("".join(t))
    return c(i + 1, t + "+" + s[i]) + c(i + 1, t + s[i])
print(c(1, s[0]))
# bit 全探索
print(sum(eval(s[0] + ''.join('+' * (b >> i & 1) + s[i+1] for i in range(n-1)))for b in range(1<<n-1)))

# shortest by keijak
a, b, k = 0, 0, 1
for d in input():
    a, b = 2 * a + b, 10 * b + int(d) * k
    k *= 2
print(a + b)
