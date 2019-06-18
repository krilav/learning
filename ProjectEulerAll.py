import time


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
        print(
            'Последнее число ряда Фибоначи, не привышающее {0} = {1}, а сумма ряда = {2}'.format(n, a[i - 1], sum_fib))
        print('Время работы функции - ', time.time() - start_time)

    return sum_fib


def project_euler_3(n, index=1):
    """Проект Эйлера, Задача 3.

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


def project_euler_4(n, index=1):
    """Проект Эйлера, Задача 4.

       Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
       Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
       Найдите самый большой палиндром, полученный умножением двух трехзначных чисел."""

    start_time = time.time()
    all_pol = []

    for h1 in range(10*(n-1), 10**n):

        for h2 in range(10*(n-1), 10**n):
            k = 0
            pr_chis = h1 * h2
            test_chis = str(pr_chis)
            light_chis = len(test_chis)

            for i in range(light_chis // 2):
                if test_chis[i] == test_chis[light_chis - i - 1]:
                    k = k + 1
                else:
                    break

            if k == light_chis // 2:
                all_pol.append(pr_chis)

    if index == 1:
        print('Время работы функции - ', time.time() - start_time)
        print('Максимальный число-палиндром из ', n, ' значных чмсел = ', max(all_pol))

    return max(all_pol)


def project_euler_5(n, index=1):
    """Проект Эйлера, Задача 5.

       2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
       Какое самое маленькое число делится нацело на все числа от 1 до 20?"""

    start_time = time.time()

    if index == 1:
        print('Время работы функции - ', time.time() - start_time)
        print(n)

    return


# project_euler_1(1000, 0)
# project_euler_2(4000000, 0)
# project_euler_3(600851475143, 1)
# project_euler_4(3, 1)
# project_euler_5()
# print(project_euler_2.__doc__)
