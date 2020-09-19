# Сортировка слиянием
from array import array
import random
n = 100
random.seed("ANTON")

def genarr(n):
    arr = array('b')   
    for i in range(0,n):
        arr.append(random.randint(-100,100))
    return arr

a = genarr(n)

for i in range(0,n):
    j = i
    while j > 0 and a[j] < a[j-1]:
        a[j-1],a[j] = a[j],a[j-1] #так делается swap в python
        j-=1

print(a)