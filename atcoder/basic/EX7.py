a = True # True または False
b = False # True または False
c = True # True または False

# ここから先は変更しないこと

assert (a is True) or (a is False)
assert (b is True) or (b is False)
assert (c is True) or (c is False)

# aの存在確認
if a:
    print("At", end="")
else:
    print("Yo", end="")

# bの存在確認　存在しちゃだめです
if not a and b:
    print("Bo", end="")
else:
    print("Co", end="")

# cの存在確認　存在していいです
if a and b and c:
    print("foo!", end="")
elif True and False:
    print("year!", end="")
elif not a or c:
    print("der", end="")

print("")
