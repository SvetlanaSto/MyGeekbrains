# Задача 3: Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random

list = []
for i in range(20):
    list.append(random.randint(0, 20))

print(list)

result = []
for i in list:
    if i not in result:
        result.append(i)

print(result)
