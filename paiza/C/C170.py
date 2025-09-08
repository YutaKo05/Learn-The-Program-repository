
# お会計の回数を表す整数 N 
# 目標ポイントを表す整数 M 
# n,target = map(input().split())
n, target = map(int, input().split())
# print(n)
# print(target)
# 2 行目に i (1 ≦ i ≦ N) 回目のお会計の金額 t_i が半角スペース区切りで与えられます。
input_2=input()
# input_2の内容を割る100してポイントを累計すべし
# その後、目標ポイントまで何ポイント必要か引き算でだして、100倍すれば答えが出る
# targetを出力としよう

nums=input_2.split()
# print(nums)
# 数字にしないといけないらいしい
nums=[int(n) for n in input_2.split()]
total = sum(n//100 for n in nums)

# ans=(target-total)*100
# これだとマイナスになってしまうので、max関数を使用して既に目標を達成している場合は、0を表示すべき
remain = max(0, target - total)*100
print(remain)