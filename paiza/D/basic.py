
values = input().split()
N = int(values[0])
K = int(values[1])

# 長さNの空配列を用意
A=[0]*N
list_values = input().split()

# valuesのi成分をAのi成分に入れる
for i in range(N):
    A[i] = int(list_values[i])

print(A[K-1])


list_1 = [[1,2,3,4,5,6],[8,1,3,3,1,8]]
# 要素数をカウントするようにしないといけないのかな
# forループで要素を取り出す
# countを定義して数えるようにする
list_1div= []
# count = 0
# for i in list_1:
#     list_1div = 
# こんなことしなくていい
# 2次元配列を一次元にするには、2重ループを使う
# 行列のi,j成分を一つのlistに追加していくような感じ
for i in range(len(list_1)):
    for j in range(len(list_1[i])):
        # appendで要素を追加
        list_1div.append(list_1[i][j])
        

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# リスト内包表記
flattened = [item for row in matrix for item in row]
# これでいい
print(len(list_1div))   

# 行数と列数を取得すれば良い
# EOFエラーはインプットの情報がない時に表示される

# 2次元配列の要素数を求める
# 行*列で要素数求めれるよね　いちいち　一次元に変換しなくてもいい
li = [[1, 2, 3, 4, 5, 6], [8, 1, 3, 1, 3, 8]]
print(len(li) * len(li[0]))

# 行ごとに取り出す場合
line_2div = [[6,5,4,3,2,1],[3,1,8,8,1,3]]
for i in range(len(line_2div)):
    out_put = line_2div[i]
    # アンパックして出力
    print(*out_put)



#一要素ずつ取り出す場合
line_2div = [[6,5,4,3,2,1],[3,1,8,8,1,3]]
for i in range(len(line_2div)):
    for j in range(len(line_2div[i])):
        out_put = line_2div[i][j]
        print(out_put)
        
        
# 各行の要素数を出力
matrix =[[1],[2, 3],[4 ,5, 6]]


# --- 行列（2次元配列）の標準入力パターン ---

# N行M列のデータを受け取る例
# 入力例:
# 3 4
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12

# 1. 最初の行で行数N、列数Mを取得
# values = input().split()
# N = int(values[0])
# M = int(values[1])

# 2. N回ループして行を受け取る（リスト内包表記）
# matrix = [list(map(int, input().split())) for _ in range(N)]

# print(matrix)


# --- N（行数）のみが与えられるパターン ---
# 列数はデータ依存、または固定（例：5列）の場合
# 入力例:
# 3
# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15

# N = int(input())  # 最初の行で行数Nを取得
# matrix = [list(map(int, input().split())) for _ in range(N)]

# ※もし「列ごと」にデータを持ちたい場合（転置）
# columns = list(zip(*matrix))
# print(columns)
# input()の()を忘れた
N =int(input())
for _ in range(N):
    column = list(map(int,input().split()))
    print(*column)
# もしエラーが起きるのであれば、入力データ数が5個未満の行がある場合だとある




for i in range(len(matrix)):
    print(len(matrix[i]))
    

# 行数Mを取得
M = int(input())
# print(M)
matrix =[]
# valuesの取り方
# ここでMを使ってループしながら取らないといけないと思う
for _ in range(M+1):
    row = list(map(int, input().split())) # 1行読み込んで数字のリストにする
    # 行を出力すれば良かったのでこれでいい
    print(*row)
    matrix.append(row)
    
    
# 先に配列を用意して大きさをいろんなサイズで値を取ってから、内容を出力するようなコードになっている
# 行数を習得
M = int(input())

# 5行M列の2次元配列を用意
A = [[0] * M for _ in range(5)]
# 5行M列のデータを受け取る
for i in range(5):
    values = input().split()
    for j in range(M):
        A[i][j] = int(values[j])

# 2次元配列の内容を出力
for i in range(5):
    for j in range(M):
        # 要素を出力
        print(A[i][j], end="")

        if j < M - 1:
            print(end=" ")
        else:
            print()
