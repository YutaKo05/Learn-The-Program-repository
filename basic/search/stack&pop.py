# D-Take ABC
# 文字列なので
S = input()

# 制約
# 連続した部分列ABCを含む限り、以下の操作を繰り返す。
# 発見したABCの中で一番左の内容が削除される

# スタック用の配列を用意する。
stack = []
# 考え方
# 配列の中にABCがある限り繰り返す。
for char in S:
  stack.append(char)
  
  # 文字列を一個ずつstackしていく
  # もし、長さが3以上かつ後ろから3つ目がABCであったら？？
  if len(stack) >= 3 and stack[-3:] == ['A','B','C']:
    # pop()は配列の要素を取り出すという意味なので
    # 後ろ3つ（ABC）を削除すると言うこと
    # スタックのルール上後ろから取り出す
    # Cを消す
    stack.pop()
    # Bを消す
    stack.pop()
    # Aを消す
    stack.pop()
    
# 空白なしでprint
print("".join(stack))

