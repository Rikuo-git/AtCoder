# my solution
s=int(input())
a=[]
while s not in a:
    a.append(s)
    if s%2==0:
        s//=2
    else:
        s=3*s+1
print(-~len(a))

# shortest by c_r_5
s=int(input())
i=2
while~-s:s=[s//2,s*3+1][s%2];i+=1
print(max(i,4))