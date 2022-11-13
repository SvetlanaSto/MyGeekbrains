# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random

numbers = list(range(-1, 10))
random.shuffle(numbers)
print(numbers)

len_result_numbers = int(len(numbers) / 2 + len(numbers) % 2)
a = numbers[:len_result_numbers]
b = reversed(numbers[len_result_numbers - 1:])
c = list(map(lambda it: it[0]*it[1], zip(a, b)))
print(f'Произведение пар чисел: {c}')
