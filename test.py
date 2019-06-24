
import time

start_time = time.time()
n = 100000
a = 0
b = 0

for i in range(n + 1):
    a += i * i
    b += i

print(b**2 - a)

print('Время работы функции - ', time.time() - start_time)