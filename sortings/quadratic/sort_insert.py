# Сортировка вставками
# Солдаты в армии по росту
# Прапорщик берет солдата и идёт с ним сравнивая, если меньше то меняет
import random
A = [random.randint(100) for x in range(100)]
for i in A:
    j = i
    while j > 0 and a[j] < a[j-1]:
        a[j-1],a[j] = a[j],a[j-1] #так делается swap в python
        j-=1
