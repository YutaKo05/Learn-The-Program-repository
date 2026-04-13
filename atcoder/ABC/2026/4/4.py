# ABC-2026-4

# A - Gothec
M,D = map(int,input().split())
# print(M)
# print(D)
# 要件
# 五節句が含まれていたらYes、そうでなければNo


# 1-7
# 3-3
# 5-5
# 9-9
# 
# 考え方は合ってた
# dictじゃなくてタプルのリストで
# check_goseku = {M==1:D==7,M==3:D==3,M==5:D==5,M==7:D==7,M==9:D==9}
check_goseku = [(1,7),(3,3),(5,5),(7,7),(9,9)]


if (M , D) in check_goseku:
  print("Yes")
else:
  print("No")

# B - Draw Frame 
H,W = map(int,input().split())

# 1行目と最終行は全て#、それ以外は最初と最後が#でそれ以外は.を出力する
for i in range(H):
    for j in range(W):
        if i == 0 or i == H-1 or j == 0 or j == W-1:
            print('#', end='')
        else:
            print('.', end='')
    # 改行を入れる場所が間違ってた
    print('')


# 考え方はあってた、しかし、相変わらず細かい出力の書き方とかが間違っていたりend=''とかって覚えてない
# 1行目と最終行は全て#、それ以外は最初と最後が#でそれ以外は.を出力する
# これは自力で思いつけた
# まだまだ力不足
# 面白かったが

# C - Fishbones

