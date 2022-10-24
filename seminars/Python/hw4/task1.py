#Задача 1: Вычислить число c заданной точностью d.

d = float(input('Задайте точность вычисления числа Пи (например, 0.00001): '))

n = 1
sign = 1
pi = 0
prev = 3

while abs(prev-pi) >= d:
    prev = pi
    pi += 4/n*sign
    sign = -sign
    n += 2

print(f'При точности {d} число Пи равно {pi}. n={n}')