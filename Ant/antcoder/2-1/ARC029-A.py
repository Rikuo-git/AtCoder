# my solution
n,*t=map(int, open(0).read().split())
t.sort()
def c(i,j):
    if t==None:return min(i,j)
    if i>j:
        j += t.pop(-1)
    else:
        i += t.pop(-1)
    return c(i,j)
print(c(i,j))

# shortest by c_r_5 再帰しなくても良かったね、、分岐してないし
_,*t=map(int,open(0))
S=[0,0]
t.sort()
while t:S[S[0]>S[1]]+=t.pop()
print(max(S))