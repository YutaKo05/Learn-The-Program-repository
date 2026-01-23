def bubble_sort(A, N):
    #　配列の各要素分だけループする
    for i in range(N):
        # 隣接要素を比較するために、N-i-1までループする
        for j in range(0, N-i-1):
            # バブルソートは隣接要素を比較して入れ替える作業である
            if A[j] > A[j+1]:
                # ほら入れ替えているでしょ
                A[j], A[j+1] = A[j+1], A[j]
    return A


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    
    sorted_A = bubble_sort(A, N)
    print(" ".join(map(str, sorted_A)))
