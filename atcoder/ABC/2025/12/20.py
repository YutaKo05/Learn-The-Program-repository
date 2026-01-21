# A
A,B = map(int,input().split())
# １フィートは12インチです
# AフィートBインチは何インチですか？

ans = A*12 +B
print(ans)

# 反省
# クソ簡単


# B
H,W,N = map(int,input().split())
# H行、W列の行列を取る
# 行列取るやつ（厳密にいうと行ごとに）
# 制約を見たら全探索しても問題ないオーダーみた
# 答えの入れ物
isfind = 0
ans = []
# 叫んだ内容を配列で保存
B = []
matrix_A = [list(map(int, input().split())) for _ in range(H)]
# print(matrix_A)

# for _ in range(N):
#   # Bの内容をリストで取得する
#   input_B= int(input())
#   B.append(input_B)

# もっと簡素にかける
B = []
for _ in range(N):
    B.append(int(input()))
# print(B)


# 条件とか
# Bの整数は、叫んだ回数、整数
# 考え方
# 各行に、行列の内容に含まれているかカウントすればいいと思う。
# ロジック分解
# 行を取得し、行の中に数字が含まれているかスキャンすればいい
# ＝＝で


# # 各行ごとにスキャン開始
# for i in range(H):
#   isfind = 0
#   # W行あるので、その回数分ループを回せば良い
#   # i行目を取り出して、Bの配列Bの要素があるかスキャン
#   # スキャンして、あったらcountに保存して、ansの配列に入れる
#   # その後、max(ans)で回答を出力すればいいのでは？
#   for j in range(W):
#     # この条件式だと行列全部入っているかみたいな話になっている
#     if matrix_A[i] in B:
#       # 発見回数をインクリメント
#       isfind +=1
#     ans.append(isfind)
#   print(max(ans))

# 行ごと取り出す
for row in matrix_A:
  isfind = 0
  # 行の要素を一個ずつ取り出す
  for x in row:
    if x in B:
      isfind += 1
  ans.append(isfind)

print(max(ans))

# 反省
# ほぼ自力でロジック分解はできた。
# Bの配列を用意することやforで行ごと回して、インクリメントして、それを配列に入れて、最大値をprintすればいいやんってことも自力で気づけた
# しかし、行の中の要素を一個ずつ取り出す部分が抜けていた
# あと、文法力がまだ低いので、自分の思っていることをコードに落とし込みきれなくてもどかしいなという気分です
# 悔しい

# C
# 眺めても、わかりませんでした、
# あとでやります。