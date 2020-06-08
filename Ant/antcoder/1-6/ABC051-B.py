# my solution
k, s = map(int, input().split())
c = 0
for i in range(k + 1):
    for j in range(k + 1):
        c += 1 * (0 <= s - i - j <= k)
print(c)
# sum(0 <= s - i - j <= k for for i in range(k + 1) for j in range(k + 1))
# 二重ループでぎり。　全探索で3重にしたくなったら2重にする方法を考える。

# shortest by c_r_5
k, s = map(int, input().split())
k += 1
print(sum(k > s - I // k - I % k >= 0 for I in range(k * k)))
# やってることは同じだけど表現の仕方がいい (k+1)**2-1 をk+1 で割った余りと商は確かに

# fastest by DivineJK
K, S = map(int, input().split())
X = (S + 2) * (S + 1)
if S - K - 1 >= 0:
    X -= 3 * (S - K + 1) * (S - K)
if S - 2 * K - 2 >= 0:
    X += 3 * (S - 2 * K) * (S - 2 * K - 1)
print(X // 2)

# まずs個のボールを入れる3つの箱を考えるとボールの入れ方は
# (S + 2-1) * (S + 1)/2通り
# 次にs>=k+1の時、k+1個以上入っている箱がある場合のボールの入れ方は
# 3 * (S - (K + 1) +2-1) * (S - (K +1) +1)/2通り
# 次にs>=2-1*k+2の時、k+1個以上入っている箱が2つ以上ある組は上の式で二重にカウントされている。そこでそのくみの数は
# 3 * (S - (2-1 * K+2-1) +2-1) * (S - (2-1 * K+2-1) + 1)
