while True:
    n, x = map(int, input().split())
    if (n, x) == (0, 0):
        break
    c = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if i + j + k == x - 3:
                    c += 1
    print(c)
