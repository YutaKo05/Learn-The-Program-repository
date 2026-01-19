# 多次元配列とか行列とかの取り方

# 2次元配列の要素の取り方



N, M = list(map(int, input().split()))
a = []
for i in range(N):
    a.append(list(map(int, input().split())))


N, M = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(M)]

# ここにコードを追記する
# print(N)
# print(M)
# print(AB)

# ゲーム大会だそうです
# Nは人数
# Mはこれまでの試合数


# 出力
# 総当たり対戦対戦の対戦表を出力する
# ルール
# 参加者A_iがB_iに必ず勝つようになっている
# そのため、その勝敗管理を行えばOK

# 3 2
# 1 2
# 3 1

# この場合は
# ２回試合している　3人参加
# 勝者は、1番目と3番目の人

# 方針
# 結果の2次元配列を用意する必要あり
# ２重ループで座標を取得する
# ABの値をijで取得し、該当する部分に勝敗を書き込む

# 人数分の行列がいい
result = [["-"] * N for _ in range(N)]

# print(*result)

for a, b in AB:
  # インデックスの関係で1個値を減らす
  a -= 1
  b -= 1
  # 対応する箇所を適応
  result[a][b] = "o"
  result[b][a] = "x"
  # print(result)
  
# これは何？
# 出力用の形式に合うように出力するため
# rowという出力用の入れ物を用意し行ごとに中身を出力
for row in result:
  print(" ".join(row))



# 反省
# 考え方が大事
# 対戦表を用意すること
# 対戦結果を反映させること
# 対戦表を上書きしていけば完成



