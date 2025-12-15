# 計算の回数がN
N = int(input())
# 最初の値がA
A = int(input())
# ここにプログラムを追記
# forループでそれぞれの計算ステップをとってこないといけない
# N回まで取得する必要あり
# 答えを入れる変数が必要
# ここで初期値先に入れとけばよくね？？
total=A
for i in range(N):
  # 演算子を取り出す必要がある
  # op,BでとってきてそのうちのAは演算子、Bはその演算子を行う動作として使用する
    #ここmapで撮る必要がない
    # map関数は   
  op,B = input().split()
  B=int(B)
  
  if op == "+":
    total+=B
  elif op == "-":
    total-=B
  elif op == "*":
    total*=B
  elif op == "/" and B!=0:
    total//=B
  else:
    print("error")
    break
  
  # 答えの出力の仕方はこれ
  print(i + 1, total)