# Копирование массива
N = int(input())
A = [0]*N
B = [0]*N
for k in range(N):
    A[k] = int(input())
for k in range(N):
    B[k] = A[k]
# C = A - нельзя, нужно поэлементное копирование
# A[0] = 777
# Будет C[0] тоже 777