# my solution
c,*s=input()
n=len(s)
def a(i,j):
    if i == n:
        if eval(j)==7:
            return j+"=7"
        else:
            return False
    if a(i+1,j+"+"+s[i]):
        return a(i+1,j+"+"+s[i])
    if a(i+1,j+"-"+s[i]):
        return a(i+1,j+"-"+s[i])
    return False
print(a(0,c))

# bit ver
c,*s=input()
n=len(s) # nは決まってる
for b in range(1<<n):
    t = c + ""
    for i in range(n):
        t += ["-","+"][b>>i & 1] + s[i]
    if eval(t) == 7:
        print(t+"=7")
        break

# shortest by c_r_5
a,b,c,d=input()
o='+-'
for i in range(8):
    s=a+o[i&1]+b+o[i&2]+c+o[i&4]+d
    if eval(s)==7:print(s+'=7');break