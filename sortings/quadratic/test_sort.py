# Тестировка массивов на сортировку

def test_sort(sort_algorithm):
    print("Тестируем: ", sort_algorithm.__doc__)
    print("Test #1: ", end="")
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    # Сравнение двух массивов за O(n): O(len(A))
    print("OK" if A == A_sorted else "FAILED")

    print("Test #2: ", end="")
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(20))
    sort_algorithm(A)
    # Сравнение двух массивов за O(n): O(len(A))
    print("OK" if A == A_sorted else "FAILED")

    print("Test #3: ", end="")
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(A)
    # Сравнение двух массивов за O(n): O(len(A))
    print("OK" if A == A_sorted else "FAILED")

    print("Test #4: ", end="")
    A = [1, 2, 3, 5, 2, 7, 6, 0, 9, 9, 2, 8, 6, 3, 4, 1, 5, 2, 3, 7, 6, 6, 1, 3, 5, 2]
    A_sorted = [0, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 8, 9, 9]
    sort_algorithm(A)
    # Сравнение двух массивов за O(n): O(len(A))
    print("OK" if A == A_sorted else "FAILED")
