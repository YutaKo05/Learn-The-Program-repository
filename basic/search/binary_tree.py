# Atcoder C Snuke Festival

# ２分木使わないでゴリ押しする場合
# 計算量O(N^3)
# 今回与えられている量では無理
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C= list(map(int,input().split()))

# 標準入力OK
# 問題のロジックを考える
# uper midle lowerの3つのパーツが必要
# それぞれのパーツがN個ある
# i個目

# 制約
# midleのサイズはuperより大きく,lowerはmidleより大きくないといけない
# 大小関係
# uper < midle < lower
# 多分これが条件式になる
# これを満たす任意の3つのピースで祭壇を作ることができる

# 出力
# 作ることができる祭壇の種類数


# 最低限3つの組み合わせを求めるだけだから順番はあんまり関係ないので、ソートしていいかな
A.sort()
B.sort()
C.sort()
count = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            if A[i] < B[j] < C[k]: # 値を比較
                count += 1

print(count)



# 2分木を使う方法
# これだと計算量がO(N^2 log N)になる
import bisect
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C= list(map(int,input().split()))   
A.sort()
C.sort()
count = 0
for b in B:
    # Aの中でbより小さい数の個数
    a_count = bisect.bisect_left(A,b)
    # Cの中でbより大きい数の個数
    # Nで引くのは、右端のインデックスを求めているから
    c_count = N - bisect.bisect_right(C,b)
    count += a_count * c_count
print(count)