# Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
# Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.

import math
import time

start = time.time()


def issi(a):
    max_r = math.ceil(math.sqrt(a))
    lst = []
    for i in range(3, max_r):
        if a % i == 0:
            if not issi(i):
                lst.append(i)
    return lst


r = issi(600851475143)
print(max(r))
print(time.time() - start)
