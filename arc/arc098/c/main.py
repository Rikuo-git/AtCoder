n = int(input())
s = input()
e = s.count("E")
ans = 10**6
for i in s:
    e -= i == "E"
    ans = min(ans, e)
    e += i == "W"
print(ans)
