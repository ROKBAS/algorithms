n = int(input())
A = [int(i) for i in input().split(" ")]


def nvp(A: list):
    """
    """
    F = [0] * n
    for i in range(n):
        for j in range(i):
            if A[j] < A[i] and F[j] > F[i]:
                F[i] = F[j]
        F[i] += 1
    return F


def nvp_recursive(F: list):
    """
    """
    P = [-1] * n
    for i in range(n):
        for j in range(i):
            if(A[j] < A[i]) and F[j] > F[i]:
                F[i] = F[j]
                P[i] = j
        F[i] += 1
    return P
