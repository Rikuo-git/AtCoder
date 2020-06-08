l = 10
n = 3
x = [2,6,7]
print(max(min(i,l-i)for i in x))
print(max(max(i,l-i)for i in x))