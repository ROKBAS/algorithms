from functools import lru_cache


def fib_c1(n):
    """Не классический фибонначи, длинный фибонначи"""
    return n if n <= 1 else fib_c1(n - 1) + fib_c1(n - 2)


def fib_c2(n):
    """Обычный фиббоначи, основывается на предыдущих"""
    if n == 0:
        return [0, 1]
    else:
        prev, next = fib_c2(n-1)
        return [next, prev+next]


def fib_c3(n):
    """Математический фибонначи, проблема с округлением"""
    a = (1 + 5 ** 0.5) / 2
    return round(a ** n / 5 ** 0.5)

def matrix_multiply(A, B):
    a, b, c, d = A
    x, y, z, w = B
    
    return (
        a*x + b*z,
        a*y + b*w,
        c*x + d*z,
        c*y + d*w,
    )

def matrix_power(A, m):
    if m == 0:
        return [1, 0, 0, 1]
    elif m == 1:
        return A
    else:
        B = A
        n = 2
        while n <= m:
            B = matrix_multiply(B, B)
            n = n*2
        R = matrix_power(A, m-n//2)
        return matrix_multiply(B, R)


F1 = [1, 1, 
      1, 0]



def fib_c4(n):
    """Матричный фибонначи"""
    return matrix_power(F1, n)[1]


def fib_c5(n):
    """ Метод Doubling Фибонначи """
    if n == 0:
        return (0, 1)
    else:
        a, b = fib_c5(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)


@ lru_cache(100)
def fib_c6_memoized(n):
    """ Memoize Фибонначи, храним значения в кэше """
    if n < 2:
        return n
    else:
        return fib_c6_memoized(n-1) + fib_c6_memoized(n-2)


def test_fibo(function):
    print(function(5))
    print(function(15))
    print(function(50))


# test_fibo(fib_c1)
test_fibo(fib_c2)
test_fibo(fib_c3)
test_fibo(fib_c4)
test_fibo(fib_c5)
test_fibo(fib_c6_memoized)
