n = 4
a= [1,2,4,7]
k = 13
def bubun(i,sum):
    if i ==n:return sum == k
    if bubun(i+1,sum):return True
    if bubun(i+1,sum+a[i]):return True
    return False
print(bubun(0,0))


for bit in range(1 << n):
    sum = 0

    for i in range(n):
        # bit に i 番目のフラグが立っているかどうか
        if bit & (1 << i):
            # フラグが立っているならば sum に加算する
            sum += a[i]

    if sum == k:
        print("Yes")
        exit()

print("No")