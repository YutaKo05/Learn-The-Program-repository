num_problems = int(input())

for _ in range(num_problems):
    s = input()
    t = input()
    if sorted(s) == sorted(t):
        print("Yes")
    else:
        print("No")      


#　ソートが思いつかなかった。
# 一文字ずつ比較しようとしていた（その場合は、計算コストかなりもったいない）