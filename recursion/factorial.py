from time import time
def fact(n):
    """ Факториал с помощью рекурсии"""
    if n == 1:
        return 1
    else:
        return (n * fact(n-1))


def fact_cicle(n):
    """ Факториал с помощью цикла """
    factorial = 1
    if n == 1:
        return factorial
    else:
        for i in range(1, n + 1):
            factorial = factorial * i
        return factorial


def fact_cicle_ternar(n):
    """ Факториал с помощью цикла """
    factorial = 1
    if n == 1:
        return factorial
    else:
        return [factorial := factorial * i for i in range(1, n+1)][-1:]

start = time()
print(fact(10))
print(time()-start)

start = time()
print(fact_cicle(10))
print(time()-start)

start = time()
print(fact_cicle_ternar(10))
print(time()-start)
