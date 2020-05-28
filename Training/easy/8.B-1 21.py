# my solution
n = int(input().replace(" ", ""))
print("YNeos"[int(n ** 0.5) ** 2 != n::2])

# shortest by Ruki
print("YNeos"[int(input().replace(" ", "")) ** .5 % 1 > 0::2])
# これがやりたかった…
