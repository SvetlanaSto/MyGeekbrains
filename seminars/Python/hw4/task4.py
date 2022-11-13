#Задача 4: Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random

k = int(input('Задайте степень k от 0 до 100: '))

list = [random.randint(0, k) for i in range(k + 1)]

print(list)

f = open('file.txt', 'w')
for i in list:
    f.write(str(i) + "\n")
f.close()