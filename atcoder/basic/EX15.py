N, S = map(int, input().split()) 

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# リンゴ・パイナップルをそれぞれ1つずつ購入するとき合計S円になるような買い方が何通りあるか
# ここにプログラムを追記
# N個売られている
# i個目のりんご、の値段をA,Bのリストで表示

# ちょうどS円になるように買う時何通りあるか

# 実装方針
# 2重ループで総当たりして足し算する
# 足し算して、＝＝Sになった時にcountをインクリメントすれば良さそう
# 2重ループを実装して、i,jで探していく感じになる。
# 何通りあるのかのカウント
count = 0
for i in range(len(A)):
  for j in range(len(B)):
    tem_value = A[i]+B[j]
    if S == tem_value:
      count += 1

print(count)


# 反省
# 何も見ずに行けた
# 気持ちいね！！
# もっとスマートな実装方法があるはず

# これでもいい
# pythonの内包表記を使う方法
# 1はインクリメントを意味しているのかな？
# あとは、forループで2重ループを回している
# で、if文で条件をつけている
count = sum(1 for a in A for b in B if a + b == S)
print(count)

# Counterを使う方法
# あらかじめ差分を求めて、それに合致するやつを探していくような感じだと思う。
from collections import Counter

# Bの要素がそれぞれ何個あるか数えておく
count_B = Counter(B)

count = 0
for a in A:
    # 合計がSになるために必要な値は target = S - a
    target = S - a
    # その値がBの中にいくつあるかを足す
    count += count_B[target]

print(count)