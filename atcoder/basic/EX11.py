S = input()

count = 1

# Sの文字数長さで演算がどのくらい繰り返すかを書く
for i in range(len(S)):
    if S[i] =="+":
        count += 1
    
    if S[i] == "-":
        count -=1
print(count)