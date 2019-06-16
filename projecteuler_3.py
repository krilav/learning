# Простые делители числа 13195 - это 5, 7, 13 и 29.
# Каков самый большой делитель числа 600851475143, являющийся простым числом?

import time

start = time.time()
N = 600851475143


def sim_fun(n):

    i = 2
    while n != 1:
        if n % i == 0:
            n = n / i
        else:
            i += 1
    return i


print('Самый большой простой делитель числа {} = {}'.format(N, sim_fun(N)))


print(time.time() - start)
