input_line = input()
input_line_len =len(input_line)
out_object =""

# 文字数＋2個分＋を生成すればいいことがわかったので、ループで生成
for _ in range(input_line_len+2):
    out_object += "+"

print(out_object)
print(f"+{input_line}+")
print(out_object)