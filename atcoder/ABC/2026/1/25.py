# A
S = input()
# 問題ロジック
# ドットの個数を調べてねだです

# 解法
# ドットの集合を定義する

dotts = ["i","j"]

count = 0

for i in S:
  if i in dotts:
    count +=1

print(count)



# B
Q = int(input())

# ロジック
volume = 0
isStop = False


for _ in range(Q):
  A = int(input())
  if A == 1:
    volume +=1
  elif A == 2:
    if volume == 0:
      break
    else:
      volume -= 1
  elif A == 3:
    if isStop == False:
      isStop =True
    else:
      isStop = False
      
  if isStop == False and volume >= 3:
    print("Yes")
  else:
    print("No")


# Q回操作を行う。
# 数字によって動作を変える
# 1 +1
# 2 if volume <= 1 音量１下げ、0だと何もしない
# 3 曲を停止、停止してれば再生

# 最終判定
# 音量が3以上で再生されているかどうか
# if isStop == False and volume <= 3:
#   print("Yes")
# else:
#   print("No")

Q = int(input())

volume = 0
is_playing = False

for _ in range(Q):
    A = int(input())
    
    if A == 1:
        volume += 1
    elif A == 2:
        if volume > 0:
            volume -= 1
    elif A == 3:
        is_playing = not is_playing
    
    if is_playing and volume >= 3:
        print("Yes")
    else:
        print("No")



# C
import math

N,M = map(int,input().split())

# 回答用
ans = []
# 利害関係
rel_counts = [0] * (N + 1)

for _ in range(M):
  A,B = map(int,input().split())
  rel_counts[A] += 1
  rel_counts[B] += 1

# 計算部分
for i in range(1, N+1):
  K = (N-1) -rel_counts[i]
  # (関係者以外の人数）C 3
  ans.append(math.comb(K,3))
  
print(*ans)

# 問とロジック
# N人M個の利害関係
# 同じ行のABの研究は利害関係あり
# しかし、査読には、利害関係のない3人が必要
# AB以外のNから2人引いた人数を3人で埋める組み合わせが必要である。
# 標準入力から関係者集合みたいなのを作る必要がありそう

# 例をみる
# 6人5個関係
# 1の場合　関係者２４３以外なので残りは５６だから3人組作れない
# 2　関係者 13が関係者なので４５６がOK　なので１組
# 3 関係者　１２５なので、3人組つkれない
# 4 １のみなので、2356で作れる3人組なので、4C3で４通り
# ５　
# ６は１０通り12345いけるから

# 何通りかの計算は（関係者以外の人数）C３を計算式に打ち込めば算出できるのでそれをappend
# すればよい


# 反省
# AB自力Cのロジックの核心まで自力でいけた。
# 実装力がちょっと上がった気がするが、まだまだだなと感じた。
# ABC合わせて30分くらいで解けるよういなりたい。
# Cに30分かかってる