n = int(input())
i=0
# インクリメントと、今何回ループしているのかを管理しないといけない
# 忘れていた
while i < n:
  A,B=map(int,input().split())
  print(A+B)
  i+=1