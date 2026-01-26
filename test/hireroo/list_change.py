def solution(nums, n):
    # TODO: Implement me!
    # x_1〜x_n,
    # 配列の長さの半分なのがn

    # このとき
    # x_1,y_1,x_2,y_2...x_n,y_nみたいに並べ替えしてねだそうです。

    #ロジック
    # nがポイント　
    # n以降の要素がy成分に当たるので配列スライス表示でいい感じに撮ってこれないかな
    # n番目がxの要素
    x = nums[:n]
    y = nums[n:]
    # 答え用の配列
    ans=[]
    # これを交互に入れるにはどうする？？
    # forループでお互いの先頭の要素をx,yの順番でいれればいい
    for i in range(n):
        ans.append(x[i])
        ans.append(y[i])
    return ans