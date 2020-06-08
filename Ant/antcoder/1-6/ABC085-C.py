#my solution
n,y=map(int,input().split())
y //= 1000
for i in range(n+1):
    for j in range(n-i+1):
        if 9*i + 4*j + n == y:
            print(i,j,n-i-j)
            exit()
print("-1 "*3)

# faster ver.
n,y=map(int,input().split())
y //= 1000
for i in range(n+1):
    p,q = divmod(y-n-i,4)
    if q == 0 and i <= p-i <= n:
        print(i,p-2*i, n-p+i)
        exit()
print("-1 "*3)

# fast and short by faogr
n,y = map(int,input().split())
d=y//1000-n
a=(d*7)%9 # 7=4^-1
b=(d-a*4)//9
c=n-a-b
if c>=0 and b>=0:
    print(b,a,c)
else:
    print(-1,-1,-1)

# 最小のjを求める
# d = 9*i + 4j
# d = 4j (mod 9)
# d*7 = j (mod 9)
# この時、残りの数が0以上の時、実現可能
