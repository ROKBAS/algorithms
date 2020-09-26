from random import randint
from sort_insertion import genarr

a = genarr(100)

def partition(a, left, right):
    pivot = a[randint(left,right)]
    i = left - 1
    j = right + 1
    while True:
        i+=1
        while a[i] < pivot:
            i+=1
        j-=1
        while a[j] > pivot:
            j -= 1
        if(i>=j):
            return j
        
        a[i], a[j] = a[j], a[i]

def sort_quick(a):
    def _sort_quick(items, left, right):
        if(left < right):
            split_index = partition(items, left, right)
            _sort_quick(items, left, split_index)
            _sort_quick(items, split_index+1, right)
    _sort_quick(a, 0, len(a) - 1)


sort_quick(a)
print(a)
