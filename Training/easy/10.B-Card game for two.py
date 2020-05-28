# my solution
_, *a = map(int, open(0).read().split())
a.sort()
print(sum(a[-1::-2]) - sum(a[-2::-2]))

# shortest by c_r_5
_,s=open(0);c=0
for a in sorted(map(int,s.split())):c=a-c
print(c)
