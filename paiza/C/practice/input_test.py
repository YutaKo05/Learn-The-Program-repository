# 自分の得意な言語で
# Let's チャレンジ！！
n = int(input())
# print(n)
# barth_day_list=[]
# for barth_day_list in range(n):
#     print(barth_day_list)
for i in range(n):
    # ここは自力でできた。
    user_info = input().split(" ")
    # ２つとも定義しちゃうのが大事
    # かつ別々で
    name = user_info[0]
    age = int(user_info[1])
    new_age = age+1
    print(name, new_age)
