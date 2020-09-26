# Пузырьковая сортировка
# Сортировка методом пузырька
# Близорукий прапорщик
# Вы неправильно стоите поменяйтесь
def sort_bubble(array):
    swapped = True
    while swapped:
        swapped = False
        for i in range(array.buffer_info()[1]-1):
            if array[i] > array[i+1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
import random
A = [random.randint(100) for x in range(100)]

sort_bubble(A)
print(A)