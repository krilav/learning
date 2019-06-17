
import time

start = time.time()


def project_euler_1(n, index=1):
    """Проект Эйлера, Задача 1.

       Если выписать все натуральные числа меньше 10,
       кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
       айдите сумму всех чисел меньше 1000, кратных 3 или 5."""

    start_time = time.time()
    s_35 = sum([i for i in range(n) if i % 3 == 0 or i % 5 == 0])

    if index == 1:
        print('сумма элементов ряда от 1 до ', n, 'делимых на цело на 3 и 5 =', s_35)
        print('Время работы функции - ', time.time() - start_time)

    return s_35


def project_euler_2(n, index=1):
    """Проект Эйлера, Задача 2.

       Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих.
       Начиная с 1 и 2, первые 10 элементов будут:
       Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона."""

    start_time = time.time()
    i = 2
    sum_fib = 0
    a = {1: 1, 2: 1}

    while n > a[i]:
        i += 1
        a[i] = a[i - 1] + a[i - 2]

        if a[i - 1] % 2 == 0:
            sum_fib += a[i - 1]

    if index == 1:
        print('Последнее число ряда Фибоначи, не привышающее {0} = {1}, а сумма ряда = {2}'.format(n, a[i-1], sum_fib))
        print('Время работы функции - ', time.time() - start_time)

    return sum_fib


def project_euler_3(n, index=1):
    """Проект Эйлера, Задача 2.

       Простые делители числа 13195 - это 5, 7, 13 и 29.
       Каков самый большой делитель числа 600851475143, являющийся простым числом?"""
    
    start_time = time.time()
    old_n = n
    i = 2
    while n != 1:
        if n % i == 0:
            n = n / i
        else:
            i += 1
    if index == 1:
        print('Самый большой простой делитель числа {} = {}'.format(old_n, i))
        print('Время работы функции - ', time.time() - start_time)

    return i


# project_euler_1(1000, 0)
# project_euler_2(4000000, 0)
project_euler_3(600851475143, 1)
# print(project_euler_2.__doc__)
