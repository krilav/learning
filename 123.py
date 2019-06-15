import time

start = time.time()


def three_five(n):
    return sum([i for i in range(n) if i % 3 == 0 or i % 5 == 0])


x = int(input('введите целое число: '))

print('сумма ряда от 1 до ', x, 'с делением на цело на 3 и 5 =', three_five(x))

print('время работы программы = ', time.time() - start, 'sec')
