#--------------------Факториал--------------------
def factorial(n: int) -> int:
    """Вычисление факториала"""
    if n < 0:
        raise ValueError('Число должно быть положительным')
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def factorial_recursive(n: int) -> int:
    """Вычисление факториала рекурсивно"""
    if n < 0:
        raise ValueError('Число должно быть положительным')
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)


#--------------------Фибоначчи--------------------
def fibo(n: int) -> int:
    """Вычисление чисел Фибоначчи"""
    if n < 0:
        raise ValueError('Число должно быть положительным')
    if n == 0:
        return 0
    if n == 1:
        return 1
    sp_fibo = [0, 1]
    for i in range(2, n + 1):
        elem = sp_fibo[i - 1] + sp_fibo[i - 2]
        sp_fibo.append(elem)
    return sp_fibo[n]


def fibo_recursive(n: int) -> int:
    """Вычисление чисел Фибоначчи рекурсивно"""
    if n < 0:
        raise ValueError('Число должно быть положительным')
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)