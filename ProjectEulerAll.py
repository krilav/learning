import time
import math


def all_simple_find(n):
    """Постоение массива из простых чисел меньших n.

    """

    p = 2
    all_simple = []
    find_simple = [True for k in range(n)]

    while p * p < n:
        for i in range(p * p, n, p):
            find_simple[i] = False
        p += 1

    for p in range(2, n):
        if find_simple[p]:
            all_simple.append(p)

    return all_simple


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
    all_simple = all_simple_find(n)

    if index == 1:
        print('Время работы функции - ', time.time() - start_time)
        print(all_simple[n - 1])

    return all_simple


def project_euler_8(n, index=1):
    """Проект Эйлера, Задача 8.

    Наибольшее произведение четырех последовательных цифр в нижеприведенном 1000-значном
    числе равно 9 × 9 × 8 × 9 = 5832.
    Найдите наибольшее произведение тринадцати последовательных цифр в данном числе.
    """

    start_time = time.time()

    nmb = '73167176531330624919225119674426574742355349194934'
    nmb += '96983520312774506326239578318016984801869478851843'
    nmb += '85861560789112949495459501737958331952853208805511'
    nmb += '12540698747158523863050715693290963295227443043557'
    nmb += '66896648950445244523161731856403098711121722383113'
    nmb += '62229893423380308135336276614282806444486645238749'
    nmb += '30358907296290491560440772390713810515859307960866'
    nmb += '70172427121883998797908792274921901699720888093776'
    nmb += '65727333001053367881220235421809751254540594752243'
    nmb += '52584907711670556013604839586446706324415722155397'
    nmb += '53697817977846174064955149290862569321978468622482'
    nmb += '83972241375657056057490261407972968652414535100474'
    nmb += '82166370484403199890008895243450658541227588666881'
    nmb += '16427171479924442928230863465674813919123162824586'
    nmb += '17866458359124566529476545682848912883142607690042'
    nmb += '24219022671055626321111109370544217506941658960408'
    nmb += '07198403850962455444362981230987879927244284909188'
    nmb += '84580156166097919133875499200524063689912560717606'
    nmb += '05886116467109405077541002256983155200055935729725'
    nmb += '71636269561882670428252483600823257530420752963450'

    lst_of_prov = []

    for i in range(0, len(nmb)):

        k = 1
        for j in nmb[i:i + n]:
            k *= int(j)
        lst_of_prov.append(k)
        # print(nmb[i:i + 4], '--', k)

    if index == 1:
        print('Время работы функции - ', time.time() - start_time)
        print(max(lst_of_prov))

    return max(lst_of_prov)


def project_euler_9(n, index=1):
    """Проект Эйлера, Задача 9.

        Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство
        a^2 + b^2 = c^2
        Например, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

        Существует только одна тройка Пифагора, для которой a + b + c = 1000.
        Найдите произведение abc
    """

    start_time = time.time()
    count_pif = []
    for a in range(int(round(n / 2))):

        for b in range(int(round(n / 2))):

            if a + b + math.sqrt(a ** 2 + b ** 2) == n and (n - a - b) ** 2 == (a ** 2 + b ** 2):
                count_pif = [a, b, n - a - b]
        if len(count_pif) > 1:
            pass
    if len(count_pif) > 1:
        pass

    if index == 1:
        print('Время работы функции - ', time.time() - start_time)
        print(count_pif, count_pif[0] * count_pif[1] * count_pif[2])

    return count_pif[0] * count_pif[1] * count_pif[2]


def project_euler_10(n, index=1):
    """Проект Эйлера, Задача 10.

    Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
    Найдите сумму всех простых чисел меньше двух миллионов.
    """

    start_time = time.time()
    all_simple = all_simple_find(n)

    if index == 1:
        print('Время работы функции - ', time.time() - start_time)
        print(all_simple)

    return all_simple


def project_euler_11(n, index=1):
    """Проект Эйлера, Задача 11.

        Каково наибольшее произведение четырех подряд идущих чисел в таблице 20×20,
        расположенных в любом направлении (вверх, вниз, вправо, влево или по диагонали)?

        [n] - количество чисел идущих подряд
        [index] - если значение  = 1, то выводить решение на экран
    """

    start_time = time.time()

    table = ['08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08'.split(' '),
             '49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00'.split(' '),
             '81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65'.split(' '),
             '52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91'.split(' '),
             '22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80'.split(' '),
             '24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50'.split(' '),
             '32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70'.split(' '),
             '67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21'.split(' '),
             '24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72'.split(' '),
             '21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95'.split(' '),
             '78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92'.split(' '),
             '16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57'.split(' '),
             '86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58'.split(' '),
             '19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40'.split(' '),
             '04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66'.split(' '),
             '88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69'.split(' '),
             '04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36'.split(' '),
             '20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16'.split(' '),
             '20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54'.split(' '),
             '01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'.split(' ')]

    # в право и в лево
    record = 0
    all_pr = []
    all_pr_r = []
    all_pr_c = []
    pr_r = 1
    pr_c = 1
    row = 0
    col = 0
    i = 0
    j = 0

    while i < 20:
        while row < 20:
            while col < 20:
                while j < n:
                    if row + n > 20 or col + n > 20:
                        pass
                    else:
                        pr_r *= int(table[row + i][col + j])
                        pr_c *= int(table[col + j][row + i])
                    j += 1

                all_pr_r.append(pr_r)
                all_pr_c.append(pr_c)
                pr_r = 1
                pr_c = 1
                j = 0
                col += 1

            row += 1

        i += 1
        row = 0
        col = 0

    # по диагонали в право
    all_pr_rl = []
    pr_rl = 1
    row = 0
    col = 0
    i = 0
    j = 0

    while i < 20:
        while row < 20:
            while col < 20:
                while j < n:
                    try:
                        pr_rl *= int(table[row + i + j][col + j])
                    except IndexError:
                        record += 1
                        pass
                    j += 1

                if record == 0:
                    all_pr_rl.append(pr_rl)
                else:
                    all_pr_rl.append(-1)
                record = 0
                pr_rl = 1
                j = 0
                col += 1

            row += 1

        i += 1
        row = 0
        col = 0

    # по диагонали в лево
    all_pr_cl = []
    pr_cl = 1
    row = 0
    col = 0
    i = 0
    j = 0

    while i < 20:
        while row < 20:
            while col < 20:
                while j < n:
                    try:
                        if col - j >= 0:
                            pr_cl *= int(table[row + i + j][col - j])
                        else:
                            record += 1
                    except IndexError:
                        record += 1
                        pass
                    j += 1

                if record == 0:
                    all_pr_cl.append(pr_cl)
                else:
                    all_pr_cl.append(-1)
                record = 0
                pr_cl = 1
                j = 0
                col += 1

            row += 1

        i += 1
        row = 0
        col = 0

    if index == 1:
        print('Время работы функции - ', time.time() - start_time)
        all_pr.append(max(all_pr_r))
        all_pr.append(max(all_pr_c))
        all_pr.append(max(all_pr_rl))
        all_pr.append(max(all_pr_cl))
        print(max(all_pr))

    return table


print(project_euler_11.__doc__)
project_euler_11(4, 1)
