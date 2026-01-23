# 挿入ソートの実装


def insertion_sort(A,N):
    # 思考
    # 数列Aを昇順に並べ替える挿入ソート
    
    
    # 1からn-1までループ
    for i in range(1, N):
        key = A[i]
        # ソート済み部分の最後のインデックス
        j = i - 1
        
        # keyより大きい要素を右にシフト
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            # 挿入する場所を探しために、配列を右から左へスキャンしているから
            # 1個減らして、1個前の要素をみる
            j -= 1
        
        # keyを正しい位置に挿入
        A[j + 1] = key
    print(A)
    
    return A

# 実行
if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    
    sorted_A = insertion_sort(A, N)
    print(" ".join(map(str, sorted_A)))