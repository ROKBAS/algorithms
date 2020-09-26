N_max = 100000
A = [0] * N_max
n = 0
x = int(input())
A[n] = x
n += 1

A = []
x = int(input())
A.append(x)
# Список это есть объект, динамический массив
n = len(A)

x = A.pop()
# Возвращает последний и удаляет

# List comprehensions быстрее чем второй способ
# Генераторы списков
# Временная переменная на время создания списка
A = [x**2 for x in range(10)]
# <>
A = []
for x in range(10):
    A.append(x**2)
# for супер списочный
for x in A:
    print(x)
# Фильтрация
A = [1, 2, 3, 4, 5, 7, 12, 9, 6]
B = [x**2 for x in A if x % 2 == 0]
B = [0 if x < 0 else x**2 for x in A if x % 2 == 0]
 