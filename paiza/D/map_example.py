# --- map関数の動作解説 ---
# map(関数, リストなどのデータ) は、データの全ての要素にその関数を適用します。

# 例1: 文字列のリストを数値に変換する（競技プログラミングで頻出）
str_numbers = ["1", "2", "3"]
# int("1"), int("2"), int("3") をそれぞれ実行してくれるイメージです
int_numbers = list(map(int, str_numbers)) 
print(f"例1: {int_numbers}") # 出力: [1, 2, 3]

# mapを使わないとこう書く必要があります（面倒臭い）
# int_numbers = []
# for s in str_numbers:
#     int_numbers.append(int(s))


# 例2: 自分で作った関数を適用する
def double(x):
    return x * 2

nums = [10, 20, 30]
# numsの各要素を double 関数に渡した結果のリストを作る
doubled_nums = list(map(double, nums))
print(f"例2: {doubled_nums}") # 出力: [20, 40, 60]


# 例3: lambda（無名関数）を使って1行で書く
# リストの各要素を2乗する
squared = list(map(lambda x: x**2, [1, 2, 3, 4, 5]))
print(f"例3: {squared}") # 出力: [1, 4, 9, 16, 25]


# 注意点:
# map() の戻り値は「mapオブジェクト」という特殊なデータです。
# 中身を確認したり、インデックスでアクセスしたりしたい場合は list() で変換します。
raw_map = map(int, ["10", "20"])
print(f"mapのまま: {type(raw_map)}") # <class 'map'>
print(f"listに変換: {list(raw_map)}") # [10, 20]
