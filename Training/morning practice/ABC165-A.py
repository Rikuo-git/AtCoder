# my solution
k, a, b = map(int, open(0).read().split())
print("NOGK"[a // k < b // k or a // k == a / k::2])

# shortest by dorapon2000
k, a, b = map(int, open(0).read().split());
print('ONKG'[b < b % k + a::2])

"""
a = pK + q` (1<q`<=q)
b = pK + q (q<K)
のとき不成立
すなわち
pK < a 
b - q < a
b < q +a 
よって
b < b%k + a  
"""
