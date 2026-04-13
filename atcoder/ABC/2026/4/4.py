# ABC-2026-4

# A
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

