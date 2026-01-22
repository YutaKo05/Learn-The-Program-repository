import sys

def main(lines):

    # 例
    # efed→edef
    # 1と３
    # 2と４を入れ替えている
    # 各文字ごとスキャンする必要
    # ２文字ごとに入れ替え

    # 出力すべきこと
    #　ソート結果を1行で出力すべし
    
    target =lines[0]
    chars = list(target)
    n = len(chars)

    #　配列を奇数ごと、偶数ごとに取り出してソートすればいいかも
    even = list(chars[::2])
    odd = list(chars[1::2])

    even.sort()
    odd.sort()

    # 答え用の空配列
    ans = [0] * n
    ans[0::2] = even
    ans[1::2] = odd

    # print(*ans) これじゃだめ
    print("".join(ans))


    # このやり方だと実行時間がかかりすぎて後半のケースを突破できない
    # forループだと無理みたいなので、配列操作すればいいのでは？
    # for i in range(n):
    #     for j in range(0,n-2):
    #         # 条件
    #         if chars[j] >chars[j+2]:
    #             chars[j],chars[j+2] = chars[j+2],chars[j]
    
    # print("".join(chars))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
    

# バブルソートの似たような問題
# バブルソートは隣り合うものをソートしているが、これは、2つ飛ばしでソートしている
# なので、奇数番目と偶数番目で分けてソート　これを自力で考えられたのはよかった。
# 配列のスライスが何も知らない状態だと書けないので、これの対策もしないと行けないことがわかった。

# コーディングテストの特徴はわかってきたかもしれない
# ただ、まだまだ、素の力が足りてないので、解けない。。。
# freeeも厳しそうな気がする。。。