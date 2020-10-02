# Сортировка вставками
# Солдаты в армии по росту
# 4 2 5 1 3
# Прапорщик берет солдата и идёт с ним сравнивая, если меньше то меняет
from test_sort import test_sort


def sort_insert(A: list):
    """Сортировка списка А вставками.
Время: O(n^2)."""
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j] < A[j-1]:
            A[j-1], A[j] = A[j], A[j-1]  # так делается swap в python
            j -= 1


test_sort(sort_insert)
