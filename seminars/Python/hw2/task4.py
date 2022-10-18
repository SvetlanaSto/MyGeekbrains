# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
from itertools import product
import random

N = int(input('Введите число N: '))
l = []
for i in range(0, N):
    l.append(random.randint(-N, N-1))

print(f'Сгенерирован список из {N} элементов: {l}')

f = open('file.txt', 'w')
for index in range(0, random.randint(1, N-1) + 1):
    f.write(str(random.randint(0, N-1)) + '\n')
f.close()

product = 1
f = open('file.txt', 'r')
for i in f:
    product *= l[int(i)]

f.close()
print(f'Произведение элементов из файла равно {product}')
