n,*a=map(int,open(0).read().split())
s=1
if 0 in a:
    print(0)
    exit()
for i in a:
    s*=i # 判定してからかけてあげるのが吉　s > 1e18/i まあpythonならいける
    if  s > 1e18:
        print(-1)
        exit()
print(s)

# かけすぎだめ
n=int(input())
s=eval(input().replace(" ", "*"))
print([-1,s][s<10**18])


# 復習
n,*a=map(int,open(0).read().split())
s=1
a.sort()
for i in a:
    s *= i
    if s > 1e18:
        print(-1)
        exit()
print(s)