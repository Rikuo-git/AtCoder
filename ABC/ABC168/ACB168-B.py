#my solution

k = int(input())
s = input()
print(s if len(s) <= k else s[:k] +"...")

#shortest by c_r_5
k,s=open(0)
k=int(k)
print(s[:k]+'...'*(len(s)-1>k))

#open メゾっどは行ごとに取得できるみたい　ex [f.split() for f in open(0)]