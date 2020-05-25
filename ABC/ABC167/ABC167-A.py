#my solution
#open より input の方が速そう
s, t = open(0).read().split()
print("Yes" if t[:-1] == s else "No")

#shortest by maji_ji
#sliceにおいてtrue or false は　1 or 0　と同じ働きのようだ
print("YNeos"[input()!=input()[:-1]::2])