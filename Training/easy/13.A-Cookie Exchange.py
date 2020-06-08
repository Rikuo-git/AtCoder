# my solution
*a, = map(int,input().split())
if any(map(lambda x: bin(x)[-1]== "1", a)):
     print("0")
     exit()
a = [bin(abs(a[i+1]-a[i]))[::-1].find('1') for i in range(2)]
print(max(a) if a[0]*a[1]<0 else min(a))

# revised var
*a,=map(int,input().split())
b=[bin(a[i+1]-a[i])[::-1].find('1')for i in (0,1)]
print((max(b)*(b[0]*b[1]<0) or min(b))*(1-sum(a)%2))

# # shortest by orangecolor
a,b,c=map(int,input().split());o=0
if a==b==c:print(a%2-1);exit()
while~-a*~-b*~-c%2:a,b,c=(b+c)//2,(c+a)//2,(a+b)//2;o+=1
print(o)