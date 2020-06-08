# my solution
_,d,x,*a=map(int, open(0).read().split())
print(sum(~-d//i+1 for i in a)+x)

# shortest KouCuriosity
_,d,x,*l=map(int,open(0).read().split());print(x-sum(-d//a for a in l))
