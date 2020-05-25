#my solution
a,b,c,k = map(int, open(0).read().split())
if k <= a:
    print(k)
else:
    if k-a <= b:
        print(a)
    else:
        print(a-(k-a-b))

#shortest solution
a,b,c,k=map(int,input().split())
print(min(2*a+b-k,a,k))