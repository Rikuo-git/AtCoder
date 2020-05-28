n = 5
a = (2,3,4,5,10)
c = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            len=a[i]+a[j]+a[k]
            c = max(c, (a[i]+a[j]+a[k])*(len > 2*max(a[i],a[j],a[k])))
print(c)