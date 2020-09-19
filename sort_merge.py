from insertion import genarr
from array import array
n = 50

a = genarr(n)
b = genarr(n)

def merge(a,b):
    n = a.buffer_info()[1]
    m = b.buffer_info()[1]
    i = 0
    j = 0
    k = 0
    c = array('b')
    while i < n or j < m:
        if j == m or (i<n and a[i]<b[j]):
            c.append(a[i]) 
            k += 1
            i += 1
        else:
            c.append(b[j]) 
            k += 1
            i += 1
    return c

print(merge(a,b))

