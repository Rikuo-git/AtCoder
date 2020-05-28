# my solution
print(sum(divmod(eval(input().replace(" ", "*")), 2))) # h,w が1の時がだめ

# AC ver
h,w=map(int,input().split())
print([1,sum(divmod(h*w, 2))][h>1<w])


# shortest by c_r_5
h,w=map(int,input().split())
print([1,h*w+1>>1][h>1<w])

# h*w+1>>1 いいですね。。。　2n + 1 or 2n の時も　a >> 1 でいいしな
