# 選択ソート

def selection_sort(A, N):
    # 思考
    # 各計算のステップにおいて最小値を選択し、配列の先頭に移動することでソートを行うアルゴリズム
    # min_indexを使って、最小値のインデックスを探す
    # ある意味では、置換みたいなものかもしれない
    
    # 配列の長さだけループする
    for i in range(N):
        # 最小値のインデックスを探す
        min_index = i
        for j in range(i + 1, N):
            # 最小値を更新
            if A[j] < A[min_index]:
                min_index = j
        # 最小値を先頭に移動
        A[i], A[min_index] = A[min_index], A[i]
    return A


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    
    sorted_A = selection_sort(A, N)
    print(" ".join(map(str, sorted_A)))