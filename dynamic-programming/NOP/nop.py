def dp_nop(a: list, b: list):
    """ на входи принимается два списка
    на выходе возвращается список D с 
    матрицей подпоследовательностей
    """
    n, m = len(a), len(b)

    D = []
    for i in range(n+1):
        D.append([0]*(m+1))

    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                D[i][j] = D[i-1][j-1] + 1
            else:
                D[i][j] = max(D[i-1][j], D[i][j-1])
    return D


def dp_nop_recursive(D: list, A: list, B: list):
    n, m = len(A), len(B)
    i = n
    j = m
    ans = []
    ans_a = []
    ans_b = []
    while i > 0 and j > 0:
        if A[i-1] == B[j-1]:
            ans.append(A[i-1])
            ans_a.append(i)
            ans_b.append(j)
            i -= 1
            j -= 1
        elif D[i][j-1] == D[i][j]:
            j -= 1
        else:
            i -= 1
    print(len(ans_a))
    print(*ans_a[::-1])
    print(*ans_b[::-1])
    return ans


A = ['A', 'N', 'T', 'O', 'N']
B = ['F', 'O', 'M', 'I', 'N']
n = len(A)
m = len(B)

C = dp_nop(A, B)
print(C)

ans = dp_nop_recursive(C, A, B)
print(ans)
