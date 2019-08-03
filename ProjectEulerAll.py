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


project_euler_10(20, 1)
# print(project_euler_8.__doc__)
