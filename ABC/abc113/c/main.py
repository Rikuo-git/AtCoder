import sys
from collections import defaultdict

(n, m), *q = [[*map(int, i.split())] for i in sys.stdin]
d = defaultdict(list)
for k, v in q:
    d[k].append(v)
c = defaultdict(dict)
for k, v in d.items():
    for i, j in enumerate(sorted(v)):
        c[k][j] = i + 1
for p, y in q:
    print("{:0>6}{:0>6}".format(p, c[p][y]))
