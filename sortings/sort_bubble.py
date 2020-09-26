# Пузырьковая сортировка

def sort_bubble(array):
    swapped = True
    while swapped:
        swapped = False
        for i in range(array.buffer_info()[1]-1):
            if array[i] > array[i+1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

from sort_insertion import genarr

array = genarr()

sort_bubble(array)

print(array)