# Задача 2: Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

multipliers = []
number = int(input("Введите число: "))
i = 2
while number > 1:
    if (number % i == 0):
        multipliers.append(i)
        number = number / i
    else:
        i += 1

print(multipliers)
