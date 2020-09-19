from insertion import genarr
from array import array
from random import shuffle
from operator import lt
n = 100
a = genarr(n)

def TopDownMergeSort(M, compare = lt):
    if len(M) < 2:
        return M[:]
    else:
        middle = int(len(M)/2)
        left = TopDownMergeSort(M[:middle], compare)
        right = TopDownMergeSort(M[middle:], compare)
        return merge(left, right, compare)

def merge(left, right, compare):
    result = array('b')
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
        while i < len(left):
            result.append(left[i])
        while j < len(right):
            result.append(right[j])
        return result







# Top-down реализация

print(a)

# Shuffle
shuffle(a)

# Bottom-up реализация

print(a)

