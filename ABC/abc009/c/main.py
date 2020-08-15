n, k = map(int, input().split())
s = [i for i in input()]
t = sorted(s)
ans = ""
for i in range(n):
    for j in range(len(t)):
        if t[j] == s[i]:
            ans += t[j]
            del t[j]
            break
        else:
            nt = t[:j] + t[j + 1:]
            ns = s[i + 1:]
            for p in ns:
                if p in nt:
                    nt.remove(p)
            if len(nt) + sum(p != q
                             for p, q in zip(s[:i + 1], ans + t[j])) <= k:
                ans += t[j]
                del t[j]
                break
print(ans)
