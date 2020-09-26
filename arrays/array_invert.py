def invert_array(A:list, N:int):
    """Обращение массива (поворот задом-наперёд)
    в рамках индексов от 0 до N-1.
    """
    for k in range(N//2):
        A[k], A[N-1-k] = A[N-1-k], A[k]
        # Множественное присваивание

# N//2 чтобы не переходить серединку
# A[N-1-k], k = 0 место в соседнем массиве, N = кол-во элементов, -1 потому что N = 5, от 0 до 4, -1
# Крест на крест меняю 

def test_invert_array():
    A1 = [1, 2, 3, 4, 5]
    print(A1)
    invert_array(A1, 5)
    print(A1)
    if(A1 == [5,4,3,2,1]):
        print("#test1 - ok")
    else:
        print("#test1 - fail")

    A2 = [0, 0, 0, 0, 0, 0, 0, 10]
    print(A2)
    invert_array(A2, 8)
    print(A2)
    if(A2 == [10, 0, 0, 0, 0, 0, 0, 0]):
        print("#test2 - ok")
    else:
        print("#test2 - fail")
test_invert_array()