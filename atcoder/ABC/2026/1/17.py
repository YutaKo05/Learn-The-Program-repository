# A
# 方針
# とりあえず四変数を受け取ろう
P,Q = map(int,input().split())
X,Y = map(int,input().split())

#TODO
# (i,j)をマスとして考える
# マス目のうち、マス (P,Q) を一番左上のマスとした 
# 100×100 マスの領域のみが黒く塗られており、それ以外のマスは白く塗られています。

# (X,Y) が黒く塗られているならば Yes を、そうでないならば No を出力せよ。
# 分解すると
# マス目の判断
# PQの要素の中にX,Yが含まれていたらYES、含まれていないのであればNOを返すようにすればいい
#　行列を用意する必要はない
# 黒い領域を数値化すればいい
# X P+99
# Y Q+99
# つまりXがP以上で、P＋100未満か
if P <= X <=P+99 and Q <=Y<=Q+99:
  print("Yes")
else:
  print("No")



# B
# とりあえず入力を受け取る
N,M = map(int,input().split())
S = input()
T = input()
Q = int(input())
w =[] 

# print(N)
# print(M)
# print(S)
# print(T)
# print(Q)

for i in range(Q):
  value = input()
  w.append(value)
  # print(val)

# 標準入力は受け取れた。
# OUTPUT
# Q行出力
# 出力時に高橋語、か青木語か判断すべし

# 判断条件
# 高橋：長さ N の文字列 S
# 青木：長さ M の文字列 T 

# 判断方法
# 受け取った文字列の中に、文字列Sであれば、高橋。Tだったら青木
# 判断できない（両方ある、ないなど）は不明にすれば良い
# in で判断すれば良さそう

# SとTの集合を作る
# これ思いつかない
set_S = set(S)
set_T = set(T)
# print(set_S)
# print(set_T)

# さっき定義したwから値を読み出す
for value in w:
  # 与えられたvalueの文字列がそれぞれの集合に含まれているか確認
  # all関数とin関数を組み合わせる
  # それぞれの文字がset_S,set_Tに含まれているか確認   
  # それをforで全部に対して回す

  is_takahashi =all(c in set_S for c in value)
  is_aoki =all(c in set_T for c in value)

  # 条件分岐
  if is_takahashi and not is_aoki:
    print("Takahashi")
  elif is_aoki and not is_takahashi:
    print("Aoki")
  else:
    print("Unknown")


# C
# 入力を受け取る
N,K,X = map(int,input().split())
A = list(map(int, input().split()))

# 杯数を考える上で、大きい順にソートしといた方がいい
A.sort(reverse=True)
# カップにA_iml入っているらしい
# K個のカップは日本酒、それ以外は水
# 判別つかない

# 問Xml以上の日本酒を飲みには、最低なんカップ飲めばいいかだって

# カップ数 N個
# 日本酒　K個
# 水　N-K個
# Xml飲むか

# 回答最低何個飲めばXに到達するか
# 最大10^9の総当たり

# 考えヒント
# 飲む杯数は絶対水の個数より上じゃないとおかしい

# そもそも小さい順に全ての日本酒を飲んでも到達不可能であれば早期リターン
if sum(A[N-K:]) < X:
  # 早期リターンのため 先にダメなやつを試行する
  # ヒントぽいやつ
  # 飲む杯数は絶対水の個数より上じゃないとおかしい
  print(-1)
else:
  # 酒の定義
  sake_sum=0
  # 最低でもN-K杯は飲まないといけない
  # N-K＝水
  for m in range(N-K,N):
    sake_sum +=A[m]
    # 終了条件
    if sake_sum >=X:
      print(m+1)
      break
  # どんどん足しってて何杯目になるかを出力すればいい（それが最低飲まないといけない杯数となるから）



# 反省
# pythonのライブラリの使い方が完璧ではない
# setの使い方を覚えた
# all関数の使い方を覚えた
# 数学的な考え方がまだまだ甘い
# 基礎的な標準入力の受け取り方はほぼできるようになったので、これから確認しないで、メインロジックを素早く書くようにしたい。

