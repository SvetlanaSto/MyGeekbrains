# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num_str = str(float(input('Введите число: ')))
num_str = num_str.replace('-', '')
num_str = num_str.replace('.', '')
print(num_str)

sum = 0
num_list = list(num_str)
for i in num_list:
    sum += int(i)

print(f'Сумма цифр числа равна: {sum}')
