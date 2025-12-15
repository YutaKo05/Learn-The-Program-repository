# 平均の分母N人
N = int(input())
# ここにプログラムを追記

# 配列の中身をintにして取り出したいからmap関数を使用
A =list(map(int,input().split()))
# 重要なこと
# それぞれの人の点数が平均点から何点離れているか計算してください。
# Aの中身は、N個ある
# なので、先に平均点を求める必要がある
total=sum(A)
ave=int(total/N)

for i in range(N):
  # リストAの中身を一個ずつ取り出して
  diff =abs(A[i] - ave)
  print(diff)

