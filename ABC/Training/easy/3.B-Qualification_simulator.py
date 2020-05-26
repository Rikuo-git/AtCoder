# my solution
n, a, b = map(int, input().split())
s = input()
q = [1] * n
for i, l in enumerate(s):
    q[i] *= ((l == "b" and b > 0) or l == "a") and a + b > 0
    b -= q[i] * (l == "b")
    a -= q[i] * (l == "a")
print("\n".join(["YNeos"[1 - i::2] for i in q]))

# shortest by aki1502
# 素直に解けばよかった…
_, A, B = map(int, input().split())
for c in input():
    if (c == "a") & (A + B > 0):
        print("Yes")
        A -= 1
    elif (c == "b") & (A + B > 0) & (B > 0):
        print("Yes")
        B -= 1
    else:
        print('No')
