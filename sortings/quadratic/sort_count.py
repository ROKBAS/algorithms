# Сортировка подсчётом
from typing import overload
from test_sort import test_sort


def array_search(A, x):
    """ Осуществляет поиск числа х в массиве А
от 0 до N-1 индекса включительно.
Возвращает индекс элемента х в массиве А.
Или -1, если такого нет.
Если в массиве неск. один. элементов равных х,
то вернуть индекс первого по счёту."""
    if isinstance(A, list):
        for k in A:
            if A[k] == x:
                return k
        return -1
    elif isinstance(A, dict):
        for k in A.keys():
            if k == x:
                return k
        return -1


def sort_count(A: list):
    """ Сортировка списка A подсчётом, массив частот
Время: O(n).
Память: O(m) - кол-во различных элементов.
    """
    B = {}
    for i in range(len(A)):
        if(array_search(B, A[i]) == -1):
            B.update({A[i]: 0})
            B[A[i]] += 1
        else:
            B[A[i]] += 1
    B = dict(sorted(B.items()))
    A.clear()
    for key in B.keys():
        count = B[key]
        for i in range(count):
            A.append(key)


test_sort(sort_count)
