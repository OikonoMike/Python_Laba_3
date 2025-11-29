from src.factor_and_fibo import (factorial, factorial_recursive, fibo,
                                 fibo_recursive)


# --------------------factorial--------------------
def test_factorial_zero():
    assert factorial(0) == 1


def test_factorial_positive():
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800


def test_factorial_large():
    # Проверка на большое число (не вызывает ошибку)
    assert factorial(20) == 2432902008176640000


def test_factorial_negative_raises():
    try:
        factorial(-1)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Число должно быть положительным"


# --------------------factorial_recursive--------------------
def test_factorial_recursive_zero():
    assert factorial_recursive(0) == 1


def test_factorial_recursive_positive():
    assert factorial_recursive(1) == 1
    assert factorial_recursive(4) == 24
    assert factorial_recursive(7) == 5040


def test_factorial_recursive_matches_iterative():
    for n in range(0, 15):
        assert factorial_recursive(n) == factorial(n)


def test_factorial_recursive_negative_raises():
    try:
        factorial_recursive(-5)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Число должно быть положительным"


# --------------------fibo--------------------
def test_fibo_zero():
    assert fibo(0) == 0


def test_fibo_one():
    assert fibo(1) == 1


def test_fibo_positive():
    assert fibo(2) == 1
    assert fibo(5) == 5
    assert fibo(10) == 55


def test_fibo_large():
    assert fibo(20) == 6765


# --------------------fibo_recursive--------------------
def test_fibo_recursive_zero():
    assert fibo_recursive(0) == 0


def test_fibo_recursive_one():
    assert fibo_recursive(1) == 1


def test_fibo_recursive_positive():
    assert fibo_recursive(2) == 1
    assert fibo_recursive(6) == 8
    assert fibo_recursive(7) == 13


def test_fibo_recursive_matches_iterative():
    for n in range(0, 15):
        assert fibo_recursive(n) == fibo(n)


def test_fibo_recursive_negative_raises():
    try:
        fibo_recursive(-3)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Число должно быть положительным"
