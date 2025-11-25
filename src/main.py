from src.factorial_and_fibo import factorial, factorial_recursive, fibo, fibo_recursive


while (put := input()):
    match put:

        case 'factorial':
            print(factorial(int(put)))
        case 'factorial_recursive':
            print()
        case 'fibo':
            print()
        case 'fibo_recursive':
            print()
        case 'bubble_sort':
            print()