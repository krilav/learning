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
    simple_comp = []  # можно поставить первое число 1, как первый простой множитель.
    while n != 1:
        if n % i == 0:
            n = n / i
            simple_comp.append(i)
        else:
            i += 1
    if index == 1:
        print('Самый большой простой делитель числа {} = {}'.format(old_n, max(simple_comp)))
        print('Время работы функции - ', time.time() - start_time)

    return simple_comp


def project_euler_4(n, index=1):
    """Проект Эйлера, Задача 4.

       Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
       Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
       Найдите самый большой палиндром, полученный умножением двух трехзначных чисел."""

    start_time = time.time()
    all_pol = []

    for h1 in range(10 * (n - 1), 10 ** n):

        for h2 in range(10 * (n - 1), 10 ** n):
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
       Какое самое маленькое число делится нацело на все числа от 1 до 20?

       n - число, до которого формируем список делителей ( от 1 до n)
       index - печатать время работы программы и результат или нет. Значение '1' печатать, остальные значения -
       не печатать."""

    start_time = time.time()
    new_all_mn = []
    new_all_mn2 = []

    for i in range(n):  # Поиск сокращенного списка для перебора деления без остатка
        # all_mn = set.union(set(all_mn), set(project_euler_3(i + 1, 0)))  # все простые можители, без повторений
        all_mn = project_euler_3(n - i, 0)

        for z in all_mn:
            pvt_all_mn = all_mn.count(z)
            new_all_mn.append(z ** pvt_all_mn)

        new_all_mn2 += new_all_mn

    new_all_mn2 = set(new_all_mn2)  # Список без повторений
    col_all_mn = len(new_all_mn2)
    k = max(new_all_mn2)  # Определение шага итерации
    j = 0

    while j != col_all_mn:  # Поиск меньшего числа, делимого без остатка на заданный список чисел

        j = 0

        for i in new_all_mn2:

            if k % i == 0:
                j += 1
                continue
            else:
                k += max(new_all_mn2)
                break

    if index == 1:
        print('Время работы функции - ', time.time() - start_time)
        print('Максимальное число, которое делится без остатка на числа из ряда от 1 до', n, '=', k)

    return new_all_mn2


def project_euler_6(n, index=1):
    """Проект Эйлера, Задача 6.

       Сумма квадратов первых десяти натуральных чисел равна
       1^2 + 2^2 + ... + 10^2 = 385
       Квадрат суммы первых десяти натуральных чисел равен
       (1 + 2 + ... + 10)^2 = 552 = 3025
       Следовательно, разность между суммой квадратов и квадратом суммы первых десяти натуральных чисел
       составляет 3025 − 385 = 2640.
       Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел."""

    start_time = time.time()

    # a = [i + 1 for i in range(n)]
    # b = [sum(a[n:i:-1]) for i in range(n - 1)]
    # a.pop()
    # raz_mez_kvd = 0

    # for k in range(n-1):
    #    raz_mez_kvd += 2 * a[k] * b[k]

    a = 0
    b = 0

    for i in range(n + 1):
        a += i * i
        b += i

    raz_mez_kvd = b ** 2 - a

    if index == 1:
        print('Время работы функции - ', time.time() - start_time)
        print(raz_mez_kvd)

    return raz_mez_kvd


def project_euler_7(n, index=1):
    """Проект Эйлера, Задача 7.

    Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.

    Какое число является 10001-ым простым числом?
    """

    start_time = time.time()
    i = 0
    j = 3

    all_simple = [2]
    while i != n - 1:

        h = 0

        for k in all_simple:
            if j % k == 0:
                pass
            else:
                h += 1

        if h == len(all_simple):
            all_simple.append(j)
            i += 1

        j += 2

    if index == 1:
        print('Время работы функции - ', time.time() - start_time)
        print(all_simple[n - 1])

    return all_simple


# project_euler_1(1000, 0)
# project_euler_2(4000000, 0)
# print(project_euler_3(600851475143, 0))
# project_euler_4(3, 1)
# project_euler_5(20, 1)
project_euler_7(10001, 1)
# print(project_euler_2.__doc__)
