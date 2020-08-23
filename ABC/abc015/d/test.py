import numpy as np


def solve(stdin):
    w, n, k = stdin[:3]
    s = stdin[3:].reshape([n, 2])
    dp = np.zeros((k + 1, w + 1), np.int64)
    for a, b in s:
        for i in range(k):
            dp[i][a:] = np.maximum(dp[i][a:], dp[i + 1][:-a] + b)
    return dp[0][w]


def main():
    stdin = np.fromstring(open(0).read(), dtype=np.int64, sep=" ")
    print(solve(stdin))


def cc_export():
    from numba.pycc import CC

    cc = CC("my_module")
    cc.export("solve", "(i8[:],)")(solve)
    cc.compile()


if __name__ == "__main__":
    import sys

    if sys.argv[-1] == "ONLINE_JUDGE":
        cc_export()
        exit(0)
    #from my_module import solve

    main()
