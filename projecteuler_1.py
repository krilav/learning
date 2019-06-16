# Если выписать все натуральные числа меньше 10,
# кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.

# Найдите сумму всех чисел меньше 1000, кратных 3 или 5.

import time

start = time.time()


def three_five(n):
    return sum([i for i in range(n) if i % 3 == 0 or i % 5 == 0])


# x = int(input('введите целое число: '))

x = 1000
print('сумма ряда от 1 до ', x, 'с делением на цело на 3 и 5 =', three_five(x))

print(time.time() - start)
