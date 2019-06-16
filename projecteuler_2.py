# Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих.
# Начиная с 1 и 2, первые 10 элементов будут:
# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.

# sum([i for i in range(n) if i % 3 == 0 or i % 5 == 0])

import time

start = time.time()
x = 4000000


def s_fib_fun(n):
    i = 2
    sum_fib = 0
    a = {1: 1, 2: 1}

    while n > a[i]:
        i += 1
        a[i] = a[i - 1] + a[i - 2]

        if a[i - 1] % 2 == 0:
            sum_fib += a[i - 1]

    return sum_fib, a[i-1]


i_max, s_fib = s_fib_fun(x)

print('Последнее число ряда Фибоначи, не привышающее {0} = {1}, а сумма ряда = {2}'.format(x, i_max, s_fib))

print(time.time() - start)
