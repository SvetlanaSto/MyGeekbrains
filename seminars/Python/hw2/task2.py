# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

n = int(input('Введите число: '))
product = 1
list = [product]

for i in range(2, n+1):
    product *= i
    list.append(product)

print(f'Произведения чисел от 1 до {n}: {list}')