# A
N = int(input())
# 長さがN未満の文字列S
S = input()

S_list = S

# 求めるもの
# 長さがSになるまで先頭にoを追加していってください
S_len =len(S)

if N > S_len:
  # 配列の結合
  S = 'o' * (N - S_len) + S

print(S)


# B


# これ、2次元配列の空配列を作る方法
N = int(input())
matrix = [[0 for _ in range(N)] for _ in range(N)]




# 出力はマス上で出す
# N-1のi,j成分を出す。

# 計算ロジック
# (9,N-1/2)
# N^2-1回繰り返す
# 前回

# 必要なこと
# Ai,jのからの配列を用意する必要があるのでは？
# NNの容器を用意

# 思考
# 繰り返す処理
# 前回の内容を取得
# [0][(N-1/2)]、書き込んだ整数kを求めないとだめ
# 条件式
# 次書き込むところ（(r-1) mod N、（C+1) mod N）のインデックスが==0であれば書き込む
# x mod N はxをNで割ったあまりなのでx%Nでいいかな？

N = int(input())
matrix = [[0]*N for _ in range(N)]
# print(matrix)

# r,cは外であらかじめ定義すべし
# これは初期値！！
r,c = 0,(N-1) // 2
# 一番初めの書き込みを忘れてる
matrix[r][c] = 1

# 1回目は外で定義している
# N^2−１回繰り返さないといけない
for k in range(1,N**2):
  # 嫌いなやつ
  # 次の計算すべき箇所
  next_r = (r-1)%N
  next_c = (c+1)%N
  
  # 条件式
  if matrix[next_r][next_c] == 0:
    # そのまま値更新するよ！！
    r,c =next_r,next_c
    
  else:
    # インデックスは個別に変化せて更新すべし
    r,c = (r+1)%N ,c
  
  # ifの外で加算
  # kは一番はじめに1を書き込むから
  matrix[r][c] = k+1

# 出力内容
# 各マスに書き込まれる整数を求めてください
for row in matrix:
  print(*row)

# 反省
# B問は、本当に仕様をそのまま実装できるかどうかを問われる問題なのだなろ感じた。