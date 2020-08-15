from collections import Counter
x = lambda : sorted(Counter(input()).values())
print('YNeos'[x()!=x()::2])
