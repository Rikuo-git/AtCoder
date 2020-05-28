# my solution
s, w = map(int, input().split())
print("un" * (s <= w) + "safe")

# shortest by c_r_5
print('un'*eval(input().replace(' ','<='))+'safe')