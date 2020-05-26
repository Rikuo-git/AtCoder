#my solution
print("AABRCC"[input()[1]=="B"::2])
print("AABRCC"["B" in input()::2])



#solution by fsdshn
print('AARBCC'[input()>'AC'::2])
#文字列の大小はコードポイントの大きさで比較される。A-Za-zの順番

#solution by c_r_5
print('A%sC'%'BR'[id(id)%9%2])

print(*{'ABC','ARC'}-{input()})

#アスタリスクはカッコを外して出力