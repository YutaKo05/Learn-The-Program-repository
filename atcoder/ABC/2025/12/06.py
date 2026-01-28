# A
N = int(input())

# 1以上N以下の整数を全て足し合わせた値を出力する
# print(N)
ans = 0

for i in range(1,N+1):
  ans += i
print(ans)


# B
# 標準入力
N = int(input())
A = list(map(int,input().split()))

# 条件
# 1<l<r<Nを満たす整数の組（l,r）があるらしい
# l<i<rを満たす任意の整数iについて、Aの列の約数じゃない？？
# 出力例から何すれば良いかみる
# (l,r)の値が少しずつ変わるこれが何組満たすのかを出力する
# 回答を入れる用の箱
ans = 0

# やらないといけないこと
# 配列の総和を計算する
# lとrの値がAの列のインデックスに該当する
# 配列全てで探索
for l in range(N):
  # lとrについての探索
  for r in range(l,N):
    # lとrのサイズで配列の総和を取りたい
    #これがむずい（配列スライスでとってくる） 
    l2r_arry = A[l : r + 1]
    current_sum = sum(l2r_arry)
    
    # 条件を判定しないといけない
    # フラグ管理
    is_ok = True
    # print(current_sum)
    for x in l2r_arry:
      # 約数かどうかの判定
      if current_sum % x == 0:
          is_ok = False
          break
    
    # インデントミス
    if is_ok:
      ans += 1
print(ans)

# 反省
# 配列スライス２重ループでl,rを変更しながらその値を入れていく愚直なやり方がある。
# 約数判定のやり方はわかっていた。
# フラグ管理で判定するは、よく使いそうなので、他の実装でも使えるようにしときたい。
# あと今日は普通にES書くとかで忙しかったので、あまり集中できなかったし、疲れてた。
# 絶対もっと高速にできるはず

# 高速にやる方法



# C
