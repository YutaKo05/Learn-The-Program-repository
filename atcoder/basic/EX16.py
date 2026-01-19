# リスト内包表記を使うと、リストを簡潔に生成
# [(変数を使った処理) for (変数名) in (変数を動かす範囲)] 

N,K = list(map(int,input().split()))
# この取り方がベストだと思う。
S = list(input().split())

# print(N)
# print(K)
# print(S)

ans = []
# 出力
# 一要素ずつ取得し、K文字以上の単語を取り出して出力
# ループしていく
# このループの書き方だとSが寄与してなくないか？
for i in range(N):
  # K文字以上か判断する これはOKだと思う
  if len(S[i]) >= K:
    ans.append(S[i])

print(*ans)  

# これがリスト内包表記を使った書き方
ans = [word for word in S if len(word) >= K]

print(*ans)


# 極限のスマート
N, K = map(int, input().split())
S = input().split()

# 内包表記でフィルタリング
ans = [s for s in S if len(s) >= K]

print(*ans)

# 反省
# リスト内包表記をもっと使いこなせるようになりたい
# 何も見ずに通るようになったので、リスト内表記になれるようにすればよい