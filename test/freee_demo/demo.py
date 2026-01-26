# 1-1

# 制約
# 文字列を抜き出して何個freeeっていう文字列ができるか確認する問題

S = input()
# print(S)

# 解法
# それぞれの文字列をカウントしていけばええのでは？
f_count = 0
r_count = 0
e_count = 0

# fの数とrの数とeの数さえ分かれば何個いけるかわかるのでは？
# in raneg(len(S)):は間違っている
# あくまでも文字列Sの中身にアクセスするにはfor char in S:で良い
# S[i]みたいな感じでやる場合は、for i in range(len(S)):で良い
# Sの中身を1文字ずつスキャンしていく
for char in S:
  if char == "f":
    f_count += 1
  if char == "r":
    r_count += 1
  if char == "e":
    e_count += 1

# さらに簡単に書く場合は、以下の通りに書くことで対応できる。
f_count = S.count('f')
r_count = S.count('r')
e_count = S.count('e')


# print(f_count)
# print(r_count)
# print(e_count)
# 最小値でいけばOK
freee_count = min(f_count,r_count,e_count/3)

# 1つのfreeeって言葉を作るのに必要な最小条件
# fの数、rの数
# e/3で切り捨て
print(freee_count)


# 1-2
# 1の条件＋元の順番を保ったまま抜き出す問題

S = input()


