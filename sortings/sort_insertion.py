# Сортировка слиянием
from array import array
import random
n = 100

def genarr(n=100):
    arr = array('b')   
    random.seed("ANTON")
    for i in range(0,n):
        arr.append(random.randrange(100))
    return arr

a = genarr(n)

for i in range(0,n):
    j = i
    while j > 0 and a[j] < a[j-1]:
        a[j-1],a[j] = a[j],a[j-1] #так делается swap в python
        j-=1
