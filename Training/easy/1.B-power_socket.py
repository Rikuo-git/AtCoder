# my solution
a, b = map(lambda x: int(x) - 1, input().split())
print((b + a - 1) // a)

# short solution by c_r_5
a, b = map(int, input().split())
print(0 - -~-b // ~-a)

# 繰り上げの方法 1,(b + a - 1)//a 2, (0--b//a)
# ~- = -1 -~ = +1
