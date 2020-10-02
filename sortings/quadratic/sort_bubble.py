# Пузырьковая сортировка
# Сортировка методом пузырька
# Близорукий прапорщик
# Вы неправильно стоите поменяйтесь
from test_sort import test_sort


def sort_bubble(A: list):
    """ Сортировка списка А методом пузырька.
Время: O(n^2)."""
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N - bypass):
            if(A[k] > A[k+1]):
                A[k], A[k+1] = A[k+1], A[k]


test_sort(sort_bubble)
