 # my solution
n = int(input())
t=2
while n//t>0:
    t *= 2
print(t//2)

# shortest by aki1502
print(1<<len(bin(int(input())))-3)
# 2で割るならバイナリの方が早いよね。。。
# バイナリの桁求めて最大値をかける