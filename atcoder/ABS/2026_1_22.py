# atcoder Beginner Selection
# https://atcoder.jp/contests/abs

# 基礎（標準入力）
a = int(input())
b,c = map(int,input().split())
# 文字列
s = input()
ans = a+b+c
print(f"{ans} {s}")


# 偶奇判定
a,b = map(int,input().split())
ans =a*b
# 偶奇判定は2で割れるかで考える
if ans % 2 == 0:
  print("Even")
else:
  print("Odd")
  

# 文字列の中の特定の文字の数を数える
s = input()
# print(s)
# print(s[0])
# print(s[1])
# print(s[2])
count = 0

# ビー玉をマス
# sの文字列をスキャンして1の回数をインクリメントすればいいんじゃね？
for i in range(len(s)):
  if s[i] in "1":
    count +=1

print(count)


# Shift only 
N =int(input())
A = list(map(int,input().split()))

count = 0
# print(N)
# print(A)

# 全て偶数だと配列の中身を全て2で割ったものに置き換える
# forループで各要素ごとやる
# 条件式で割れるかどうかチェックする
# 全ての配列
# 出力するものは、最大何回操作を行うか＝操作回数の配列を用意して最大値を出力すればいい？

# 配列の全要素分ループを回す。
# 終了条件がむずいな
# 条件は、リストAの要素が全て偶数である間
while True:
  # 全て偶数かどうかのフラグ
  all_even = True
  for i in range(N):
    # Aの各要素が偶数かそうではないかを判定する
    # A_Nまで割れることを確認できたら
    if A[i] % 2 != 0:
      # 全部2で割れたら配列の中身をすべて2で割る
      all_even = False
      break

  if all_even:
    # すべて偶数なら、実際に2で割ってAを更新する
    A = [x // 2 for x in A]
    count += 1 
  else:
    # 奇数があればループを抜ける
    break
    
print(count)

# 反省
# whileのフラグが思いつかなかった。
# しかし、考え方の方向性はほとんどあっていた、ただ、自分の考えをまだ、100％文法に落とし込めてない

# より高速に行う
N =int(input())
A = list(map(int,input().split()))

# すべての数字が割れなくなるまで続ける = 一番早く奇数になってしまう数字に合わせる
# ボトルネックを探すという考え方もある
ans_list =[]

for x in A:
  divide_count = 0
  while x % 2 ==0:
    #2で割る
    x//=2
    divide_count +=1
  ans_list.append(divide_count)
  
# 全体の最小値がボトルネックとなり、答えとなる
print(min(ans_list))

# ABC087B - Coins
# ちょうどの支払いって問題と同じpaizaの
# 500円
A =int(input())
# 100円
B =int(input())
# 50円
C =int(input())
# 金額
X =int(input())


# それぞれの試行における枚数を渡すための入れ物
# 総当たりで合計に一致するのは何通りかこれがこの問題の鍵である。
# 何通りあるのかの
ans = 0

# 硬貨を選んで何通りで払えるのかを求める
# 考え方
# Xの大きさでまず比較するのが大事そう
# forを複数書いてやらないと行けない
for i in range(A+1):
  # A枚までインクリメント
  for j in range(B+1):
    # B枚までインクリメント
    for k in range(C+1):
      # C枚までインクリメント
      # 合計の保存
      total = 500*i + 100*j + 50*k 
      # print(total)
      if X == total:
        ans +=1

print(ans)

# 反省
# forのijkをそのまま入れればいいだけ
# 全ての組み合わせを試すという発想はできた
# 無駄にインクリメントしようとせず、そのまま書けばよかったと
# 惜しい

# ABC083B - Some Sums 
def findSumOfDigits(n):
  sum = 0
  while n > 0:
    # nを10で割った余りをsumに足し続ける→10進法だから
    sum += n % 10
    # 次の桁で試行する
    # /だと浮動小数点、//はintで返す整数除算
    n //= 10
  return sum

N,A,B = map(int,input().split())

# 10進法での各行の和がA以上、B以下であるものの総和
# Nは整数

# 入れ物
count = 0

# 考え
# 各桁を足し合わせてA、Bの範囲に入っているかどうか判断する必要がある
# Nまでの配列を抜き出せばいいんじゃないかと一瞬思った。

# 機能を分割して考えるのもあり
# 1~Nまでなので、0のインデックスの分をずらす必要あり
for i in range(1,N+1):
  sum = findSumOfDigits(i)
  # print(sum)
  # xには、各行の足し合わせた数字が入っている
  # A以上、B以下を満たせばインクリメント
  if A <= sum and sum <= B:
    # さっき6出たのは、6回動作しただけだから
    # 求めるものは、整数の総和
    count +=i
    # print(count)

print(count)  

# 反省
# for文の開始地点がrange(N)だと違う。インデックス文だけ直す必要がある。
# 各桁を取り出して足し合わせる関数を作成する発想は良かった
# count +=1 じゃなくて、count +=iだよ！！


# 
# N枚
N = int(input())
# カードに書いている数字
a = list(map(int,input().split()))

# print(N)
# print(a)
a_score = 0
b_score = 0

# 1枚ずつ取るって
# 出力
# Alice は Bob より何点多く取るかを出力する

# 考え
# aのリストから奇数をAliceの点数、偶数のBobの点数でリストをとって行けばいいんじゃねと思った
# aのサイズでループを回す。
# 追記
# aのリストをソートすべき
a_rev=sorted(a, reverse=True)
# print(a_rev)

for i in range(len(a_rev)):
  # 条件式
  # 奇数であれば、Alice、偶数であればBobの点に入れる
  if i % 2 == 0:
    a_score += a_rev[i]
    # print(a_score)
  else:
    b_score += a_rev[i]
    # print(b_score)
  
  
# print(a_score)
# print(b_score)
ans = a_score - b_score
print(ans)

# 反省
# 自力実装できた！！
# 気持ち良すぎる！！
# 自力でデバックできてソートすれば解決するということまで考えて実装できた！！


# もっとスマートにやる方法
# 入力の受け取り
N = int(input())
a = list(map(int, input().split()))

# 降順（大きい順）にソート
a.sort(reverse=True)

# スライスを使って合計の差を計算
# a[::2]  -> 0, 2, 4... 番目（Alice）
# a[1::2] -> 1, 3, 5... 番目（Bob）
ans = sum(a[::2]) - sum(a[1::2])

print(ans)




# ABC085B - Kagami Mochi