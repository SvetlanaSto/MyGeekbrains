# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random

numbers = list(range(-1, 10))
random.shuffle(numbers)
print(numbers)

result_numbers = []
len_result_numbers = int(len(numbers) / 2 + len(numbers) % 2)

for i in range(len_result_numbers):
    product = numbers[i] * numbers[-i-1]
    result_numbers.append(product)

print(f'Произведение пар чисел: {result_numbers}')
