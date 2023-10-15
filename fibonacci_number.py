# Нахождения N числа Фибоначчи в зависимости от текущего дня +1
def find_the_fibonacci_number(day):
    day += 1
    if day < 1:
        raise Exception("Введите положительное число!")
    fib1 = 1
    fib2 = 1

    for _ in range(2, day):
        fib1, fib2 = fib2, fib1 + fib2
    return fib2
