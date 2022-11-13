# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

import random

a = [round(random.uniform(0.01, 100), 2) for i in range(10)]
print(a)

#b = [round(elem % 1, 2) for elem in a if elem % 1 != 0]
b = list(map(lambda it: round(it % 1, 2), filter(lambda it: it % 1 != 0, a)))
print(b)

min = b[0]
max = b[0]
for i in range(1, len(b)):
    if min > b[i]:
        min = b[i]
    elif max < b[i]:
        max = b[i]

diff = round(max - min, 2)
print(
    f'Разница между максимальным ({max}) и минимальным ({min}) элементами равна: {diff}')
