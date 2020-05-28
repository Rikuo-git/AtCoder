# my solution
from scipy.misc import comb
print(int(sum(comb(list(map(int,input().split())),2, exact = False))+0.5))

# shortest by c_r_5
n,m=map(int,input().split());print(n*~-n+m*~-m>>1)

#r = 2 なんだからわざわざcmb使わなくて良かった。。。