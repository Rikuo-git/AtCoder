# my solution
# TLE ver
x= int(input())
a = [2]
n = 2
while a[-1] < x:
    n += 1
    if all(n%i for i in a):
        a.append(n)
print(n)

# fermat var AC
def f(n):
    if n==2:return 2
    for i in range(2,[n, 5][n>5]):
        if i**n%n != i:
            return f(n+1)
    return n
print(f(int(input())))

# shortest ver
x=int(input())
while any(x%i<1for i in range(2,x)):x+=1
print(x)
# この量なら普通に攻めても問題なかった

# short and fast
x = int(input())
while any(x%i<1 for i in range(2,int(x**0.5)+1)):
  x+=1
print(x)