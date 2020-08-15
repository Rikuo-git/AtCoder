#!/usr/bin/env python3
import copy
n, *masu = [i.split() for i in open(0)]
h, w, k = map(int, n)
c = 0
masu = [list(*i) for i in masu]
for i in range(2**h):
    hi = []
    for j in range(h):
        if i>>j &1:
            hi.append(j)
    for p in range(2**w):
        wi = []
        for q in range(w):
            if p>>q &1:
                wi.append(q)
        d = copy.deepcopy(masu)
        for r in hi:
            d[r] = ["."] * w

        for r in wi:
            for o in range(h):
                d[o][r] = "."
        if k == sum(s == "#" for s in sum(d, [])):
            c += 1
print(c)

# これでよかった 焦りすぎ
H,W,K=map(int,input().split())
S=[input() for i in range(H)]
P=0
Q=0
for i in range(1<<H):
  for j in range(1<<W):
    Q=0
    for k in range(H):
      for l in range(W):
        if S[k][l]=='#' and i&(1<<k)!=0 and j&(1<<l)!=0:
          Q+=1
    if Q==K:
      P+=1
print(P)
