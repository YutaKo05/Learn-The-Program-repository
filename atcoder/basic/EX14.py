data = [int(c) for c in input().split()]
# dataの中で隣り合う等しい要素が存在するなら"YES"を出力し、そうでなければ"NO"を出力する
# ここにプログラムを追記
# print(data)
# 方針
# for ループで値を取ってきて前の値と同じかどうか判断する
# 答えのフラグ用意
# 理由：これがないと全てを試行した時に判定できないから
ans = False
# data-1なのは、これインデックスの関係
for k in range(len(data)-1):
    if data[k]==data[k+1]:
        ans = True

if ans == True:
  print("YES")
else:
  print("NO")
