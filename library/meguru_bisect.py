def is_ok(arg):

    return


def bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

'''
初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
まずis_okを定義すべし
ng ok は  とり得る最小の値-1 とり得る最大の値+1
最大最小が逆の場合はよしなにひっくり返す
'''
