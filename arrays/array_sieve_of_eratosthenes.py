# Решето Эратосфена
# True or False
# Число простое или нет
N = 7
A = [True] * N
A[0] = A[1] = False
for k in range(2,N):
    if(A[k]):
        for m in range(k + k,N,k):
            A[m]=False
for k in range(N):
    # Тернарные операторы
    print(k,"-", 'Простое' if A[k] else 'Составное')
