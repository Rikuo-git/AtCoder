n,x,*a=map(int, open(0).read().split())
a.sort()
for i in range(n):
    x-=a[i]
    if x<0:
      print(i)
      exit()
    elif x==0:
      print(-~i)
      exit()
print(n-1)

# shortest
n,x,*a=map(int,open(0).read().split());c=0
for t in sorted(a):
  x-=t
  if x<0:break
  c+=1
print(c-(x>0))