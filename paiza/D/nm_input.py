# 入力例
# 3 4
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12

# 1行目でN(行数)とM(列数)を受け取る
# values = input().split()
# N = int(values[0])
# M = int(values[1])
# もっとPythonらしく書くなら:
N, M = map(int, input().split())

# N行分のデータを受け取る
# リスト内包表記を使うのが一番簡単
matrix = [list(map(int, input().split())) for _ in range(N)]

# 確認用出力
for row in matrix:
    print(*row)


# これで提出した
N,M = map(int,input().split())
# print(N)
# print(M)

# matrix = [list(map(int,input().split())) for _ in range(N)]
# matrix = [list(map(int, input().split())) for _ in range(N)]
# print(*matrix)
for _ in range(N):
    row = list(map(int,input().split()))
    print(*row)