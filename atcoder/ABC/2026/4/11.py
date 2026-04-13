# A
# 要件
# 連続する0を取り除く


N = int(input())
S = input()

# print(N)
# print(S)

# 先頭に連続するoを取り除く

# 方針
# インデックス0番目から探索
# o出なくなるまでループ
# o出なくなったら、そのindexまでを

ans=S.lstrip("o")
print(ans)


# B
T, X = map(int, input().split())
A = list(map(int, input().split()))

ans = []
before_value = A[0]
ans.append((0, A[0])) 

# 0からスタートじゃなくて初期値を入れておく
for t in range(1, T + 1):
    current = A[t]
    if abs(current - before_value) >= X:
        ans.append((t, current))
        before_value = current

for t, v in ans:
    print(t, v)


# 反省
# 標準入力と基礎的なpythonの書き方を少し忘れてしまった。
# 次回は、コンテスト前に、過去問をちゃんと解いてABまで自力で素早く時、Cに挑戦するような感じでいきたいと感じてる。

