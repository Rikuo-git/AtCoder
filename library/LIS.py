# 最長増加部分文字列を求める。　longest increasing subsequence
from bisect import bisect_left


def lis(li):
    lis_li = [li[0]]
    for i in li:
        if i > lis_li[-1]:
            lis_li.append(i)
        else:
            lis_li[bisect_left(lis_li, i)] = i
    return lis_li
