
values = input().split()
N = int(values[0])
K = int(values[1])

# 長さNの空配列を用意
A=[0]*N
list_values = input().split()

# valuesのi成分をAのi成分に入れる
for i in range(N):
    A[i] = int(list_values[i])

print(A[K-1])

